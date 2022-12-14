from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep
from datetime import date
import datetime
import requests
import os

roomlistdict = {
0:{30:("3F","Training Room"),50:("5F","Absolut"),60:("6F","Martell Meal"),61:("6F","Chivas"),70:("7F","Boardroom")},
3:{31:"Altos",32:"Havana Club",33:"Kinobi",34:"Jacob's Creek",35:"Lillet",36:"Ballantine's Finest"},
5:{51:"Aberlour",52:"Church Road",53:"Kahlúa",54:"Ricard",55:"Beefeater",56:"Olmeca",57:"Monkey 47",58:"The Glenlivet"},
6:{62:"Drinks & Co",63:"Malibu",64:"Martell PTI",65:"Mumm",66:"Pernod",67:"Secret Speyside",68:"Perrier-Jouet",69:"Royal Salute"},
7:{71:"Cognac",72:"Jameson",73:"Whisky",74:"White spirits",75:"Wine",76:"Martell QSS"}
}

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--disable-dev-shm-usage')
chromedriver = ChromeDriverManager().install()
os.environ["webdriver.chrome.driver"] = chromedriver

def run(roomlistdict):
	weekday = datetime.date.today().isoweekday()
	apiurl = os.getenv('URL')
	apidate = datetime.date.today()
	params={"sign":"S591485253",
		"channel":1,
		"text":"{}巡检成功".format(apidate)}

	if weekday == 1 or weekday == 3:
		print("将执行以下自动化：\n" + str(roomlistdict[0]) + '\n' + str(roomlistdict[6]) + '\n' + str(roomlistdict[7]))
		run6F(roomlistdict)
		run7F(roomlistdict)
		runDaily(roomlistdict)
		print('Success')
	elif weekday == 2 or weekday == 4:
		print("将执行以下自动化：\n" + str(roomlistdict[0]) + '\n' + str(roomlistdict[3]) + '\n' + str(roomlistdict[5]))
		run3F(roomlistdict)
		run5F(roomlistdict)
		runDaily(roomlistdict)
		print('Success')
	elif weekday == 5:
		print("将执行以下自动化：\n" + str(roomlistdict[0]))
		runDaily(roomlistdict)
		print('Success')
	
	response = requests.get(apiurl, params=params)

def run3F(roomlistdict):
	
	driver = webdriver.Chrome(options=chrome_options,executable_path=chromedriver)
	driver.get(os.getenv('FORM'))
	sleep(3)

	for meetingroom3 in roomlistdict[3].values():
		driver.find_element(By.XPATH,value="//div[@aria-posinset='0']").click()
		sleep(0.5)
		driver.find_element(By.XPATH,value="//div[@aria-label='3F']").click()
		sleep(0.5)
		driver.find_element(By.XPATH,value="//div[@aria-posinset='0']").click()
		sleep(0.5)
		driver.find_element(By.XPATH,value="//div[@aria-label=\"{}\"]".format(str(meetingroom3))).click()
		sleep(0.5)
		driver.find_element(By.XPATH,value="//div[@aria-posinset='0']").click()
		sleep(0.5)
		driver.find_element(By.XPATH,value="//div[@aria-label='Good']").click()
		sleep(0.5)
		driver.find_element(By.XPATH,value="//button[@title='Submit']").click()
		sleep(2.5)
		driver.find_element(By.LINK_TEXT,value="Submit another response").click()
		sleep(0.5)
	driver.close()

def run5F(roomlistdict):
	
	driver = webdriver.Chrome(options=chrome_options,executable_path=chromedriver)
	driver.get(os.getenv('FORM'))
	sleep(3)

	for meetingroom5 in roomlistdict[5].values():
		driver.find_element(By.XPATH,value="//div[@aria-posinset='0']").click()
		sleep(0.5)
		driver.find_element(By.XPATH,value="//div[@aria-label='5F']").click()
		sleep(0.5)
		driver.find_element(By.XPATH,value="//div[@aria-posinset='0']").click()
		sleep(0.5)
		driver.find_element(By.XPATH,value="//div[@aria-label=\"{}\"]".format(str(meetingroom5))).click()
		sleep(0.5)
		driver.find_element(By.XPATH,value="//div[@aria-posinset='0']").click()
		sleep(0.5)
		driver.find_element(By.XPATH,value="//div[@aria-label='Good']").click()
		sleep(0.5)
		driver.find_element(By.XPATH,value="//button[@title='Submit']").click()
		sleep(2.5)
		driver.find_element(By.LINK_TEXT,value="Submit another response").click()
		sleep(0.5)
	driver.close()

