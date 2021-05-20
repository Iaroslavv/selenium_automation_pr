import time
from selenium import webdriver
from math import log, sin
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


link = "http://suninjuly.github.io/explicit_wait2.html"

def calc(x):
    return str(log(abs(12*sin(int(x)))))


try:
    first = webdriver.ChromeOptions()
    first.add_argument("--remote-debugging-port=9222")
    browser = webdriver.Chrome(options=first) 
    browser.get(link)

    WebDriverWait(browser, 13).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )
    browser.find_element_by_id("book").click()
    
    number = browser.find_element_by_id("input_value")
    number_to_txt = number.text
    answer = calc(number_to_txt)
    
    browser.find_element_by_id("answer").send_keys(answer)
    browser.find_element_by_id("solve").click()
    
    time.sleep(4)
    

# выводим сообщение об ошибке в читаемом виде
except Exception as e:
    print(f"The traceback is: {e}")

finally:
    time.sleep(20)
    #закрываем браузер
    browser.close()
    #закрываем сессию
    browser.quit()
