from selenium import webdriver
from selenium.webdriver.common.by import By
web_browser = webdriver.Chrome()
web_browser.maximize_window()
web_browser.get('http://demo.seleniumeasy.com/basic-first-form-demo.html')
# web_browser.implicitly_wait(5)
popup = web_browser.find_element(By.CLASS_NAME, 'btn-primary')
popup2 = web_browser.find_element(By.CSS_SELECTOR, '#get-input > .btn')
print(popup2)
# print(popup.get_attribute('Show Message'))
print(popup)

assert 'Show Message' in web_browser.page_source

user_message = web_browser.find_element(By.ID, 'user-message')
user_message.clear()
user_message.send_keys('i am super cool')

popup.click()
input("press enter to exit")
