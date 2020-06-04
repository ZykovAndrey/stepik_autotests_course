from selenium import webdriver
import time
import math

try:
    link = "http://suninjuly.github.io/math.html"

    browser = webdriver.Chrome()
    browser.get(link)

    def xfind():
        element_x = browser.find_element_by_xpath("//span[@id = 'input_value']")
        x = element_x.text
        return (x)

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    x = xfind()
    y = calc(x)
    answer = browser.find_element_by_xpath("//input[@id = 'answer']")
    answer.send_keys(y)
    checkbox = browser.find_element_by_xpath("//input[@id = 'robotCheckbox']")
    checkbox.click()
    radiobutton = browser.find_element_by_xpath("//label[@for = 'robotsRule']")
    radiobutton.click()
    sendbutton = browser.find_element_by_xpath("//button[@class = 'btn btn-default']")
    sendbutton.click()

finally:
    time.sleep(10)
    browser.quit()

