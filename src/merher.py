import re

def read_file(filename):
    s = []
    with open(filename) as f:
            s = f.read().splitlines()
    return s



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
    'sp': 14,
    'ra': 15 }

def asmtoint(asm):
    asm_split = re.split(" |, |\(|\)", asm)
    args = []
    for i in range (len(asm_split)):
        if (asm_split[i] != ""):
            args.append(asm_split[i])
    #print args
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
        opcode = 1
        rd = registers[args[1]]
        rs1 = registers[args[2]]
        rs2 = registers[args[3]]

    elif (args[0] == "addi"):
        if (len(args) != 4):
            return 0, 0, 0, 0, 0
        opcode = 1
        rd = registers[args[1]]
        rs1 = registers[args[2]]
        imm = convert_to_int(args[3])

    elif (args[0] == "adc"):
        if (len(args) != 4):
            return 0, 0, 0, 0, 0
        opcode = 2
        rd = registers[args[1]]
        rs1 = registers[args[2]]
        rs2 = registers[args[3]]

    elif (args[0] == "adci"):
        if (len(args) != 4):
            return 0, 0, 0, 0, 0
        opcode = 2
        rd = registers[args[1]]
        rs1 = registers[args[2]]
        imm = convert_to_int(args[3])

    elif (args[0] == "sub"):
        if (len(args) != 4):
            return 0, 0, 0, 0, 0
        opcode = 3
        rd = registers[args[1]]
        rs1 = registers[args[2]]
        rs2 = registers[args[3]]

    elif (args[0] == "subi"):
        if (len(args) != 4):
            return 0, 0, 0, 0, 0
        opcode = 3
        rd = registers[args[1]]
        rs1 = registers[args[2]]
        imm = convert_to_int(args[3])

    elif (args[0] == "cmp"):
        if (len(args) != 3):
            return 0, 0, 0, 0, 0
        opcode = 4
        rs1 = registers[args[1]]
        rs2 = registers[args[2]]

    elif (args[0] == "cmpi"):
        if (len(args) != 3):
            return 0, 0, 0, 0, 0
        opcode = 4
        rs1 = registers[args[1]]
        imm = convert_to_int(args[2])

    elif (args[0] == "or"):
        if (len(args) != 4):
            return 0, 0, 0, 0, 0
        opcode = 5
        rd = registers[args[1]]
        rs1 = registers[args[2]]
        rs2 = registers[args[3]]

    elif (args[0] == "ori"):
        if (len(args) != 4):
            return 0, 0, 0, 0, 0
        opcode = 5
        rd = registers[args[1]]
        rs1 = registers[args[2]]
        imm = convert_to_int(args[3])

    elif (args[0] == "and"):
        if (len(args) != 4):
            return 0, 0, 0, 0, 0
        opcode = 6
        rd = registers[args[1]]
        rs1 = registers[args[2]]
        rs2 = registers[args[3]]

    elif (args[0] == "andi"):
        if (len(args) != 4):
            return 0, 0, 0, 0, 0
        opcode = 6
        rd = registers[args[1]]
        rs1 = registers[args[2]]
        imm = convert_to_int(args[3])

    elif (args[0] == "xnor"):
        if (len(args) != 4):
            return 0, 0, 0, 0, 0
        opcode = 7
        rd = registers[args[1]]
        rs1 = registers[args[2]]
        rs2 = registers[args[3]]

    elif (args[0] == "xnori"):
        if (len(args) != 4):
            return 0, 0, 0, 0, 0
        opcode = 7
        rd = registers[args[1]]
        rs1 = registers[args[2]]
        imm = convert_to_int(args[3])

    elif (args[0] == "shft"):
        if (len(args) != 4):
            return 0, 0, 0, 0, 0
        opcode = 8
        rd = registers[args[1]]
        rs1 = registers[args[2]]
        rs2 = registers[args[3]]

    elif (args[0] == "shfti"):
        if (len(args) != 4):
            return 0, 0, 0, 0, 0
        opcode = 8
        rd = registers[args[1]]
        rs1 = registers[args[2]]
        imm = convert_to_int(args[3])
