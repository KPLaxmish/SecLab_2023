
payload3.o:     file format elf32-littleriscv


Disassembly of section .text.startup:

00000000 <main>:
   0:	09400513          	li	a0,148
   4:	4581                	li	a1,0
   6:	4601                	li	a2,0
   8:	00000073          	ecall
   c:	08001537          	lui	a0,0x8001
  10:	00050513          	mv	a0,a0
  14:	4581                	li	a1,0
  16:	4601                	li	a2,0
  18:	20000837          	lui	a6,0x20000
  1c:	20880813          	addi	a6,a6,520 # 20000208 <main+0x20000208>
  20:	000800e7          	jalr	a6
  24:	4501                	li	a0,0
  26:	8082                	ret
