
payload2.o:     file format elf32-littleriscv


Disassembly of section .text.startup:

00000000 <main>:
   0:	451d                	li	a0,7
   2:	d40d35b7          	lui	a1,0xd40d3
   6:	44458593          	addi	a1,a1,1092 # d40d3444 <main+0xd40d3444>
   a:	00000073          	ecall
   e:	4515                	li	a0,5
  10:	4581                	li	a1,0
  12:	00000073          	ecall
  16:	4519                	li	a0,6
  18:	800045b7          	lui	a1,0x80004
  1c:	92058593          	addi	a1,a1,-1760 # 80003920 <main+0x80003920>
  20:	00000073          	ecall
  24:	4505                	li	a0,1
  26:	4581                	li	a1,0
  28:	4601                	li	a2,0
  2a:	00000073          	ecall
  2e:	4501                	li	a0,0
  30:	8082                	ret
