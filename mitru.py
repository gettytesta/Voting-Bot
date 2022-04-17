import csv
import random
import time
from selenium import webdriver 
from selenium.webdriver.common.keys import Keys

firstNames = []
lastNames = []
zipCodes = []
tempCount = 0

with open('firstnames.csv') as csvfile:
	reader = csv.reader(csvfile)
	for row in reader:
		firstNames.append(row[0])

with open('lastnames.csv') as csvfile:
	reader = csv.reader(csvfile)
	for row in reader:
		lastNames.append(row[0].capitalize())

with open('zipcodes.csv') as csvfile:
	reader = csv.reader(csvfile)
	for row in reader:
		zipCodes.append(row[0])

for i in range(300):
	driver = webdriver.Chrome('/Users/maxwelltesta/Desktop/Mitru/chromedriver')
	driver.get("https://www.surveymonkey.com/r/HG2HJT6?embedded=1")

	nameForm = driver.find_element_by_id('613160334_4032761712')
	nameForm.send_keys(random.choice(firstNames) + " " + random.choice(lastNames))

	zipForm = driver.find_element_by_id('613160334_4032761718')
	zipForm.send_keys(str(random.choice(zipCodes)))

	emailForm = driver.find_element_by_id('613160334_4032761720')
	emailForm.send_keys(random.choice(firstNames) + "124@gmail.com")

	nextButton = driver.find_element_by_xpath('//*[@id="patas"]/main/article/section/form/div[2]/button')
	nextButton.click()

	for j in range(7):
		nextButton = driver.find_element_by_xpath('//*[@id="patas"]/main/article/section/form/div[2]/button[2]')
		nextButton.click()

	categoryForm = driver.find_element_by_id('613260677_4033392025')
	categoryForm.send_keys("Photobooth")

	nomineeForm = driver.find_element_by_id('613260677_4033395703')
	nomineeForm.send_keys("BuffaLoveBus")

	doneButton = driver.find_element_by_xpath('//*[@id="patas"]/main/article/section/form/div[2]/button[2]')
	doneButton.click()

	driver.close()
	tempCount += 1
	print(tempCount)
	time.sleep(3.5)
