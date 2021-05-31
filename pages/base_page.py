class BasePage:
    def __init__(self, browser: str, url: str):
        """Class constructor.
        :param browser:
        :param url:
        """
        self.browser = browser
        self.url = url
    
    def open(self):
        """ Opens the page using the method (get)
        """
        self.browser.get(self.url)

        