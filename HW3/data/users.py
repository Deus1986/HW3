import dataclasses


@dataclasses.dataclass
class User:
    name: str
    last_name: str
    email: str
    gender: str
    number: str
    birthday: str
    current_address: str


user_semen = User('Semen', 'Shpak', 'ShpakS@mail.ru', 'Male', '9543231207', '04 December,1986',
                  'Ленинградская область, Гатчина, бульвар Авиаторов, 9')
