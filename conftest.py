import pytest
from selene import browser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="session")
def set_browser_window_size():
    browser.config.driver_name = "firefox"
    browser.config.window_height = 1024
    browser.config.window_width = 768
