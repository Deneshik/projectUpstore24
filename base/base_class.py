import datetime
import os

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class Base():

    def __init__(self, driver):
        self.driver = driver

    """Method get current url"""
    def get_current_url(self):
        """Метод проверки url"""
        get_url = self.driver.current_url
        print(f"Текущий URL: {get_url}")
        return get_url

    """Method assert word"""
    def assert_word(self, element, expected_text):
        """Проверяет, что текст элемента соответствует ожидаемому значению"""
        try:
            value_word = WebDriverWait(self.driver, 10).until(EC.visibility_of(element)).text
            assert value_word == expected_text, f"Ожидалось: {expected_text}, но получили: {value_word}"
            print("Значение текста верно")
        except TimeoutException:
            raise AssertionError("Ошибка: элемент не найден или не содержит текст")

    """Method Screenshot"""
    # def get_screenshot(self):
    #     """Создание скриншота"""
    #     now_date = datetime.datetime.now().strftime("%Y.%m.%d.%H.%M")
    #     name_screenshot = f"screenshot_{now_date}.png"
    #     self.driver.save_screenshot(f"screen/{name_screenshot}")
    #     print(f"Скриншот сохранен: {name_screenshot}")

    def get_screenshot(self):
        """Создание скриншота"""
        now_date = datetime.datetime.now().strftime("%Y.%m.%d.%H.%M")
        screenshot_folder = "screen"  # Папка для скриншотов
        os.makedirs(screenshot_folder, exist_ok=True)  # Создаём папку, если её нет

        name_screenshot = f"{screenshot_folder}/screenshot_{now_date}.png"
        self.driver.save_screenshot(name_screenshot)
        print(f"Скриншот сохранен: {os.path.abspath(name_screenshot)}")

    """Method assert url"""
    def assert_url(self, expected_url):
        """Проверяет соответствие текущего URL ожидаемому"""
        get_url = self.get_current_url()
        assert get_url == expected_url, f"Ожидалось: {expected_url}, но получили: {get_url}"
        print("Значение URL верно")
