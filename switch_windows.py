import time
from selenium import webdriver
from math import log, sin


link = "http://suninjuly.github.io/redirect_accept.html"

def calc(x):
    return str(log(abs(12*sin(int(x)))))


try:
    first = webdriver.ChromeOptions()
    first.add_argument("--remote-debugging-port=9222")
    browser = webdriver.Chrome(options=first) 
    browser.get(link)
    
    # first_window = browser.window_handles[0]

    current = browser.window_handles[0]

    button = browser.find_element_by_css_selector("button.btn")
    time.sleep(3)
    button.click()
    
    new_window = browser.window_handles[1]
    
    browser.switch_to.window(new_window)

    number = browser.find_element_by_id("input_value")
    number_to_txt = number.text
    answer = calc(number_to_txt)
    
    browser.find_element_by_id("answer").send_keys(answer)
    browser.find_element_by_css_selector("button.btn").click()
    
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
