import pytest
from selenium import webdriver
import math
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

answer = []

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    first = webdriver.ChromeOptions()
    first.add_argument("--remote-debugging-port=9222")
    browser = webdriver.Chrome(options=first)
    yield browser
    browser.quit()


@pytest.mark.parametrize("links", ["lesson/236895/step/1", "lesson/236896/step/1",
                                       "lesson/236897/step/1", "lesson/236898/step/1",
                                       "lesson/236899/step/1", "lesson/236903/step/1",
                                       "lesson/236904/step/1", "lesson/236905/step/1"])
def test_pages(browser, links):
    link = f"https://stepik.org/{links}"
    browser.get(link)
    browser.implicitly_wait(10)
    browser.find_element_by_tag_name("textarea").send_keys(str(math.log(int(time.time()))))
    browser.find_element_by_class_name("submit-submission").click()
        
    WebDriverWait(browser, 3).until(
        EC.presence_of_element_located((By.CLASS_NAME, "smart-hints__hint"))
    )
    text_el = browser.find_element_by_class_name("smart-hints__hint")
    if text_el.text != "Correct!":
        answer.append(text_el.text)
    assert text_el.text == "Correct!", "It is not equal"
