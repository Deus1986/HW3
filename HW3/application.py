from HW3.components.leftpanel import LeftPanel
from HW9.pages.registration_page import RegistrationPage
from HW9.pages.simple_registration_page import SimpleRegistrationPage


class Application:
    def __init__(self):
        self.registration_page = RegistrationPage()
        self.simple_registration_page = SimpleRegistrationPage()
        self.left_panel = LeftPanel()


app = Application()
