from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/explicit_wait2.html")

# говорим WebDriver искать каждый элемент в течение 5 секунд
# browser.implicitly_wait(5)

# говорим Selenium проверять в течение 15 секунд, пока цена не станет $100
wait = WebDriverWait(browser, 15)
wait.until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))

button = browser.find_element(By.ID, "book")
button.click()

x = int(browser.find_element(By.CSS_SELECTOR, "#input_value").text)

def calc(x):
    return str(math.log(abs(12 * math.sin(x))))

result = calc(x)

add_result = browser.find_element(By.CSS_SELECTOR, "#answer")
browser.execute_script("return arguments[0].scrollIntoView(true);", add_result)
add_result.send_keys(result)

button1 = browser.find_element(By.ID, "solve")
button1.click()

time.sleep(5)  # добавлено для наглядности результатов
browser.quit()
