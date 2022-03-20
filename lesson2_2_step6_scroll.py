import math
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

link = "http://suninjuly.github.io/execute_script.html"

def calc(x):
  return str(math.log(abs(12 * math.sin(x))))

try:
  browser = webdriver.Chrome()
  browser.get(link)
  x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
  x = int(x_element.text)
  y = calc(x)
  # browser.execute_script("window.scrollBy(0, 3000);")
  button = browser.find_element(By.CSS_SELECTOR, ".btn.btn-primary")
  browser.execute_script("return arguments[0].scrollIntoView(true);", button)
  button.click()
  input = browser.find_element(By.CSS_SELECTOR, "#answer")
  input.send_keys(y)
  checkbox = browser.find_element(By.CSS_SELECTOR, "[for='robotCheckbox']")
  checkbox.click()
  radio = browser.find_element(By.CSS_SELECTOR, "[for='robotsRule']")
  radio.click()
  # button = browser.find_element(By.CSS_SELECTOR, ".btn.btn-primary")
  button.click()

finally:
  # успеваем скопировать код за 30 секунд
  time.sleep(5)
  # закрываем браузер после всех манипуляций
  browser.quit()
