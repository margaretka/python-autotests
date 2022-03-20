import math
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/redirect_accept.html"

try:
  browser = webdriver.Chrome()
  browser.get(link)
  button = browser.find_element(By.CSS_SELECTOR, ".trollface.btn")
  button.click()
  new_window = browser.window_handles[1]
  browser.switch_to.window(new_window)
  x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
  x = float(x_element.text)
  input = browser.find_element(By.CSS_SELECTOR, "#answer")
  input.send_keys(str(math.log(abs(12*math.sin(x)))))
  button = browser.find_element(By.CSS_SELECTOR, ".btn.btn-primary")
  button.click()

finally:
  # успеваем скопировать код за 30 секунд
  time.sleep(30)
  # закрываем браузер после всех манипуляций
  browser.quit()
