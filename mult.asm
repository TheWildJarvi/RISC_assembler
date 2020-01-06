limm r1 multiplicand
limm r2 multiplier
limm r3 0x01
//bitmask
limm r4 0x00
//result register
limm r5 0x00
//test register

loop
        cmp r2 r0
        beq done
        //test multiplier for odd
        and r5 r2 r3
        //set lsb of r5(test reg) to 1 if multiplier is odd
        cmp r5 r0
        beq SOMEWHERE
        //if its even go somewhere(dont add multiplicand to result)
        add r4 r4 r1
        //add multiplicand to result
somewhere
        add r1 r1 r1
        //left shift multiplicand
        rshft r2 r2 r0
        //rshft the multiplier
        cmp r0 r0
        beq loop
done
