import json
import requests
import os

def getConfigData(path):
	try:
		with open(path, 'r') as file:
			for line in file:
				data = line.replace("\n", "")
		return data
	except:
		return ""
		
def makeToken(pathToToken):
	with open(pathToToken, 'w+') as file:
		file.write(input("Paste your dicord token here: "))

def makeChannel(pathToChannel):
	with open(pathToChannel, 'w+') as file:
		file.write(input('Paste your channel ID here: '))

def fetchToken():
	pathToToken = os.path.join(os.getcwd(),'discordDir', 'token.txt')
	token = getConfigData(pathToToken)
	if(token == "" or token == None):
		makeToken(pathToToken)
		fetchToken()
	else:
		return token

def fetchChannel():
	pathToChannel = os.path.join(os.getcwd(), 'discordDir', 'channel.txt')
	channel = getConfigData(pathToChannel)
	if(channel == "" or channel == None):
		makeChannel(pathToChannel)
		fetchChannel()
	return channel


def sendMessage(name,commit, url):
	baseURL = "https://discordapp.com/api/channels/{}/messages".format(str(fetchChannel()))

	string = "@here {} Just got a new commit: __**{}**__! {}".format(name, commit, url)
	POSTedJSON =  json.dumps({"content":string})

	headers = { "Authorization":"Bot {}".format(fetchToken()),
				"User-Agent":"CloutWatch (v1.0.0)",
				"Content-Type":"application/json", }

	r = requests.post(baseURL, headers = headers, data = POSTedJSON)
