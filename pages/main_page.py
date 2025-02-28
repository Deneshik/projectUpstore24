import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base
from utilities.logger import Logger


class MainPage(Base):

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

        Logger.add_start_step(method="Select catalogue")
        self.click_button_catalogue()
        self.assert_url('https://upstore24.ru/collection/all')
        Logger.add_end_step(url=self.driver.current_url, method="Select catalogue")

    def select_smartphones(self):
        """Переход в раздел Смартфоны"""
        with allure.step("Select smartphones"):
            Logger.add_start_step(method="Select smartphones")
            self.click_smartphones_collection()
            self.assert_url('https://upstore24.ru/collection/phones')
            Logger.add_end_step(url=self.driver.current_url, method="Select smartphones")

