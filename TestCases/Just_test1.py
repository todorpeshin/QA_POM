from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.common.keys import Keys
import time


driver = webdriver.Chrome("C:\\Users\\TodorPeshin\\kryonsystems\\google-chrome\\chromedriver.exe")
driver.get("https://www.abv.bg/")

button_toclick = driver.find_element(By.ID, 'username')
button_toclick.send_keys("tpp")
time.sleep(1)
driver.__exit__()