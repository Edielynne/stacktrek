
from selenium import webdriver
from selenium.webdriver.common.key import Keys
import time

PATH = 'C:\Program Files (x86)\Chrome Driver\chromedriver.exe'
driver = webdriver.Chrome(PATH)

driver.get("https://stacktrek.com/")
print(driver.title)
search = driver.find_element_by_name("l")
driver.quit()