from selenium import webdriver
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/redirect_accept.html"

    browser = webdriver.Chrome("C:\Projects\stepik_qa\driver\chromedriver.exe")
    browser.get(link)

    button_i_want = browser.find_element_by_xpath("//button[@class='trollface btn btn-primary']")
    button_i_want.click()

    list_of_windows = browser.window_handles
    new_window = list_of_windows[1]
    browser.switch_to.window(new_window)


    number_from_page = int(browser.find_element_by_id("input_value").text)
    text_field = browser.find_element_by_id("answer").send_keys(calc(number_from_page))

    browser.find_element_by_xpath("//button[@class ='btn btn-primary']").click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()


