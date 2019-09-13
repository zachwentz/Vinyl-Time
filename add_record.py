def add_record():
	import json

	artist = input("Who is the Artist to Add? ")
	album = input("What is the Album? ")
	sides = input("How Many Sides is the Album? ")
	color = input("What Color is the Album? ")
	speed = input("What Speed is the Album? ")
	size = input("What Size is the Album? ")


	with open('record_collection.json') as handle:
		try:
			records = json.loads(handle.read())
		except:
			records = {}

	if artist in records.keys():
		records[artist].update({album:{'Sides':int(sides),'Color':color,'Speed':int(speed),'Size':int(size)}})
	else:
		records[artist] = {album:{'Sides':int(sides),'Color':color,'Speed':int(speed),'Size':int(size)}}
	
	with open('record_collection.json','w') as outfile:
		json.dump(records,outfile)
