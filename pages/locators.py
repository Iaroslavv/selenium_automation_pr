from selenium.webdriver.common.by import By

class MainPageLocators:
    pass

class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTRATION_FORM = (By.CSS_SELECTOR, "#register_form")
    EMAIL = (By.NAME, "registration-email")
    PASSWORD = (By.NAME, "registration-password1")
    CONFIRM_PASSWORD = (By.NAME, "registration-password2")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "button.btn-primary[value='Register']")

class ProductPageLocators:
    ADD_BUTTON = (By.CLASS_NAME, "btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, "div.product_main > h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    MESSAGE = (By.CSS_SELECTOR, "div.alertinner > strong")
    TOTAL_PRICE = (By.CSS_SELECTOR, "div.basket-mini")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-success")

class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class BasketPageLocators:
    BASKET_ITEMS = (By.CLASS_NAME, "basket-items")
    TEXT_EMPTY_BASKET = (By.ID, "content_inner")
    BASKET_BUTTON = (By.CSS_SELECTOR, "span.btn-group")
