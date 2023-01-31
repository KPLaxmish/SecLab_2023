import subprocess
import os
code = ""
fin_code = ""
with open('payload2.o', 'r') as binary:
	lines = binary.readlines()
	for i in lines:
		if(i!=lines[0]):
			code = code+((str(i).replace(" ","")).replace("\n",""))
	ecall = '73000000'		
	code = code.split(ecall)
	for i in range(0,4):
		fin_code = fin_code + code[i]+ecall
with open('payload2.hex', 'w') as final_hex: final_hex.write(fin_code)	
