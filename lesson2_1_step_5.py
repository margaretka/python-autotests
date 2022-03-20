import math
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/math.html"

try:
  browser = webdriver.Chrome()
  browser.get(link)
  x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
  x = x_element.text
  y = calc(x)
  input = browser.find_element(By.CSS_SELECTOR, "#answer")
  input.send_keys(y)
  option = browser.find_element(By.CSS_SELECTOR, "[for='robotCheckbox']")
  option.click()
  radio = browser.find_element(By.CSS_SELECTOR, "[for='robotsRule']")
  radio.click()
  submit = browser.find_element(By.CSS_SELECTOR, ".btn.btn-default")
  submit.click()

finally:
  # успеваем скопировать код за 30 секунд
  time.sleep(5)
  # закрываем браузер после всех манипуляций
  browser.quit()
