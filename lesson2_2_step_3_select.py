import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

link = "http://suninjuly.github.io/selects1.html"

try:
  browser = webdriver.Chrome()
  browser.get(link)
  num1_element = browser.find_element(By.CSS_SELECTOR, "#num1")
  num1 = int(num1_element.text)
  num2_element = browser.find_element(By.CSS_SELECTOR, "#num2")
  num2 = int(num2_element.text)
  sum = str(num1 + num2)
  # print(sum)
  select = Select(browser.find_element(By.TAG_NAME, "select"))
  select.select_by_value(sum)
  button = browser.find_element(By.CSS_SELECTOR, ".btn.btn-default")
  button.click()

finally:
  # успеваем скопировать код за 30 секунд
  time.sleep(5)
  # закрываем браузер после всех манипуляций
  browser.quit()
