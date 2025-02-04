# 1. Перейти в раздел: смартфоны
#
# 2. С помощью фильтров выбрать товар (чем больше фильтров тем лучше)
#
# 3. Выбрать телефон.
#
# 4. Нажать "в корзину".
#
# 5. Нажать "оформить заказ".
#
# 6. Ввести данные.
#
# 7. Нажать "подтвердить заказ".
#
# 2. Добавить товар в корзину и пройти весь бизнес путь
#
# 3. Использовать в построении проекта и теста принципы ООП и Page Object Model и PyTest
#
# 4. Максимально усложнить бизнес логику теста, для закрепления знаний, использовать проверочные методы
#
# 5. Написать подробную аннотацию к проекту

import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# from pages.cart_page import CartPage
# from pages.client_information_page import ClientInformationPage
# from pages.finish_page import FinishPage
# from pages.login_page import LoginPage
from pages.main_page import MainPage
# from pages.payment_page import PaymentPage


def test_buy_product(driver):

    print("Старт теста - покупка смартфона")

    mp = MainPage(driver)
    mp.select_catalogue()

    print("Конец теста покупки смартфона")


