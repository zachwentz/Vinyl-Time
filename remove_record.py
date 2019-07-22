def remove():

	import json
	#from add_record import *


	with open('record_collection.json') as handle:
		try:
			records = json.loads(handle.read())
			delete = True
		except:
			print('You must have a collection to delete!!!!')
			#add_record()


    
		#while delete == True:
		artist = input('Enter Artist to remove: ')
		album = input('Enter Album to remove: ')
		del records[artist][album]
		if len(records[artist]) == 0:
			del records[artist]
			#answer = input("Do you need to remove another record? ").lower()
        
        	#if answer[0] == 'n':
			#	delete = False
        
    
	with open('record_collection.json','w') as outfile:
		json.dump(records,outfile)
	
