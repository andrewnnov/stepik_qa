import time

from selenium import webdriver

driver = webdriver.Chrome("C:\Projects\stepik_qa\driver\chromedriver.exe")
time.sleep(5)
driver.get("https://stepik.org/lesson/25969/step/12")
text_area = driver.find_element_by_css_selector(".textarea")
text_area.send_keys("get()")
time.sleep(5)
submit_button = driver.find_element_by_css_selector(".submit-submission")
submit_button.click()
time.sleep(5)
driver.quit()