            limm r1 0x05
            limm r2 0x05
            limm r3 0x01
            limm r4 0x00
            limm r5 0x00
            cmp r2 r0
            beq 0d16
            and r5 r2 r3
            cmp r5 r0
            beq 0d12
            add r4 r4 r1
            add r1 r1 r1
            rshft r2 r2 r0
            cmp r0 r0
            beq 0d6

