import allure

from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.order_page import OrderPage
from pages.smartphones_page import SmartphonesPage


@allure.description("Test buy product")
def test_buy_product(driver):
    print("Старт теста")

    lp = LoginPage(driver)
    lp.authorization()

    print("Авторизация")

    mp = MainPage(driver)
    mp.select_catalogue()
    mp.select_smartphones()

    print("Переход в каталог, выбор подраздела каталога - смартфоны")

    sp = SmartphonesPage(driver)
    sp.buy_smartphone()

    print("Применение фильтров, выбор смартфона, добавление выбранного смартфона в корзину, открытие корзины, "
          "проверка, что товар добавлен в корзину")

    op = OrderPage(driver)
    op.place_your_order()

    print("Подтверждение заказа, создание заказа")

    print("Конец теста покупки смартфона")
