# ### Shop: отображение страницы товара ###
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
# Shop = driver.find_element_by_id('menu-item-40').click()
# HTML5_Forms = driver.find_element_by_css_selector('[title="Mastering HTML5 Forms"]').click()
#
# Name = WebDriverWait(driver, 5).until(
#     EC.text_to_be_present_in_element((By.CSS_SELECTOR, 'h1.product_title'), "HTML5 Forms"))
#
# driver.quit()


### Shop: количество товаров в категории ###
# import time
# from selenium import webdriver
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.maximize_window()
# driver.implicitly_wait(5)
# driver.get("https://practice.automationtesting.in/")
#
# My_Account = driver.find_element_by_id('menu-item-50').click()
# email = driver.find_element_by_id('username').send_keys('bagirov.orudj@gmail.com')
# Password = driver.find_element_by_id('password').send_keys('Oleg2000.')
# Login = driver.find_element_by_css_selector('[name="login"]').click()
# Shop = driver.find_element_by_id('menu-item-40').click()
# HTML = driver.find_element_by_css_selector('.cat-item-19 a').click()
# Books = driver.find_elements_by_class_name('woocommerce-LoopProduct-link')
# assert len(Books) == 3

# driver.quit()


### Shop: сортировка товаров ###
# import time
# from selenium import webdriver
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.maximize_window()
# driver.implicitly_wait(5)
# driver.get("https://practice.automationtesting.in/")
#
# My_Account = driver.find_element_by_id('menu-item-50').click()
# email = driver.find_element_by_id('username').send_keys('bagirov.orudj@gmail.com')
# Password = driver.find_element_by_id('password').send_keys('Oleg2000.')
# Login = driver.find_element_by_css_selector('[name="login"]').click()
# Shop = driver.find_element_by_id('menu-item-40').click()
#
# selector_default = driver.find_element_by_css_selector('[value="menu_order"]')
# selector_default_attribute = selector_default.get_attribute('selected')
# assert selector_default_attribute == 'true'
#
# from selenium.webdriver.support.select import Select
# selector = driver.find_element_by_class_name('orderby')
# select = Select(selector)
# select.select_by_value("price-desc")
#
# selector_desc = driver.find_element_by_css_selector('[value="price-desc"]')
# selector_desc_attribute = selector_desc.get_attribute('selected')
# assert selector_desc_attribute == 'true'

# driver.quit()


### Shop: отображение, скидка товара ###
# import time
# from selenium import webdriver
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# wait = WebDriverWait(driver, 10)
# driver.maximize_window()
# driver.implicitly_wait(5)
# driver.get("https://practice.automationtesting.in/")
#
# My_Account = driver.find_element_by_id('menu-item-50').click()
# email = driver.find_element_by_id('username').send_keys('bagirov.orudj@gmail.com')
# Password = driver.find_element_by_id('password').send_keys('Oleg2000.')
# Login = driver.find_element_by_css_selector('[name="login"]').click()
# Shop = driver.find_element_by_id('menu-item-40').click()
#
# Android = driver.find_element_by_css_selector('.product_cat-android>a>img').click()
#
# Old_price = driver.find_element_by_css_selector('del .amount')
# Old_price_text = Old_price.text
# assert Old_price_text == '₹600.00'
#
# New_price = driver.find_element_by_css_selector('ins .amount')
# New_price_text = New_price.text
# assert New_price_text == '₹450.00'
#
# img = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "images"))).click()
# close = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "pp_close"))).click()
#
# driver.quit()


### Shop: проверка цены в корзине ###
# import time
# from selenium import webdriver
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# wait = WebDriverWait(driver, 10)
# driver.maximize_window()
# driver.implicitly_wait(5)
# driver.get("https://practice.automationtesting.in/")
#
# Shop = driver.find_element_by_id('menu-item-40').click()
# Add_to_basket = driver.find_element_by_css_selector('[data-product_id="182"]').click()
# time.sleep(5)
#
# Items = driver.find_element_by_class_name('cartcontents')
# Items_text = Items.text
# assert Items_text == '1 Item'
#
# Price = driver.find_element_by_css_selector('.wpmenucart-contents .amount')
# Price_text = Price.text
# assert Price_text == '₹180.00'
#
# Basket = driver.find_element_by_class_name('wpmenucart-contents').click()
# Subtotal_price = wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".cart-subtotal .amount"), "₹180.00"))
# Total_price = wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".order-total .amount"), "₹183.60"))
#
# driver.quit()



