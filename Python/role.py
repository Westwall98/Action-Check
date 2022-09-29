from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from time import sleep
from datetime import date
import datetime
import requests
import os

# For Chrome 105 #

F5roomlist = ['Aberlour','Church Road','Kahlúa','Ricard','Beefeater','Olmeca','Monkey 47','The Glenlivet']
F7roomlist = ['Cognac','Jameson','Whisky','White spirits','Wine','Martell QSS']
Dailyroomlist = [['7F','Boardroom']]

def run(F5roomlist,F7roomlist,Dailyroomlist):

	weekday = datetime.date.today().isoweekday()
  	apiurl = "https://api.westwall.vip/v1/sender/CNzjsKwGEiJBRDVZRVNISDNJWk9RM05LTkpOV1pRM09TWFhZTEFPT1Q0IgkIAhoFQ2hlY2sqIkFFUUM3VFlSVTdZSlFQVlZSQklXNVpJNkNWNU9PRlI1N1U..RK2ROlBmZIXp_c2_0BL7mZVYsm_W5hxtjfqKjjk3aQo"
	apidate = datetime.date.today()
	payload={'text': '{}会议室巡检运行成功'.format(apidate)}

	if weekday == 1 or weekday == 3:
		run7F(F7roomlist)
	elif weekday == 2 or weekday == 4:
		run5F(F5roomlist)
	elif weekday == 5:
		runDaily(Dailyroomlist)
    
  response = requests.post(apiurl, data = payload)

def run5F(F5roomlist):
	
	chrome_options = webdriver.ChromeOptions()
	chrome_options.add_argument('--headless')
	chrome_options.add_argument('--no-sandbox')
	chrome_options.add_argument('--disable-gpu')
	chrome_options.add_argument('--disable-dev-shm-usage')
	chromedriver = "/usr/bin/chromedriver"
	os.environ["webdriver.chrome.driver"] = chromedriver
	driver = webdriver.Chrome(chrome_options=chrome_options,executable_path=chromedriver)
	driver.get("https://forms.office.com/r/3AQwbrGbms")
	sleep(2)

	for meetingroom5 in F5roomlist:
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
		sleep(1)
		driver.find_element(By.XPATH,value="//button[@title='Submit']").click()
		sleep(3)
		driver.find_element(By.LINK_TEXT,value="Submit another response").click()
		sleep(0.5)
	driver.close()

def run7F(F7roomlist):
	
	chrome_options = webdriver.ChromeOptions()
	chrome_options.add_argument('--headless')
	chrome_options.add_argument('--no-sandbox')
	chrome_options.add_argument('--disable-gpu')
	chrome_options.add_argument('--disable-dev-shm-usage')
	chromedriver = "/usr/bin/chromedriver"
	os.environ["webdriver.chrome.driver"] = chromedriver
	driver = webdriver.Chrome(chrome_options=chrome_options,executable_path=chromedriver)

	driver.get("https://forms.office.com/r/3AQwbrGbms")
	sleep(2)

	for meetingroom7 in F7roomlist:
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
		sleep(1)
		driver.find_element(By.XPATH,value="//button[@title='Submit']").click()
		sleep(3)
		driver.find_element(By.LINK_TEXT,value="Submit another response").click()
		sleep(0.5)
	driver.close()

def runDaily(Dailyroomlist):
	
	chrome_options = webdriver.ChromeOptions()
	chrome_options.add_argument('--headless')
	chrome_options.add_argument('--no-sandbox')
	chrome_options.add_argument('--disable-gpu')
	chrome_options.add_argument('--disable-dev-shm-usage')
	chromedriver = "/usr/bin/chromedriver"
	os.environ["webdriver.chrome.driver"] = chromedriver
	driver = webdriver.Chrome(chrome_options=chrome_options,executable_path=chromedriver)
	driver.get("https://forms.office.com/r/3AQwbrGbms")
	sleep(2)

	for Dailycheckresult in Dailyroomlist:
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
		sleep(1)
		driver.find_element(By.XPATH,value="//button[@title='Submit']").click()
		sleep(3)
		driver.find_element(By.LINK_TEXT,value="Submit another response").click()
		sleep(0.5)
	driver.close()

run(F5roomlist,F7roomlist,Dailyroomlist)
