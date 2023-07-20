import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class HomePage:
    def __init__(self, driver):
        self.driver = driver

    locators = {
        "ok_button": (By.ID, "onetrust-accept-btn-handler"),
        "message": (By.XPATH, '//*[@id="content"]/div/div[2]/div/div/div/div/form/div/h1')
    }

    def click_on_ok_button(self):
        wait = WebDriverWait(self.driver, 10)
        ok_button = wait.until(EC.visibility_of_element_located(self.locators["ok_button"]))
        ok_button.click()
        time.sleep(1)

    def check_display_login_text(self, expected_message_text):
        element = self.driver.find_element(*self.locators["message"])
        actual_text = element.text.strip()
        return actual_text == expected_message_text 
