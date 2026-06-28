# Create a base class Animal and subclasses Dog and Cat.

class Animal:
    def sound(self):
        print("Animals make sounds")

class Dog(Animal):
    def bark(self):
        print("Dog barks")

class Cat(Animal):
    def meow(self):
        print("Cat meows")

d = Dog()
d.sound()
d.bark()

c = Cat()
c.sound()
c.meow()

# Create a class hierarchy for Vehicle → Car → ElectricCar.

class Vehical:
    def vehical_info(self):
        print("This is a vehical.")
    
class Car(Vehical):
    def car_info(self):
        print("This is a Car.")

class ElectricCar(Car):
    def electric_info(self):
        print("This is an electric car.")

e = ElectricCar()

e.vehical_info()
e.car_info()
e.electric_info()

# Implement method overriding in a base and derived class.

class Animal:
    def sound(sound):
        print("Animal makes a sound.")

class Dog(Animal):
    def sound(self):
        print("Dog barks")

d = Dog()
d.sound()

# Demonstrate multiple inheritance with two parent classes.

class Father:
    def skills(self):
        print("Programming")

class Mother:
    def talent(self):
        print("Painting")

class Child(Father, Mother):
    pass

c = Child()

c.skills()
c.talent()

# Create a polymorphic function that works with different shapes.

class Reactangle:
    def area(self):
        print("Rectangle Area = Length * width")

class Circle:
    def area(self):
        print("Circle Area = 3.14 * radius * radius")

def calculate_area(shape):
    shape.area()

r = Reactangle()
c = Circle()

calculate_area(r)
calculate_area(c)

# Create a Bank system with SavingsAccount and CurrentAccount classes.

class BankAccount:
    def __init__(self, balance):
        self.balance = balance

class SavingsAccount(BankAccount):
    def show_balance(self):
        print("Savings Balance:", self.balance)

class CurrentAccount(BankAccount):
    def show_balance(self):
        print("Current Balance:", self.balance)
        
s = SavingsAccount(10000)
c = CurrentAccount(15000)

s.show_balance()
c.show_balance()

# Create a class with private attributes and getter/setter methods.

class Person:
    def __init__(self, name):
        self.name = name

class Teacher(Person):
    def display(self):
        print("Teacher:", self.name)

class Student(Person):
    def display(self):
        print("Student:", self.name)

t = Teacher("Rahul")
s = Student("Mili")

t.display()
s.display()

# Create a Teacher and Student class to show inheritance.

class Student:
    def __init__(self):
        self.__marks = 0

    def set_marks(self, marks):
        self.__marks = marks

    def get_marks(self):
        return self.__marks

s = Student()

s.set_marks(85)

print("Marks:", s.get_marks())

# Create a MusicPlayer class and subclass Spotify to override the play method.

class MusicPlayer:
    def play(self):
        print("Playing music")

class Spotify(MusicPlayer):
    def play(self):
        print("Playing music from Spotify")

s = Spotify()

s.play()

# Demonstrate the use of super() in inheritance.

class Person:
    def __init__(self, name):
        self.name = name

class Student(Person):
    def __init__(self, name, roll):
        super().__init__(name)
        self.roll = roll

    def display(self):
        print("Name:", self.name)
        print("Roll No:", self.roll)

s = Student("Mahi", 101)

s.display()