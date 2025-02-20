from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.order_page import OrderPage
from pages.smartphones_page import SmartphonesPage


def test_buy_product(driver):

    print("Старт теста - покупка смартфона")

    lp = LoginPage(driver)
    lp.authorization()

    mp = MainPage(driver)
    mp.select_catalogue()
    mp.select_smartphones()

    sp = SmartphonesPage(driver)
    sp.buy_smartphone()

    op = OrderPage(driver)
    op.place_your_order()

    print("Конец теста покупки смартфона")


