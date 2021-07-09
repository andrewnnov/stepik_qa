from selenium import webdriver
import time
import math


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/math.html"

    browser = webdriver.Chrome("C:\Projects\stepik_qa\driver\chromedriver.exe")
    browser.get(link)

    people_radio_btn = browser.find_element_by_id("peopleRule")
    people_atr = people_radio_btn.get_attribute("checked")
    print("value of people radio: ", people_atr)
    assert people_atr is not None, "People radio is not selected by default"

    people_radio_btn = browser.find_element_by_id("robotsRule")
    people_atr = people_radio_btn.get_attribute("checked")
    print("value of people radio: ", people_atr)
    assert people_atr is None


    submit_button = browser.find_element_by_css_selector("button.btn")
    submit_button_atr = submit_button.get_attribute("disable")
    print(submit_button_atr)


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()