#--------------------------------------------------------------------
# ABSOLUTE BRANCH INSTRUCTIONS
#--------------------------------------------------------------------
    elif (args[0] == "beq"):
        if (len(args) != 2):
            return 0, 0, 0, 0, 0
        opcode = 9
        rd =  '0'
        rs2 = registers[args[1]]

    elif (args[0] == "beqi"):
        if (len(args) != 2):
            return 0, 0, 0, 0, 0
        opcode = 9
        rd =  '0'
        imm = convert_to_int(args[1])

    elif (args[0] == "bneq"):
        if (len(args) != 2):
            return 0, 0, 0, 0, 0
        opcode = 9
        rd =  '2'
        rs2 = registers[args[1]]

    elif (args[0] == "bneqi"):
        if (len(args) != 2):
            return 0, 0, 0, 0, 0
        opcode = 9
        rd =  '2'
        imm = convert_to_int(args[1])

    elif (args[0] == "bgt"):
        if (len(args) != 2):
            return 0, 0, 0, 0, 0
        opcode = 9
        rd =  '4'
        rs2 = registers[args[1]]

    elif (args[0] == "bgti"):
        if (len(args) != 2):
            return 0, 0, 0, 0, 0
        opcode = 9
        rd =  '4'
        imm = convert_to_int(args[1])

    elif (args[0] == "bgte"):
        if (len(args) != 2):
            return 0, 0, 0, 0, 0
        opcode = 9
        rd =  '6'
        rs2 = registers[args[1]]

    elif (args[0] == "bgtei"):
        if (len(args) != 2):
            return 0, 0, 0, 0, 0
        opcode = 9
        rd =  '6'
        imm = convert_to_int(args[1])

    elif (args[0] == "blt"):
        if (len(args) != 2):
            return 0, 0, 0, 0, 0
        opcode = 9
        rd =  '8'
        rs2 = registers[args[1]]

    elif (args[0] == "blti"):
        if (len(args) != 2):
            return 0, 0, 0, 0, 0
        opcode = 9
        rd =  '8'
        imm = convert_to_int(args[1])

    elif (args[0] == "blte"):
        if (len(args) != 2):
            return 0, 0, 0, 0, 0
        opcode = 9
        rd =  '10'
        rs2 = registers[args[1]]

    elif (args[0] == "bltei"):
        if (len(args) != 2):
            return 0, 0, 0, 0, 0
        opcode = 9
        rd =  '10'
        imm = convert_to_int(args[1])
# --------------------------------------------------------------------
# RELATIVE BRANCH INSTRUCTIONS
# --------------------------------------------------------------------
    elif (args[0] == "breq"):
        if (len(args) != 2):
            return 0, 0, 0, 0, 0
        opcode = 9
        rd =  '1'
        rs2 = registers[args[1]]

    elif (args[0] == "breqi"):
        if (len(args) != 2):
            return 0, 0, 0, 0, 0
        opcode = 9
        rd =  '1'
        imm = convert_to_int(args[1])

    elif (args[0] == "brneq"):
        if (len(args) != 2):
            return 0, 0, 0, 0, 0
        opcode = 9
        rd =  '3'
        rs2 = registers[args[1]]

    elif (args[0] == "brneqi"):
        if (len(args) != 2):
            return 0, 0, 0, 0, 0
        opcode = 9
        rd =  '3'
        imm = convert_to_int(args[1])

    elif (args[0] == "brgt"):
        if (len(args) != 2):
            return 0, 0, 0, 0, 0
        opcode = 9
        rd =  '5'
        rs2 = registers[args[1]]

    elif (args[0] == "brgti"):
        if (len(args) != 2):
            return 0, 0, 0, 0, 0
        opcode = 9
        rd =  '5'
        imm = convert_to_int(args[1])

    elif (args[0] == "brgte"):
        if (len(args) != 2):
            return 0, 0, 0, 0, 0
        opcode = 9
        rd =  '7'
        rs2 = registers[args[1]]

    elif (args[0] == "brgtei"):
        if (len(args) != 2):
            return 0, 0, 0, 0, 0
        opcode = 9
        rd =  '7'
        imm = convert_to_int(args[1])

    elif (args[0] == "brlt"):
        if (len(args) != 2):
            return 0, 0, 0, 0, 0
        opcode = 9
        rd =  '9'
        rs2 = registers[args[1]]

    elif (args[0] == "brlti"):
        if (len(args) != 2):
            return 0, 0, 0, 0, 0
        opcode = 9
        rd =  '9'
        imm = convert_to_int(args[1])

    elif (args[0] == "brlte"):
        if (len(args) != 2):
            return 0, 0, 0, 0, 0
        opcode = 9
        rd =  '11'
        rs2 = registers[args[1]]

    elif (args[0] == "brltei"):
        if (len(args) != 2):
            return 0, 0, 0, 0, 0
        opcode = 9
        rd =  '11'
        imm = convert_to_int(args[1])
