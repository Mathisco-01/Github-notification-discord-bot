import json
import requests
import os

def getToken(pathToToken):
	try:
		with open(pathToToken, 'r') as file:
			for line in file:
				discord_token = line.replace("\n", "")
		return discord_token
	except:
		return ""
		
def makeToken(pathToToken):
	with open(pathToToken, 'w+') as file:
		file.write(input("Paste your dicord token here: "))

def fetchToken():
	pathToToken = os.path.join(os.getcwd(),'discordDir', 'token.txt')
	token = getToken(pathToToken)
	if(token == "" or token == None):
		makeToken(pathToToken)
		fetchToken(pathToToken)
	else:
		return token

def sendMessage(name,commit, url):
	baseURL = "https://discordapp.com/api/channels/{}/messages".format('550724065581596684')

	string = "@here {} Just got a new commit: __**{}**__! {}".format(name, commit, url)
	POSTedJSON =  json.dumps({"content":string})

	headers = { "Authorization":"Bot {}".format(fetchToken()),
				"User-Agent":"CloutWatch (v1.0.0)",
				"Content-Type":"application/json", }

	r = requests.post(baseURL, headers = headers, data = POSTedJSON)
