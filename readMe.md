SHORT SUMMARY OF THE WAY THE EXPLOIT WORKS:

* Connect to the board via JLink, reset riscv
* Connect to ESP via pyserial, Parse bootlog for MAC address, reset, close connection
* Make password from MAC address, unlock the board
* Pass 'l' when the game menu loads.(Game iteration 1)
* Send custom game size to be 0x800
* Generate payload1 by running makefile_p1.sh from python script. Makefile uses the payload1.c file as a base, compiles with riscv64-unknown-elf toolchain and creates a .o file with instruction binary. A small python script then process .o file and extracts hex for only relevant instructions.
* (The payload1.c is written with basic inlined assembly code)
* Send Payload1 which executes Syscall 3 and Syscall 1. Flood the rest of the buffer with 'A'.
* Now the secret debug key is present on the console.
* The main python script parses the console output for the debug key.
* The debug key is now appended to the payload2.c file used to generate payload2.
* Generate payload2 by running makefile_p2.sh from python script. Makefile uses the payload2.c file as a base, compiles with riscv64-unknown-elf toolchain and creates a .o file with instruction binary. A small python script then process .o file and extracts hex for only relevant instructions.
* (The payload2.c is also written with basic inlined assembly code)
* Pass 'l' when the game menu loads (Game iteration 2)
* Send custom game size to be 0x800
* Send Payload2 which executes the following syscalls in order.Flood the rest of the buffer with 'B'.
  Syscall 7 - to unlock priviledged syscalls
  Syscall 5 - to set stack size(for this exercise it is hardcoded to 0). If needed this can be changed in the main script(line 80)
  Syscall 6 - to get stack bottom address and overwrite to stack_size (address 0x80003920 is overwritten with 80003000)
  (R/W priviledges extended to include control over GPIO MMIO)
  Syscall 1 - to exit game
* Send Payload3 which configures the GPIO and turns the Blue LED.Flood the rest of the buffer with 'C'.
* Main Script processes console information, parses and prints stack bottom address	
	

