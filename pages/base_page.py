from selenium.common.exceptions import NoSuchElementException, NoAlertPresentException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.locators import BasePageLocators, BasketPageLocators, LoginPageLocators
import math

class BasePage:
    def __init__(self, browser: str, url: str, timeout=5):
        """Class constructor.
        :param browser:
        :param url:
        """
        self.browser = browser
        self.url = url
        # self.browser.implicitly_wait(timeout)
    
    def go_to_login_page(self):
        link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        link.click()
    
    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"
    
    def go_to_basket(self):
        button = self.browser.find_element(*BasketPageLocators.BASKET_BUTTON)
        button.click()
    
    def register_new_user(self, email, password):
        self.browser.find_element(*LoginPageLocators.EMAIL).send_keys(email)
        self.browser.find_element(*LoginPageLocators.PASSWORD).send_keys(password)
        self.browser.find_element(*LoginPageLocators.CONFIRM_PASSWORD).send_keys(password)
        self.browser.find_element(*LoginPageLocators.SUBMIT_BUTTON).click()
        
    
    def open(self):
        """ Opens the page using the method (get)
        """
        self.browser.get(self.url)
    
    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True
    
    def is_not_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True
        return False

    def is_disappeared(self, how, what, timeout=10):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException).\
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True
        
    def solve_quiz_and_get_code(self):
        WebDriverWait(self.browser, 3).until(EC.alert_is_present())
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except (NoAlertPresentException, TimeoutException):
            print("No second alert presented")

        