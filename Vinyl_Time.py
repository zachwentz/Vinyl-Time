
import random
import os
clear = lambda: os.system('cls')
clear()
from add_record import * 
from records import * 
from remove_record import *
import time
import ctypes
import sys
from import_records import *

up_one = '\x1b[1A'
erase = '\x1b[2K'

print('__  __  __ ____  __  __  __  __    ')
print('\ \/ /  || |   \ | | \ \/ /  | |   ')
print(' \  /   || | |\ \| |  |  |   | |__ ')
print('  \/    || |_| \___|  |__|   |____|')

print('   ______  __ ___  __  ______      ')
print('   |__ __| || |  \/  | |  _*_|     ')
print('     | |   || |      | |  |__      ')
print('     |_|   || |_|\/|_| |_____|     ')
time.sleep(1)
clear()


mainprogram = True

while mainprogram:


	print('Please Choose an option     ')
	print('1: Add a record?            ')
	print('2: Remove a record?         ')
	print('3: Create a playlist?       ')
	print('4: Import Record Collection?')
	print('5: Exit?                    ')

	select = int(input('Selection:  '))
	while not int(select) in range(0,6):
		select = int(input('Your Selection Must Be 1-4:  '))

	

	update = 'n'
	delete = 'n'
	playlst = 'n'
	import_lst = 'n'

	if select == 1:
		update = 'y'
	else:
		update = 'n'

	if select == 2:
		delete = 'y'
	else:
		delete = 'n'
	if select == 3:
		playlst = 'y'
	else:
		playlst = 'n'
	if select == 4:
		import_lst = 'y'
	else:
		import_lst = 'n'

	if select == 5:
		#font = pygame.font.Font(None,40)
		clear()
		print('Good Bye')#.font.nFont = 16
		time.sleep(2)
		mainprogram = False

		#break
	clear()

	'''
	Determin if the user wants to add records to the collection
	'''

	#update = input("Do you need to add records to the collection? ").lower()

	while select == 1 and update[0] =='y':
	    add_record()
	    clear()
	    update = input("Do you need to add another record? ").lower()
	    while update[0].lower() not in ('y','n'):
	    	update = input('You must select Yes or No!')
	    	sys.stdout.write(up_one)
	    	sys.stdout.write(erase)

	clear()

	#delete = input("Do you need to remove a record from your collection? ").lower()

	while select == 2 and delete[0] == 'y':
		remove()
		clear()
		delete = input("Do you need to remove another record? ").lower()
		while delete[0].lower() not in ('y','n'):
			delete = input('You must select Yes or No!')
			sys.stdout.write(up_one)
			sys.stdout.write(erase)

	clear()

	while select == 4 and import_lst[0] == 'y':
		import_rec()
		print('Your Collection Has Been Imported!')
		time.sleep(2)
		import_lst = 'n'
		clear()


	clear()


	'''
	create a playlist
	'''
	while select == 3 and playlst[0] == 'y':
		from records import * 

		record_num = 1
		records = records()
		counter = int(input(f"How many records do you want to listen to? Pick 1 - {len(records)-1}: "))
		while int(counter) not in range(0,len(records)):
			counter = int(input(f'Please pick a number 1 - {len(records)}: '))
			sys.stdout.write(up_one)
			sys.stdout.write(erase)
		reshuffle = counter
		shuffle = True

		clear()

		while shuffle:

			while counter > 0:
				randomtitle = random.randint(0,len(records)-1)
				pick = records[randomtitle]
				print(f'\nRecord {record_num}:\nAlbum: {pick[:-1]}\nSide: {pick[len(pick)-1]}\n')
				print('------------------------------------------------------------')
				del records[randomtitle]
				counter -= 1
				record_num += 1
		    

			answer = input("Reshuffle? ")
			while answer[0].lower() not in ('n','y'):
				answer = input('You must select Yes or No!')
				sys.stdout.write(up_one)
				sys.stdout.write(erase)
			if answer[0].lower() == 'y':
				clear()
				#shuffle =  True
				counter = reshuffle
				record_num = 1
			else:
				shuffle = False
				playlst = 'n'
				clear()

