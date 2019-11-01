import os
import sys
import subprocess
import socket
try:
	host = socket.gethostname(url)
	host_ip = socket.gethostbyname(host)
	
except:
	print("Unable to connect the ip")
	


def nmap_info(ip):
	os.system("nmap -A -v -p 1-65535 -sV -O -sS -T5 "+ip)

def dmitry_info(ip):
	os.system("dmitry "+ip)


def glismero_info(ip):
	print(20*)
	os.system('golismero '+ip)


def donna_info(ip):
	os.system("doona -m HTTP -t "+ip+" -M 5")

def nikto_info():
	os.system('nikto '+'-h '+ip)

def dotdotpwn_info(ip):
	os.system('dotdotpwn -m http -h '+ip)


def osscanner_info(ip,port):
	os.system('osscanner -s '+ip+'-P '+port)


def sidguess(ip):
	os.system('sidguess '+'-i '+ip+' -d /usr/share/wordlists/metasploit/unix_users.txt')

def davtest(ip):
	os.system('davtest -url '+ip)

def dirb_info(ip):
	os.system('dirb '+ip+' /usr/share/wordlists/dirb/common.txt')

def go_buster(ip):
	os.system('gobuster -e -u '+ip+' -w /usr/share/wordlists/dirb/common.txt')

def webshag(ip):
	os.system('cd ../../data/webshagt/')
	os.system('./webshag.py '+ip)

def info_web(url):
	nmap_info(url)

def basic_info(url):
	nmap_info(url)
	dmitry_info(url)
	glismero_info(url)

def full_info(url):
	nmap_info(url)
	dmitry_info(url)
	glismero_info(url)
	donna_info(url)
	nikto_info(url)
	dotdotpwn_info(url)
	osscanner_info(url, 80)
	sidguess(url)
	davtest(url)
	dirb_info(url)
	go_buster(url)
	webshag(url)


	