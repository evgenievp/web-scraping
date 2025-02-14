import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

song_name = input("This bot will start random entered song. Please enter singer and song: ")
url = "https://www.youtube.com/"
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(chrome_options)
driver.get(url)

agree_all = driver.find_element(By.XPATH, '//*[@id="content"]/div[2]/div[6]/div[1]/ytd-button-renderer[2]/yt-button-shape/button')
agree_all.send_keys(Keys.ENTER)

time.sleep(1)

search_btn = driver.find_element(By.CSS_SELECTOR, '#center > yt-searchbox > div.ytSearchboxComponentInputBox.ytSearchboxComponentInputBoxDark > form > input')

search_btn.send_keys(song_name)

search_btn.send_keys(Keys.ENTER)

time.sleep(1)

container = driver.find_element(By.XPATH, '//*[@id="dismissible"]/ytd-thumbnail')

for i in range(100):
    try:
        video_title = ''
        container.find_element(By.TAG_NAME, 'a').click()
    except Exception:
        pass


