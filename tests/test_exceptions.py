import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from page_objects.exception_page import ExceptionPage


class TestExceptions:
    @pytest.mark.exceptions
    def test_no_such_element_exception(self, driver):
        exception_page = ExceptionPage(driver)
        exception_page.open()
        exception_page.add_second_row()
        assert exception_page.is_row2_displayed(), "Row 2 input should be displayed, but it's not"
        
        # # Open page
        # driver.get("https://practicetestautomation.com/practice-test-exceptions/")

        # # Click Add button
        # add_button_locator = driver.find_element(By.ID, "add_btn")
        # add_button_locator.click()

        # # Verify Row 2 input field is displayed
        # wait = WebDriverWait(driver, 10)
        # row_2_input_element = wait.until(ec.presence_of_element_located((By.XPATH, "//div[@id='row2']/input")))
        # assert row_2_input_element.is_displayed(), "Row 2 input should be displayed, but it's not"


    @pytest.mark.exceptions
    def test_element_not_interactable_exception(self, driver):
        exception_page = ExceptionPage(driver)
        exception_page.open()
        exception_page.add_second_row()
        exception_page.add_second_food("Falafel")
        assert exception_page.get_confirmation_message() == "Row 2 was saved", "Confirmation message is not displayed"
        
        # # Open page
        # driver.get("https://practicetestautomation.com/practice-test-exceptions/")

        # # Click Add button
        # add_button_locator = driver.find_element(By.ID, "add_btn")
        # add_button_locator.click()

        # # Wait for the second row to load
        # wait = WebDriverWait(driver, 10)
        # row_2_input_element = wait.until(ec.presence_of_element_located((By.XPATH, "//div[@id='row2']/input")))

        # # Type text into the second input field
        # row_2_input_element.send_keys("Falafel")

        # # Push Save button using locator By.name(“Save”)
        # # driver.find_element(By.NAME, "Save").click()
        # driver.find_element(By.XPATH, "//div[@id='row2']/button[@name='Save']").click()

        # # Verify text saved
        # confirmation_element = wait.until(ec.visibility_of_element_located((By.ID, "confirmation")))
        # confirmation_message = confirmation_element.text
        # assert confirmation_message == "Row 2 was saved", "Confirmation message is not displayed"


    @pytest.mark.exceptions
    def test_invalid_element_state_exception(self, driver):
        exception_page = ExceptionPage(driver)
        exception_page.open()
        exception_page.modify_row1_input("Falafel")
        assert exception_page.get_confirmation_message() == "Row 1 was saved", "Confirmation message is not displayed"
        
        # # Open page
        # driver.get("https://practicetestautomation.com/practice-test-exceptions/")

        # # Clear input field
        # driver.find_element(By.XPATH, "//div[@id='row1']/button[@id='edit_btn']").click()
        
        # row_1_input_element = driver.find_element(By.XPATH, "//div[@id='row1']/input")
        # wait = WebDriverWait(driver, 10)
        # wait.until(ec.element_to_be_clickable(row_1_input_element))
        # row_1_input_element.clear()

        # # Type text into the input field
        # row_1_input_element.send_keys("Falafel")
        # driver.find_element(By.XPATH, "//div[@id='row1']/button[@id='save_btn']").click()

        # # Verify text changed
        # # text = row_1_input_element.get_attribute("value")
        # # assert text == "Falafel", "Expected Falafel, but still received Pizza"
        # confirmation_element = wait.until(ec.visibility_of_element_located((By.ID, "confirmation")))
        # confirmation_message = confirmation_element.text
        # assert confirmation_message == "Row 1 was saved", "Confirmation message is not displayed"


    @pytest.mark.exceptions
    def test_stale_element_reference_exception(self, driver):
        exception_page = ExceptionPage(driver)
        exception_page.open()
        exception_page.add_second_row()
        assert not exception_page.are_instructions_displayed(), "Instruction text element should not be displayed"
        
        # # Open page
        # driver.get("https://practicetestautomation.com/practice-test-exceptions/")

        # # Find the instructions text element
        # # instructions_text_element = driver.find_element(By.ID, "instructions")

        # # Push add button
        # add_button = driver.find_element(By.XPATH, "//div[@id='row1']/button[@id='add_btn']")
        # add_button.click()

        # # Verify instruction text element is no longer displayed
        # wait = WebDriverWait(driver, 10)
        # assert wait.until(ec.invisibility_of_element_located((By.ID, "instructions")), "Instruction text element is still displayed")


    @pytest.mark.exceptions
    @pytest.mark.debug
    def test_timeout_exception(self, driver):
        exception_page = ExceptionPage(driver)
        exception_page.open()
        exception_page.add_second_row()
        assert exception_page.is_row2_displayed(), "Row 2 input should be displayed, but it's not"
        
        # # Open page
        # driver.get("https://practicetestautomation.com/practice-test-exceptions/")

        # # Click Add button
        # driver.find_element(By.XPATH, "//div[@id='row1']/button[@id='add_btn']").click()

        # # Wait for 3 seconds for the second input field to be displayed
        # wait = WebDriverWait(driver, 6)
        # row_2_input_element = wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@id='row2']/input")), "Failed waiting for Row 2 input to be visible")

        # # Verify second input field is displayed
        # assert row_2_input_element.is_displayed(), "Row 2 input should be displayed, but it's not"
    