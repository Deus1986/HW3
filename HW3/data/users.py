import dataclasses
import datetime
from enum import Enum


class User:
    user_semen = {'0': 'Semen Shpak',
                  '1': 'ShpakS@mail.ru',
                  '2': 'Ленинградская область, Гатчина, бульвар Авиаторов, 9',
                  '3': 'Ленинградская область, Всеволожский район, деревня Новое Девяткино, Арсенальная улица, 3'}


class UserData(Enum):
    name = 0
    email = 1
    currentAddress = 2
    permanentAddress = 3
