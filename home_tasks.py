# Задание 1:
#
# Создайте класс «Город». Необходимо хранить в полях класса: название города, название региона,
# название страны, количество жителей в городе, почтовый индекс города, телефонный код города.
# Реализуйте доступ к отдельным полям через методы класса.
#
# get and set (по примеру на уроке)
#
import re


# class City:
#     __city_name: str = "no name"
#     __region: str = "no name"
#     __country: str = "no name"
#     __people: int = 0
#     __post_index: str = "no index"
#     __phone_code: str = "no code"
#
#     def __init__(self, city_name, region, country, people, post_index, phone_code):
#         self.__city_name = city_name
#         self.__region = region
#         self.__country = country
#         self.__people = people
#         self.__post_index = post_index
#         self.__phone_code = phone_code
#         # применение инкапсуляции
#         self.set_name(city_name)
#         self.set_region(region)
#         self.set_country(country)
#         self.set_people(people)
#         self.set_post_index(post_index)
#         self.set_phone_code(phone_code)
#
#     def set_name(self, city_name):
#         if 1 < len(city_name) < 30:
#             self.__city_name = city_name
#         else:
#             print("Incorrect length of the name")
#
#     def get_name(self):
#         return self.__city_name
#
#     def set_region(self, region):
#         if 2 < len(region) < 50:
#             self.__region = region
#         else:
#             print("Incorrect length of the region")
#
#     def get_region(self):
#         return self.__region
#
#     def set_country(self, country):
#         if 1 < len(country) < 30:
#             self.__country = country
#         else:
#             print("Incorrect length of the country")
#
#     def get_country(self):
#         return self.__country
#
#     def set_people(self, people):
#         if 0 < people:
#             self.__people = people
#         else:
#             print("You should enter 1 or more")
#
#     def get_people(self):
#         return self.__people
#
#     def set_post_index(self, post_index):
#         pattern = r'^\d{6}$'
#         if re.match(pattern, post_index):
#             self.__post_index = post_index
#         else:
#             print("Invalid post index")
#
#     def get_post_index(self):
#         return self.__post_index
#
#     def set_phone_code(self, phone_code):
#         pattern = r'^\d{3,5}$'
#         if re.match(pattern, phone_code):
#             self.__phone_code = phone_code
#         else:
#             print("Invalid phone code")
#
#     def get_phone_code(self):
#         return self.__phone_code
#
#     def show_info(self):
#         print(f"City name: {self.__city_name}, region: {self.__region},"
#               f"\ncountry:{self.__country}, people: {self.__people},\n"
#               f"post index: {self.__post_index}, phone code: {self.__phone_code}.")
#         print()
#
#
# try:
#     city = City("Avesta", "Dalarna", "Sweden", 11949, "123456", "047")
#     # city.show_info()
#     # city.set_region("i")
#     # city.set_people(-8)
#     # city.set_country("I")
#     # city.set_phone_code("12")
#     # city.set_post_index("1234567890")
#     print(city.get_region())
#     # city.show_info()
#
#     city_2 = City("Nagoya", "Aichi", "Japan", 10110000, "000001", "2458")
#     city_2.show_info()
#
#     print(city_2.get_country())
#     city_2.set_phone_code("2678")
#     print(city_2.get_phone_code())
#
# except Exception as error:
#     print(error)

# Задание 2:
#
# Создайте класс «Страна». Необходимо хранить в полях класса: название страны,
# название континента, количество жителей в стране, телефонный код страны, название столицы,
# название городов страны. Реализуйте доступ к отдельным полям через методы класса.
#
# get and set (по примеру на уроке)

# class Country:
#     __country: str = "no name"
#     __continent: str = "no name"
#     __people: int = 0
#     __phone_code: str = "no code"
#     __capital: str = "no name"
#     __cities = []
#
#     def __init__(self, country, continent, people, phone_code, capital, cities):
#         self.__country = country
#         self.__continent = continent
#         self.__people = people
#         self.__phone_code = phone_code
#         self.__capital = capital
#         self.__cities = cities
#         # применение инкапсуляции
#         self.set_country(country)
#         self.set_continent(continent)
#         self.set_people(people)
#         self.set_phone_code(phone_code)
#         self.set_capital(capital)
#         self.set_cities(cities)
#
#     def set_country(self, country):
#         if 1 < len(country) < 30:
#             self.__country = country
#         else:
#             print("Incorrect length of the country")
#
#     def get_country(self):
#         return self.__country
#
#     def set_continent(self, continent):
#         if 1 < len(continent) < 50:
#             self.__continent = continent
#         else:
#             print("Incorrect length of the continent")
#
#     def get_continent(self):
#         return self.__continent
#
#     def set_people(self, people):
#         if 0 < people:
#             self.__people = people
#         else:
#             print("Amount of people can not be negative")
#
#     def get_people(self):
#         return self.__people
#
#     def set_phone_code(self, phone_code):
#         pattern = r'^\+\d{2,4}$'
#         if re.match(pattern, phone_code):
#             self.__phone_code = phone_code
#         else:
#             print("Incorrect phone code")
#
#     def get_phone_code(self):
#         return self.__phone_code
#
#     def set_capital(self, capital):
#         if 1 < len(capital) < 30:
#             self.__capital = capital
#         else:
#             print("Incorrect length of the capital")
#
#     def get_capital(self):
#         return self.__capital
#
#     def set_cities(self, cities):
#         pattern = r'[a-zA-Z]{2,50}'
#         valid_cities = []
#
#         # добавляем предыдущие правильные города в список valid_cities
#         valid_cities.extend(self.__cities)
#
#         for city in cities:
#             if re.match(pattern, city):
#                 valid_cities.append(city)
#             else:
#                 print(f"Incorrect length or type of the city {city}")
#
#         valid_cities = set(valid_cities) # Вызываем set, чтобы убрать дубликаты
#         self.__cities = list(valid_cities) # Делаем опять valid_cities списком
#
#     def get_cities(self):
#         return self.__cities
#
#     def show_info(self):
#         print(f"Country: {self.__country}, continent: {self.__continent},\n"
#               f"people: {self.__people}, phone code: {self.__phone_code},\n"
#               f"capital: {self.__capital}, cities: {self.__cities}")
#
#
# try:
#     city = ["Kyiv", "Odessa"]
#     country_1 = Country("Ukraine", "Eurasia", 43790000, "+38", "Kyiv", city)
#     country_1.show_info()
#     print(country_1.get_cities())
#     country_1.set_cities(["123"])
#     country_1.set_cities(["i", "r", "Kharkiv"])
#     print(country_1.get_cities())
#     print(country_1.get_capital())
# except Exception as error:
#     print(error)