def run6F(roomlistdict):
	
	driver = webdriver.Chrome(options=chrome_options,executable_path=chromedriver)
	driver.get(os.getenv('FORM'))
	sleep(3)

	for meetingroom6 in roomlistdict[6].values():
		driver.find_element(By.XPATH,value="//div[@aria-posinset='0']").click()
		sleep(0.5)
		driver.find_element(By.XPATH,value="//div[@aria-label='6F']").click()
		sleep(0.5)
		driver.find_element(By.XPATH,value="//div[@aria-posinset='0']").click()
		sleep(0.5)
		driver.find_element(By.XPATH,value="//div[@aria-label=\"{}\"]".format(str(meetingroom6))).click()
		sleep(0.5)
		driver.find_element(By.XPATH,value="//div[@aria-posinset='0']").click()
		sleep(0.5)
		driver.find_element(By.XPATH,value="//div[@aria-label='Good']").click()
		sleep(0.5)
		driver.find_element(By.XPATH,value="//button[@title='Submit']").click()
		sleep(2.5)
		driver.find_element(By.LINK_TEXT,value="Submit another response").click()
		sleep(0.5)
	driver.close()

def run7F(roomlistdict):
	
	driver = webdriver.Chrome(options=chrome_options,executable_path=chromedriver)
	driver.get(os.getenv('FORM'))
	sleep(3)

	for meetingroom7 in roomlistdict[7].values():
		driver.find_element(By.XPATH,value="//div[@aria-posinset='0']").click()
		sleep(0.5)
		driver.find_element(By.XPATH,value="//div[@aria-label='7F']").click()
		sleep(0.5)
		driver.find_element(By.XPATH,value="//div[@aria-posinset='0']").click()
		sleep(0.5)
		driver.find_element(By.XPATH,value="//div[@aria-label=\"{}\"]".format(str(meetingroom7))).click()
		sleep(0.5)
		driver.find_element(By.XPATH,value="//div[@aria-posinset='0']").click()
		sleep(0.5)
		driver.find_element(By.XPATH,value="//div[@aria-label='Good']").click()
		sleep(0.5)
		driver.find_element(By.XPATH,value="//button[@title='Submit']").click()
		sleep(2.5)
		driver.find_element(By.LINK_TEXT,value="Submit another response").click()
		sleep(0.5)
	driver.close()

def runDaily(roomlistdict):
	
	driver = webdriver.Chrome(options=chrome_options,executable_path=chromedriver)
	driver.get(os.getenv('FORM'))
	sleep(3)

	for Dailycheckresult in roomlistdict[0].values():
		driver.find_element(By.XPATH,value="//div[@aria-posinset='0']").click()
		sleep(0.5)
		driver.find_element(By.XPATH,value="//div[@aria-label=\"{}\"]".format(str(Dailycheckresult[0]))).click()
		sleep(0.5)
		driver.find_element(By.XPATH,value="//div[@aria-posinset='0']").click()
		sleep(0.5)
		driver.find_element(By.XPATH,value="//div[@aria-label=\"{}\"]".format(str(Dailycheckresult[1]))).click()
		sleep(0.5)
		driver.find_element(By.XPATH,value="//div[@aria-posinset='0']").click()
		sleep(0.5)
		driver.find_element(By.XPATH,value="//div[@aria-label='Good']").click()
		sleep(0.5)
		driver.find_element(By.XPATH,value="//button[@title='Submit']").click()
		sleep(2.5)
		driver.find_element(By.LINK_TEXT,value="Submit another response").click()
		sleep(0.5)
	driver.close()

run(roomlistdict)
