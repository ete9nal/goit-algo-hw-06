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
        # перевірка, що телефон складається виключно з 10 цифр
        if len(value) == 10 and value.isdigit():
            self.value = value
        else: 
            raise ValueError("Phone must be 10 digits only")

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    # метод для додавання обʼєктів Phone
    def add_phone(self, phone):
          self.phones.append(Phone(phone))

    # метод для видалення обʼєктів Phone
    def remove_phone(self, phone):
        p = self.find_phone(phone)
        if p:
            self.phones.remove(p)
    
    # метод для зміни обʼєкту Phone
    def edit_phone(self, old, new):
        if self.find_phone(old):
            self.remove_phone(old)
            self.add_phone(new)

    # метод для пошуку обʼєкту Phone
    def find_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                return p
        return None
                
    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):

    # метод для додавання записів у словник за ключем (імʼя), значенням якого стає об'єкт record
    def add_record(self, record):
        self.data[record.name.value] = record

    # метод для пошуку обʼєкту record за імʼям 
    def find(self, name):
        if name in self.data:
            return self.get(name)
        else:
            return None
        
    # метод для видалення запису за імʼям        
    def delete(self, name):
        if name in self.data:
            self.data.pop(name)

    # магічний метод для повернення рядка з усіма записами словника
    def __str__(self):
        result = ""
        for record in self.data.values():
            phones_str = "; ".join(p.value for p in record.phones)
            result += f"Contact name: {record.name.value}, phones: {phones_str}\n"
        return result.strip()
    


# Створення нової адресної книги
book = AddressBook()

# Створення запису для John
john_record = Record("John")
john_record.add_phone("1234567890")
john_record.add_phone("5555555555")

# Додавання запису John до адресної книги
book.add_record(john_record)

# Створення та додавання нового запису для Jane
jane_record = Record("Jane")
jane_record.add_phone("9876543210")
book.add_record(jane_record)

# Виведення всіх записів у книзі
    
print(book)

# Знаходження та редагування телефону для John
john = book.find("John")
john.edit_phone("1234567890", "1112223333")

print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

# Пошук конкретного телефону у записі John
found_phone = john.find_phone("5555555555")
print(f"{john.name}: {found_phone}")  # Виведення: John: 5555555555

# Видалення запису Jane
book.delete("Jane")
