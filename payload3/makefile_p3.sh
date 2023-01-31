#!/bin/bash

# Exit on failure of any command.
set -e
#cd payload3

rm -f payload3.o payload3.asm payload3.hex

riscv64-unknown-elf-gcc -nostartfiles -nostdlib -Tlinker.ld --entry=_start -Wl,--gc-sections -mno-relax -march=rv32imac -mabi=ilp32 -mtune=sifive-3-series -Os -c payload3.c -save-temps
riscv64-unknown-elf-objdump -d payload3.o > payload3.asm
riscv64-unknown-elf-objcopy -O verilog payload3.o
#python3 hex_code_p2.py

echo "Final payload3 generated in payload3.hex"

rm -f payload3.i payload3.s 

