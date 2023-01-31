Unfortunately this exploit was not successful. However the approach to the exploit building is written below

1. An interrupt is triggered from user mode by setting the a0 reg to 94 (as reverse engineering showed that the timer interrupt code was 94). Then a ecall is triggered to switch privilege to M-Mode

2. A character array with the command AT+RST is initialised in the trap handler at location 0x8001000

3.In the M-Mode the function for sending a command to ESP via SPI is called (inst 0x20000208), the arguments a0 being the address of the AT+RST command