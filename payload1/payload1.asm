
payload1.o:     file format elf32-littleriscv


Disassembly of section .text:

00000000 <main>:
   0:	1141                	addi	sp,sp,-16
   2:	c622                	sw	s0,12(sp)
   4:	0800                	addi	s0,sp,16
   6:	450d                	li	a0,3
   8:	800045b7          	lui	a1,0x80004
   c:	9a458593          	addi	a1,a1,-1628 # 800039a4 <main+0x800039a4>
  10:	4611                	li	a2,4
  12:	00000073          	ecall
  16:	4505                	li	a0,1
  18:	4581                	li	a1,0
  1a:	4601                	li	a2,0
  1c:	00000073          	ecall
  20:	4781                	li	a5,0
  22:	853e                	mv	a0,a5
  24:	4432                	lw	s0,12(sp)
  26:	0141                	addi	sp,sp,16
  28:	8082                	ret