### Shop: работа в корзине ###
# import time
# from selenium import webdriver
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.maximize_window()
# driver.implicitly_wait(5)
# driver.get("https://practice.automationtesting.in/")
#
# Shop = driver.find_element_by_id('menu-item-40').click()
# driver.execute_script("window.scrollBy(0, 300);")
# Add_to_basket_first = driver.find_element_by_css_selector('[data-product_id="182"]').click()
# time.sleep(3)
# Add_to_basket_second = driver.find_element_by_css_selector('[data-product_id="180"]').click()
# time.sleep(3)
# Basket = driver.find_element_by_class_name('wpmenucart-contents').click()
# time.sleep(3)
#
# Remove = driver.find_element_by_css_selector('[data-product_id="182"]').click()
# Undo = driver.find_element_by_css_selector('.woocommerce-message a').click()
# Quantity = driver.find_element_by_css_selector('[name="cart[045117b0e0a11a242b9765e79cbf113f][qty]"]')
# Quantity.clear()
# Quantity.send_keys('3')
# Update_Basket = driver.find_element_by_css_selector('[name="update_cart"]').click()
# Quantity_value = Quantity.get_attribute('value')
# assert Quantity_value == '3'
# time.sleep(3)
# Apply_Coupon = driver.find_element_by_css_selector('[name="apply_coupon"]').click()
# Error = driver.find_element_by_css_selector('.woocommerce-error li').text
# assert Error == 'Please enter a coupon code.'
#
# driver.quit()


### Shop: покупка товара ###
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
wait = WebDriverWait(driver, 10)
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("https://practice.automationtesting.in/")

Shop = driver.find_element_by_id('menu-item-40').click()
driver.execute_script("window.scrollBy(0, 300);")
Add_to_basket_first = driver.find_element_by_css_selector('[data-product_id="182"]').click()
time.sleep(3)
Basket = driver.find_element_by_class_name('wpmenucart-contents').click()
ProceedToCheckout = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "checkout-button")))
ProceedToCheckout = driver.find_element_by_class_name('checkout-button').click()

First_Name = driver.find_element_by_id('billing_first_name').send_keys('Oleg')
Last_Name = driver.find_element_by_id('billing_last_name').send_keys('Olegov')
Email = driver.find_element_by_id('billing_email').send_keys('bagirov.orudj@gmail.com')
Phone = driver.find_element_by_id('billing_phone').send_keys('89009004444')
Country = driver.find_element_by_id('s2id_billing_country').click()
Country1 = driver.find_element_by_id('s2id_autogen1_search').send_keys('Russia')
time.sleep(3)
Country_Russia = driver.find_element_by_class_name('select2-match').click()

Address_1 = driver.find_element_by_id('billing_address_1').send_keys('Pushkina')
Address_2 = driver.find_element_by_id('billing_address_2').send_keys('38')
City = driver.find_element_by_id('billing_city').send_keys('Kukuevo')
State = driver.find_element_by_id('billing_state').send_keys('Russia')
Postcode = driver.find_element_by_id('billing_postcode').send_keys('8800')

driver.execute_script("window.scrollBy(0, 600);")
time.sleep(3)
Check_Payments = driver.find_element_by_id('payment_method_cheque').click()
Place_order = driver.find_element_by_id('place_order').click()
time.sleep(3)

Thank_you = wait.until(EC.text_to_be_present_in_element((By.CLASS_NAME, "woocommerce-thankyou-order-received"),
                                                        "Thank you. Your order has been received."))
Payment_Method = wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "tfoot tr:nth-child(3)>td"),
                                                        "Check Payments"))
driver.quit()