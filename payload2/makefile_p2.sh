#!/bin/bash

# Exit on failure of any command.
set -e
cd payload2

rm -f payload2.o payload2.asm payload2.hex

riscv64-unknown-elf-gcc -nostartfiles -nostdlib -mno-relax -march=rv32imac -mabi=ilp32 -mtune=sifive-3-series -Os -c payload2.c -save-temps
riscv64-unknown-elf-objdump -d payload2.o > payload2.asm
riscv64-unknown-elf-objcopy -O verilog payload2.o
python3 hex_code_p2.py

echo "Final payload2 generated in payload2.hex"

rm -f payload2.i payload2.s 
