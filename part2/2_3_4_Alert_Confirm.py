from selenium import webdriver
import time
import math
import os


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))



try:
    link = "http://suninjuly.github.io/alert_accept.html"

    browser = webdriver.Chrome("C:\Projects\stepik_qa\driver\chromedriver.exe")
    browser.get(link)

    button_i_want = browser.find_element_by_xpath("//button[@class ='btn btn-primary']")
    button_i_want.click()

    confirm = browser.switch_to.alert
    confirm.accept()

    number_from_page = int(browser.find_element_by_id("input_value").text)
    text_field = browser.find_element_by_id("answer").send_keys(calc(number_from_page))

    browser.find_element_by_xpath("//button[@class ='btn btn-primary']").click()

    # получаем путь к директории текущего исполняемого файла








finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()


