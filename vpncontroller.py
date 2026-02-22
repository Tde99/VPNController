#!/usr/bin/env python
import os
import shlex
os.system("apt-get install figlet")
os.system("clear")
def menu():
	try:
		while True:
			os.system("figlet VPN CONTROLLER")
			print(""" 
Welcome to VPN controller 	
			""")
			ipcont = input("Enter the target IP: ")
			if not ipcont:
				continue
			
			target_ip = shlex.quote(ipcont)
			print(f"Scaning {target_ip} for the Main Mode ")
			os.system("ike-scan " + ipcont)
			
			print(f"\nTesting {target_ip} for Aggressive Mode ")
			os.system(f"ike-scan --aggressive --id=vpnclient {target_ip}")
			
			if os.path.exists("hash.txt"):
				print("Hash captured! Starting psk-crack")
				os.system("\npsk-crack hash.txt")
			cont = input("\nScan another IP? (Y/n): ")
			if cont.lower() == 'y':
				os.system("clear")
				continue
			else:
				print("Exiting...")
				break
	except KeyboardInterrupt:
        	print(" Exiting....")				
if __name__ == "__main__":
	menu()		
