from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

place = 'София'

WINDOW_SIZE = '1920, 1080'

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)

chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=%s" % WINDOW_SIZE)

chrome = webdriver.Chrome(chrome_options)

url = 'https://www.sinoptik.bg/sofia-bulgaria-100727011'
chrome.get(url=url)

ok_btn = chrome.find_element(By.XPATH, '/html/body/div[8]/div[2]/div[2]/div[2]/div[2]/button[1]').click()

feel_like = chrome.find_element(By.XPATH, '//*[@id="wfCurrent"]/div/span[2]')

now_temp = chrome.find_element(By.XPATH, '//*[@id="wfCurrent"]/div/span[1]/span')

print("Температура в София:", now_temp.text)
print(feel_like.text)

chrome.quit()



