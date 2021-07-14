from selenium import webdriver
import pytest

link = "http://selenium1py.pythonanywhere.com/"


@pytest.fixture(scope="function")
def browser():
    print("start browser for test...")
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    browser = webdriver.Chrome("C:\\Projects\\stepik_qa\\driver\\chromedriver.exe", options=options)
    yield browser
    print("\nquit browser")
    browser.quit()


class TestMainPage():


    @pytest.mark.smoke
    def test_guess_should_see_login_link(self, browser):
        browser.get(link)
        browser.find_element_by_css_selector("#login_link")

    @pytest.mark.win10
    @pytest.mark.smoke
    def test_guest_should_see_basket_link_on_the_main_page(self, browser):
        browser.get(link)
        browser.find_element_by_css_selector(".basket-mini .btn-group > a")


    @pytest.mark.skip
    @pytest.mark.smoke
    def test_guest_should_see_basket_link_on_the_main_page2(self, browser):
        browser.get(link)
        browser.find_element_by_css_selector(".basket-mini .btn-group > a")

    @pytest.mark.xfail(reason="fixing this bug right now") # use -rx to see this message
    @pytest.mark.smoke
    def test_guest_should_see_search_button_on_the_main_page(self, browser):
        browser.get(link)
        browser.find_element_by_css_selector("button.favorite")
