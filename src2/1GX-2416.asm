add   s0, s1,   s2
add   s0, s1, 0x45
adc   s0, s1,   s2
adc   s0, s1, 0x45
addv  s0, s1,   s2
sub   s0, s1,   s2
sub   s0, s1, 0x45
nor   s0, s1,   s2
nor   s0, s1, 0x45
and   s0, s1,   s2
and   s0, s1, 0x45
xor   s0, s1,   s2
xor   s0, s1, 0x45
abs   s0,       s1
limm  s0,   0x4321
rshft s0,       s1


tset  s5, t4, t3, lteq


#test a comment

mvflg s3, 0x00

#should move flags reg to s3

mvflg s3, 0x01

#should move s3 to flags reg

push s0
push s1

pop  s1
pop  s0

#RAM
lw s0, 0x7ff
#7FF is max ram addr
lw s1,    s0

sw s2, 0x7FF
sw s3,    s2


