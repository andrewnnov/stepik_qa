from selenium import webdriver
import time
import unittest




class TestAbs(unittest.TestCase):

    def test_successful_registration(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome("C:\\Projects\\stepik_qa\\driver\\chromedriver.exe")
        browser.get(link)

        input_first_name = browser.find_element_by_tag_name('[placeholder="Input your first name"]')
        input_first_name.send_keys("Ivan")
        input_last_name = browser.find_element_by_tag_name('[placeholder="Input your last name"]')
        input_last_name.send_keys("Petrov")
        input_email = browser.find_element_by_tag_name('[placeholder="Input your email"]')
        input_email.send_keys("test@testmail.com")

        button = browser.find_element_by_css_selector("button.btn")
        button.click()
        time.sleep(1)
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        welcome_text = welcome_text_elt.text

        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "Texts Should be equal")


    def test_unsuccessful_registration(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome("C:\\Projects\\stepik_qa\\driver\\chromedriver.exe")
        browser.get(link)

        input_first_name = browser.find_element_by_tag_name('[placeholder="Input your name"]')
        input_first_name.send_keys("Ivan")
        input_last_name = browser.find_element_by_tag_name('[placeholder="Input your last name"]')
        input_last_name.send_keys("Petrov")
        input_email = browser.find_element_by_tag_name('[placeholder="Input your email"]')
        input_email.send_keys("test@testmail.com")

        button = browser.find_element_by_css_selector("button.btn")
        button.click()
        time.sleep(1)

        welcome_text_elt = browser.find_element_by_tag_name("h1")
        welcome_text = welcome_text_elt.text
        print(welcome_text)

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "Texts Should be equal")

    if __name__ == "__main__":
        unittest.main()




