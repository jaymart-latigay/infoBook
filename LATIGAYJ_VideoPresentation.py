#CMSC 12 PROJECT: PERSONAL ORGANIZER
#Latigay, Jaymart Gonzales
# June 7, 2021


print("\n")
print("Hello! I'm Jay your Personal Organizer. What can I do for you today?" + "\n")

def showMenu():
	print("You are in the Main Menu.")
	print("Here are your options:")

	print("[1] Go to Event Scheduler")
	print("[2] Go to Notes")
	print("[3] Go to TODO list")
	print("[4] Overview: Check all entries on a certain date")
	print("[0] Stop program")

	choice = int(input("Choice: "))
	return choice
	print("\n")



# EVENT SCHEDULER 
def eventScheduler():
	def esShowMenu():
		print("Hey! You're in the Event Scheduler.")
		print("Here are your options:")

		print("[1] Add Event")
		print("[2] Delete Event")
		print("[3] Delete All Events")
		print("[4] View Event")
		print("[5] View All Events")
		print("[6] Save Recently Added Events To File")
		print("[7] Load Previously Saved Events From File")
		print("[0] Exit Event Scheduler")

		esChoice = int(input("Choice: "))
		return esChoice
		print("\n")


	def addEvent():
		print("You can start adding an event now.")
		date = input("Date: ")
		if date in eventsInfo:
			print(f"Sorry! You already have an event on {date}. Pick another date.")
			date = input("Date: ")
		time = str(input("Time (format: hh:mm PM/AM): ").upper())
		title = input("Title: ")
		description = input("Description: ")
		place = input("Place: ")
		print("\n")

		eventDetails = {}
		eventDetails["Time"] = time
		eventDetails["Title"] = title
		eventDetails["Description"] = description
		eventDetails["Place"] = place
		eventsInfo[date] = eventDetails
	

	def deleteEvent():
		check_eventDate = input("Enter the Event Date: ")

		if check_eventDate in eventsInfo:
			eventsInfo.pop(check_eventDate)
			print(f"Your event on {check_eventDate} has been deleted.")
		else:
			print(f"Sorry, you don't have an event on {check_eventDate}.")
		print("\n")


	def deleteAllEvent():
		eventsInfo.clear()
		print("All of your events are deleted")
		print("\n")


	def viewEvent():
		check_eventDate = input("When is your event?: ")

		if check_eventDate in eventsInfo:
			print("Here are the details of your event: ")
			entry_info = list(eventsInfo[check_eventDate].values())
			print("Date:", check_eventDate)
			print("Time:", entry_info[0])
			print("Title:", entry_info[1])
			print("Description:", entry_info[2])
			print("Place:", entry_info[3])
		else:
			print(f"Sorry, you don't have an event on {check_eventDate}.")
		print("\n")


	def viewAllEvent():
		print("Here are all the details of your events:")
		counter = 1
		for k in eventsInfo:
			print(str(counter) + ". \n" + "Date: ", k )
			eventDetails = eventsInfo[k]
			print("Date:", k)
			print("Time: ", eventDetails["Time"])
			print("Title: ", eventDetails["Title"])
			print("Description: ", eventDetails["Description"])
			print("Place: ", eventDetails["Place"])
			counter += 1

		if counter == 1:
			print("You do not have any events to view.")
		print("\n")
	

	def esSaveToFile():
		filehandle = open("es_records.txt","w")

		for k in eventsInfo:
			eventDetails = eventsInfo[k]
			time = eventDetails["Time"]
			title = eventDetails["Title"]
			description = eventDetails["Description"]
			place = eventDetails["Place"]
			filehandle.write(k + "|" + time + "|" + title + "|" + description + "|" + place + "\n")
		filehandle.close()

		count = 0
		for k in eventsInfo:
			count += 1
		print(f"Successfully added {count} Event entries.")
		print("\n")


	def esLoadFromFile():
		filehandle = open("es_records.txt", "r")
		eventsInfo.clear()
		for line in filehandle:
			data = line[0:-1].split("|")
			date = data[0]
			time = data[1]
			title = data[2]
			description = data[3]
			place = data[4]

			eventDetails = {}
			eventDetails["Time"] = time
			eventDetails["Title"] = title
			eventDetails["Description"] = description
			eventDetails["Place"] = place
			eventsInfo[date] = eventDetails
		filehandle.close()

		with open("es_records.txt", "r") as file:
			x = len(file.readlines())
			print(f"Successfully loaded Event records from file. ({x} entries)")
		print("\n")


	eventsInfo = {}


	while True:
		esChoice = esShowMenu()
		if esChoice == 1:
			addEvent()
		elif esChoice == 2:
			deleteEvent()
		elif esChoice == 3:
			deleteAllEvent()
		elif esChoice == 4:
			viewEvent()
		elif esChoice == 5:
			viewAllEvent()
		elif esChoice == 6:
			esSaveToFile()
		elif esChoice == 7:
			esLoadFromFile()
		elif esChoice == 0:
			print("You have exited Event Scheduler") 
			("\n")
			break
		else:
			print("Sorry that's not an option. Try again!")
			print("\n")



