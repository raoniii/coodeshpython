import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC

class CadastroPage:
    def __init__(self, driver):
        self.driver = driver

    ok_button_id = "onetrust-accept-btn-handler"
    nova_conta_button_xpath = '//*[@id="content"]/div/div[1]/div/nav/div/div/div[4]/div[1]/a'
    full_name_field_xpath = '//*[@id="field-6"]'
    email_field_xpath = '//*[@id="field-7"]'
    password_field_xpath = '//*[@id="field-8"]'
    li_aceito_button_xpath = '//*[@id="tabs-12--tabpanel-0"]/div/div[5]/label[1]/span'
    inscreva_button_xpath = '//*[@id="tabs-12--tabpanel-0"]/div/button[2]'
    onboarding_message_xpath = '//*[@id="header"]/div[1]/div/div/h1'

    career_frontend_xpath = '//*[@id="__next"]/div[3]/div/div/div/div/div[1]/form/div[3]/div[2]/div/div/span'
    habilidade_field_xpath = '//*[@id="__next"]/div[3]/div/div/div/div/div[1]/form/div[4]/div[1]/div[2]/div/span[6]'
    area_tech_xpath = '//*[@id="__next"]/div[3]/div/div/div/div/div[1]/form/div[4]/div[2]/div/div[3]/span[5]'
    rc_slider_handle = '//*[@class="rc-slider-handle"]'
    job_preference_xpath = '//select[@id="preferences.job_search"]'
    option_job_preference_xpaht = '//select[@id="preferences.job_search"]/option[1]'

    def click_on_ok_button(self):
        wait = WebDriverWait(self.driver, 10)
        ok_button = wait.until(EC.visibility_of_element_located((By.ID, self.ok_button_id)))
        ok_button.click()
        time.sleep(1)
    
    

    def click_on_element(self, element_name, xpath,):
        element = self.driver.find_element(By.XPATH, xpath)
        element.click()
       

    def click_on_element_id(self, element_name, id,):
        element_id = self.driver.find_element(By.ID, id)
        element_id.click()
        time.sleep(1)

    def click_on_nova_conta_button(self):
        self.click_on_element("nova_conta_button_xpath", self.nova_conta_button_xpath)
        time.sleep(2)

    def enter_full_name(self, full_name_text):
        full_name_field = self.driver.find_element(By.XPATH, self.full_name_field_xpath)
        full_name_field.send_keys(full_name_text)
        time.sleep(1)
    
    def enter_email(self, email_text):
        email_field = self.driver.find_element(By.XPATH, self.email_field_xpath)
        email_field.send_keys(email_text)
        time.sleep(1)
   
    def enter_password(self, password_text):
        password_field = self.driver.find_element(By.XPATH, self.password_field_xpath)
        password_field.send_keys(password_text)
       

    def click_on_li_aceito(self):
        self.click_on_element("li_aceito_button_xpath", self.li_aceito_button_xpath)
        time.sleep(1)

    def click_on_inscreva(self):
        self.click_on_element("inscreva_button_xpath", self.inscreva_button_xpath)
        time.sleep(5)

    def check_display_onboarding_text(self, expected_message_text):
        time.sleep(5)
        element = self.driver.find_element(By.XPATH, self.onboarding_message_xpath)
        actual_text = element.text.strip()
        time.sleep(5)
        return actual_text == expected_message_text 


#################################################
#                                               #
#       DAQUI PRA BAIXO CADASTROCOMPLETO        #
#                                               #
#################################################


    def click_on_career(self):
        time.sleep(3)
        self.click_on_element("career_frontend_xpath", self.career_frontend_xpath)
        time.sleep(2)

    def enter_habilidade(self):
        time.sleep(2)
        self.click_on_element("habilidade_field_xpath", self.habilidade_field_xpath)
        time.sleep(3)


    def click_on_exptech(self):
        wait = WebDriverWait(self.driver, 5)
        self.driver.implicitly_wait(5)
        slider_handle = self.driver.find_element(By.XPATH, self.rc_slider_handle)


        # Calcula o deslocamento necessário para alcançar 50%
        deslocamento = 50

        # Cria uma instância da classe ActionChains para manipular ações do mouse
        action_chains = ActionChains(self.driver)

        # Move o controle deslizante para 50%
        action_chains.drag_and_drop_by_offset(slider_handle, deslocamento, 0).perform()
        time.sleep(5)
    
    def select_job_preference(self):
        wait = WebDriverWait(self.driver, 5)
        self.driver.implicitly_wait(5)
        self.click_on_element("search_field_xpath", self.job_preference_xpath)
        self.click_on_element("search_field_xpath", self.option_job_preference_xpaht)
        
        time.sleep(5)
