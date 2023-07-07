# Создать телефонную книгу с возможностью сохранения в файл.
# Реализовать меню: 1 - добавить контакт, 2- изменить порядковый номер контакта,
# 3 - удалить контакт, 4 - переименовать контакт, 5 - выйти из программы

class PhoneBook:
    def __init__(self):
        self.phone_book = {}
        self.id = 1

    def read_contacts(self, filename):
        try:
            with open(filename, 'r') as file:
                lines = file.readlines()  # выводим списком строки
                for line in lines:
                    contact_id, name, phone = line.strip().split(":")
                    # присваиваем значение трем переменным через разделение строки
                    self.phone_book[int(contact_id)] = {"name": name, "phone": phone}
                    self.id = int(contact_id) + 1
        except FileNotFoundError as error:
            print(error)

    def save_contacts(self, filename):
        with open(filename, "w") as file:
            for contact_id, contact in self.phone_book.items():  # перебираем элементы словаря self.phone_book
                # Каждая итерация цикла присваивает переменной contact_id ключ словаря,
                # а переменной contact необходимое значение.
                name = contact["name"]
                phone = contact["phone"]
                file.write(f"{contact_id}: {name}: {phone}\n")

    def add_contact(self, name, phone):
        contact_id = self.id
        self.phone_book[contact_id] = {"name": name, "phone": phone}
        self.id += 1
        print(f"Contact {contact_id}: {name}: {phone} successfully added.")

    def update_contact_id(self, contact_id, new_id):
        if contact_id in self.phone_book:
            contact = self.phone_book.pop(contact_id)
            self.phone_book[new_id] = contact
            print(f"Id of the contact {contact['name']} successfully updated") # перепроверить в случае ошибки
        else:
            print(f"There is no contact with such {contact_id} id")

    def delete_contact(self, contact_id):
        if contact_id in self.phone_book:
            contact = self.phone_book.pop(contact_id)
            print(f"Contact {contact['name']} was successfully deleted")
        else:
            print(f"There is no contact with such {contact_id} id")

    def rename_contact(self, contact_id, new_contact_name):
        if contact_id in self.phone_book:
            contact = self.phone_book[contact_id]
            contact['name'] = new_contact_name
            print(f"Contact with {contact_id} id was successfully renamed")
        else:
            print(f"There is no contact with such {contact_id} id")

    def print_phone_book(self):
        if self.phone_book:
            print(f"Phone book: ")
            for contact_id, contact in self.phone_book.items():
                name = contact['name']
                phone = contact['phone']
                print(f"id:{contact_id}, name:{contact['name']}, phone:{contact['phone']}")
        else:
            print("Phone book is empty =(")


def display_menu():
    # не требует передачи аргументов, в том числе self, потому что она не является методом класса
    # и просто выводит список действий
    print("Menu: ")
    print("Print 1 to add contact")
    print("Print 2 to change the id of the contact")
    print("Print 3 to delete the contact")
    print("Print 4 to rename the contact")
    print("Print 5 to save the contact and close the program")

try:
    phone_book = PhoneBook()
    # with open("phonebook.txt", "w" ) as test_file:
    #     test_file.write("")

    phone_book.read_contacts("phonebook.txt")

    while True:
        display_menu()
        user_choice = int(input("What do you want to do? "))

        match user_choice:
            case 1:
                name = input("Enter contact name: ")
                stripped_name = name.strip()
                phone = input("Enter phone number: ")
                stripped_phone = phone.strip()
                phone_book.add_contact(stripped_name, stripped_phone)
            case 2:
                contact_id = int(input("Enter current id of  the contact: "))
                new_id = int(input("Enter new id for the contact: "))
                phone_book.update_contact_id(contact_id, new_id)
            case 3:
                contact_id = int(input("Enter id of  the contact: "))
                phone_book.delete_contact(contact_id)
            case 4:
                contact_id = int(input("Enter id of  the contact: "))
                new_name = input("Enter new name: ")
                stripped_new_name = new_name.strip()
                phone_book.rename_contact(contact_id, stripped_new_name)
            case 5:
                phone_book.save_contacts("phonebook.txt")
                print("Contact is saved. Program is finished")
                break
            case _:
                print("Incorrect choice. Enter number from 1 to 5")

except Exception as error:
    print(error)
