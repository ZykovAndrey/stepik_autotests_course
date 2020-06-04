from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math

link = "http://suninjuly.github.io/explicit_wait2.html"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")
browser = webdriver.Chrome(options=chrome_options)


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


browser.get(link)

price = WebDriverWait(browser, 13).until(
    EC.text_to_be_present_in_element((By.XPATH, "//*[@id='price']"), "$100")
)

button = WebDriverWait(browser, 5).until(
    EC.element_to_be_clickable((By.XPATH, "//*[@id='book']"))
)

button.click()

x_element = browser.find_element_by_id("input_value")
x = x_element.text
y = calc(x)
input_f = browser.find_element_by_xpath("//input[@id='answer']")
insert_answer = input_f.send_keys(y)
submit = browser.find_element_by_xpath("//*[@id='solve']")
submit.click()



