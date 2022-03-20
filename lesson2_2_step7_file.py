import time
import os

from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/file_input.html"

try:
  browser = webdriver.Chrome()
  browser.get(link)
  first_name = browser.find_element(By.CSS_SELECTOR, "[name = 'firstname']")
  first_name.send_keys("Ivan")
  last_name = browser.find_element(By.CSS_SELECTOR, "[name = 'lastname']")
  last_name.send_keys("Ivan")
  email = browser.find_element(By.CSS_SELECTOR, "[name = 'email']")
  email.send_keys("Ivan")
  file = browser.find_element(By.CSS_SELECTOR, "#file")
  current_dir = os.path.abspath(os.path.dirname(__file__))
  file_path = os.path.join(current_dir, 'file.txt')
  file.send_keys(file_path)
  button = browser.find_element(By.CSS_SELECTOR, ".btn.btn-primary")
  button.click()

finally:
  # успеваем скопировать код за 30 секунд
  time.sleep(5)
  # закрываем браузер после всех манипуляций
  browser.quit()
