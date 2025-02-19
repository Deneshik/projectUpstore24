from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class MainPage(Base):
    url = 'https://upstore24.ru/'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(self.url)  # Открываем страницу при создании объекта

    # Locators

    button_catalogue = "//a[@class='hamburger-trigger js-nav-collections-trigger']"
    smartphones_collection = "//div[@class='subcollection_card-title']//a[text()='Смартфоны']"

    # Getters

    def get_button_catalogue(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_catalogue)))

    def get_smartphones_collection(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.smartphones_collection)))

    # Actions

    def click_button_catalogue(self):
        self.get_button_catalogue().click()
        print("Нажать кнопку Каталог")

    def click_smartphones_collection(self):
        self.get_smartphones_collection().click()
        print("Нажать на кнопку Смартфоны в Каталоге")

    # Methods

    def select_catalogue(self):
        """Переход в раздел Каталог"""
        # self.get_current_url()
        self.click_button_catalogue()
        self.assert_url('https://upstore24.ru/collection/all')

    def select_smartphones(self):
        """Переход в раздел Смартфоны"""
        # self.get_current_url()
        self.click_smartphones_collection()
        self.assert_url('https://upstore24.ru/collection/phones')

