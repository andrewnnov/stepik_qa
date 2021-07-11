from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/explicit_wait2.html"

    browser = webdriver.Chrome("C:\Projects\stepik_qa\driver\chromedriver.exe")
    browser.get(link)

    button = browser.find_element_by_id("book")
    WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
        )
    button.click()

    number_from_page = int(browser.find_element_by_id("input_value").text)
    text_field = browser.find_element_by_id("answer").send_keys(calc(number_from_page))

    browser.find_element_by_id("solve").click()



finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()


