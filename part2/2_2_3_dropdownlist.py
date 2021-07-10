from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select


try:
    link = "http://suninjuly.github.io/selects1.html"

    browser = webdriver.Chrome("C:\Projects\stepik_qa\driver\chromedriver.exe")
    browser.get(link)

    number_one = browser.find_element_by_id("num1").text
    number_two = browser.find_element_by_id("num2").text
    sum = int(number_one) + int(number_two)
    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(f"{sum}")
    browser.find_element_by_css_selector("button.btn").click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()


