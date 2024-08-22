from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from page_objects.base_page import BasePage


class LoggedInSuccessfullyPage(BasePage):
    __url = "https://practicetestautomation.com/logged-in-successfully/"
    __header_locator = (By.TAG_NAME, "h1")
    __logout_button_locator = (By.LINK_TEXT, "Log out")

    def __init__(self, driver: WebDriver):
        # self._driver = driver
        super().__init__(driver)
    
    @property
    def expected_url(self) -> str:
        return self.__url
    
    @property
    def header(self) -> str:
        # return self._driver.find_element(self.__header_locator).text
        return super()._get_text(self.__header_locator)
    
    def is_logout_button_displayed(self) -> bool:
        # return self._driver.find_element(self.__logout_button_locator).is_displayed()
        return super()._is_displayed(self.__logout_button_locator)