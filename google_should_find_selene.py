from selene import browser, be, have

browser.config.driver_name = 'firefox'


def test_google_search():
    browser.open('https://google.com')
    search_value = "@#$$#%#@$@#@%"
    browser.element('[name="q"]').should(be.blank).type(search_value).press_enter()
    browser.element('[id="botstuff"]').should(have.text(f'По запросу {search_value} ничего не найдено.'))
