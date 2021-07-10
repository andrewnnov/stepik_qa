from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select
import math
import os


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))



try:
    link = "http://suninjuly.github.io/file_input.html"

    browser = webdriver.Chrome("C:\Projects\stepik_qa\driver\chromedriver.exe")
    browser.get(link)

    first_name = browser.find_element_by_xpath("//input[@name='firstname']")
    first_name.send_keys("Ivan")

    last_name = browser.find_element_by_xpath("//input[@name='lastname']")
    last_name.send_keys("Ivanov")

    email = browser.find_element_by_xpath("//input[@name='email']")
    email.send_keys("Ivanov@test.com")

    element_file = browser.find_element_by_id("file")

    # получаем путь к директории текущего исполняемого файла
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'example.txt')
    element_file.send_keys(file_path)

    browser.find_element_by_xpath("//button[text()= 'Submit']").click()







finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()


