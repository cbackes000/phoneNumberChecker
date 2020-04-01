import string
import re

def numCheck(file_contents):

	global matches
	matches = []

	for x in file_contents:

		isValid = re.search("[^0-9]", x)
		if isValid != None:
			matches.append(x)
		else:
			continue

	return matches

def wordCheck(char, file_contents):

	global matches
	matches = []

	for x in file_contents:

		isValid = re.search(char, x)
		if isValid != None:
			matches.append(x)
		else:
			continue

	return matches

# LENGTH CHECK DOES NOT WORK PROPERLY #

def lengthCheck(length, file_contents):

	global matches
	matches = []

	#words = wordInput.split()

	#for x in words:
	for x in file_contents:

		if len(x) != length:
			matches.append(x)
		else:
			continue

	return matches

###############

while True:
	try:
		textFile = input("Text filename: ")
		with open(textFile) as fl:
			file_contents = [x.rstrip() for x in fl]
	except IOError:
		print("File not found. Try again:")
		continue
	else:
		break


while True:
	userChoice = str(input("========\nCheck text file for:\n (1) for invalid characters \n (2) for invalid length\n"))
	if userChoice != "1" and userChoice != "2":
		print("Invalid choice, try again.")
		continue

	else:
		break


if userChoice == "1":
	while True:
		secChoice = input("Custom search? (y/n):\n")
		if secChoice == "n":
			numCheck(file_contents)
			print("========\nInvalid entries:")
			if matches == []:
				print("None")
			else:
				for x in matches:
					print(x)
			break
		elif secChoice == "y":
			char = input("========\nEnter the characters to search for:\n")
			wordCheck(char,file_contents)
			print("========\nInvalid entries:")
			if matches == []:
				print("None")
			else:
				for x in matches:
					print(x)
			break
		else:
			print("Invalid response.")
			continue


elif userChoice == "2":
	length = int(input("========\nEnter the correct length to check against:\n"))
	lengthCheck(length,file_contents)
	print("========\nInvalid entries:")
	if matches == []:
		print("None")
	else:
		for x in matches:
			print(x)






