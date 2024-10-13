from HW9.pages.registration_page import RegistrationPage


class SimpleRegistrationPage:
    def __init__(self):
        self.page = RegistrationPage()

    def open(self):
        self.page.open_page()

    def register(self, user):
        self.page.fill_fully_name(user["0"])
        self.page.fill_user_email(user["1"])
        self.page.fill_current_address(user["2"])
        self.page.fill_permanent_address(user["3"])
        self.page.scroll_to_element()
        self.page.click_submit()

    def should_have_registered(self, user_data, user_enum):
        self.page.should_have_registered(user_data, user_enum)
