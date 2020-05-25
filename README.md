# 1GX-2416_assembler
AUTHORS:
### - TheWildJarvi
### - Nano
### - Lululombard


# File SRC2 contains the updated version

Use any python ide like pycharm or repl.it to run it. You can easily change the way it works for your own risc ISA. You can chage the amount of arguments per instruction, and how large they should be.

This is designed for a 24bit instruction word stored in PROM where each instruction is fetched in a single cycle. It is deisgned for a 16 bit Data loop. 


### It is currently not finished for my new ISA but works with my old one
You can look thru the instructions to see what you can put in your .asm file
You can look at my example ASM code to see how it works

Immediates do not need to be specified, ie) there is no addi, just use add, and replace rs2 with an immediate. 0x, 0d, and 0b immediates are all allowed and will generate an exception if the immediate size you enter is out of range.
