import time
from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(chrome_options)

driver.get("https://orteil.dashnet.org/cookieclicker/")

time.sleep(10)

button = driver.find_element(By.ID, 'bigCookie')

while True:
    button.click()



