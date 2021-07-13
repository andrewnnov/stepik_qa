from selenium import webdriver
import pytest

link = "http://selenium1py.pythonanywhere.com/"


@pytest.fixture
def browser():
    print("start browser for test...")
    browser = webdriver.Chrome("C:\\Projects\\stepik_qa\\driver\\chromedriver.exe")
    return browser


class TestMainPage1():
    # вызываем фикстуру в тесте, передав ее как параметр
    def test_guess_should_see_login_link(self, browser):
        browser.get(link)
        browser.find_element_by_css_selector("#login_link")

    def test_guest_should_see_basket_link_on_the_main_page(self, browser):
        browser.get(link)
        browser.find_element_by_css_selector(".basket-mini .btn-group > a")