# NOTES SECTION 
def notesSection():
	def nsShowMenu():
		print("\n")
		print("Hello! You are in the Notes Section")
		print("Here are your options:")

		print("[1] Add Note")
		print("[2] Delete Note")
		print("[3] Delete All Notes")
		print("[4] View Note")
		print("[5] View All Notes")
		print("[6] Save Recently Added Notes To File")
		print("[7] Load Previously Saved Note From File")
		print("[0] Exit Notes Section")

		nsChoice = int(input("Choice: "))
		return nsChoice
		print("\n")


	def addNote():
		print("You may start adding your notes now.")
		date = input("Date: ")
		if date in notesInfo:
			print(f"Sorry! You already have a Note for {date}. Pick another date.")
			date = input("Date: ")
		time = str(input("Time (format: hh:mm PM/AM): ").upper())
		title = input("Title: ")
		content = input("Content: ")
		print("\n")

		notesDetails = {}
		notesDetails["Time"] = time
		notesDetails["Title"] = title
		notesDetails["Content"] = content
		notesInfo[date] = notesDetails


	def deleteNote():
		check_noteDate = input("Enter the Note Date: ")

		if check_noteDate in notesInfo:
			notesInfo.pop(check_noteDate)
			print(f"Your Note for {check_noteDate} has been deleted.")
		else:
			print(f"Sorry, you don't have a Note for {check_noteDate}.")
		print("\n")


	def deleteAllNotes():
		notesInfo.clear()
		print("All of your Notes are deleted")
		print("\n")


	def viewNote():
		check_noteDate = input("When is your Note for?: ")

		if check_noteDate in notesInfo:
			print("Here are the details of your Note: ")
			entry_info = list(notesInfo[check_noteDate].values())
			print("Date:", check_noteDate)
			print("Time:", entry_info[0])
			print("Title:", entry_info[1])
			print("Content:", entry_info[2])
		else:
			print(f"Sorry, you don't have a Note for {check_noteDate}.")
		print("\n")


	def viewAllNotes():
		print("Here are all the details of your Notes:")
		counter = 1
		for k in notesInfo:
			print(str(counter) + ". \n" + "Date: ", k )
			notesDetails = notesInfo[k]
			print("Time: ", notesDetails["Time"])
			print("Title: ", notesDetails["Title"])
			print("Content: ", notesDetails["Content"])
			counter += 1

		if counter == 1:
			print("You do not have any notes to view.")
		print("\n")


	def nsSaveToFile():
		filehandle = open("ns_records.txt","w")

		for k in notesInfo:
			notesDetails = notesInfo[k]
			time = notesDetails["Time"]
			title = notesDetails["Title"]
			content = notesDetails["Content"]
			filehandle.write(k + "|" + time + "|" + title + "|" + content + "\n")
		filehandle.close()

		count = 0
		for k in notesInfo:
			count += 1
		print(f"Successfully added {count} Note entries.")
		print("\n")


	def nsLoadFromFile():
		filehandle = open("ns_records.txt", "r")
		notesInfo.clear()
		for line in filehandle:
			data = line[0:-1].split("|")
			date = data[0]
			time = data[1]
			title = data[2]
			content = data[3]

			notesDetails = {}
			notesDetails["Time"] = time
			notesDetails["Title"] = title
			notesDetails["Content"] = content
			notesInfo[date] = notesDetails
		filehandle.close()

		with open("ns_records.txt", "r") as file:
			x = len(file.readlines())
			print(f"Successfully loaded Note records from file. ({x} entries)")
		print("\n")


	notesInfo = {}


	while True:
		nsChoice = nsShowMenu()
		if nsChoice == 1:
			addNote()
		elif nsChoice == 2:
			deleteNote()
		elif nsChoice == 3:
			deleteAllNotes()
		elif nsChoice == 4:
			viewNote()
		elif nsChoice == 5:
			viewAllNotes()
		elif nsChoice == 6:
			nsSaveToFile()
		elif nsChoice == 7:
			nsLoadFromFile()
		elif nsChoice == 0:
			print("You have exited the Notes Section") 
			print("\n")
			break
		else:
			print("Sorry that's not an option. Try again!")
			print("\n")



