import pytest

data1 = [
    (00, True),
    (2, True),
    (4, True),
    (6, False),
    (15, False),
    (22, True)
]

data2 = [
    (2, None, True),
    (4, None, True),
    (6, None, False),
    (15, None, False),
    (22, None, True),
    (2, False, False),
    (4, False, False),
    (6, False, False),
    (15, False, False),
    (22, False, False),
    (2, True, True),
    (4, True, True),
    (6, True, True),
    (15, True, True),
    (22, True, True)
]


@pytest.mark.parametrize("time_value, status", data1)
def test_dark_theme_by_time(time_value, status):
    """
    Протестируйте правильность переключения темной темы на сайте в зависимости от времени
    """
    current_time = time_value
    # TODO переключите темную тему в зависимости от времени суток (с 22 до 6 часов утра - ночь)

    if 6 <= current_time < 22:
        is_dark_theme = False
    else:
        is_dark_theme = True
    assert is_dark_theme == status


@pytest.mark.parametrize("time_value, enabled_by_user, dark_theme_status", data2)
def test_dark_theme_by_time_and_user_choice(time_value, enabled_by_user, dark_theme_status):
    """
    Протестируйте правильность переключения темной темы на сайте
    в зависимости от времени и выбора пользователя
    dark_theme_enabled_by_user = True - Темная тема включена
    dark_theme_enabled_by_user = False - Темная тема выключена
    dark_theme_enabled_by_user = None - Пользователь не сделал выбор (используется переключение по времени системы)
    """
    current_time = time_value
    dark_theme_enabled_by_user = enabled_by_user
    # TODO переключите темную тему в зависимости от времени суток,
    #  но учтите что темная тема может быть включена вручную

    if dark_theme_enabled_by_user is not None:
        is_dark_theme = dark_theme_enabled_by_user
    else:
        if 6 <= current_time < 22:
            is_dark_theme = False
        else:
            is_dark_theme = True
    assert is_dark_theme == dark_theme_status


def test_find_suitable_user():
    """
    Найдите нужного пользователя по условиям в списке пользователей
    """
    users = [
        {"name": "Oleg", "age": 32},
        {"name": "Sergey", "age": 24},
        {"name": "Stanislav", "age": 15},
        {"name": "Olga", "age": 45},
        {"name": "Maria", "age": 18},
    ]

    # TODO найдите пользователя с именем "Olga"
    suitable_users = None
    for user in users:
        if user["name"] == "Olga":
            suitable_users = user

    assert suitable_users == {"name": "Olga", "age": 45}

    # TODO найдите всех пользователей младше 20 лет
    suitable_users = []
    for user in users:
        if user["age"] < 20:
            suitable_users.append(user)

    assert suitable_users == [
        {"name": "Stanislav", "age": 15},
        {"name": "Maria", "age": 18},
    ]


# Сделайте функцию, которая будет печатать
# читаемое имя переданной ей функции и значений аргументов.
# Вызовите ее внутри функций, описанных ниже
# Подсказка: Имя функции можно получить с помощью func.__name__
# Например, вызов следующей функции должен преобразовать имя функции
# в более читаемый вариант (заменить символ подчеркивания на пробел,
# сделать буквы заглавными (или первую букву), затем вывести значения всех аргументов этой функции:
# >>> open_browser(browser_name="Chrome")
# "Open Browser [Chrome]"


def test_readable_function():
    open_browser(browser_name="Chrome")
    go_to_companyname_homepage(page_url="https://companyname.com")
    find_registration_button_on_login_page(page_url="https://companyname.com/login", button_text="Register")


def open_browser(browser_name):
    actual_result = print_function_name_and_arguments(open_browser, browser_name)
    assert actual_result == "Open Browser [Chrome]"


def go_to_companyname_homepage(page_url):
    actual_result = print_function_name_and_arguments(go_to_companyname_homepage, page_url)
    assert actual_result == "Go To Companyname Homepage [https://companyname.com]"


def find_registration_button_on_login_page(page_url, button_text):
    actual_result = print_function_name_and_arguments(find_registration_button_on_login_page, page_url, button_text)
    assert actual_result == "Find Registration Button On Login Page [https://companyname.com/login, Register]"


def print_function_name_and_arguments(function_name, *args):
    function_name_text = function_name.__name__.replace("_", " ").title()
    function_args = ''
    for _ in args:
        function_args = ', '.join(args)
    return function_name_text + f" [{function_args}]"
