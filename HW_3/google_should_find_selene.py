import datetime
import time

from selene import browser, be, have


def test_negative_google_search(set_browser_window_size):
    browser.open('https://www.google.ru/')
    search_value = "@#$$#%#@$@#@%"
    browser.element('[name="q"]').should(be.blank).type(search_value).press_enter()
    browser.element('[id="botstuff"]').should(have.text(f'По запросу {search_value} ничего не найдено.'))


def test_google_search(set_browser_window_size):
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('User-oriented Web UI browser tests in Python'))
