registers = {
    'r0': '000',
    'r1': '001',
    'r2': '010',
    'r3': '011',
    'r4': '100',
    'r5': '101',
    'r6': '110',
    'r7': '111',
}

alu_op = {
    'add': '001',
    'sub': '010',
    'nor': '011',
    'and': '100',
    'xnor': '101',
    'rshft': '110',
    'cmp': '111',
}

branch = {
    'bgt': '100',
    'beq': '010',
    'blt': '001',
}

LIMM = {
    'limm': '000'
}

RAM = {
    'rram': '000',
    'wram': '001'
}

DISPLAY = {
    'disp': '000'
}

SEGMENT = {
    'seg': '000'
}

def convert_to_int(s):
    if s[1] == 'x':
        return int(s[2:], 16)
    elif s[1] == 'b':
        return int(s[2:], 2)
    elif s[1] == 'd':
        return int(s[2:], 10)
    else:
        return 0


def int_to_binary(i):
    return bin(i)[2:]


def string_to_binary(s, lenght=8):
    value = int_to_binary(convert_to_int(s))
    for i in range(lenght - len(value)):
        value = '0' + value
    return value


def read_file(filename):
    with open(filename, 'r') as f:
        s = f.read()
    return s


def line_to_code(line):
    current_line = ''
    words = line.split(' ')
    op = words[0]
    print(words)
    if op in alu_op:
        current_line = current_line + '0001'
        if op == 'cmp':
            current_line = current_line + '000'
        for word in words[1:]:
            current_line = current_line + ' ' + registers[word]
        current_line = current_line + ' ' + alu_op[op]
    elif op in branch:
        current_line = current_line + '0010'
        current_line = current_line + ' ' + branch[op]
        if words[1][0] == 'r':
            current_line = current_line + ' 1 00 ' + registers[words[1]] + ' 000'
        else:
            current_line = current_line + ' 0 ' + string_to_binary(words[1])
    elif op in LIMM:
        current_line = current_line + '0011'
        current_line = current_line + ' ' + registers[words[1]] + ' 0'
        current_line = current_line + string_to_binary(words[2])
    elif op in RAM:
        if op == 'rram':
            current_line = current_line + '0100'
        else:
            current_line = current_line + '0101'
        current_line = current_line + ' ' + registers[words[1]]
        if words[2][0] == 'r':
            current_line = current_line + ' 100' + registers[words[2]] + '000'
        else:
            current_line = current_line + ' 0' + string_to_binary(words[2])
    elif op in DISPLAY:
        current_line = current_line + '0110' + '000'
        current_line = current_line + ' ' + registers[words[1]]
        current_line = current_line + ' ' + registers[words[2]]
        current_line = current_line + ' ' + string_to_binary(words[3], 3)
    elif op in SEGMENT:
        current_line = current_line + '0111' + '000'
        current_line = current_line + ' ' + registers[words[1]]
        current_line = current_line + ' 0000' + string_to_binary(words[2], 2)

    print(current_line)
    return current_line.replace(" ", "")


def asm_to_binary(asm):
    outputcode = []
    for line in asm.splitlines():
        if line.startswith('//'):
            continue
        code = line_to_code(line)
        if code is not None and code != '':
            outputcode.append(code)
    return outputcode


asm_code = read_file('C:\\Users\\Alex\\PycharmProjects\\MCRISCassembler\\src\\multy.asm')  # STICK PATH HERE AS STRING LIKE SO  -> 'file.asm'
binary_code = asm_to_binary(asm_code)
print()
for index, code_line in enumerate(binary_code):
    print(repr(index) + ': ' + repr(code_line))


