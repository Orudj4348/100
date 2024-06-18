### Home: добавление комментария ###
import time
from selenium import webdriver
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("https://practice.automationtesting.in/")

driver.execute_script("window.scrollBy(0, 600);")
Selenium_Ruby = driver.find_element_by_css_selector('[href="https://practice.automationtesting.in/product/selenium-ruby/"] h3').click()
Reviews = driver.find_element_by_class_name('reviews_tab').click()
Stars = driver.find_element_by_class_name('star-5').click()
My_Review = driver.find_element_by_id('comment').send_keys('Nice book!')
Name = driver.find_element_by_id('author').send_keys('Oleg')
email = driver.find_element_by_id('email').send_keys('bagirov.orudj@gmail.com')
Submit = driver.find_element_by_id('submit').click()

driver.quit()