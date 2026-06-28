# Create a Car class with attributes like brand, model, and speed, and methods to accelerate/brake.

class Car: 
    def __init__(self, brand, model, speed):
        self.brand = brand
        self.model = model
        self.speed = speed 

    def accelerate(self):
        self.speed += 10
        print("Speed after acceleration: ", self.speed)

    def brake(self):
        self.speed -= 10
        print("Speed after brake: ", self.speed)

car1 = Car("Toyota", "Fortuner", 50)

car1.accelerate()
car1.brake()
        

# Create a BankAccount class with deposit and withdraw methods.

class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def deposite(self, ammount):
        self.balance += ammount
        print("Deposited: ", ammount)

    def withdraw(self, ammount):
        if ammount <= self.balance:
            self.balance -= ammount
            print("Withdraw: ", ammount)
        else:
            print("Insufficient Balance!")

    def displays(self):
        print("Balance: ", self.balance)

acc = BankAccount(5000)

acc.deposite(1000)
acc.withdraw(2000)
acc.displays()
        
        
# Create a Student class with a method to calculate average marks.

class Student:
    def __init__(self, name, m1, m2, m3):
        self.name = name
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def CalculateAvg(self):
        avg = (self.m1 + self.m2 + self.m3) / 3
        print("Average Marks: ", avg)

s = Student("Diya", 89, 96, 99)
s.CalculateAvg()

# Create a Rectangle class with methods to find area and perimeter.

class Reactangle():
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        print("Area= ", self.length * self.width) 

    def perimeter(self):
        print("Perimeter= ", 2 * (self.length + self.width))

r = Reactangle(10, 5)
r.area()
r.perimeter()


# Create an Employee class that displays salary details.

class Employee:
    def __init__(self, name, salary):
        self.name = name 
        self.salary = salary

    def display(self):
        print("Name: ", self.name)
        print("Salary: ", self.salary)

e = Employee("Prince", 50000)

e.display()


# Create a Book class to store title, author, and price, and display details.

class Book:
    def __init__(self, tittle, author, price):
        self.tittle = tittle
        self.author = author
        self.price = price

    def display(self):
        print("Book's tittle: ", self.tittle)
        print("Book's author: ", self.author)
        print("Book's price: ", self.price)

b = Book("Python basics", "John", 500)

b.display()
        

# Create a Circle class to find area and circumference.

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def FindArea(self):
        print("Area of the circle: ", 3.14 * self.radius * self.radius)

    def Circumference(self):
        print("Circumference: ", 2 * 3.14 * self.radius)

c = Circle(12)
c.FindArea()
c.Circumference()
        

# Create a Laptop class with a method to apply discounts on price.

class Laptop:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

    def Apply_Disccount(self, discount):
        final_price = self.price - (self.price * discount / 100 )
        print("Price after discount: ", final_price)
        
l = Laptop("HP", 70000)
l.Apply_Disccount(10)

# Create a Flight class with seat booking functionality.

class Flight:
    def __init__(self, total_seats):
        self.total_seats = total_seats

    def book_seat(self, seats):
        if seats <= self.total_seats:
            self.total_seats -= seats
            print("Booking Sucessfull")
            print("Reamining Seates:", self.total_seats)
        else:
            print("Seates Not Available")

f = Flight(150)
f.book_seat(30)


# Create a Shop class with a method to add and list products.

class Shop:
    def __init__(self):
        self.products = []

    def AddProduct(self, product):
        self.products.append(product)
    
    def list_products(self):
        print("Products:")
        for item in self.products:
            print(item)

s = Shop()

s.AddProduct("Laptop")
s.AddProduct("Mouse")
s.AddProduct("Keyboard")

s.list_products()