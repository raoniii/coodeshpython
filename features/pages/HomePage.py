import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class HomePage:
    def __init__(self, driver):
        self.driver = driver

    ok_button_id = "onetrust-accept-btn-handler"
    email_field_id = "field-6"
    message_xpath = '//*[@id="content"]/div/div[2]/div/div/div/div/form/div/h1'


    def click_on_ok_button(self):
        wait = WebDriverWait(self.driver, 10)
        ok_button = wait.until(EC.visibility_of_element_located((By.ID, self.ok_button_id)))
        ok_button.click()

    def check_display_login_text(self, expected_message_text):
        element = self.driver.find_element(By.XPATH, self.message_xpath)
        actual_text = element.text.strip()
        time.sleep(10)
        return actual_text == expected_message_text 

    def enter_email_login(self, email_text):
        email_field = self.driver.find_element(By.ID, self.email_field_id)
        email_field.send_keys(email_text)
        time.sleep(10)
