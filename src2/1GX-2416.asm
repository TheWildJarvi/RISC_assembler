add s2, t0, t1
or s4, t1, ra
or s3, ra, 0b110000
and s1, s3, 0x30
add s2, t0, 0d48
#this line will generate an exception: or s2, t1, 0b101001011111
