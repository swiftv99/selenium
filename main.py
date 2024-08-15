from time import sleep
from selenium import webdriver

driver = webdriver.Chrome()

sleep(3)
driver.get("https://practicetestautomation.com/practice-test-login/")
sleep(3)

driver.quit()
