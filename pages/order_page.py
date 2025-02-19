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

    # Getters
    def get_button_place_order(self):
        return WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.XPATH, self.button_place_order)))

    # def get_filter_color_white(self):
    #     return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.filter_color_white)))
    #
    # def get_first_smartphone(self):
    #     return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.first_smartphone)))
    #
    # def get_button_add_to_cart(self):
    #     return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_add_to_cart)))
    #
    # def get_button_open_cart(self):
    #     return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_open_cart)))
    #
    # def get_cart_product_name(self):
    #     return WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, self.cart_product_name)))

    # Actions
    def place_order(self):
        self.get_button_place_order().click()
        print("Нажата кнопка Оформить заказ")

    # def apply_filters(self):
    #     self.get_filter_brand_apple().click()
    #     print("Выбран бренд Apple")
    #
    #     self.get_filter_color_white().click()
    #     print("Выбран цвет белый")
    #
    #     print("Фильтры применены")
    #
    # def select_smartphone(self):
    #     smartphone_name = self.get_first_smartphone().text
    #     self.get_first_smartphone().click()
    #     print(f"Выбран смартфон: {smartphone_name}")
    #     return smartphone_name
    #
    # def add_to_cart(self):
    #     self.get_button_add_to_cart().click()
    #     print("Товар добавлен в корзину")
    #
    # def open_cart(self):
    #     self.get_button_open_cart().click()
    #     print("Открыть корзину")

    # Method
    def place_your_order(self):
        self.place_order()

        # self.scroll_to_filters()
        # self.apply_filters()
        # time.sleep(3)
        # selected_smartphone_name = self.select_smartphone()
        # self.add_to_cart()
        # self.open_cart()
        # self.assert_url("https://upstore24.ru/cart_items")
        # print("Переход в корзину")
        # self.assert_word(self.get_cart_product_name(), selected_smartphone_name)
        # print("Товар успешно добавлен в корзину")
