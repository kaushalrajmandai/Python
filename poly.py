class Animal:
    def sound(self):
        print("Animal makes a sound")

class Dog(Animal):
    def sound(self): #Overriding the parent method
        print("Dog barks")

class Cat(Animal):
    def sound(self): #Overriding the parent method
        print("Cat meows")

# Objects
a = Animal()
d = Dog()
c = Cat()

# Method calls
a.sound() # Animal makes a sound
d.sound() # Dog barks -> overridden
c.sound() # Cat meows -> overridden


class calculator:
    def add(self, a,b=0, c=0):
        return a+b+c
    
calc = calculator()
print(calc.add(5))
print(calc.add(5,10))
print(calc.add(5,10,15))


class car:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

car1 = car("BMW", 550000)

print(car1.brand)
print(car1.price)

class Car:
    def __init__(self):
        self._speed = 120

class SportsCar(Car):
    def show_speed(self):
        print("Speed:", self._speed)

car = SportsCar()
car.show_speed()
print(car._speed)

class Bank:
    def __init__(self, balance):
        self._balance = balance

    def get_balance(self):
        return self._balance

b = Bank(5000)
print(b.get_balance())

class Bank:
    def __init__(self, balance):
        self._balance = balance  # Use _ for convention of a 'protected' attribute

    # Getter method to retrieve the balance
    def get_balance(self):
        return self._balance

    # Setter method to set the balance with validation
    def set_balance(self, amount):
        if amount >= 0:
            self._balance = amount
        else:
            print("Invalid Amount")

# Example Usage:
b = Bank(5000)  # Initialize bank account with 5000
print(f"Initial Balance: {b.get_balance()}")

b.set_balance(9000)  # Set new valid balance
print(f"New Balance after valid set: {b.get_balance()}")

b.set_balance(-100) # Attempt to set invalid balance
print(f"Balance after invalid set attempt: {b.get_balance()}")