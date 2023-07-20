import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
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
        "rc_slider_handle": (By.XPATH, '//*[@id="__next"]/div[3]/div/div/div/div/div[1]/form/div[4]/div[2]/div/div[4]'),
        "job_preference": (By.XPATH, '//select[@id="preferences.job_search"]'),
        "option_job_preference": (By.XPATH, '//select[@id="preferences.job_search"]/option[1]'),
        "integral_checkbox": (By.XPATH, '//*[@id="home-office-integral"]'),
        "whatsapp_field": (By.XPATH, '//*[@id="__next"]/div[3]/div/div/div/div/div[1]/form/div[5]/div[2]/div[1]/div[1]/input'),
        "city_field": (By.XPATH, '//*[@id="address.city"]'),
        "proximo_button": (By.XPATH, '//*[@id="footer-portal"]/div/div/button'),
        "comunidades_field": (By.XPATH, '//*[@id="__next"]/div[3]/div/div/div/div/div[2]/form/div[1]/div[1]/div/div[2]/span[1]'),
        "relacao_comunidades_field": (By.ID, "communities-0-relation"),
        "relacao_comunidades_enthusiast_option": (By.XPATH, '//*[@id="communities-0-relation"]/option[2]'),
        "causas_field": (By.ID, 'react-select-3-input'),
        "raca_cor_field": (By.ID, 'race'),
        "gender_field": (By.ID, 'gender'),
        "sexual_orientation_field": (By.ID, 'sexual_orientation'),
        "disabilities_field": (By.ID, 'disabilities.type'),
        "proximo_button2": (By.XPATH, '//*[@id="footer-portal"]/div/div/button[2]'),
        "scorecard_message": (By.XPATH, '//*[@id="__next"]/div[3]/div[2]/div[1]/span'),
        "responder_button": (By.XPATH, '//*[@id="footer-portal"]/div/div/a'),
        "rc_slider_handle_scoreb1_opt1": (By.XPATH, '//*[@id="__next"]/div[3]/div/div/form/table/tbody/tr[1]/td/div/div[4]'),
        "rc_slider_handle_scoreb1_opt1": (By.XPATH, '//*[@id="__next"]/div[3]/div/div/form/table/tbody/tr[1]/td/div/div[4]'),
        "rc_slider_handle_scoreb1_opt2": (By.XPATH, '//*[@id="__next"]/div[3]/div/div/form/table/tbody/tr[2]/td/div/div[4]'),
        "rc_slider_handle_scoreb1_opt3": (By.XPATH, '//*[@id="__next"]/div[3]/div/div/form/table/tbody/tr[3]/td/div/div[4]'),
        "rc_slider_handle_scoreb1_opt4": (By.XPATH, '//*[@id="__next"]/div[3]/div/div/form/table/tbody/tr[4]/td/div/div[4]'),
        "rc_slider_handle_scoreb1_opt5": (By.XPATH, '//*[@id="__next"]/div[3]/div/div/form/table/tbody/tr[5]/td/div/div[4]'),
        "rc_slider_handle_scoreb1_opt6": (By.XPATH, '//*[@id="__next"]/div[3]/div/div/form/table/tbody/tr[6]/td/div/div[4]'),
        "rc_slider_handle_scoreb1_opt7": (By.XPATH, '//*[@id="__next"]/div[3]/div/div/form/table/tbody/tr[7]/td/div/div[4]'),
        "rc_slider_handle_scoreb1_opt8": (By.XPATH, '//*[@id="__next"]/div[3]/div/div/form/table/tbody/tr[8]/td/div/div[4]'),
        "rc_slider_handle_scoreb1_opt9": (By.XPATH, '//*[@id="__next"]/div[3]/div/div/form/table/tbody/tr[9]/td/div/div[4]'),
        "rc_slider_handle_scoreb1_opt10": (By.XPATH, '//*[@id="__next"]/div[3]/div/div/form/table/tbody/tr[10]/td/div/div[4]'),
        "proximo_score1_button": (By.XPATH, '//*[@id="footer-portal"]/div/div/button[2]'),
        "proximo_score1_buttonpt2": (By.XPATH, '//*[@id="footer-portal"]/div/div/button[2]'),
        "enviar_button": (By.XPATH, '//*[@id="footer-portal"]/div/div/button[2]'),
        "concluir_button": (By.XPATH, '//*[@id="footer-portal"]/div/div/a')
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
        time.sleep(2)

    def click_on_inscreva(self):
        self.click_on_element(self.locators["inscreva_button"])
        time.sleep(5)

    def check_display_onboarding_text(self, expected_message_text):
        time.sleep(5)
        element = self.driver.find_element(*self.locators["onboarding_message"])
        actual_text = element.text.strip()
        return actual_text == expected_message_text 

    def click_on_career(self):
        time.sleep(5)
        self.click_on_element(self.locators["career_frontend"])

    def enter_habilidade(self):
        time.sleep(5)
        self.click_on_element(self.locators["habilidade_field"])

    def click_on_exptech(self):
        time.sleep(1)
        wait = WebDriverWait(self.driver, 10)
        exptech = wait.until(EC.visibility_of_element_located(self.locators["rc_slider_handle"]))
        exptech.click()
        exptech.send_keys(Keys.ARROW_RIGHT)      
    
    def enter_whatsapp(self, whatsapp_field_text):
        time.sleep(1)
        self.enter_text(self.locators["whatsapp_field"], whatsapp_field_text)
        time.sleep(1)
    
    def enter_city(self, city_filed_text):
        time.sleep(1)
        self.enter_text(self.locators["city_field"], city_filed_text)
        time.sleep(1)

    def click_on_integral_checkbox(self):
        time.sleep(3)
        wait = WebDriverWait(self.driver, 10)
        integral_checkbox_option = wait.until(EC.visibility_of_element_located(self.locators["integral_checkbox"]))
        integral_checkbox_option.click()
        time.sleep(3)

    def click_proximo_button(self):
        time.sleep(1)
        wait = WebDriverWait(self.driver, 10)
        proximo_button = wait.until(EC.visibility_of_element_located(self.locators["proximo_button"]))
        proximo_button.click()
        time.sleep(3)

    def click_on_comunidades(self):
        
        wait = WebDriverWait(self.driver, 10)
        comunidades_field = wait.until(EC.visibility_of_element_located(self.locators["comunidades_field"]))
        comunidades_field.click()
        time.sleep(3)

    def click_on_relacao_comunidades(self):
        time.sleep(1)
        wait = WebDriverWait(self.driver, 10)
        select = Select(self.driver.find_element(*self.locators["relacao_comunidades_field"]))
        select.select_by_visible_text('Entusiasta')
        time.sleep(1)

    def click_on_causas_sociais(self, causas_field_text):
        time.sleep(1)
        wait = WebDriverWait(self.driver, 10)
        causas_field = wait.until(EC.visibility_of_element_located(self.locators["causas_field"]))
        self.enter_text(self.locators["causas_field"], causas_field_text)
        causas_field.send_keys(Keys.RETURN)
        time.sleep(1)

    def click_on_raca_cor(self):
        time.sleep(1)
        wait = WebDriverWait(self.driver, 10)
        select = Select(self.driver.find_element(*self.locators["raca_cor_field"]))
        select.select_by_visible_text('Pessoa Branca')
        time.sleep(1)

    def click_on_genero(self):
        time.sleep(1)
        wait = WebDriverWait(self.driver, 10)
        select = Select(self.driver.find_element(*self.locators["gender_field"]))
        select.select_by_visible_text('Homem')
        time.sleep(1)

    def click_on_orientacao_sexual(self):
        time.sleep(1)
        wait = WebDriverWait(self.driver, 10)
        select = Select(self.driver.find_element(*self.locators["sexual_orientation_field"]))
        select.select_by_visible_text('Heterossexual')
        time.sleep(1)

    def click_on_deficiencia(self):
        time.sleep(1)
        wait = WebDriverWait(self.driver, 10)
        select = Select(self.driver.find_element(*self.locators["disabilities_field"]))
        select.select_by_visible_text('Nenhuma deficiência')
        time.sleep(3)

    def click_proximo_button2(self):
        time.sleep(1)
        wait = WebDriverWait(self.driver, 10)
        proximo_button = wait.until(EC.visibility_of_element_located(self.locators["proximo_button2"]))
        proximo_button.click()
        time.sleep(10)

    def check_display_scorecard_text(self, expected_message_text):
        time.sleep(3)
        element = self.driver.find_element(*self.locators["scorecard_message"])
        actual_text = element.text.strip()
        return actual_text == expected_message_text
    
    def click_proximo_responder(self):
        wait = WebDriverWait(self.driver, 10)
        proximo_button = wait.until(EC.visibility_of_element_located(self.locators["responder_button"]))
        proximo_button.click()
        time.sleep(10)        
    
    def preencher_scorecard1(self):
        time.sleep(3)
        wait = WebDriverWait(self.driver, 10)
        exptech1 = wait.until(EC.visibility_of_element_located(self.locators["rc_slider_handle_scoreb1_opt1"]))
        exptech1.click()
        exptech1.send_keys(Keys.ARROW_RIGHT)
        exptech1.send_keys(Keys.TAB)

        wait = WebDriverWait(self.driver, 10)
        exptech2 = wait.until(EC.visibility_of_element_located(self.locators["rc_slider_handle_scoreb1_opt2"]))
        exptech2.click()
        exptech2.send_keys(Keys.ARROW_RIGHT)
        exptech2.send_keys(Keys.TAB)

        wait = WebDriverWait(self.driver, 10)
        exptech3 = wait.until(EC.visibility_of_element_located(self.locators["rc_slider_handle_scoreb1_opt3"]))
        exptech3.click()
        exptech3.send_keys(Keys.ARROW_RIGHT)
        exptech3.send_keys(Keys.TAB)

        wait = WebDriverWait(self.driver, 10)
        exptech4 = wait.until(EC.visibility_of_element_located(self.locators["rc_slider_handle_scoreb1_opt4"]))
        exptech4.click()
        exptech4.send_keys(Keys.ARROW_RIGHT)
        exptech4.send_keys(Keys.TAB)

        wait = WebDriverWait(self.driver, 10)
        exptech5 = wait.until(EC.visibility_of_element_located(self.locators["rc_slider_handle_scoreb1_opt5"]))
        exptech5.click()
        exptech5.send_keys(Keys.ARROW_RIGHT)
        exptech5.send_keys(Keys.TAB)

        wait = WebDriverWait(self.driver, 10)
        exptech6 = wait.until(EC.visibility_of_element_located(self.locators["rc_slider_handle_scoreb1_opt6"]))
        exptech6.click()
        exptech6.send_keys(Keys.ARROW_RIGHT)
        exptech6.send_keys(Keys.TAB)

        wait = WebDriverWait(self.driver, 10)
        exptech7 = wait.until(EC.visibility_of_element_located(self.locators["rc_slider_handle_scoreb1_opt7"]))
        exptech7.click()
        exptech7.send_keys(Keys.ARROW_RIGHT)
        exptech7.send_keys(Keys.TAB)

        wait = WebDriverWait(self.driver, 10)
        exptech8 = wait.until(EC.visibility_of_element_located(self.locators["rc_slider_handle_scoreb1_opt8"]))
        exptech8.click()
        exptech8.send_keys(Keys.ARROW_RIGHT)
        exptech8.send_keys(Keys.TAB)

        wait = WebDriverWait(self.driver, 10)
        exptech9 = wait.until(EC.visibility_of_element_located(self.locators["rc_slider_handle_scoreb1_opt9"]))
        exptech9.click()
        exptech9.send_keys(Keys.ARROW_RIGHT)
        exptech9.send_keys(Keys.TAB)

        #wait = WebDriverWait(self.driver, 10)
        #exptech10 = wait.until(EC.visibility_of_element_located(self.locators["rc_slider_handle_scoreb1_opt10"]))
        #exptech10.click()
        #exptech10.send_keys(Keys.ARROW_RIGHT)
        #exptech10.send_keys(Keys.TAB)
        
        time.sleep(5)

    def click_proximo_button3(self):
        wait = WebDriverWait(self.driver, 10)
        button3 = wait.until(EC.visibility_of_element_located(self.locators["proximo_score1_button"]))
        button3.click()
        time.sleep(5)

    def preencher_scorecard2(self):
        time.sleep(3)
        wait = WebDriverWait(self.driver, 10)
        exptech11 = wait.until(EC.visibility_of_element_located(self.locators["rc_slider_handle_scoreb1_opt1"]))
        exptech11.click()
        exptech11.send_keys(Keys.ARROW_RIGHT)
        exptech11.send_keys(Keys.TAB)

        wait = WebDriverWait(self.driver, 10)
        exptech22 = wait.until(EC.visibility_of_element_located(self.locators["rc_slider_handle_scoreb1_opt2"]))
        exptech22.click()
        exptech22.send_keys(Keys.ARROW_RIGHT)
        exptech22.send_keys(Keys.TAB)

        wait = WebDriverWait(self.driver, 10)
        exptech33 = wait.until(EC.visibility_of_element_located(self.locators["rc_slider_handle_scoreb1_opt3"]))
        exptech33.click()
        exptech33.send_keys(Keys.ARROW_RIGHT)
        exptech33.send_keys(Keys.TAB)

        wait = WebDriverWait(self.driver, 10)
        exptech44 = wait.until(EC.visibility_of_element_located(self.locators["rc_slider_handle_scoreb1_opt4"]))
        exptech44.click()
        exptech44.send_keys(Keys.ARROW_RIGHT)
        exptech44.send_keys(Keys.TAB)

        wait = WebDriverWait(self.driver, 10)
        exptech55 = wait.until(EC.visibility_of_element_located(self.locators["rc_slider_handle_scoreb1_opt5"]))
        exptech55.click()
        exptech55.send_keys(Keys.ARROW_RIGHT)
        exptech55.send_keys(Keys.TAB)

        wait = WebDriverWait(self.driver, 10)
        exptech66 = wait.until(EC.visibility_of_element_located(self.locators["rc_slider_handle_scoreb1_opt6"]))
        exptech66.click()
        exptech66.send_keys(Keys.ARROW_RIGHT)
        exptech66.send_keys(Keys.TAB)

        wait = WebDriverWait(self.driver, 10)
        exptech77 = wait.until(EC.visibility_of_element_located(self.locators["rc_slider_handle_scoreb1_opt7"]))
        exptech77.click()
        exptech77.send_keys(Keys.ARROW_RIGHT)
        exptech77.send_keys(Keys.TAB)

        wait = WebDriverWait(self.driver, 10)
        exptech88 = wait.until(EC.visibility_of_element_located(self.locators["rc_slider_handle_scoreb1_opt8"]))
        exptech88.click()
        exptech88.send_keys(Keys.ARROW_RIGHT)
        exptech88.send_keys(Keys.TAB)

        wait = WebDriverWait(self.driver, 10)
        exptech99 = wait.until(EC.visibility_of_element_located(self.locators["rc_slider_handle_scoreb1_opt9"]))
        exptech99.click()
        exptech99.send_keys(Keys.ARROW_RIGHT)
        exptech99.send_keys(Keys.TAB)

        wait = WebDriverWait(self.driver, 10)
        exptech10 = wait.until(EC.visibility_of_element_located(self.locators["rc_slider_handle_scoreb1_opt10"]))
        exptech10.click()
        exptech10.send_keys(Keys.ARROW_RIGHT)
        exptech10.send_keys(Keys.TAB)

    def click_proximo_button4(self):
        wait = WebDriverWait(self.driver, 10)
        button4 = wait.until(EC.visibility_of_element_located(self.locators["proximo_score1_buttonpt2"]))
        button4.click()
        time.sleep(10)

    def preencher_scorecard3(self):
        time.sleep(3)
        wait = WebDriverWait(self.driver, 10)
        exptech111 = wait.until(EC.visibility_of_element_located(self.locators["rc_slider_handle_scoreb1_opt1"]))
        exptech111.click()
        exptech111.send_keys(Keys.ARROW_RIGHT)
        exptech111.send_keys(Keys.TAB)

        wait = WebDriverWait(self.driver, 10)
        exptech222 = wait.until(EC.visibility_of_element_located(self.locators["rc_slider_handle_scoreb1_opt2"]))
        exptech222.click()
        exptech222.send_keys(Keys.ARROW_RIGHT)
        exptech222.send_keys(Keys.TAB)

        wait = WebDriverWait(self.driver, 10)
        exptech333 = wait.until(EC.visibility_of_element_located(self.locators["rc_slider_handle_scoreb1_opt3"]))
        exptech333.click()
        exptech333.send_keys(Keys.ARROW_RIGHT)
        exptech333.send_keys(Keys.TAB)

    def click_enviar(self):
        wait = WebDriverWait(self.driver, 10)
        enviar = wait.until(EC.visibility_of_element_located(self.locators["enviar_button"]))
        enviar.click()
        time.sleep(5) 

    def click_concluir(self):
        wait = WebDriverWait(self.driver, 10)
        enviar = wait.until(EC.visibility_of_element_located(self.locators["concluir_button"]))
        enviar.click()
        time.sleep(10) 
    
