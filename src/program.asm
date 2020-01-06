//r7 = RAM pointer, r0 = zero, all other regs are GPRs
limm r1 0x01
limm r2 0x01
limm r3 0x01
//constant of 1
limm r7 0x00
//initialize RAM_PTR to 0
limm r4 0d233

cmp r2 r4
beq 0d26
disp r1 r2 0x03
seg r1 0b01
add r1 r1 r2
disp r1 r2 0x03
seg r1 0b01
add r2 r1 r2
//``````````````
wram r1 r7
//write r1 into address contained in r7
add r7 r7 r3
wram r2 r7
//write r2 into address contained in r7
add r7 r7 r3
//
cmp r0 r0
beq 0d06
//--------------
//---------
rram r1 r7
seg r1 0b01
sub r7 r7 r3
rram r2 r7
seg r1 0b10
sub r7 r7 r3
cmp r7 r0
beq 0d40
cmp r0 r0
beq 0d26
//test shit
wram r3 0xff
wram r3 0b11111111
wram r3 0d255

rram r3 0xff
rram r3 0b11111111
rram r3 0d255
//end test shit

