from enum import Enum
import abc


# region Классы

# Перегрузка операторов
# https://metanit.com/python/tutorial/7.7.php
# В коде ниже только: __init__, __str__, __del__

# Абстрактные классы и методы
# https://metanit.com/python/tutorial/7.8.php

class Gender(Enum):
    MALE = 'male'
    FEMALE = 'female'


class User:
    __name: str
    __age: int
    __gender: Gender

    def __init__(self, *, name: str, age: int, gender: Gender):
        self.__name = name
        self.__gender = gender
        self.age = age

    def __del__(self):
        print('Пользователь удалился')

    def __str__(self):
        return f'Name: {self.__name}' \
               f'Age: {self.__age}' \
               f'Gender: {self.__gender}'

    @staticmethod
    def hello():
        print('Hello')

    def log(self):
        print(self)

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age: int):
        if age < 0:
            raise Exception('Возраст не может быть отрицательным')

        self.__age = age


class AuthUser(User):
    __token: str

    def __init__(self, *, name: str, age: int, gender: Gender, token: str):
        super().__init__(name=name, age=age, gender=gender)
        self.__token = token

    def log(self):
        super().log()
        print(f'Token: {self.__token}')


user: User = User(
    name='Biba',
    age=54,
    gender=Gender.MALE
)

user.age = 27
user.log()

User.hello()

# True
isinstance(user, User)

# endregion


class Shape(abc.ABC):

    @abc.abstractmethod
    def some_method(self): pass
