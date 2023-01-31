#!/bin/bash

# Exit on failure of any command.
set -e
cd payload1

rm -f payload1.o payload1.asm payload1.hex

riscv64-unknown-elf-gcc -nostartfiles -nostdlib -mno-relax -march=rv32imac -mabi=ilp32 -c payload1.c -save-temps
riscv64-unknown-elf-objdump -d payload1.o > payload1.asm
riscv64-unknown-elf-objcopy -O verilog payload1.o
python3 hex_code_p1.py

echo "Final payload1 generated in payload1.hex"

rm -f payload1.i payload1.s 
