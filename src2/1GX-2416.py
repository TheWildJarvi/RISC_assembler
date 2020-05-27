#AUTHORS#
#TheWildJarvi#
#Nano#
#Lululombard#



import re
import argparse
import os

output_choices = ['bin', 'lst']

#handles the input arg
parser = argparse.ArgumentParser(description='Assemble code')
parser.add_argument('-i', '--input', type=argparse.FileType('r'), help='Input assembly file')
parser.add_argument('-f', '--output-format', type=str, choices=output_choices, help='Input assembly file')

args = parser.parse_args()

input_file = args.input
output_format = args.output_format


#if no input arg, ask for one
if not input_file:
  filename = raw_input('Input file? ')
  input_file = open(filename)

while not output_format:
  user_input = raw_input('Output format? Allowed format are {} '.format(output_choices))
  if user_input not in output_choices:
    print 'Invalid input, allowed is {}'.format(output_choices)
    continue
  else:
    output_format = user_input
    break

#  pseudo ops
# lim
# nop
# unconditional branch

def read_file(f):
    s = []
    s = f.read().splitlines()
    return s


def convert(a, base=4):
    if a < 0:
        a = a & pow(2,base)-1
    return format(a, '0' + repr(base) + 'b')

#def print_asm(decimal_values):
#    for input in decimal_values:
#        for index, element in enumerate(input):
#            print(convert(element, 4 if index < 4 else 8 ), end=' ')
#    print()

def convert_to_int(s): #takes a signed immediate and converts it to int(ex, -0xff = -255)
    neg = 1
    if s[0] == '-':
        neg = -1
        s = s[1:]
    if s[0] == '+':
        s = s[1:]
    if s[1] == 'x':
        return neg * int(s[2:], 16)
    elif s[1] == 'b':
        return neg * int(s[2:], 2)
    elif s[1] == 'd':
        return neg * int(s[2:], 10)
    else:
        return 0




def xlen(bw, val, sign=False): #this takes a decimal integer an converts to binary
    if sign:
        if val < -2**(bw - 1): #checking if its too negative
            raise ValueError('error0: val under '+ str(bw) + ' bit range')
        elif val > (2**(bw - 1) - 1): #checking if its too positive
            raise ValueError('error1: val over ' + str(bw) + ' bit range')
        if val < 0: #if val is negative
            val += 2**bw # 2's comp convert, aka -105 becomes +151

    else:
        if val < 0:  # checking if its too negative
            raise ValueError('error2: val under ' + str(bw) + ' bit range')
        elif val > ((2 **bw) - 1):  # checking if its too positive
            raise ValueError('error3: val over ' + str(bw) + ' bit range')
    return "{0:b}".format(val).zfill(bw) # turning val to binary value of bw bits

#try:
#print xlen(12, -185, 0)
#except  ValueError as e:
    #print e


registers = {
    'r0': 0,
    't0': 1,
    't1': 2,
    't2': 3,
    't3': 4,
    't4': 5,
    's0': 6,
    's1': 7,
    's2': 8,
    's3': 9,
    's4': 10,
    's5': 11,
    's6': 12,
    'r13': 13,
    'id': 14,
    'ra': 15 }

def asmtoint(asm):

    asm_split = re.split(" |, |\(|\)", asm)
    args = []
    i=0
    for i in range (len(asm_split)):
        if (asm_split[i] != ""):
            args.append(asm_split[i])
    #print (args)
    #print args[0]
    #print args[3]
    if not len(args):
        return
    opcode = 0
    rd = 0
    rs1 = 0
    rs2 = 0
    imm = 0