# TODO LIST SECTION
def toDoList():
	def tdShowMenu():
		print("Hello! You are in the Notes Section")
		print("Here are your options:")

		print("[1] Add Item")
		print("[2] Mark as Done")
		print("[3] View Item")
		print("[4] View All Items")
		print("[5] Save Recently Added Notes To File")
		print("[6] Load Previously Saved Note From File")
		print("[0] Exit TODO List Section")

		tdChoice = int(input("Choice: "))
		return tdChoice
		print("\n")


	def tdAddItem():
		print("You may start adding an item now.")
		title = input("Enter Title: ")
		content = input("Enter Content: ")
		
		tdListDetails = {}
		tdListDetails["Content"] = content
		toDoListInfo[title] = tdListDetails
		toDoListInfo[title]["Status"] = "NOT DONE"
		print("\n")
	

	def markDone():
		print("Yay! You finished an item from your TODO List! Now, mark it as done")
		markItemDone = input("Enter Item Title: ")

		if toDoListInfo[markItemDone]["Status"] != "DONE":
			toDoListInfo[markItemDone]["Status"] = "DONE"
			print(f"Item {markItemDone} is done!")
		else:
			print(f"Item ({markItemDone}) is already marked as done.")
		print("\n")


	def viewItem():
		checkItem = input("Enter Item Title: ")

		if checkItem in toDoListInfo:
			print("Here are the details of your Item: ")
			entry_info = list(toDoListInfo[checkItem].values())
			print("Title: ", checkItem)
			print("Content: ", entry_info[0])
			print("Status: ", entry_info[1])
		else:
			print(f"Sorry, Item ({checkItem}) does not exist.")
		print("\n")


	def viewAllItems():
		print("Here are all your TODO list Items and their details:")
		counter = 1
		for k in toDoListInfo:
			print(str(counter) + ". \n" + "Title: ", k )
			tdListDetails = toDoListInfo[k]
			print("Content: ", tdListDetails["Content"] )
			print("Status: ", tdListDetails["Status"])
			counter += 1

		if counter == 1:
			print("You do not have any Items in you TODO List to view.")
		print("\n")


	def tdSaveToFile():
		filehandle = open("td_records.txt","w")

		for k in toDoListInfo:
			tdListDetails = toDoListInfo[k]	
			content = tdListDetails["Content"]	
			status = tdListDetails["Status"]
			filehandle.write(k + "|" + content + "|" + status + "\n")
		filehandle.close()

		count = 0
		for k in toDoListInfo:
			count += 1
		print(f"Successfully added {count} Item entries.")
		print("\n")


	def tdLoadFromFile():
		filehandle = open("td_records.txt", "r")
		toDoListInfo.clear()
		for line in filehandle:
			data = line[0:-1].split("|")
			title = data[0]
			content = data[1]
			status = data[2]

			tdListDetails = {}
			tdListDetails["Content"] = content
			tdListDetails["Status"] = status
			toDoListInfo[title] = tdListDetails
		filehandle.close()

		with open("td_records.txt", "r") as file:
			x = len(file.readlines())
			print(f"Successfully loaded TODO List Item records from file. ({x} entries)")
		print("\n")


	toDoListInfo = {}


	while True:
		tdChoice = tdShowMenu()
		if tdChoice == 1:
			tdAddItem()
		elif tdChoice == 2:
			markDone()
		elif tdChoice == 3:
			viewItem()
		elif tdChoice == 4:
			viewAllItems()
		elif tdChoice == 5:
			tdSaveToFile()
		elif tdChoice == 6:
			tdLoadFromFile()
		elif tdChoice == 0:
			print("You have exited the TODO List Section") 
			print("\n")
			break
		else:
			print("Sorry that's not an option. Try again!")
			print("\n")



#OVERVIEW
def overview():
	print("Hi! You are in Overview")
	print("Here, you'll be able to access Events and Notes information according to their date" + "\n") 

	esFile = open("es_records.txt")
	nsFile = open("ns_records.txt")
	
	date = input("Enter date: ")

	counter1 = 1
	counter2 = 1
	print("Event: ")
	for line in esFile:
		if line.startswith(date):
			data = line.split("|")
			print("Date:", data[0])
			print("Time:", data[1])
			print("Title:", data[2])
			print("Description:", data[3])
			print("Place:", data[4])
			counter1 +=1
	if counter1 == 1:
		print("You do not have any Events to view.")


	print("Note: ")
	for line in nsFile:
		if line.startswith(date):
			data = line.split("|")
			print("Date:", data[0])
			print("Time:", data[1])
			print("Title:", data[2])
			print("Content:", data[3])
			counter2 += 1
	if counter2 == 1:
		print("You do not have any Notes to view.")
		print("\n")


#Main while loop
while True:
	choice = showMenu()

	if choice == 1:
		eventScheduler()
	elif choice == 2:
		notesSection()
	elif choice == 3:
		toDoList()
	elif choice == 4:
		overview()
	elif choice == 0:
		print("Thank you! See you next time!")
		break
	else:
		print("Sorry that's not an option. Try again!")
