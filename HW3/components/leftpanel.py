from selene import browser, have, command


class LeftPanel:
    def __init__(self):
        self.container = browser.element(".left-pannel")

    def open_form(self, element_group, item):
        (browser.element(f'//h5[text()="{element_group}"]')
         .perform(command.js.scroll_into_view).click())
        self.container.all('//ul[@class="menu-list"]//span').element_by(have.exact_text(item)).click()

    def open_simple_registration_form(self):
        browser.open("/")
        self.open_form("Elements", "Text Box")