#--------------------------------------------------------------------
# ARITHMETIC AND LOGIC INSTRUCTIONS
#--------------------------------------------------------------------
    if (args[0] == "add"):
        if (len(args) != 4):
            return 0, 0, 0, 0, 0
        opcode = 0
        rd = registers[args[1]]
        rs1 = registers[args[2]]
        if args[3][:2] in ["0x","0d","0b"]: #check if second source is an IMM
            imm = convert_to_int(args[3])   #
        else:
            rs2 = registers[args[3]]

    elif (args[0] == "addv"): #no immediate used for add vector
        if (len(args) != 4):
            return 0, 0, 0, 0, 0
        opcode = 1
        rd = registers[args[1]]
        rs1 = registers[args[2]]
        rs2 = registers[args[3]]

    elif (args[0] == "adc"):
        if (len(args) != 4):
            return 0, 0, 0, 0, 0
        opcode = 2
        rd = registers[args[1]]
        rs1 = registers[args[2]]
        if args[3][:2] in ["0x", "0d", "0b"]:
            imm = convert_to_int(args[3])
        else:
            rs2 = registers[args[3]]

    elif (args[0] == "sub"):
        if (len(args) != 4):
            return 0, 0, 0, 0, 0
        opcode = 3
        rd = registers[args[1]]
        rs1 = registers[args[2]]
        if args[3][:2] in ["0x", "0d", "0b"]:
            imm = convert_to_int(args[3])
        else:
            rs2 = registers[args[3]]

    elif (args[0] == "nor"):
        if (len(args) != 4):
            return 0, 0, 0, 0, 0
        opcode = 4
        rd = registers[args[1]]
        rs1 = registers[args[2]]
        if args[3][:2] in ["0x", "0d", "0b"]:
            imm = convert_to_int(args[3])
        else:
            rs2 = registers[args[3]]

    elif (args[0] == "and"):
        if (len(args) != 4):
            return 0, 0, 0, 0, 0
        opcode = 5
        rd = registers[args[1]]
        rs1 = registers[args[2]]
        if args[3][:2] in ["0x", "0d", "0b"]:
            imm = convert_to_int(args[3])
        else:
            rs2 = registers[args[3]]

    elif (args[0] == "xor"):
        if (len(args) != 4):
            return 0, 0, 0, 0, 0
        opcode = 6
        rd = registers[args[1]]
        rs1 = registers[args[2]]
        if args[3][:2] in ["0x","0d","0b"]:
            imm = convert_to_int(args[3])
        else:
            rs2 = registers[args[3]]

    elif (args[0] == "abs"):
        if (len(args) != 3):
            return 0, 0, 0, 0, 0
        opcode = 7
        rd = registers[args[1]]
        if args[3][:2] in ["0x","0d","0b"]:
            imm = convert_to_int(args[3])
        else:
            rs2 = registers[args[3]]

    elif (args[0] == "limm"): #IMM is 16 bits, top byte goes into rs1,rs2, and low byte goes into imm
        if (len(args) != 3):
            return 0, 0, 0, 0, 0
        opcode = 8
        rd = registers[args[1]]
        #convert args[2] into 2 4bit nibbles and a byte.
        rs1 = (convert_to_int(args[2]) >> 12) & 0x0f #grab high nib
        rs2 = (convert_to_int(args[2]) >> 8) & 0x0f #grab low nib
        imm = convert_to_int(args[2]) & 0xff  #grab low byte




# --------------------------------------------------------------------
# ABSOLUTE BRANCH INSTRUCTIONS
# --------------------------------------------------------------------
    elif (args[0] == "beq"):
        if (len(args) != 2):
            return 0, 0, 0, 0, 0
        opcode = 9
        rd = 0
        if args[1][:2] in ["0x","0d","0b"]:
            imm = convert_to_int(args[1])
        else:
            rs2 = registers[args[1]]

    elif (args[0] == "bneq"):
        if (len(args) != 2):
            return 0, 0, 0, 0, 0
        opcode = 9
        rd = 2
        if args[1][:2] in ["0x","0d","0b"]:
            imm = convert_to_int(args[1])
        else:
            rs2 = registers[args[1]]

    elif (args[0] == "bgt"):
        if (len(args) != 2):
            return 0, 0, 0, 0, 0
        opcode = 9
        rd = 4
        if args[1][:2] in ["0x","0d","0b"]:
            imm = convert_to_int(args[1])
        else:
            rs2 = registers[args[1]]

    elif (args[0] == "bgte"):
        if (len(args) != 2):
            return 0, 0, 0, 0, 0
        opcode = 9
        rd = 6
        if args[1][:2] in ["0x","0d","0b"]:
            imm = convert_to_int(args[1])
        else:
            rs2 = registers[args[1]]

    elif (args[0] == "blt"):
        if (len(args) != 2):
            return 0, 0, 0, 0, 0
        opcode = 9
        rd = 8
        if args[1][:2] in ["0x","0d","0b"]:
            imm = convert_to_int(args[1])
        else:
            rs2 = registers[args[1]]

    elif (args[0] == "blte"):
        if (len(args) != 2):
            return 0, 0, 0, 0, 0
        opcode = 9
        rd = 10
        if args[1][:2] in ["0x","0d","0b"]:
            imm = convert_to_int(args[1])
        else:
            rs2 = registers[args[1]]
# --------------------------------------------------------------------
# RELATIVE BRANCH INSTRUCTIONS
# --------------------------------------------------------------------
    elif (args[0] == "breq"):
        if (len(args) != 2):
            return 0, 0, 0, 0, 0
        opcode = 9
        rd = 1
        if args[1][:2] in ["0x","0d","0b"]:
            imm = convert_to_int(args[1])
        else:
            rs2 = registers[args[1]]

    elif (args[0] == "brneq"):
        if (len(args) != 2):
            return 0, 0, 0, 0, 0
        opcode = 9
        rd = 3
        if args[1][:2] in ["0x","0d","0b"]:
            imm = convert_to_int(args[1])
        else:
            rs2 = registers[args[1]]

    elif (args[0] == "brgt"):
        if (len(args) != 2):
            return 0, 0, 0, 0, 0
        opcode = 9
        rd = 5
        if args[1][:2] in ["0x","0d","0b"]:
            imm = convert_to_int(args[1])
        else:
            rs2 = registers[args[1]]

    elif (args[0] == "brgte"):
        if (len(args) != 2):
            return 0, 0, 0, 0, 0
        opcode = 9
        rd = 7
        if args[1][:2] in ["0x","0d","0b"]:
            imm = convert_to_int(args[1])
        else:
            rs2 = registers[args[1]]

    elif (args[0] == "brlt"): #branch relative less than
        if (len(args) != 2):
            return 0, 0, 0, 0, 0
        opcode = 9
        rd = 9
        if args[1][:2] in ["0x","0d","0b"]:
            imm = convert_to_int(args[1])
        else:
            rs2 = registers[args[1]]

    elif (args[0] == "brlte"): #branch relative less than or equal
        if (len(args) != 2):
            return 0, 0, 0, 0, 0
        opcode = 9
        rd = 11
        if args[1][:2] in ["0x","0d","0b"]:
            imm = convert_to_int(args[1])
        else:
            rs2 = registers[args[1]]
