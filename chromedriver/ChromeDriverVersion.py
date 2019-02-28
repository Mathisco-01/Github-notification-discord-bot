import os
import sys

macpath = os.path.join(os.getcwd(),"chromedriver/macosdriver/chromedriver")
windowspath = os.path.join(os.getcwd(),"chromedriver/windowsdriver/chromedriver.exe")
linuxpath = os.path.join(os.getcwd(),"chromedriver/linuxdriver/chromedriver")

currentPath = ""

os = sys.platform


def getPath():
	try:
		global currentPath
		if(currentPath == ""):
			if(os == "linux"):
				currentPath = linuxpath
			elif(os == "win32" or os == "cygwin"):
				currentPath = windowspath
			elif(os == "darwin"):
				currentPath = macpath

			#print("ChromeDriver found: " + currentPath)
			return currentPath
		else:
			return currentPath
	except Exception as e:
		print(e)