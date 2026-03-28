# Practice 3: Object-Oriented Programming (OOP)
# Topics: classes, __init__, instance methods, class variables, inheritance, polymorphism

# --- Basic class ---
class Animal:
    # Class variable shared by all instances
    kingdom = "Animalia"

    def __init__(self, name, sound):
        self.name = name    # instance variable
        self.sound = sound

    def speak(self):
        return f"{self.name} says {self.sound}!"

    def __str__(self):
        return f"Animal({self.name})"


dog = Animal("Rex", "Woof")
cat = Animal("Whiskers", "Meow")
print(dog.speak())
print(cat.speak())
print("Kingdom:", dog.kingdom)
print(dog)

# --- Inheritance ---
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name, "Woof")
        self.breed = breed

    def fetch(self, item):
        return f"{self.name} fetches the {item}!"

    def speak(self):
        # Override parent method
        return f"{self.name} barks: Woof woof!"


class Cat(Animal):
    def __init__(self, name, indoor=True):
        super().__init__(name, "Meow")
        self.indoor = indoor

    def speak(self):
        return f"{self.name} purrs: Meow~"


my_dog = Dog("Buddy", "Labrador")
my_cat = Cat("Luna")

print(my_dog.speak())
print(my_dog.fetch("ball"))
print(my_cat.speak())
print("Is indoor cat:", my_cat.indoor)

# --- Polymorphism ---
animals = [Animal("Parrot", "Squawk"), Dog("Max", "Poodle"), Cat("Mochi")]
print("\nAll animals speaking:")
for animal in animals:
    print(" ", animal.speak())

# --- Class with property and encapsulation ---
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self._balance = balance     # convention: "private"

    @property
    def balance(self):
        return self._balance

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print(f"Deposited ${amount}. New balance: ${self._balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > self._balance:
            print("Insufficient funds.")
        elif amount <= 0:
            print("Withdrawal amount must be positive.")
        else:
            self._balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self._balance}")

    def __str__(self):
        return f"Account({self.owner}, balance=${self._balance})"


account = BankAccount("Alice", 100)
print("\n" + str(account))
account.deposit(50)
account.withdraw(30)
account.withdraw(200)
print("Final balance:", account.balance)
