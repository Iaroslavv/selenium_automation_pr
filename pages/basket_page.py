from pages.base_page import BasePage
from pages.locators import BasketPageLocators

class BasketPage(BasePage):
    
    def should_not_be_products_in_empty_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), "There are basket items, but shouldn't be"

    def should_be_text_about_empty_basket(self):
        assert self.is_element_present(*BasketPageLocators.TEXT_EMPTY_BASKET), "There isn't any text, but should be"
