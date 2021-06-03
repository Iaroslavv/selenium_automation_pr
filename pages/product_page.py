import selenium
from pages.base_page import BasePage
from pages.locators import ProductPageLocators

class ProductPage(BasePage):

    def should_be_add_to_basket_button(self):
        assert self.is_element_present(*ProductPageLocators.ADD_BUTTON), "There's no add to basket button"
    
    def add_product_to_basket(self):
        button = self.browser.find_element(*ProductPageLocators.ADD_BUTTON)
        button.click()
    
    def should_be_message_about_adding(self):
        # check if the product name exists on the page
        assert self.is_element_present(*ProductPageLocators.PRODUCT_NAME), "There's no book name"
        # check if alert after adding a book appears
        assert self.is_element_present(*ProductPageLocators.MESSAGE), "There's no message in alert"
        # get the name
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        # get the message
        message = self.browser.find_element(*ProductPageLocators.MESSAGE).text
        # check the book's name is equal to the one in the alert message
        assert product_name == message, "The book name is not the same as in the message"
    
    def should_be_equal_price(self):
        # check if the product price exists on the page
        assert self.is_element_present(*ProductPageLocators.PRODUCT_PRICE), "There's no price for this"
        # check if the total price exists on the page
        assert self.is_element_present(*ProductPageLocators.TOTAL_PRICE), "There's no total price found"
        # get the price
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        # get the total price
        total_price = self.browser.find_element(*ProductPageLocators.TOTAL_PRICE).text
        assert product_price in total_price, "The price is not equal"
 
