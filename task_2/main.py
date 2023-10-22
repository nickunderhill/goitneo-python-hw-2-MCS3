from collections import UserDict


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    def __init__(self, value):
        super().__init__(value)


class Phone(Field):
    def __init__(self, value):
        self.validate_phone(value)
        super().__init__(value)

    def validate_phone(self, value):
        if not (len(value) == 10 and value.isdigit()):
            raise ValueError("Phone must contain 10 digits")


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def find_phone(self, phone):
        return next((p for p in self.phones if p.value == phone), None)

    def edit_phone(self, old, new):
        existing_phone = self.find_phone(old)
        if not existing_phone:
            error_msg = f"Phone {old} number not found for record {self.name}"
            raise LookupError(error_msg)

        existing_phone.value = new

    def remove_phone(self, phone):
        existing_phone = self.find_phone(phone)
        if existing_phone:
            self.phones.remove(existing_phone)

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"


class AddressBook(UserDict):
    def add_record(self, record):
        key = record.name.value
        self.data[key] = record

    def find(self, name):
        return self.data[name]

    def delete(self, name):
        self.data.pop(name)


def main():

 # Створення нової адресної книги
    book = AddressBook()

    print("# Створення запису для John")
    john_record = Record("John")
    john_record.add_phone("1234567890")
    john_record.add_phone("5555555555")

    print(john_record)

    print("# Додавання запису John до адресної книги")
    book.add_record(john_record)

    print("# Створення та додавання нового запису для Jane")
    jane_record = Record("Jane")
    jane_record.add_phone("9876543210")
    book.add_record(jane_record)

    print("# Виведення всіх записів у книзі")
    for name, record in book.data.items():
        print(record)

    print("Знаходження та редагування телефону для John")
    john = book.find("John")
    john.edit_phone("1234567890", "1112223333")

    print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

    print("# Пошук конкретного телефону у записі John")
    found_phone = john.find_phone("5555555555")
    print(f"{john.name}: {found_phone}")  # Виведення: 5555555555

    book.delete("Jane")
    print("# Виведення всіх записів у книзі після видалення запису Jane")
    for name, record in book.data.items():
        print(record)


if __name__ == "__main__":
    main()
