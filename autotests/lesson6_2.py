from selenium import webdriver
import time

try:
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    first = browser.find_element_by_xpath("//input[@placeholder='Input your first name']")
    first.send_keys("A")
    last = browser.find_element_by_xpath("//input[@placeholder='Input your last name']")
    last.send_keys("Z")
    email = browser.find_element_by_xpath("//input[@placeholder='Input your email']")
    email.send_keys("my_email@ya.ru")
    phone = browser.find_element_by_xpath("//input[@placeholder='Input your phone:']")
    phone.send_keys("79229999887")
    address = browser.find_element_by_xpath("//input[@placeholder='Input your address:']")
    address.send_keys("47б")
    button = browser.find_element_by_xpath("//button[@class='btn btn-default']")
    button.click()


   # Отправляем заполненную форму
    # button = browser.find_element_by_css_selector("button.btn")
    # button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
