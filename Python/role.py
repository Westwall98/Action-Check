from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep
from datetime import date
import datetime
import requests
import os
import threading

roomlistdict = {
# 0:{30:("3F","Training Room"),50:("5F","Absolut"),60:("6F","Cordon Bleu"),61:("6F","Chivas"),70:("7F","Boardroom"),76:("7F","XXO")},
0:{30:("3F","Training Room"),60:("6F","Cordon Bleu"),61:("6F","Chivas")},
1:{50:("5F","Absolut"),70:("7F","Boardroom"),76:("7F","XXO"),77:("7F","Bar Area")},
3:{31:"Altos",32:"Havana Club",33:"Kinobi",34:"Jacob's Creek",35:"Lillet",36:"Ballantine's Finest"},
5:{51:"Aberlour",52:"Church Road",53:"Kahlúa",54:"Ricard",55:"Beefeater",56:"Olmeca",57:"Monkey 47",58:"The Glenlivet"},
6:{62:"Longmorn",63:"Malibu",64:"Noblige",65:"Mumm",66:"Pernod",67:"Secret Speyside",68:"Perrier-Jouet",69:"Royal Salute"},
7:{71:"Jameson",72:"Single Cru",73:"The Chuan",74:"Helan Mountain"}
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
	
	checkt0 = threading.Thread(target = runDaily0, args =(roomlistdict,))
	checkt1 = threading.Thread(target = runDaily1, args =(roomlistdict,))
	check3f = threading.Thread(target = run3F, args =(roomlistdict,))
	check5f = threading.Thread(target = run5F, args =(roomlistdict,))
	check6f = threading.Thread(target = run6F, args =(roomlistdict,))
	check7f = threading.Thread(target = run7F, args =(roomlistdict,))

	if weekday == 1 or weekday == 3 or weekday == 5:
		checkt0.start()
		checkt0.join()
		print('Success')
	elif weekday == 2 or weekday == 4:
		checkt1.start()
		checkt1.join()
		print('Success')
	
	response = requests.get(apiurl, params=params)

def run3F(roomlistdict):
	
	driver = webdriver.Chrome(options=chrome_options,executable_path=chromedriver)
	
	for meetingroom3 in roomlistdict[3].values():
		driver.get(os.getenv('FORM'))
		sleep(3)
		driver.find_elements(By.XPATH,value="//div[@aria-haspopup='listbox']")[0].click()
		sleep(0.5)
		driver.find_element(By.XPATH,value="//span[@aria-label='3F']").click()
		sleep(0.5)
		driver.find_elements(By.XPATH,value="//div[@aria-haspopup='listbox']")[1].click()
		sleep(0.5)
		driver.find_element(By.XPATH,value="//span[@aria-label=\"{}\"]".format(str(meetingroom3))).click()
		sleep(0.5)
		driver.find_elements(By.XPATH,value="//div[@aria-haspopup='listbox']")[2].click()
		sleep(0.5)
		driver.find_element(By.XPATH,value="//span[@aria-label='Good']").click()
		sleep(0.5)
		driver.find_element(By.XPATH,value="//button[@data-automation-id='submitButton']").click()
		sleep(3)
	driver.close()

def run5F(roomlistdict):
	
	driver = webdriver.Chrome(options=chrome_options,executable_path=chromedriver)
	

	for meetingroom5 in roomlistdict[5].values():
		driver.get(os.getenv('FORM'))
		sleep(3)
		driver.find_elements(By.XPATH,value="//div[@aria-haspopup='listbox']")[0].click()
		sleep(0.5)
		driver.find_element(By.XPATH,value="//span[@aria-label='5F']").click()
		sleep(0.5)
		driver.find_elements(By.XPATH,value="//div[@aria-haspopup='listbox']")[1].click()
		sleep(0.5)
		driver.find_element(By.XPATH,value="//span[@aria-label=\"{}\"]".format(str(meetingroom5))).click()
		sleep(0.5)
		driver.find_elements(By.XPATH,value="//div[@aria-haspopup='listbox']")[2].click()
		sleep(0.5)
		driver.find_element(By.XPATH,value="//span[@aria-label='Good']").click()
		sleep(0.5)
		driver.find_element(By.XPATH,value="//button[@data-automation-id='submitButton']").click()
		sleep(3)
	driver.close()

def run6F(roomlistdict):
	
	driver = webdriver.Chrome(options=chrome_options,executable_path=chromedriver)
	
	for meetingroom6 in roomlistdict[6].values():
		driver.get(os.getenv('FORM'))
		sleep(3)
		driver.find_elements(By.XPATH,value="//div[@aria-haspopup='listbox']")[0].click()
		sleep(0.5)
		driver.find_element(By.XPATH,value="//span[@aria-label='6F']").click()
		sleep(0.5)
		driver.find_elements(By.XPATH,value="//div[@aria-haspopup='listbox']")[1].click()
		sleep(0.5)
		driver.find_element(By.XPATH,value="//span[@aria-label=\"{}\"]".format(str(meetingroom6))).click()
		sleep(0.5)
		driver.find_elements(By.XPATH,value="//div[@aria-haspopup='listbox']")[2].click()
		sleep(0.5)
		driver.find_element(By.XPATH,value="//span[@aria-label='Good']").click()
		sleep(0.5)
		driver.find_element(By.XPATH,value="//button[@data-automation-id='submitButton']").click()
		sleep(3)
	driver.close()

def run7F(roomlistdict):
	
	driver = webdriver.Chrome(options=chrome_options,executable_path=chromedriver)
	
	for meetingroom7 in roomlistdict[7].values():
		driver.get(os.getenv('FORM'))
		sleep(3)
		driver.find_elements(By.XPATH,value="//div[@aria-haspopup='listbox']")[0].click()
		sleep(0.5)
		driver.find_element(By.XPATH,value="//span[@aria-label='7F']").click()
		sleep(0.5)
		driver.find_elements(By.XPATH,value="//div[@aria-haspopup='listbox']")[1].click()
		sleep(0.5)
		driver.find_element(By.XPATH,value="//span[@aria-label=\"{}\"]".format(str(meetingroom7))).click()
		sleep(0.5)
		driver.find_elements(By.XPATH,value="//div[@aria-haspopup='listbox']")[2].click()
		sleep(0.5)
		driver.find_element(By.XPATH,value="//span[@aria-label='Good']").click()
		sleep(0.5)
		driver.find_element(By.XPATH,value="//button[@data-automation-id='submitButton']").click()
		sleep(3)
	driver.close()

def runDaily0(roomlistdict):
	
	driver = webdriver.Chrome(options=chrome_options,executable_path=chromedriver)

	for Dailycheckresult in roomlistdict[0].values():
		driver.get(os.getenv('FORM'))
		sleep(10)
		driver.find_elements(By.XPATH,value="//div[@aria-haspopup='listbox']")[0].click()
		sleep(0.5)
		driver.find_element(By.XPATH,value="//span[@aria-label=\"{}\"]".format(str(Dailycheckresult[0]))).click()
		sleep(0.5)
		driver.find_elements(By.XPATH,value="//div[@aria-haspopup='listbox']")[1].click()
		sleep(0.5)
		driver.find_element(By.XPATH,value="//span[@aria-label=\"{}\"]".format(str(Dailycheckresult[1]))).click()
		sleep(0.5)
		driver.find_elements(By.XPATH,value="//div[@aria-haspopup='listbox']")[2].click()
		sleep(0.5)
		driver.find_element(By.XPATH,value="//span[@aria-label='Good']").click()
		sleep(0.5)
		driver.find_element(By.XPATH,value="//button[@data-automation-id='submitButton']").click()
		sleep(10)
	driver.close()

def runDaily1(roomlistdict):
	
	driver = webdriver.Chrome(options=chrome_options,executable_path=chromedriver)

	for Dailycheckresult in roomlistdict[1].values():
		driver.get(os.getenv('FORM'))
		sleep(10)
		driver.find_elements(By.XPATH,value="//div[@aria-haspopup='listbox']")[0].click()
		sleep(0.5)
		driver.find_element(By.XPATH,value="//span[@aria-label=\"{}\"]".format(str(Dailycheckresult[0]))).click()
		sleep(0.5)
		driver.find_elements(By.XPATH,value="//div[@aria-haspopup='listbox']")[1].click()
		sleep(0.5)
		driver.find_element(By.XPATH,value="//span[@aria-label=\"{}\"]".format(str(Dailycheckresult[1]))).click()
		sleep(0.5)
		driver.find_elements(By.XPATH,value="//div[@aria-haspopup='listbox']")[2].click()
		sleep(0.5)
		driver.find_element(By.XPATH,value="//span[@aria-label='Good']").click()
		sleep(0.5)
		driver.find_element(By.XPATH,value="//button[@data-automation-id='submitButton']").click()
		sleep(10)
	driver.close()

if __name__ == '__main__':
	run(roomlistdict)
