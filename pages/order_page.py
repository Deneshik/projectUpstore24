import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class OrderPage(Base):

    def __init__(self, driver):
        super().__init__(driver)

    # Locators

    button_place_order = "//input[@value='Оформить заказ']"
    button_create_order = "//button[@id='create_order']"

    # Getters
    def get_button_place_order(self):
        return WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located((By.XPATH, self.button_place_order)))

    def get_button_create_order(self):
        return WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located((By.XPATH, self.button_create_order)))

    # Actions
    def place_order(self):
        self.get_button_place_order().click()
        print("Нажата кнопка Оформить заказ")

    def scroll_to_apply_order(self):
        self.driver.execute_script("window.scrollTo(0, 900);")
        print("Прокрутка к подтверждению заказа выполнена")

    def create_order(self):
        self.get_button_create_order().click()
        print("Нажата кнопка Подтвердить заказ")

    # Method
    def place_your_order(self):
        self.place_order()
        self.scroll_to_apply_order()
        self.create_order()
        time.sleep(3)
        self.get_screenshot()
