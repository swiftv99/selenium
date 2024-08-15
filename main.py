from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
sleep(3)

# Go to webpage
driver.get("https://practicetestautomation.com/practice-test-login/")
sleep(3)

# Type username student into Username field
username_locator = driver.find_element(By.ID, "username")
username_locator.send_keys("student")

# Type password Password123 into Password field
password_locator = driver.find_element(By.NAME, "password")
password_locator.send_keys("Password123")

# Push Submit button
submit_button_locator = driver.find_element(By.XPATH, "//")
submit_button_locator.click()

time.sleep(2)

# Verify new page URL contains practicetestautomation.com/logged-in-successfully/
actual_url = driver.current_url
assert actual_url == "https://practicetestautomation.com/logged-in-successfully/"

# Verify new page contains expected text ('Congratulations' or 'successfully logged in')
text_locator = driver.find_element(By.TAG_NAME, "h1")
actual_text = text_locator.text
assert actual_text == "Logged In Successfully"

# Verify button Log out is displayed on the new page
logout_button_locator = driver.find_element(By.LINK_TEXT, "Log out")
assert logout_button_locator.is_displayed()

driver.quit()
