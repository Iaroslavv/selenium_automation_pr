from selenium.common.exceptions import NoSuchElementException

class BasePage:
    def __init__(self, browser: str, url: str, timeout=10):
        """Class constructor.
        :param browser:
        :param url:
        """
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)
    
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

        