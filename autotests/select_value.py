from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

try:
    link = "http://suninjuly.github.io/selects1.html"
    link2 = "http://suninjuly.github.io/selects2.html"

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--start-maximized")
    browser = webdriver.Chrome(options=chrome_options)
    browser.get(link2)

    num1 = browser.find_element_by_xpath("//span[@id='num1']")
    x_str = num1.text
    x = int(x_str)
    num2 = browser.find_element_by_xpath("//span[@id='num2']")
    y_str = num2.text
    y = int(y_str)
    sum = x + y
    sum_str = str(sum)

    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(sum_str)

    button = browser.find_element_by_tag_name("button")
    button.click()

finally:
    time.sleep(5)
    browser.quit()

