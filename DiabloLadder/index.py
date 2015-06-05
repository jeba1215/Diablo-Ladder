import urllib2, json, time, os, datetime, profile
from flask import Flask, render_template

app = Flask(__name__)
profile_tag = "Digestive-2381"

@app.route("/")
def index():
	heroes = []
	with open("battletags.txt", "a+") as f1:
		for battletag in f1:
			heroes.append(profile.get_profile(battletag.rstrip("\r\n")))


	heroes = profile.create_ladder_entries(heroes)
	heroes = sorted(heroes, key = lambda k: k["paragonLevelSeason"], reverse=True)
	
	return render_template("index.html", heroes=heroes)

if __name__ == "__main__":	
    app.run(debug=True)