#Basic class and object implementation:

class Student:
    def __init__(self , name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"Name: {self.name} and age: {self.age}")

s1 = Student("Aamir", 17)
s1.display()

def seperator(length = 120):
    print("*" * length)
seperator()

#Includes Encapsulation, Methods ,and default parameters:
class BankAccount:
    def __init__(self, owner , balance = 0):
        self.owner = owner
        self.balance = balance

    def Deposit(self, amount):
        self.balance += amount
        print(f"Deposited amount is {amount} and the new balance is {self.balance}")

    def Withdraw(self, amount,):
        if amount> self.balance:
            print("Insufficient Funds!")

        else:
            self.balance -= amount
            print(f"Wintdrawn amount {amount}. New Balance is {self.balance}")

obj = BankAccount("Aamir", 15000)
obj.Deposit( 5000)
obj.Withdraw(20001)

seperator()

#Inheritance example is given below:

class Person:
    def __init__(self, name):
        self.name = name 
        
    def show(self):
        print(f"Name of the Person: {self.name}")

class Employee(Person):
    def __init__(self, name , salary):
        super().__init__(name)
        self.salary = salary

    def show(self):
        super().show()
        print(f"Salary is {self.salary}")

obj = Employee("Aamir", 1200000)
obj.show()
seperator()

#Polymorphism:

class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def speak(self):
        print("Kutta bhokra BKL!")

class Cat(Animal):
    def speak(self):
        print("Cat meows!")

# Polymorphism in action
animals = [Dog(), Cat(), Animal()]
for animal in animals:
    animal.speak()

    print("THis the end of this program.")


