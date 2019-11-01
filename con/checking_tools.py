import os
from time import sleep

checking_tools = """

\033[36m 

           __                            __        __                                 
          /  |                          /  |      /  |                                
  _______ $$ |____    ______    _______ $$ |   __ $$/  _______    ______              
 /       |$$      \  /      \  /       |$$ |  /  |/  |/       \  /      \             
/$$$$$$$/ $$$$$$$  |/$$$$$$  |/$$$$$$$/ $$ |_/$$/ $$ |$$$$$$$  |/$$$$$$  |            
$$ |      $$ |  $$ |$$    $$ |$$ |      $$   $$<  $$ |$$ |  $$ |$$ |  $$ |            
$$ \_____ $$ |  $$ |$$$$$$$$/ $$ \_____ $$$$$$  \ $$ |$$ |  $$ |$$ \__$$ |\033[32m  __  __  __ 
$$       |$$ |  $$ |$$       |$$       |$$ | $$  |$$ |$$ |  $$ |$$    $$ |\033[32m /  |/  |/  |
 $$$$$$$/ $$/   $$/  $$$$$$$/  $$$$$$$/ $$/   $$/ $$/ $$/   $$/  $$$$$$$ |\033[32m $$/ $$/ $$/ 
                                                                /  \__$$ |            
                                                                $$    $$/             
                                                                 $$$$$$/              

"""
i = '.'*15

print(checking_tools)
def namp_checking():
	if os.path.isfile('/usr/bin/nmap') == True:
		print(f'\033[37m1:Checking Nmap {i} \033[36m ok')
	else:
		print(f'Checking Nmap{i} \033[31m Not Found')

def dmitry_check():
	if os.path.isfile('/usr/bin/dmitry') == True:
		print(f'\033[37m2:Checking Dmitry {i} \033[36m ok')
	else:
		print(f'\033[37m2:Checking Dmitry {i} \033[31m Not Found')


def glismero_Check():
	if os.path.isfile('/usr/bin/golismero') == True:
		print(f'\033[37m3:Checking Golismero {i} \033[36m ok')
	else:
		print(f'\033[37m3:Checking Golismero {i} \033[31m Not Found')

def donna_check():
	if os.path.isfile('/usr/bin/doona') == True:
		print(f'\033[37m4:Checking Doona {i} \033[36m ok')
	else:
		print(f'\033[37m4:Checking Doona {i} \033[31m Not Found')

def nito_Check():
	if os.path.isfile('/usr/bin/nikto') == True:
		print(f'\033[37m5:Checking NIkto {i} \033[36m ok')
	else:
		print(f'\033[37m5:Checking NIkto {i} \033[31m Not Found')

def dotdot_check():
	if os.path.isfile('/usr/sbin/dotdotpwn') == True:
		print(f'\033[37m6:Checking Dotdotpwn {i} \033[36m ok')
	else:
		print(f'\033[37m6:Checking Dotdotpwn {i} \033[31m Not Found')


def osscanner_check():
	if os.path.isfile('/usr/bin/oscanner') == True:
		print(f'\033[37m7:Checking osscanner {i} \033[36m ok')
	else:
		print(f'\033[37m7:Checking osscanner {i} \033[31m Not Found')

def sidguess_check():
	if os.path.isfile('/usr/bin/sidguess') == True:
		print(f'\033[37m8:Checking sidguess {i} \033[36m ok')
	else:
		print(f'\033[37m8:Checking sidguess {i} \033[31m Not Found')


def davtest_check():
	if os.path.isfile('/usr/bin/davtest') == True:
		print(f'\033[37m9:Checking davtest {i} \033[36m ok')
	else:
		print(f'\033[37m9:Checking davtest {i} \033[31m Not Found')
def dirb_check():
	if os.path.isfile('/usr/bin/dirb') == True:
		print(f'\033[37m10:Checking dirb {i} \033[36m ok')
	else:
		print(f'\033[37m10:Checking dirb {i} \033[31m Not Found')
def go_buster():
	if os.path.isfile('/usr/bin/gobuster') == True:
		print(f'\033[37m11:Checking gobuster {i} \033[36m ok')
	else:
		print(f'\033[37m11:Checking gobuster {i} \033[31m Not Found')

def check():
	namp_checking()
	sleep(1)
	dmitry_check()
	sleep(1)
	glismero_Check()
	sleep(1)
	donna_check()
	sleep(1)
	nito_Check()
	sleep(1)
	dotdot_check()
	sleep(1)
	osscanner_check()
	sleep(1)
	sidguess_check()
	sleep(1)
	davtest_check()
	sleep(1)
	dirb_check()
	sleep(1)
	go_buster()
	os.system('clear')