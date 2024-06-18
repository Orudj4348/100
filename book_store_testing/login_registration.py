# ### Registration_login: регистрация аккаунта ###
# import time
# from selenium import webdriver
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.maximize_window()
# driver.implicitly_wait(5)
# driver.get("https://practice.automationtesting.in/")
#
# My_Account = driver.find_element_by_id('menu-item-50').click()
# Email = driver.find_element_by_id('reg_email').send_keys('bagirov.orudj@gmail.com')
# Password = driver.find_element_by_id('reg_password').send_keys('Oleg2000.')
# Register = driver.find_element_by_css_selector('[name="register"]').click()
#
# driver.quit()


### Registration_login: логин в систему ###
# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.maximize_window()
# driver.implicitly_wait(5)
# driver.get("https://practice.automationtesting.in/")
#
# My_Account = driver.find_element_by_id('menu-item-50').click()
# email = driver.find_element_by_id('username').send_keys('bagirov.orudj@gmail.com')
# Password = driver.find_element_by_id('password').send_keys('Oleg2000.')
# Login = driver.find_element_by_css_selector('[name="login"]').click()
# Logout = WebDriverWait(driver, 5).until(
#     EC.text_to_be_present_in_element((By.CSS_SELECTOR, 'li [href="https://practice.automationtesting.in/my-account/customer-logout/"]'), "Logout"))
#
# driver.quit()
