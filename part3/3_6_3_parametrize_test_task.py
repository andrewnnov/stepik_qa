import pytest
from selenium import webdriver
import time
import math
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    browser = webdriver.Chrome("C:\\Projects\\stepik_qa\\driver\\chromedriver.exe", options=options)
    yield browser
    print("\nquit browser..")
    browser.quit()


list_of_number = [236895, 236896, 236897, 236898, 236899, 236903, 236904, 236905]


@pytest.mark.parametrize('number', list_of_number)
def test_guest_should_see_login_link(browser, number):
    link = f"https://stepik.org/lesson/{number}/step/1"
    browser.get(link)

    # TODO need to change waiter
    time.sleep(5)

    text_field = browser.find_element_by_xpath("//div/textarea")
    answer = math.log(int(time.time()))
    text_field.send_keys(str(answer))


    WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "submit-submission")))
    browser.find_element_by_xpath("//button[@class='submit-submission']").click()

    # TODO need to change waiter
    time.sleep(5)

    text_from_second_page = browser.find_element_by_xpath("//pre[@class ='smart-hints__hint']").text
    assert text_from_second_page == "Correct!", "it's wrong text for answer: " + text_from_second_page


