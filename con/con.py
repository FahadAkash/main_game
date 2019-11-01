#!/usr/bin/python3 
# -*- coding: utf-8 -*-
import os
import sys
import subprocess
import urllib
import re
from colorama import *
from con.banner import banner
from con.maindataa import *


red = Fore.RED
green = Fore.GREEN
blue = Fore.BLUE
banner_1st = """\033[37m

		       1:>>>>Information about web
		       2:>>>Basic web info
		       3:>>>Full Web Information

"""
global info

class Main_process():
	def web_info(self):
		print(banner_1st)
		info = input(red+"""┌─[\033[32;1mroot\033[31;1m@\033[33mFahadAkash]─[Main_game]
└──╼ \033[32;1m#"""+green)
		if info == "1":
			os.system('clear')
			input_raw = input(red+"""┌─[\033[32;1mroot\033[31;1m@\033[33mFahadAkash]─[Enter Url]
└──╼ \033[32;1m#"""+green)
			info_web(input_raw)
	
		elif info == "2":
			os.system('clear')
			input_raw = input(red+"""┌─[\033[32;1mroot\033[31;1m@\033[33mFahadAkash]─[Enter Url]
└──╼ \033[32;1m#"""+green)
			basic_info(input_raw)
			
		elif info == "3":
			os.system('clear')
			input_raw = input(red+"""┌─[\033[32;1mroot\033[31;1m@\033[33mFahadAkash]─[Enter Url]
└──╼ \033[32;1m#"""+green)
			os.system('clear')
			full_info(input_raw)
		else:
			os.system('clear')
			banner()
			st = Main_process()
			st.web_info()


