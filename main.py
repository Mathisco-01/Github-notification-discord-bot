from bs4 import BeautifulSoup
from selenium import webdriver
import chromedrivers.ChromeDriverVersion

from discordDir import discordBot

import os
import time

def getPage(url):

	chrome_options = webdriver.ChromeOptions()
	chrome_options.add_argument('--headless')
	chrome_options.add_argument('--disable-gpu')

	driver = webdriver.Chrome(str(chromedrivers.ChromeDriverVersion.getPath()), options=chrome_options)
	page = driver.get(url)
	pageContent = driver.page_source
	driver.close()
	return BeautifulSoup(pageContent, 'html.parser')


def getFileContent(file):
	lineList = []
	with open(file, 'r') as file:
		for line in file:
			lineList.append(line.replace("\n", ""))

	return lineList

def getUrls():
	urlList = []
	file = os.path.join(os.getcwd(), "toScrape.txt")
	
	return getFileContent(file)


def scrapeForNewCommits(soup):

	name, commits = "", []	
	try:
		name = (soup.find("a", {"data-pjax": "#js-repo-pjax-container"})).text
		for commit in soup.find_all("a", {"class": "message js-navigation-open"}):
				commits.append(commit.text)
	except:
		pass
	return name, commits

def compareLists(name, commits, url):
	file = os.path.join("commitVersioning" ,name + ".txt")
	if(os.path.isfile(file)):
		oldCommits = getFileContent(file)
		if(commits != oldCommits):
			print("Changes Detected!")
			discordBot.sendMessage(name, commits[0], url)
			f = open(file, 'w+')
			for commit in commits:
				f.write(str(commit + "\n"))
	else:
		f = open(file, 'w+')
		for commit in commits:
			f.write(str(commit + "\n"))

def main():

	for url in getUrls():
		print("Working on: ", url)
		if(url[-15:] == "/commits/master"):
			name, commits = scrapeForNewCommits(getPage(url))
		else:
			name, commits = scrapeForNewCommits(getPage(url + "/commits/master"))

		if(len(commits) != 0):
			compareLists(name, commits, url)
		else:
			print("No commits found! Either page is unavailable or repo is private!")

if __name__ == '__main__':
	while True:
		main()
		print("Done")
		time.sleep(10)
