import time

import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base
from utilities.logger import Logger


class LoginPage(Base):
    url = 'https://upstore24.ru/'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(self.url)

    # Locators

    button_personal_account = "//ul[contains(@class, 'js-nav-items')]//a[contains(@href, 'client_account/login')]"
    email = "//input[@id='email']"
    password = "//input[@id='password']"
    login_button = "//button[text()='Войти']"
    main_word = "//h1[@class='co-checkout-title co-title co-title--h1']"

    # Getters

    def get_button_personal_account(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_personal_account)))

    def get_email(self):
        return WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.XPATH, self.email)))

    def get_password(self):
        return WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.XPATH, self.password)))

    def get_login_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.login_button)))

    def get_main_word(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.main_word)))

    # Actions

    def enter_personal_account(self):
        self.get_button_personal_account().click()
        print("Нажата кнопка входа в Личный кабинет")

    def input_email(self, email):
        self.get_email().send_keys(email)
        print("Введен email пользователя")

    def input_password(self, password):
        self.get_password().send_keys(password)
        print("Введен пароль")

    def click_login_button(self):
        self.get_login_button().click()
        print("Нажата кнопка Войти")

    # Methods
    def authorization(self):
        """ Авторизация в системе"""
        with allure.step("Authorization"):
            Logger.add_start_step(method="Authorization")
            self.enter_personal_account()
            self.input_email("1sd908rjc613@mail.ru")
            self.input_password("12345678")
            self.click_login_button()
            self.assert_word(self.get_main_word(), "История заказов")
            Logger.add_end_step(url=self.driver.current_url, method="Authorization")
