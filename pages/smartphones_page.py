import time

import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base
from utilities.logger import Logger


class SmartphonesPage(Base):

    # Locators

    filter_brand_apple = "(//label[contains(text(), 'Apple')])[1]"
    filter_color_white = "//label[@for='filter-value-109849136']"
    first_smartphone = "(//div[@class='product_card-title'])[1]"
    button_add_to_cart = "//button[@class='button button--primary button--block button--medium']"
    button_open_cart = "//a[@class='button button--primary button--block button--large']"
    cart_product_name = "//div[@class='cart-item-title']"

    # Getters
    def get_filter_brand_apple(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.filter_brand_apple)))

    def get_filter_color_white(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.filter_color_white)))

    def get_first_smartphone(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.first_smartphone)))

    def get_button_add_to_cart(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_add_to_cart)))

    def get_button_open_cart(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_open_cart)))

    def get_cart_product_name(self):
        return WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, self.cart_product_name)))

    # Actions
    def scroll_to_filters(self):
        self.driver.execute_script("window.scrollTo(0, 300);")
        print("Прокрутка к фильтрам выполнена")

    def apply_filters(self):
        self.get_filter_brand_apple().click()
        print("Выбран бренд Apple")

        self.get_filter_color_white().click()
        print("Выбран цвет белый")

        print("Фильтры применены")

    def select_smartphone(self):
        smartphone_name = self.get_first_smartphone().text
        self.get_first_smartphone().click()
        print(f"Выбран смартфон: {smartphone_name}")
        return smartphone_name

    def add_to_cart(self):
        self.get_button_add_to_cart().click()
        print("Товар добавлен в корзину")

    def open_cart(self):
        self.get_button_open_cart().click()
        print("Открыть корзину")

    # Method
    def buy_smartphone(self):
        """Покупка смартфона: применение фильтров, выбор смартфона, добавление выбранного смартфона в корзину,
        открытие корзины, проверка, что товар добавлен в корзину"""

        with allure.step("Buy smartphone"):
            Logger.add_start_step(method="Buy smartphone")
            self.scroll_to_filters()
            self.apply_filters()
            time.sleep(3)
            selected_smartphone_name = self.select_smartphone()
            self.add_to_cart()
            self.open_cart()
            self.assert_url("https://upstore24.ru/cart_items")
            print("Переход в корзину")
            self.assert_word(self.get_cart_product_name(), selected_smartphone_name)
            print("Товар успешно добавлен в корзину")
            Logger.add_end_step(url=self.driver.current_url, method="Buy smartphone")
