from selenium import webdriver
import pytest


@pytest.fixture(scope="session")
def browser():
    print("\nstart browser for test..")
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=chrome_options)
    yield driver
    print("\nquit browser..")
    driver.quit()