# --------------------------------------------------------------------
# ABSOLUTE JUMP AND LINK INSTRUCTIONS
# --------------------------------------------------------------------
    elif (args[0] == "jal"):
        if (len(args) != 2):
            return 0, 0, 0, 0, 0
        opcode = 10
        rd =  '0'
        rs2 = registers[args[1]]

    elif (args[0] == "jali"):
        if (len(args) != 2):
            return 0, 0, 0, 0, 0
        opcode = 10
        rd =  '0'
        imm = convert_to_int(args[1])
# --------------------------------------------------------------------
# RELATIVE JUMP AND LINK INSTRUCTIONS
# --------------------------------------------------------------------
    elif (args[0] == "jral"):
        if (len(args) != 2):
            return 0, 0, 0, 0, 0
        opcode = 10
        rd = '1'
        rs2 = registers[args[1]]

    elif (args[0] == "jrali"):
        if (len(args) != 2):
            return 0, 0, 0, 0, 0
        opcode = 10
        rd = '1'
        imm = convert_to_int(args[1])

# --------------------------------------------------------------------
# ABSOLUTE JUMP AND LINK REGISTER INSTRUCTIONS
# --------------------------------------------------------------------
    elif (args[0] == "jalr"):
        if (len(args) != 3):
            return 0, 0, 0, 0, 0
        opcode = 10
        rd = '8'
        rs1 = registers[args[1]]
        rs2 = registers[args[2]]

    elif (args[0] == "jalri"):
        if (len(args) != 3):
            return 0, 0, 0, 0, 0
        opcode = 10
        rd = '8'
        rs1 = registers[args[1]]
        imm = convert_to_int(args[2])
# --------------------------------------------------------------------
# RELATIVE JUMP AND LINK REGISTER INSTRUCTIONS
# --------------------------------------------------------------------
    elif (args[0] == "jralr"):
        if (len(args) != 3):
            return 0, 0, 0, 0, 0
        opcode = 10
        rd = '9'
        rs1 = registers[args[1]]
        rs2 = registers[args[2]]

    elif (args[0] == "jralri"):
        if (len(args) != 3):
            return 0, 0, 0, 0, 0
        opcode = 10
        rd = '9'
        rs1 = registers[args[1]]
        imm = convert_to_int(args[2])
# --------------------------------------------------------------------
# LOAD INSTRUCTIONS
# --------------------------------------------------------------------

    elif (args[0] == "ld"):
        if (len(args) != 3):
            return 0, 0, 0, 0, 0
        opcode = 11
        rs1 = 0
        rd = registers[args[1]]
        rs2 = registers[args[2]]

    elif (args[0] == "ldi"):
        if (len(args) != 3):
            return 0, 0, 0, 0, 0
        opcode = 11
        rs1 = 0
        rd = registers[args[1]]
        imm = convert_to_int(args[2])

    elif (args[0] == "st"):
        if (len(args) != 3):
            return 0, 0, 0, 0, 0
        opcode = 11
        rs1 = 1
        rd = registers[args[1]]
        rs2 = registers[args[2]]

    elif (args[0] == "sti"):
        if (len(args) != 3):
            return 0, 0, 0, 0, 0
        opcode = 11
        rs1 = 1
        rd = registers[args[1]]
        imm = convert_to_int(args[2])

    else:
        return 0,0,0,0,0
    return opcode, rd, rs1, rs2, imm


out = []

asm_code = read_file('C:\\Users\\Alex\\PycharmProjects\\MCRISCassembler\\src\\24bitASMtest.asm')  # STICK PATH HERE AS STRING LIKE SO  -> 'file.asm'

for line in asm_code:
    out.append(asmtoint(line))

#test_input = 'sti, ra, 0x03'
#print(asmtoint(test_input))
print out