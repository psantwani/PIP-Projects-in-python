import time
from math import floor
from threading import Timer
from datetime import datetime
import sys

def welcomeMsg():	
	print("Hey, I am your personal reminder assistant.")

def currentTime():
	print("Current time : {0}".format(time.strftime('%b %d %Y,%l:%M %p')))

def printAlarmMessage(arg):
	print("\n-------------------------------------------")
	print("You have a new alarm.\nMessage - {0}".format(arg))

def setAlarm():
	try:
		print("-------------------------------------------")
		print("New Alarm")
		print("-------------------------------------------")
		secondsToAlarm = -1
		message = []
		while secondsToAlarm < 0:
			timeStr = input("Enter alarm time (dd-mm-yy hh:mm) > ")
			alarmTime = datetime.strptime(timeStr, '%d-%m-%y %H:%M')
			secondsToAlarm = floor((alarmTime - datetime.now()).total_seconds())
			if secondsToAlarm < 0 :
				print("Alarm time cannot be in past")

		message.append(str(input("What should I remind you about > ")))
		Timer(secondsToAlarm, printAlarmMessage, message).start()
		print("Alarm set")
		print("-------------------------------------------")
	except Exception as e:
		raise e	

def quitApp():
	sys.exit("Quitting..")


def print_time(): print("From print_time", time.time())

if __name__ == "__main__":	
	print("-------------------------------------------")
	welcomeMsg()
	currentTime()
	print("-------------------------------------------")
	operations = {
		'1' : setAlarm,		
		'2' : quitApp
	}

	print('Select operation - \n 1:Create new alarm \n 2:Quit \n')
	choice = 0	
	while choice != 2 or EOFError:
		choice = input("Your choice > ")
		try:			
			operations[choice]()
		except Exception as e:			
			print("Unknown operation. Try again")	