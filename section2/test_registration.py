import unittest
from selenium import webdriver

class TestRegistration(unittest.TestCase):
    first = webdriver.ChromeOptions()
    first.add_argument("--remote-debugging-port=9222")
    browser = webdriver.Chrome(options=first)

    def test_form1(self):
        link = "http://suninjuly.github.io/registration1.html"
        self.browser.get(link)
        self.browser.find_element_by_xpath("//div[@class='first_block']/div/input[@class='form-control first']").send_keys("iv")
        self.browser.find_element_by_xpath("//div[@class='first_block']/div/input[@class='form-control second']").send_keys("bul")
        self.browser.find_element_by_xpath("//div[@class='first_block']/div/input[@class='form-control third']").send_keys("vol")
        self.browser.find_element_by_css_selector("button.btn").click()
        welcome_text_elt = self.browser.find_element_by_tag_name("h1")
        welcome_text = welcome_text_elt.text

        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)
    
    def test_form2(self):
        link = "http://suninjuly.github.io/registration2.html"
        self.browser.get(link)
        self.browser.find_element_by_xpath("//div[@class='first_block']/div/input[@class='form-control first']").send_keys("iv")
        self.browser.find_element_by_xpath("//div[@class='first_block']/div/input[@class='form-control second']").send_keys("bul")
        self.browser.find_element_by_xpath("//div[@class='first_block']/div/input[@class='form-control third']").send_keys("vol")
        self.browser.find_element_by_css_selector("button.btn").click()
        welcome_text_elt = self.browser.find_element_by_tag_name("h1")
        welcome_text = welcome_text_elt.text

        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)

if __name__ == "__main__":
    unittest.main()
