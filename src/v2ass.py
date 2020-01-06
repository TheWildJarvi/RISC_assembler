opcode = '0000'
rd = '0000'
rs1 = '0000'
rs2 = '0000'
imm = '00000000'

registers = {
    'r0': 0,
    't0': 1,
    't1': '0010',
    't2': '0011',
    't3': '0100',
    't4': '0101',
    's0': '0110',
    's1': '0111',
    's2': '1000',
    's3': '1001',
    's4': '1010',
    's5': '1011',
    's6': '1100',
    'r13': '1101',
    'sp': '1110',
    'ra': '1111' }

#opcode = {z`
#    add
#}

#instruction = opcode + rd + rs1 + rs2 + imm
#--------------------------------------------------------------------
    if (args[0] == "add"):
        if (len(args) != 4):
            return 0, 0, 0, 0, 0
        opcode = 1
        rd = registers[args[1]]
        rs1 = registers[args[2]]
        if (args[3])
        rs2 = registers[args[3]]

    elif (args[0] == "addi"):
        if (len(args) != 4):
            return 0, 0, 0, 0, 0
        opcode = 1
        rd = registers[args[1]]
        rs1 = registers[args[2]]
        imm = convert_to_int(args[3])
