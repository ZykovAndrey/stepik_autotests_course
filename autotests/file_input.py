from selenium import webdriver
import time
import os

try:
    link = "http://suninjuly.github.io/file_input.html"

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--start-maximized")
    browser = webdriver.Chrome(options=chrome_options)

    def go_to_link():
        return browser.get(link)

    def input_fields():
        input_elements = browser.find_elements_by_xpath("//input[@class='form-control']")
        for element in input_elements:
            element.send_keys("test")
        return input_elements

    def insert_file():
        file_button = browser.find_element_by_id('file')
        current_dir = os.path.abspath(os.path.dirname(__file__))
        file_path = os.path.join(current_dir, 'file.txt')
        return file_button.send_keys(file_path)

    def click_to_button():
        button = browser.find_element_by_tag_name("button")
        return button.click()

    step1 = go_to_link()
    step2 = input_fields()
    step3 = insert_file()
    step4 = click_to_button()


finally:
    time.sleep(10)
    browser.quit()

