from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

place = 'София'
url = 'https://www.sinoptik.bg/sofia-bulgaria-100727011'
WINDOW_SIZE = '1920, 1080'

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)

chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=%s" % WINDOW_SIZE)

chrome = webdriver.Chrome(chrome_options)

chrome.get(url=url)

ok_btn = chrome.find_element(By.XPATH, '/html/body/div[8]/div[2]/div[2]/div[2]/div[2]/button[1]').click()

feel_like = chrome.find_element(By.XPATH, '//*[@id="wfCurrent"]/div/span[2]')

now_temp = chrome.find_element(By.XPATH, '//*[@id="wfCurrent"]/div/span[1]/span')

temperature = ''
temperature += f"Температура в София:, {now_temp.text}\n"
temperature += f"Чувства се като: {feel_like.text}\n"
chrome.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div[1]/div[4]/ul/li[5]/a').click()

time.sleep(1)

days_14 = chrome.find_element(By.XPATH, '//*[@id="wf10day"]/div[2]/div/div/div')

result = []
for el in days_14.text:
    result.append(el)

text = ''
for el in result:
    if el in "\n ":
        text += " "
    if el == "s":
        text += "s\n"
    else:
        text += el

print(text)

chrome.quit()