# --------------------------------------------------------------------
# ABSOLUTE JUMP AND LINK INSTRUCTIONS
# --------------------------------------------------------------------
    elif (args[0] == "jal"): #jump and link
        if (len(args) != 2):
            return 0, 0, 0, 0, 0
        opcode = 10
        rd = 0
        if args[1][:2] in ["0x","0d","0b"]:
            imm = convert_to_int(args[1])
        else:
            rs2 = registers[args[1]]
# --------------------------------------------------------------------
# RELATIVE JUMP AND LINK INSTRUCTIONS
# --------------------------------------------------------------------

    elif (args[0] == "jral"): #jump relative and link
        if (len(args) != 2):
            return 0, 0, 0, 0, 0
        opcode = 10
        rd = 1
        if args[1][:2] in ["0x", "0d", "0b"]:
            imm = convert_to_int(args[1])
        else:
            rs2 = registers[args[1]]

# --------------------------------------------------------------------
# ABSOLUTE JUMP AND LINK REGISTER INSTRUCTIONS
# --------------------------------------------------------------------
    elif (args[0] == "jalr"): #jump and  link register
        if (len(args) != 3):
            return 0, 0, 0, 0, 0
        opcode = 10
        rd = 8
        rs1 = registers[args[1]]
        if args[2][:2] in ["0x", "0d", "0b"]:
            imm = convert_to_int(args[2])
        else:
            rs2 = registers[args[2]]

# --------------------------------------------------------------------
# RELATIVE JUMP AND LINK REGISTER INSTRUCTIONS
# --------------------------------------------------------------------
    elif (args[0] == "jralr"): #jump relative and  link register
        if (len(args) != 3):
            return 0, 0, 0, 0, 0
        opcode = 10
        rd = 9
        rs1 = registers[args[1]]
        if args[2][:2] in ["0x", "0d", "0b"]:
            imm = convert_to_int(args[2])
        else:
            rs2 = registers[args[2]]
# --------------------------------------------------------------------
# LOAD / STORE INSTRUCTIONS
# --------------------------------------------------------------------

    elif (args[0] == "ld"):
        if (len(args) != 3):
            return 0, 0, 0, 0, 0
        opcode = 11
        rs1 = 0
        rd = registers[args[1]]
        if args[2][:2] in ["0x", "0d", "0b"]:
            imm = convert_to_int(args[2])
        else:
            rs2 = registers[args[2]]

    elif (args[0] == "st"):
        if (len(args) != 3):
            return 0, 0, 0, 0, 0
        opcode = 11
        rs1 = 1
        rd = registers[args[1]]

        if args[2][:2] in ["0x", "0d", "0b"]:
            imm = convert_to_int(args[2])
        else:
            rs2 = registers[args[2]]
    else:
      # It's a comment, not an instruction
      return None, None, asm
#-----------------------------------------------------------------------------------------------------#
    #else:
    #    return 0,0,0,0,0
    #(opcode, rd, rs1, rs2, imm )
    binary_instructions = [xlen(4, opcode, 0), xlen(4, rd, 0), xlen(4, rs1, 0), xlen(4, rs2, 0), xlen(8, imm, 0)]
    return ''.join(binary_instructions), binary_instructions, asm

#-----------------------------------------------------------------------------------------------------#

output_filename = os.path.splitext(input_file.name)[0] + '.' + output_format

with open(output_filename, 'w') as output_file:
  out = []

  asm_code = read_file(input_file)

  output_buffer = []

  for line in asm_code:
      instructions, instuctions_list, asm = asmtoint(line)

      lst = asm

      if instuctions_list:
        lst = asm + ' -> ' + ' '.join(instuctions_list) + ' -> ' + ''.join(instuctions_list)

      if output_format == 'bin' and instructions:
        output_buffer.append(instructions)
      elif output_format == 'lst':
        output_buffer.append(lst)

  string_buffer = '\n'.join(output_buffer)
  
  output_file.write(string_buffer)
  print string_buffer


#------------------------------------------------------------------------------------------------------#
