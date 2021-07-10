from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))



try:
    link = "http://suninjuly.github.io/execute_script.html"

    browser = webdriver.Chrome("C:\Projects\stepik_qa\driver\chromedriver.exe")
    browser.get(link)

    value_x = browser.find_element_by_id("input_value").text
    answer = calc(value_x)
    text_area = browser.find_element_by_id("answer")
    text_area.send_keys(answer)

    button = browser.find_element_by_xpath("//button[text()='Submit']")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)

    browser.find_element_by_id("robotCheckbox").click()
    browser.find_element_by_id("robotsRule").click()
    button.click()



finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()


