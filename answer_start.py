from selenium import webdriver
import time

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

driver_path = '/opt/homebrew/bin/chromedriver'
# driver = webdriver.Chrome(executable_path=driver_path)
service = Service(executable_path=driver_path) # 2) executable_pathを指定
driver = webdriver.Chrome(service=service) # 3) serviceを渡す
url = 'https://forms.office.com/Pages/ResponsePage.aspx?id=T6978HAr10eaAgh1yvlMhLFSzlSTrMtBgamnWEMH3GlUREJUSDhYNzhONDRQOVZaTVJGQVZENjk0TS4u&origin=Invitation&channel=0'
driver.get(url)
time.sleep(3)

element = driver.find_element(by=By.XPATH, value='//*[@id="question-list"]/div[1]/div[2]/div/span/input')
element.send_keys('富田凜太郎')
time.sleep(3)

element = driver.find_element(by=By.XPATH, value='//*[@id="question-list"]/div[2]/div[2]/div/div/div[1]/div/label/span[1]/input')
element.click()
time.sleep(3)

element = driver.find_element(by=By.XPATH, value='//*[@id="form-main-content1"]/div/div/div[2]/div[3]/div/button')
element.click()

driver.close()