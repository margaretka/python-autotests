import math
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

link = "http://suninjuly.github.io/explicit_wait2.html"

try:
  browser = webdriver.Chrome()
  browser.get(link)
  # price_element = browser.find_element(By.CSS_SELECTOR, "#price")
  # price_text = price_element.text
  price = WebDriverWait(browser, 15).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "#price"), "$100"))
  button = browser.find_element(By.CSS_SELECTOR, "#book")
  button.click()
  x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
  x = float(x_element.text)
  input = browser.find_element(By.CSS_SELECTOR, "#answer")
  input.send_keys(str(math.log(abs(12 * math.sin(x)))))
  button = browser.find_element(By.CSS_SELECTOR, "#solve")
  button.click()

finally:
  # успеваем скопировать код за 30 секунд
  time.sleep(30)
  # закрываем браузер после всех манипуляций
  browser.quit()
