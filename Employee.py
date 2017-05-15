#!/usr/bin/env python3


#created by Deniz Burak

import sys,os
import time
import random

print ("Welcome to Employee Database program")
print(" ")

idCheck = input ("Please Enter your Employement ID Number to start the program: ")

if idCheck.isdigit():
	print ("Please Select:")
	print(" ")
	print ("Press 1 to ENTER Employement Data to the Book")
	print(" ")
	print ("Press 2 to VIEW Empolyement Data Book")
	userInput = input ("Enter(1,2): ")

	if userInput == "1":
		EmpName = input ("Please Enter Employee Name: ")
		EmpLastName = input ("Please Enter Employee Last Name: ")
		EmpDateOfBirth = input ("Please Enter Employee Date of Birth(MM/DD/YYYY): ")
		EmpGender = input ("Please enter Employee Gender(M or F): ")
		print(" ")
		
		print ("System will Give random id Number to New Employee...")
		print ("Please wait...")
		time.sleep(3)
		print(" ")
		
		randomID = random.randint(11111,99999)
		print ("Employee ID Number: " + str(randomID))	
		print(" ")
		
		print ("Employee DataBase Entry is on Process...")
		print(" ")
		time.sleep(2)
		
		print ("Employee Name: " + EmpName)
		time.sleep(2)
		
		print ("Employee Last Name: " + EmpLastName)
		time.sleep(2)
		
		print ("Employee Date of Birth: " +EmpDateOfBirth)
		time.sleep(2)
		
		print ("Employee Gender: " + EmpGender)
		time.sleep(2)
		#print ("Employee ID Number:" +str(randomID))
		#time.sleep(2)
		#with open ("EmpDataFile.txt")
		#print ("Data Entry Process is Successful")
		#print
		print(" ")
		print ("Have a good day " + idCheck)

		with open ("EmpData.txt", "a") as f:
			f.write("Employee Name: " + EmpName + "\n")
			f.write("Employee Last Name: " + EmpLastName + "\n")
			f.write("Employee Date of Birth: " + EmpDateOfBirth + "\n")
			f.write("Employee Gender: " + EmpGender + "\n")
			f.write("Employee ID Number: " + str(randomID) + "\n")
			f.write("*Entered By: " + idCheck + "\n")
			f.write("*Entry Date: " + time.asctime() + "\n")
			f.write("-------------------------\n")	

	elif  userInput == "2":
		print ("Employee Data Book Opening")
		print (" ")
		
		print("Please Wait...")
		time.sleep(1)
		print(".")
		time.sleep(2)
		print("..")
		time.sleep(3)
		print("...")
		
		with open("EmpData.txt", "r") as f:
			for line in f:
				print(line, end='')

	elif userInput != "1" and userInput != "2":
		print ("Your input was " + userInput)
		print ("Program Closing")
		print ("**")
		print ("Please Re-Open the Program ")
	


else:
	print ("System can not recognize the id number: " + idCheck)
	print
	print ("**Program Closing")
	print("Good Bye")
	print
	

