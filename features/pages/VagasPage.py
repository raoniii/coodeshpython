import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC

class VagasPage:
    def __init__(self, driver):
        self.driver = driver

    locators = {
        "ok_button": (By.ID, "onetrust-accept-btn-handler"),
        "email_field": (By.ID, "field-6"),
        "password_field": (By.ID, "field-7"),
        "entrar_button": (By.XPATH, '//*[@id="content"]/div/div[2]/div/div/div/div/form/div/button[2]'),
        "vagas_button": (By.XPATH, '//*[@id="content"]/div/div/div[2]/div[2]/div[3]/a/div'),
        "search_field": (By.XPATH, '//*[@id="content"]/div/div[1]/form/div/div[1]/div/input')
    }

    def click_on_element(self, element_name):
        element = self.driver.find_element(*self.locators[element_name])
        element.click()

    def click_on_ok_button(self):
        wait = WebDriverWait(self.driver, 10)
        ok_button = wait.until(EC.visibility_of_element_located(self.locators["ok_button"]))
        ok_button.click()
        time.sleep(2)

    def enter_email_login(self, email_text):
        email_field = self.driver.find_element(*self.locators["email_field"])
        email_field.send_keys(email_text)
        time.sleep(1)

    def enter_password_login(self, password_text):
        password_field = self.driver.find_element(*self.locators["password_field"])
        password_field.send_keys(password_text)
        time.sleep(1)
    
    def click_on_entrar_button(self):
        self.click_on_element("entrar_button")
        time.sleep(5)

    def click_on_vagas_button(self):
        self.click_on_element("vagas_button")
        time.sleep(5)

    def enter_search_company(self, search_text):
        wait = WebDriverWait(self.driver, 5)
        self.driver.implicitly_wait(5)
        self.click_on_element("search_field")
        search_field = self.driver.find_element(*self.locators["search_field"])
        search_field.send_keys(search_text)
        search_field.send_keys(Keys.RETURN)
        time.sleep(5)
