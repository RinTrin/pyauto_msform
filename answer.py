from selenium import webdriver
import time

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

driver_path = '/opt/homebrew/bin/chromedriver'
# driver = webdriver.Chrome(executable_path=driver_path)
service = Service(executable_path=driver_path) # 2) executable_pathを指定
driver = webdriver.Chrome(service=service) # 3) serviceを渡す
url = 'https://forms.office.com/Pages/ResponsePage.aspx?id=T6978HAr10eaAgh1yvlMhBs7uN44gNpFiQdVIJJtZ5xUNkZOUUhYSDVKUFJIV0gyVEtRWDg0MjZENC4u'
driver.get(url)
time.sleep(3)

element = driver.find_element(by=By.XPATH, value='//*[@id="question-list"]/div[1]/div[2]/div/span/input')
element.send_keys('富田凜太郎')
time.sleep(3)


with open("check_start_or_end.txt", "rb") as f:
    check_start_or_end = f.read().decode("utf-8")
if int(check_start_or_end) == 0:
    element = driver.find_element(by=By.XPATH, value='//*[@id="question-list"]/div[2]/div[2]/div/div/div[1]/div/label/span[1]/input')
    element.click()
    with open("check_start_or_end.txt", "w") as f:
        f.write("1")
else:
    element = driver.find_element(by=By.XPATH, value='//*[@id="question-list"]/div[2]/div[2]/div/div/div[4]/div/label/span[1]/input')
    element.click()
    with open("check_start_or_end.txt", "w") as f:
        f.write("0")
time.sleep(3)

element = driver.find_element(by=By.XPATH, value='//*[@id="form-main-content1"]/div/div/div[2]/div[3]/div/button')
element.click()

driver.close()