import subprocess
import os
code = ""
with open('payload1.o', 'r') as binary:
	lines = binary.readlines()
	for i in lines:
		if(i!=lines[0]):
			code = code+((str(i).replace(" ","")).replace("\n",""))
	ecall = '73000000'		
	code = code.split(ecall)
	code[0] = code[0].split('0008')
	fin_code = code[0][1]+ecall
	for i in range(1,2):
		fin_code = fin_code + code[i]+ecall
with open('payload1.hex', 'w') as final_hex: final_hex.write(fin_code)	
