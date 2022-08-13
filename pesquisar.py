from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from webdrivermanager import ChromeDriverManager
driver = webdriver.Chrome()
driver.get('https://youtube.com')

searchbox = driver.find_element(By.XPATH, "//input[@id='search']")
searchbox.send_keys('hello')

searchButton = driver.find_element(By.XPATH, "//button[@id='search-icon-legacy']")
searchButton.click()
sleep(4)