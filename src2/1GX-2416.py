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

def read_file(f):
    s = []
    s = f.read().splitlines()
    return s


def convert(a, base=4):
    if a < 0:
        a = a & pow(2,base)-1
    return format(a, '0' + repr(base) + 'b')

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

    if not asm:
        return '',[], asm

    asm_split = re.split(" |, |\(|\)", asm)
    args = []
    i=0
    for i in range (len(asm_split)):
        if (asm_split[i] != ""):
            args.append(asm_split[i])
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
            imm = convert_to_int(args[3])
            rs2 = 0
        else:
            rs2 = registers[args[3]]
            imm = 0

    elif (args[0] == "addv"): #no immediate used for add vector
        if (len(args) != 4):
            return 0, 0, 0, 0, 0
        opcode = 1
        rd = registers[args[1]]
        rs1 = registers[args[2]]
        rs2 = registers[args[3]]
        imm = 0

    elif (args[0] == "adc"):
        if (len(args) != 4):
            return 0, 0, 0, 0, 0
        opcode = 2
        rd = registers[args[1]]
        rs1 = registers[args[2]]
        if args[3][:2] in ["0x", "0d", "0b"]:
            imm = convert_to_int(args[3])
            rs2 = 0
        else:
            rs2 = registers[args[3]]
            imm = 0

    elif (args[0] == "sub"):
        if (len(args) != 4):
            return 0, 0, 0, 0, 0
        opcode = 3
        rd = registers[args[1]]
        rs1 = registers[args[2]]
        if args[3][:2] in ["0x", "0d", "0b"]:
            imm = convert_to_int(args[3])
            rs2 = 0
        else:
            rs2 = registers[args[3]]
            imm = 0

    elif (args[0] == "nor"):
        if (len(args) != 4):
            return 0, 0, 0, 0, 0
        opcode = 4
        rd = registers[args[1]]
        rs1 = registers[args[2]]
        if args[3][:2] in ["0x", "0d", "0b"]:
            imm = convert_to_int(args[3])
            rs2 = 0
        else:
            rs2 = registers[args[3]]
            imm = 0

    elif (args[0] == "and"):
        if (len(args) != 4):
            return 0, 0, 0, 0, 0
        opcode = 5
        rd = registers[args[1]]
        rs1 = registers[args[2]]
        if args[3][:2] in ["0x", "0d", "0b"]:
            imm = convert_to_int(args[3])
            rs2 = 0
        else:
            rs2 = registers[args[3]]
            imm = 0

    elif (args[0] == "xor"):
        if (len(args) != 4):
            return 0, 0, 0, 0, 0
        opcode = 6
        rd = registers[args[1]]
        rs1 = registers[args[2]]
        if args[3][:2] in ["0x","0d","0b"]:
            imm = convert_to_int(args[3])
            rs2 = 0
        else:
            rs2 = registers[args[3]]
            imm = 0

    elif (args[0] == "abs"):
        if (len(args) != 3):
            return 0, 0, 0, 0, 0
        opcode = 7
        rd = registers[args[1]]
        rs1 = 0
        rs2 = registers[args[2]]
        imm = 0

    elif (args[0] == "limm"): #IMM is 16 bits, top byte goes into rs1,rs2, and low byte goes into imm
        if (len(args) != 3):
            return 0, 0, 0, 0, 0
        opcode = 8
        rd = registers[args[1]]
        #convert args[2] into 2 4bit nibbles and a byte.
        rs1 = (convert_to_int(args[2]) >> 12) & 0x0f #grab high nib
        rs2 = (convert_to_int(args[2]) >> 8) & 0x0f #grab low nib
        imm = convert_to_int(args[2]) & 0xff  #grab low byte

    elif (args[0] == "rshft"):
        if (len(args) != 3):
            return 0, 0, 0, 0, 0
        opcode = 9
        rd = registers[args[1]]
        rs1 = 0
        rs2 = registers[args[2]]
        imm = 0


    elif (args[0] == "tset"):
        if (len(args) != 5):
           return 0, 0, 0, 0, 0
        opcode = 10
        rd = registers[args[1]]
        rs1 = registers[args[2]]
        rs2 = registers[args[3]]

        if args[4] == 'lt':
           imm = 1
        elif args[4] == 'lteq':
           imm = 2
        elif args[4] == 'eq':
           imm = 4
        elif args[4] == 'gtreq':
           imm = 8
        elif args[4] == 'gtr':
           imm = 16
        else:
           imm = 0

    elif (args[0] == "mvflg"): #if imm = 0 then move flags to GPR, else flags move to GPR
        if (len(args) != 3):
            return 0, 0, 0, 0, 0
        opcode = 11

        #if args[2][:2] in ["0x", "0d", "0b"]:
        imm = convert_to_int(args[2])

        if imm == 0:
            rd = 0
            rs1 = registers[args[1]]
            rs2 = 0
        elif imm == 1:
            rd = registers[args[1]]
            rs1 = 0
            rs2 = 0
            imm = 1


    elif (args[0] == "push"):
        if (len(args) != 2):
            return 0, 0, 0, 0, 0
        opcode = 12
        rd = 0
        rs1 = registers[args[1]]
        rs2 = 0
        imm = 0


    elif (args[0] == "pop"):
        if (len(args) != 2):
            return 0, 0, 0, 0, 0
        opcode = 12
        rd = registers[args[1]]
        rs1 = 0
        rs2 = 0
        imm = 1

    elif (args[0] == "lw"):   #load word rs2 msb must = 1, , if imm then bit 2, 1, 0 of rs2, and all 8 bits of IMM field are used
        if (len(args) != 3):
            return 0, 0, 0, 0, 0
        opcode = 13
        # example) lw s0, 0x7ff(max value) s0 <=ram[0x7ff]
        rd = registers[args[1]]  # s1 in the example

        if args[2][:2] in ["0x", "0d", "0b"]:
            rs1 = 0
            imm = convert_to_int(args[2])
            rs2 = (imm >> 8) & 0x07  # bit 3 = 1, grab bits [10:8] from imm
            rs2 += 8
            imm = imm & 0xff #imm get low 8 bits[7:0] convert imm to 8 bits
        # example) lw s1, s0    s1 <= ram[s0[]]
        else:

            rs1 = registers[args[2]] #s2 in the example
            rs2 = 8 # bit 3 = 1
            imm = 0 # no imm


    elif (args[0] == "sw"):  #store word basically the same as lw but msb of rs2 = 0
        if (len(args) != 3):
            return 0, 0, 0, 0, 0
        opcode = 13
        rd = registers[args[1]]
        #example
        if args[2][:2] in ["0x", "0d", "0b"]:
            rs1 = 0
            imm = convert_to_int(args[2])
            rs2 = (imm >> 8) & 0x07  # bit 3 = 0, grab bits [10:8] from imm
            imm = imm & 0xff #imm get low 8 bits[7:0] convert imm to 8 bits
        # example) lw s1, s0    s1 <= ram[s0[]]
        else:
            rs1 = registers[args[2]] #s2 in the example
            rs2 = 0 # bit 3 = 1
            imm = 0 # no imm

    elif (args[0] == "jmp")
        opcode = 14



jmp

jal
jalr





    else:
      # It's a comment, not an instruction
      return '', [] , asm
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
        lst = asm + '\t -> ' + ' '.join(instuctions_list) + '\t -> ' + ''.join(instuctions_list)

      if output_format == 'bin' and instructions:
        output_buffer.append(instructions)
      elif output_format == 'lst':
        output_buffer.append(lst)

  string_buffer = '\n'.join(output_buffer)
  
  output_file.write(string_buffer)
  #print string_buffer


#------------------------------------------------------------------------------------------------------#
