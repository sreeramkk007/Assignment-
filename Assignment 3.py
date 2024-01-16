class Person:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def update_info(self, new_name, new_age, new_address):
        self.name = new_name
        self.age = new_age
        self.address = new_address

    def display_info(self):
        print("Name:",self.name)
        print("Age:",self.age)
        print("Address:",self.address)


person1 = Person("Emily", 20, "123 Main St.Peter's, London")
person1.display_info()

print("\nUpdated information below..\n")

person1.update_info("Ash", 15, "221B Huges Street, Uk")
person1.display_info()
