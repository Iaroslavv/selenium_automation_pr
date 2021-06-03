from _pytest import mark
from _pytest.mark import param
from pages.product_page import ProductPage
import pytest
import time

@pytest.mark.skip
def test_should_be_add_to_basket_button(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_add_to_basket_button()

@pytest.mark.parametrize('links', ["?promo=offer0","?promo=offer1", "?promo=offer2", "?promo=offer3",
                                   "?promo=offer4", "?promo=offer5", "?promo=offer6",
                                   pytest.param("?promo=offer7", marks=pytest.mark.xfail(reason="Wrong books'name")),
                                   "?promo=offer8", "?promo=offer9",
                                  ])
def test_guest_can_add_product_to_basket(browser, links):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/{links}"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_add_to_basket_button()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_message_about_adding()
    page.should_be_equal_price()
