import pytest
from selenium import webdriver

@pytest.fixture()
def driver():
    print("Creating Firefox driver")
    options = webdriver.FirefoxOptions()
    options.add_argument("-headless")
    my_driver = webdriver.Firefox(options=options)
    yield my_driver
    print("Closing Firefox driver")
    my_driver.quit()
