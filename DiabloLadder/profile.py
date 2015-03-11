import urllib2, json, time, os, datetime, profile,pprint

def create_ladder_entries(data):
	ladder_entries = []
	for profile in data:		
		for hero in profile["heroes"]:			
			if(hero["hardcore"] and hero["seasonal"]):
				ladder_entry = {}
				ladder_entry["name"] = hero["name"]
				ladder_entry["level"] = hero["level"]
				ladder_entry["class"] = hero["class"]
				ladder_entry["dead"] = hero["dead"]
				ladder_entry["battleTag"] = profile["battleTag"]
				ladder_entry["paragonLevelSeasonHardcore"] = profile["paragonLevelSeasonHardcore"]
				ladder_entries.append(ladder_entry)
	pprint.pprint (ladder_entries)
	return ladder_entries

def get_profile(profile_tag):
	path = "profiles/" + profile_tag

	def refresh_data():
		response = urllib2.urlopen("http://eu.battle.net/api/d3/profile/" + profile_tag + "/").read()
		data = json.loads(response)

		with open(path , "w") as outfile:
			outfile.write(response)

		return data


	def print_hero_data(data):
		for hero in data["heroes"]:
			if hero["seasonal"] == True and hero["hardcore"] == True:
				print hero["name"]
				print "\t" + str(hero["paragonLevel"])
				print "\t" + str(hero["class"])
		
	#-----------------------------------------------------------------------------------------------------	

	if(os.path.exists(path)):
		last_modified = time.strptime(time.ctime(os.path.getmtime("profiles/" + profile_tag)))
		current_time = datetime.date.timetuple(datetime.datetime.now())


	if(not os.path.exists(path) or time.mktime(current_time)/60/60 - time.mktime(last_modified)/60/60 > 2):	
		print "Updating data"
		data = refresh_data()
		#print_hero_data(data)
		return data
	else:
		print "Data up to date, reading from file"
		with open(path , "r") as outfile:
			data = json.loads(outfile.read())
			#print_hero_data(data)
			return data