from selenium import webdriver
import time
import math

try:
    link = "https://SunInJuly.github.io/execute_script.html"

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--start-maximized")
    browser = webdriver.Chrome(options=chrome_options)

    def go_to_link():
        return browser.get(link)

    def find_x():
        x_element = browser.find_element_by_xpath("//span[@id='input_value']")
        x = x_element.text
        return x

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    def insert_answer(y):
        input1 = browser.find_element_by_xpath("//input[@id='answer']")
        return input1.send_keys(y)

    def scroll():
        return browser.execute_script("window.scrollBy(0, 110);")

    def click_to_checkbox():
        checkbox = browser.find_element_by_xpath("//label[@for='robotCheckbox']")
        return checkbox.click()

    def select_radio():
        radio = browser.find_element_by_xpath("//label[@for='robotsRule']")
        return radio.click()

    def click_to_button():
        button = browser.find_element_by_tag_name("button")
        return button.click()

    step1 = go_to_link()
    step2 = find_x()
    step3 = calc(step2)
    step4 = insert_answer(step3)
    step5 = scroll()
    step6 = click_to_checkbox()
    step7 = select_radio()
    step8 = click_to_button()

finally:
    time.sleep(10)
    browser.quit()
