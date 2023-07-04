# import os
#
# dir = './'
# for f in os.listdir(dir):
#     if f.startswith('note'):
#         print(f)
#         os.remove(f)

# https://www.techiedelight.com/ru/delete-all-files-directory-python/

# 1. Дан текстовый файл. Необходимо создать новый файл, в который требуется переписать из исходного файла все слова,
# состоящие не менее чем из семи букв.
# import re
#
# with open("input_data.txt", "r", encoding="utf-8") as f:
#     text = f.read()
#     # print(text)
#     words = " ".join(re.findall(r"\b\w{7,}\b", text))
#     print(words)
#
# if len(words) > 0:
#     with open("output_data.txt", "w", encoding="utf-8") as f:
#         f.write(words)
# else:
#     print("No words found!")

# 2. Дан текстовый файл. Подсчитать количество слов в нём.

#################

# ООП - объектно ориентированное программирование
# Класс - это кастомный тип данных, который описывает некоторый объект.
# Класс - чертеж будущего экземпляра объекта.

# Инкапсуляция - сокрытие внутренней реализации и предоставление санкционированного доступа
# к интерфейсу класса. Как черный ящик.
# Абстрагируемся от внутренней реализации.

# Наследование - создание нового класса на основе уже существующего.
# Расширение базового класса - дочерним/дочерними классами.
# Абстрагируемся от базового класса/классов, используя дочерний класс.

# Полиморфизм - один интерфейс и много реализаций.
# Абстрагируемся от конкретной реализации

# статический метод (функция), поле (переменная) относятся к классу, и к экземпляру
# статический эл-т можно использовать не создавая экземпляр класса
# чаще всего статические классы используют для описания конфигов и прочих служебных объектов, там где нет смысла
# создавать экземпляры
# __init__ Конструктор класса - позволяет создать экземпляр класса. Может быть с параметрами и без параметров.
# self - ссылка на контекст класса, экземпляр класса
# контекст класса - все что является частью класса (экземпляра)
# class Car:
#     name = "no name"
#     year = 0
#
#     # конструктор без параметров (не по умолчанию)
#     # def __init__(self):
#     #     self.text = "some text"
#
#     # конструктор класса - создает экземпляр объекта
#     # def __new__(cls):
#     #     pass
#
#     # для инициализации объекта
#     # если явно не определить конструктор __new__ -> то в __init__ он создастся автоматически
#     # def __init__(self):
#     #     pass
#
#     def __init__(self, car_name, car_year):
#         self.name = car_name
#         self.year = car_year
#         self.material = "metal"
#
#     def show_info(self):
#         print(f"Name: {self.name} Year: {self.year} Material: {self.material}")
#
#     # декоратор - позволяет динамически добавить некий функционал
#     @staticmethod  # один из стандартных декораторов
#     def get_class_info():
#         print("This is Car class")
#
#
# toyota = Car("Camry", 2020)
# print(type(toyota))
# toyota.show_info()
# bmw = Car("X5", 2021)
# print(type(bmw))
# bmw.show_info()
#
# mers = Car("Test", 2023)
# print(type(mers))
# mers.show_info()
#
# # get_class_info() -> можем использовать без экземпляра класса так как этот метод статический -
# # то есть принадлежит не только экземпляру, но и самому типу (классу)
# mers.get_class_info()
# Car.get_class_info()
# # Car.show_info()  # TypeError: Car.show_info() missing 1 required positional argument: 'self'
# # show_info() мы не можем использовать без экземпляра класса
#
#
# class InvoiceType:
#     Urgent = "UrgentInvoice"
#     Normal = "NormalInvoice"
#
#     @staticmethod
#     def show_all_invoice_types():
#         print(InvoiceType.Urgent)
#         print(InvoiceType.Normal)
#
#
# print(InvoiceType.Urgent)
# InvoiceType.show_all_invoice_types()

##############
##
# class Person:
#     # __init__ Конструктор класса - позволяет создать экземпляр класса. Может быть с параметрами и без параметров.
#     # self - ссылка на контекст класса, экземпляр класса
#     # контекст класса - все что является частью класса (экземпляра)
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def show_person(self):
#         print(f"Name: {self.name} age: {self.age}")
#
#
# user1 = Person("Vasya", 33)
# user2 = Person("Petya", 44)
# user1.show_person()
# user2.show_person()
# print(user1.name)  # получаем доступ к полю (переменной) name -> выводим на экран
# user1.name = ""  # заменяем значение поля (переменной) экземпляра под названием user1
# print(user1.name)
# user1.show_person()
# Person.show_person(user2)

# v2
# используем не статический метод класса синтаксисом статического метода, но обязательно передаем экземпляр
# класса
# Person.show_person(user1)

#######################
###
# Инкапсуляция
# v1

# class User:
#     __name: str = "no name"  # private поле, доступно только внутри этого класса
#     __age: int = 0
#     __secret: int = 12345
#
#     def __init__(self, name, age):
#         self.__name = name
#         self.__age = age
        # применим инкапсуляцию
        # self.set_name(name)
        # self.set_age(age)

    # def set_name(self, name):
    #     if 2 < len(name) < 50:
    #         self.__name = name
    #     else:
    #         print("Incorrect name length!")
    #
    # def get_name(self):
    #     return self.__name
    #
    # def set_age(self, age):
    #     if 18 < age < 150:
    #         self.__age = age
    #     else:
    #         print("Incorrect age!")
    #
    # def get_age(self):
    #     return self.__age
    #
    # def show_info(self):
    #     print(f"Name: {self.__name} age: {self.__age}")
    #     self.__secret_info()  # так как мы находимся внутри класса - мы имеем доступ ко ВСЕМУ
        # контенту этого класса, и поэтому мы можем воспользоваться приватной функцией которая НЕДОСТУПНА
        # снаружи этого класса

    # __ два нижних подчеркивания означает что эта функция private, то есть доступна ТОЛЬКО внутри класса
    # если мы попытаемся обратиться к этой функции через экземпляр класса - будет ошибка
#     def __secret_info(self):
#         print(f"Secret code: {self.__secret}")
#
#
# vasya = User("Vasya", 33)
# vasya.show_info()
# # print(vasya.__name)
# vasya.set_age(300)
# vasya.show_info()

# vasya.__secret_info()
