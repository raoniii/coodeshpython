import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC

class CadastroPage:
    def __init__(self, driver):
        self.driver = driver

    locators = {
        "ok_button": (By.ID, "onetrust-accept-btn-handler"),
        "nova_conta_button": (By.XPATH, '//*[@id="content"]/div/div[1]/div/nav/div/div/div[4]/div[1]/a'),
        "full_name_field": (By.XPATH, '//*[@id="field-6"]'),
        "email_field": (By.XPATH, '//*[@id="field-7"]'),
        "password_field": (By.XPATH, '//*[@id="field-8"]'),
        "li_aceito_button": (By.XPATH, '//*[@id="tabs-12--tabpanel-0"]/div/div[5]/label[1]/span'),
        "inscreva_button": (By.XPATH, '//*[@id="tabs-12--tabpanel-0"]/div/button[2]'),
        "onboarding_message": (By.XPATH, '//*[@id="header"]/div[1]/div/div/h1'),
        "career_frontend": (By.XPATH, '//*[@id="__next"]/div[3]/div/div/div/div/div[1]/form/div[3]/div[2]/div/div/span'),
        "habilidade_field": (By.XPATH, '//*[@id="__next"]/div[3]/div/div/div/div/div[1]/form/div[4]/div[1]/div[2]/div/span[6]'),
        "rc_slider_handle": (By.XPATH, '//*[@class="rc-slider-handle"]'),
        "job_preference": (By.XPATH, '//select[@id="preferences.job_search"]'),
        "option_job_preference": (By.XPATH, '//select[@id="preferences.job_search"]/option[1]')
    }

    def click_on_ok_button(self):
        wait = WebDriverWait(self.driver, 10)
        ok_button = wait.until(EC.visibility_of_element_located(self.locators["ok_button"]))
        ok_button.click()

    def click_on_element(self, locator):
        element = self.driver.find_element(*locator)
        element.click()

    def enter_text(self, locator, text):
        element = self.driver.find_element(*locator)
        element.send_keys(text)

    def click_on_nova_conta_button(self):
        self.click_on_element(self.locators["nova_conta_button"])

    def enter_full_name(self, full_name_text):
        self.enter_text(self.locators["full_name_field"], full_name_text)
    
    def enter_email(self, email_text):
        self.enter_text(self.locators["email_field"], email_text)
   
    def enter_password(self, password_text):
        self.enter_text(self.locators["password_field"], password_text)

    def click_on_li_aceito(self):
        self.click_on_element(self.locators["li_aceito_button"])

    def click_on_inscreva(self):
        self.click_on_element(self.locators["inscreva_button"])

    def check_display_onboarding_text(self, expected_message_text):
        element = self.driver.find_element(*self.locators["onboarding_message"])
        actual_text = element.text.strip()
        return actual_text == expected_message_text 

    def click_on_career(self):
        self.click_on_element(self.locators["career_frontend"])

    def enter_habilidade(self):
        self.click_on_element(self.locators["habilidade_field"])

    def click_on_exptech(self):
        ...
