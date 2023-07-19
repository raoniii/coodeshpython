import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC

class VagasPage:
    def __init__(self, driver):
        self.driver = driver

    ok_button_id = "onetrust-accept-btn-handler"
    email_field_id = "field-6"
    password_field_id = "field-7"
    entrar_button_xpath = '//*[@id="content"]/div/div[2]/div/div/div/div/form/div/button[2]'
    vagas_button_xpath = '//*[@id="content"]/div/div/div[2]/div[2]/div[3]/a/div'
    search_field_xpath = '//*[@id="content"]/div/div[1]/form/div/div[1]/div/input'
    search_button_xpath = '//*[@id="content"]/div/div[1]/div/div/div[1]/div/div/button'


    def click_on_element(self, element_name, xpath,):
        element = self.driver.find_element(By.XPATH, xpath)
        element.click()
        time.sleep(1)

    def click_on_ok_button(self):
        wait = WebDriverWait(self.driver, 10)
        ok_button = wait.until(EC.visibility_of_element_located((By.ID, self.ok_button_id)))
        ok_button.click()
        time.sleep(5)

    def enter_email_login(self, email_text):
        email_field = self.driver.find_element(By.ID, self.email_field_id)
        email_field.send_keys(email_text)
        time.sleep(2)

    def enter_password_login(self, password_text):
        password_field = self.driver.find_element(By.ID, self.password_field_id)
        password_field.send_keys(password_text)
        time.sleep(2)
    
    def click_on_entrar_button(self):
        self.click_on_element("entrar_button_xpath", self.entrar_button_xpath)
        time.sleep(5)

    def click_on_vagas_button(self):
        self.click_on_element("vagas_button_xpath", self.vagas_button_xpath)
        time.sleep(5)

    
    def enter_search_company(self, search_text):
    
        wait = WebDriverWait(self.driver, 5)
        self.driver.implicitly_wait(5)
        self.click_on_element("search_field_xpath", self.search_field_xpath)
        search_field = self.driver.find_element(By.XPATH, self.search_field_xpath)
        search_field.send_keys(search_text)
        search_field.send_keys(Keys.RETURN)
        time.sleep(5)


    
    