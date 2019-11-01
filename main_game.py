#!/usr/bin/env python 
# -*- coding: utf-8 -*-
from time import sleep
from con.banner import banner
from con.checking_tools import check
from con.con import Main_process
from con import maindataa
import os
os.system('resize -s 26 119')
check()
sleep(0.1)
banner()
ST = Main_process()
ST.web_info()

