import datetime

class Base():

    def __init__(self, driver):
        self.driver = driver

    """Method get current url"""
    def get_current_url(self):
        """Метод проверки url"""
        get_url = self.driver.current_url
        print("current url " + get_url)

    """Method assert word"""
    def assert_word(self, word, result):
        """Проверка значения текста"""
        value_word = word.text
        assert value_word == result, f"Ожидалось: {result}, но получили: {value_word}"
        print("Значение текста верно")

    """Method Screenshot"""
    def get_screenshot(self):
        """Создание скриншота"""
        now_date = datetime.datetime.now().strftime("%Y.%m.%d.%H.%M")  # установка текущей даты в имени скрина
        name_screenshot = "screenshot_" + now_date + ".png"  # определение названия файла и разрешения скрина
        self.driver.save_screenshot(f"screen/{name_screenshot}")  # создание скриншота
        print(f"Скриншот сохранен: {name_screenshot}")

    """Method assert url"""
    def assert_url(self, result):
        """Проверка корректности url"""
        get_url = self.driver.current_url
        assert get_url == result
        print("Значение url верно")
