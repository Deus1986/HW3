from selene import browser

from HW3.application import app
from HW3.data.users import User, UserData


def test__simple_registration():
    app.left_panel.open_simple_registration_form()
    app.simple_registration_page.register(User.user_semen)
    app.simple_registration_page.should_have_registered(User.user_semen, UserData)
