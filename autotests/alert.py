from selenium import webdriver
import time
import math

try:
    link = "http://suninjuly.github.io/alert_accept.html"

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--start-maximized")
    browser = webdriver.Chrome(options=chrome_options)

    def go_to_link():
        return browser.get(link)

    def click_to_button():
        button = browser.find_element_by_tag_name('button')
        return button.click()

    def confirm_alert():
        confirm = browser.switch_to.alert
        return confirm.accept()

    def find_x():
        x_element = browser.find_element_by_xpath("//span[@id='input_value']")
        x = x_element.text
        return x

    def calc(x):
        y = str(math.log(abs(12 * math.sin(int(x)))))
        return y

    def insert_answer(y):
        answer = browser.find_element_by_xpath("//input[@id='answer']")
        return answer.send_keys(y)

    def click_to_submit():
        submit = browser.find_element_by_xpath("//button[@class='btn btn-primary']")
        return submit.click()

    step1 = go_to_link()
    step2 = click_to_button()
    step3 = confirm_alert()
    step4_1 = find_x()
    step4_2 = calc(step4_1)
    step4_3 = insert_answer(step4_2)
    step4_4 = click_to_submit()

finally:
    time.sleep(10)
    browser.quit()
