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


