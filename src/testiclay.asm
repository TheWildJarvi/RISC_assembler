        addi    t0, r0, 0x01 //load 1 into t0
        addi    t1, r0, 0x01 //load 1 into t1
loop    cmpi    t1, 0d233    // cmp t1 and 233
        bgtei   done         // branch if equal or greater to 'done'
        add     t0, t0, t1   // a = a+b
        add     t1, t0, t1   // b = a+b
        cmp r0, r0           // compare 0 with 0 (obviously =)
        beq loop             // goto 'loop'
done

add t1, s1, 0b10
add t2, s2, 0d10
add t3, s3, s4