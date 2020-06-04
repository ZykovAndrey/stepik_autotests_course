from selenium import webdriver
import time
import math

try:
    link = "http://suninjuly.github.io/get_attribute.html"

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--start-maximized")
    browser = webdriver.Chrome(options=chrome_options)
    browser.get(link)

    def xfind():
        element_x = browser.find_element_by_xpath("//img[@id='treasure']")
        x = element_x.get_attribute("valuex")
        return (x)

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    x = xfind()
    y = calc(x)

    answer = browser.find_element_by_xpath("//input[@id = 'answer']")
    answer.send_keys(y)
    checkbox = browser.find_element_by_xpath("//input[@id = 'robotCheckbox']")
    checkbox.click()
    radiobutton = browser.find_element_by_xpath("//input[@id='robotsRule']")
    radiobutton.click()
    sendbutton = browser.find_element_by_xpath("//button[@class = 'btn btn-default']")
    sendbutton.click()

finally:
    time.sleep(10)
    browser.quit()

