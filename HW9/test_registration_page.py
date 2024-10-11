from HW3.application import app
from HW3.data.users import User, UserData

def test_registration_page():
    app.left_panel.open_simple_registration_form()
    app.registration_page.fill_fully_name(User.user_semen["0"])
    app.registration_page.fill_user_email(User.user_semen["1"])
    app.registration_page.fill_current_address(User.user_semen["2"])
    app.registration_page.fill_permanent_address(User.user_semen["3"])
    app.registration_page.click_submit()
    app.registration_page.scroll_to_element()
    app.registration_page.should_have_registered(User.user_semen, UserData)
