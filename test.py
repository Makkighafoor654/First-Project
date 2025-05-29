from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time


driver = webdriver.Chrome()
driver.get("D:/testing project/test.html")

time.sleep(1)

userName = driver.find_element(By.ID, "username").text
userEmail = driver.find_element(By.ID, "useremail").text
print("Username:", userName)
print("Email:", userEmail)


# tag = driver.find_element(By.NAME, "Product").tag_name
# print("Tag name of the element with name 'Product List':", tag)

h2_text = driver.find_element(By.TAG_NAME, "h2").text
print("Text in the first h2 tag:", h2_text)

tag = driver.find_element(By.LINK_TEXT, "Page 1").tag_name
print("Tag name of the link with text 'Page 1':", tag)

products = driver.find_elements(By.CSS_SELECTOR, "ul>li.product")
for product in products:
    product_text = product.text
    product_id = product.get_attribute("data-id")
    print(f"Product ID: {product_id}, Info: {product_text}")





driver.quit()



