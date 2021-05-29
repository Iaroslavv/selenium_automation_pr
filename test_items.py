import time
from selenium. common. exceptions import NoSuchElementException

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_correct_language(browser):
    browser.get(link)
    time.sleep(20)
    button = browser.find_element_by_css_selector("button.btn-add-to-basket")
    assert button, "No element found"
    
    
    