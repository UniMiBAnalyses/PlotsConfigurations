# coding=utf-8


import optparse
import math

## counts the number of "set" from the line "# SM rwgt_1" to the first line starting with "#"
## this is also the number of operators
def find_number_operators(card):
    start = False
    counter = 0
    with open(card, "r") as file:
        for line in file:
            if line.startswith("# SM rwgt_1"):
                start = True
            elif line.startswith("#") and start:
                break
            elif start and "set" in line:
                counter += 1
    return counter


def get_list_operators(card):
    ops = []
    with open(card, "r") as file:
        for line in file:
            if line.startswith("#") and not line.startswith("# SM rwgt_1"):
                ## # cW=1, cHj3=1 rwgt_28
                if len(line.split(" ")) > 3:
                    break
                else:
                    op = line.split(" ")[1].split("=")[0]
                    if op not in ops:
                        ops.append(op)
    return ops



def do_lin_quad(op, card):
    file_content = ""
    w_plus = ""
    w_minus = ""

    with open(card, "r") as file:
        for line in file:
            if op in line and "," not in line:
                if op+"=1" in line:
                    w_plus = int(line.split("rwgt_")[1])
                elif op+"=-1" in line:
                    w_minus = int(line.split("rwgt_")[1])

    ## forse in realtà ci va un -1!!!
    file_content += "samples['lin_{}'] = {{".format(op) + "\n"
    file_content += "    'name': changeMEname," + "\n"
    file_content += "    'weight': changeMEweight + '*' + '0.5*(LHEReweightingWeight[{}] - LHEReweightingWeight[{}])',".format(w_plus, w_minus) + "\n"
    file_content += "    'FilesPerJob': 30," + "\n"
    file_content += "}}" + "\n\n"

    file_content += "samples['quad_{}'] = {{".format(op) + "\n"
    file_content += "    'name': changeMEname," + "\n"
    file_content += "    'weight': changeMEweight + '*' + '0.5*(LHEReweightingWeight[{}] + LHEReweightingWeight[{}]) -2*LHEReweightingWeight[0])',".format(w_plus, w_minus) + "\n"
    file_content += "    'FilesPerJob': 30," + "\n"
    file_content += "}}" + "\n\n"

    return file_content


def do_mixed(op1, op2, card):
    file_content = ""
    w = ""

    with open(card, "r") as file:
        for line in file:
            if op1 in line and op2 in line:
                    w = int(line.split("rwgt_")[1])
    
     ## forse in realtà ci va un -1!!!
    file_content += "samples['mixed_{}_{}'] = {{".format(op1,op2) + "\n"
    file_content += "    'name': changeMEname," + "\n"
    file_content += "    'weight': changeMEweight + '*' + '(LHEReweightingWeight[{}])',".format(w) + "\n"
    file_content += "    'FilesPerJob': 30," + "\n"
    file_content += "}}" + "\n\n"

    return file_content
    


if __name__ == '__main__':

    usage = 'usage: %prog [options]'
    parser = optparse.OptionParser(usage)   

    parser.add_option('--card'           , dest='card'           , help='Path to the rwgt card'                      , default=None)
    parser.add_option('--numOp'          , dest='numOp'          , help='Number of operators used in the rwgt card'  , default=None)
    
    (opt, args) = parser.parse_args()

    rw_card = opt.card

    if opt.numOp is None:
        numOp = find_number_operators(rw_card)
    else:
        numOp = opt.numOp

    ops = get_list_operators(rw_card)

    print "Number of operators: ", numOp
    print "Operators: ", ops
    # print "Number of weights (lin, quad, mixed) = ", numOp*2 + math.comb(numOp, 2)  ##lin quad + mixed

    file_content = ""

    for idx1, op1 in enumerate(ops):
        file_content += do_lin_quad(op1,rw_card)  
        for idx2, op2 in enumerate(ops):
            if idx2 > idx1:
                file_content += do_mixed(op1, op2, rw_card)

# write it all down
with open("EFTweights.py", "w") as file:
    file.write(file_content)


    