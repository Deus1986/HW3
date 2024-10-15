import pytest
from selene import browser
from selenium import webdriver


@pytest.fixture()
def set_browser_window_size():
    browser.config.window_height = 1600
    browser.config.window_width = 900


@pytest.fixture(autouse=True)
def browser_management():
    browser.config.base_url = "https://github.com/Deus1986/HW3"
    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches", ['enable-automation'])
    options.page_load_strategy = "eager"
    # options.add_argument('--headless')
    browser.config.driver_options = options
    browser.config.driver.maximize_window()

    yield
    browser.quit()
