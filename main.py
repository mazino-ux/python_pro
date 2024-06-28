
# PYTHON METHOD
# SET
# *add, remove, discard, union, intersection, difference, symmetric, pop, clear, copy
#
# Example:
# S = { 1, 2 ,3 }
# T = { 3, 4, 5 }
# Length - Print(Len[fruits])

# This is a sample Python script. Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
# See PyCharm help at https://www.jetbrains.com/help/pycharm/


num = int(input("Enter a number: "))
if num > 1 < 500:
    for i in range(2, int(num/2) + 1):
        if num % i == 0:
            print("The number " + str(num) + " is not a prime number")
            break
    else:
        print("This is a prime number")
else:
    print("The number " + str(num) + " is not a prime number less")
# ---------------------------------------------------------------------
# a = int(input("Enter a Number between 1 - 500: "))
# if 1 < a < 500:
#     is_prime = True
#     for x in range(2, a):
#         if (a % x) == 0:
#             is_prime = False
#             break
#
#     if is_prime:
#         print("Prime Number🙌🏼!!")
#     else:
#         print("Not a prime number")
# else:
#     print("Enter a number between (1, 500)")
# ---------------------------------------------------------------------
# def reverse_string(input_string):
#     return input_string[::-1]
#
# # Example usage:
# original_string = str(input("Input a string :"))
# reversed_string = reverse_string(original_string)
#
# print(f"Original: {original_string}")
# print(f"Reversed: {reversed_string}")
# import random
# print(random.randrange(1, 20))
# ---------------------------------------------------------------------
# myFruit = ["orange", "banana", "mango", 5, 7, 4.2]
# myFruit.pop()
# print(myFruit)

# name = str(input("Enter your Name: "))
# print("My name is " , name)

# convert this list to a turple
# myList = [1, 4.2, 5, 6, 7]
# myTuple = tuple(myList)
# print("This has been changed to  a tuple", myTuple)

# todolist = str(input("Enter a task: "))
# tasks = [ ]
# def add_task(task):
#     tasks.append(task)
# print("Task Successfully added ")
# add_task("Go to School")
# add_task("Eat Burgers and pizza")
# add_task("Clean the house")
# add_task("Pray to God")
# add_task("Dance and sing")
# tasks.remove("Dance and sing")
# print(tasks)

# implement a phonebook applications that stores contact information using dictionaries
# -------------------- ASSIGNMENT SOLUTION --------------------
# phoneBook = {}
# def add_phone_no(contact_name, phone_No):
#     phoneBook[contact_name] = phone_No
#     print("Task Successfully added:", contact_name)
# add_phone_no("Mathena Ditus", "810-469-4214")
# add_phone_no("Glory Lana", "810-469-4214")
# add_phone_no("Roman Reigns", "810-469-4214")
# add_phone_no("Nimrod Einstein", "810-469-4214")
# add_phone_no("Johnny Banabas", "810-469-4214")
# phoneBook.pop("Nimrod Einstein", "810-469-4214")
# print(phoneBook)
#
# def search_no(contact_name):
#     if contact_name in phoneBook:
#         print(f"Name : {contact_name}, Number: {phoneBook[contact_name]}")
#     else:
#         print("contact Not Found")
# search_no("Johnny Banabas")
#
# print(12+28/7*2)
#
# student_records = { "Ada": "87","Bull":"67"}
# student_records.update({("Johnny","81")})
# print(student_records)

# ??----------------------------------------------------------------------------------------??
# cart = { }
# def add_cart(items, price):
#     cart[items] = price
# add_cart("Bicycle", 300)
# add_cart("Eraser", 800)
# total = sum(cart.values())
# print(cart)
# print("Total Price of Items: $" + str(total))
#
# students = {}
# def stud_info(name, age):
#     students[name] = age
# stud_info("Trinity","74")
# print(students)
#
# Num = int(input("Enter any random num between 1 - 500: "))
# import random
# No = random.randint(1, 500)
# if Num == No:
#     print("Guessed Right!!, correct, bravo!!")
# else:
#     print("Awwn😬, guessed wrong, try again, the right answer is ", No)


# grades = {}
#
# def add_grade(name, grade):
#     grades[name] = grade
# add_grade("Zoe", 40)
# add_grade("Mark", 70)
# add_grade("Conrad", 90)
# add_grade("Bella", 45)
# print(grades)
# print(max(grades.values()))
# print(min(grades.values()))
# total = sum(grades.values())
# len = len(grades.values())
# print(total / len)

# motion_sensor = 0
# front_door_sensor = 1
# back_door_sensor = 0
# def is_alarm_triggered(motion_sensor, front_door_sensor,back_door_sensor):
#     if motion_sensor or front_door_sensor or back_door_sensor == True:
#         print("Alarm Will Go Off")
#     else:
#         print(False)

# for x in range(6):
#     if x == 3: continue
#     print(x)
# else:
#     print("Finally finished!")

# def tri_recursion(k):
#   if(k > 0):
#     result = k + tri_recursion(k - 1)
#     print(result)
#   else:
#     result = 0
#   return result
#
# print("\n\nRecursion Example Results")
# tri_recursion(7)
# class Myclass:
#     x = 5
# p1 = Myclass
# print(p1.x)

# class person:
#     def __init__(myref, food, mark):
#         myref.food = food
#         myref.mark = mark
# p1 = person("Rice", 40)
# print(p1.food)
# print(p1.mark)

# Lambda function is a small anonymous function which can take any number of arguments, but can only have one expression.
# class my_ndivid:
#     def __init__(self, name, age, language):
#         self.name = name
#         self.age = age
#         self.language = language
#     def __str__(self):
#         return f'{self.name}({self.age})({self.language})'
#
# obj = my_ndivid( "Janet", 23, "Python")
# print(obj)
#
# a = int(input("Enter a logic Value: "))
# b = int(input("Enter another logic Value: "))
# def and_logic(a,b):
#     return a and b
# def or_logic(a,b):
#     return a or b
# def not_logic(a):
#     return not a
# andlogic = and_logic(a,b)
# orlogic = or_logic(a,b)
# notlogic = not_logic(a)
# print(andlogic)
# print(orlogic)
# print(int(notlogic))
#
# a = int(input("Enter a number for width: "))
# b = int(input("Enter another number: "))
# class rectangle:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
# p1 = rectangle(a, b)
# area = p1.width * p1.height
# my_perimeter = p1.width + p1.height
# perimeter = 2 * my_perimeter
# if a <= 0 or b <= 0:
#     while True:
#         a = int(input("Enter a number for width: "))
#         b = int(input("Enter another number: "))
# # else:
# #     print("Invalid")
# print(area)
# print(perimeter)


# account = { }
# a = int(input("Deposit or widthdraw money: "))
# class bank_account:
#     def __init__(self, user, money):
#         self.user = user
#         self.money = money
# def add_money(user, money):
#     account[user] = money
# add_money("Initial Amount:", 500)
# total = sum(account.values()) + a
# print(account)
# print("Your balance is", total)
# add_money("Trinity", total)
# print(account)

#
# class bank_account:
#     def __init__(self, statement, amount):
#         self.statement = statement
#         self.amount = amount
# p1 = bank_account("Balance:", 0)
# deposit = int(input("Deposit money: "))
# amount = + deposit
# print(p1.statement, amount)
# current_amount = deposit
# withdraw = int(input("Withdraw money: "))
# amount = current_amount - withdraw
# if current_amount > withdraw:
#     print(p1.statement, amount)
# else:
#     print("Insufficient Balance")


#
# class Car:
#     def __init__(self, make, color, year):
#         self.make = make
#         self.color = color
#         self.year = year
# make = str(input("Enter the make: "))
# color = str(input("Give a color: "))
# year = int(input("Enter a year: "))
# my_car = Car(make, color, year)
# def display_info(car):
#     return f"Make: '{my_car.make}', Color: '{my_car.color}', Year: {my_car.year}"
# car_details = display_info(my_car)
# print({car_details})
# print()
# # car_info = { }
# while True:
#     make = str(input("Enter the make: "))
#     color = str(input("Give a color: "))
#     year = int(input("Enter a year: "))
#
#     def disp_info(car):
#         return f"Make: '{make}', Color: '{color}', Year: {year}"
#     car_detail = disp_info(my_car)
#     if year >= 2025:
#         break
#     else:
#         # print()
#         unknown = car_details, car_detail
#         for x in unknown:
#             print({x})
#             print()

# [display_info : method within the Car class, self: instance of the class,
# print: is a built-in function to display output]
# parent class is the class being inherited from("Base Class") [__init__ : constructor method: initializes new obj in a class]
# child class is the class that inherits from another class("Derived Class")
#
# class Employee:
#     def __init__(self, name, position, salary):
#         self.name = name
#         self.position = position
#         self.salary = salary
#
#     def give_raise(self, amount):
#         self.salary += amount
#         print(f"{self.name}'s salary has been increased by {amount}. New salary: {self.salary}")
#
#
# # Example usage:
# employee1 = Employee("John Doe", "Manager", 50000)
# print(f"{employee1.name} - Position: {employee1.position}, Salary: ${employee1.salary}")

# employee1.give_raise(5000)
#
# class Employee:
#     def __init__(self,name,position,salary):
#         self.name = name
#         self.position = position
#         self.salary = salary
# name = str(input("Enter Employee's name: "))
# position = str(input("Enter Employee's position: "))
# salary = float(input("Input salary: "))
# employee_info = Employee(name,position,salary)
# def hello(employee_info):
#     return f"name: {employee_info.name}, position:{employee_info.position}, salary: ${employee_info.salary}"
# print({hello(employee_info)})
# print()
#
# raised = float(input("Enter the raised amount: "))
# raise_amount = raised + salary
# print()
# print({hello(employee_info)})
# print({f"name: {employee_info.name}, position:{employee_info.position}, salary: ${raise_amount}"})




# def bubble_sort(numbers):
#     n = len(numbers)
#     for i in range(n-1):
#         for j in range(n-i-1):
#             if numbers[j] > numbers[j + 1]:
#                 numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
# numbers = [5, 2, 8, 12, 1, 6]
# bubble_sort(numbers)
# print(numbers)


# students = [
#     Student("Alice", 85)
#     Student("Bob", 92)
#     Student("Charlie", 78)
#     Student("David", 95)
#     Student("Eve", 88)
# ]

# custom_sort(students)
# for student in students:
#     print(f"Name: {student.name}, Score: {student.score}, Rank: {student.rank}")

# def pyfunc(a):
#     for x in range(a):
#         print(' '*(a-x-1) + '*' *(2*x+1))
# pyfunc(9)

# s = input("Enter Sequence: ")
# t = s[::-1]
# if s == t:
#     print(f"{t} is a palindrome of {s}!!")
# else: print(f"{t} is not a palindrome of {s}!!")

# class MyNumbers:
#   def __iter__(self):
#     self.a = 1
#     return self
#
#   def __next__(self):
#       if self.a <= 20:
#           x = self.a
#           self.a += 1
#           return x
#       else:
#           raise StopIteration
#
# my_class = MyNumbers()
# my_iter = iter(my_class)
#
# for i in my_iter:
#     print(i)
# x =20
# def myFunc():
#     x = 5
#     def my_innerFunc():
#         print(x+10)
#     my_innerFunc()
# myFunc()
# print(x)

# noinspection PyUnresolvedReferences
# import json
# x = {
#     "name": "John",
#     "age": 23,
#     "language": "Python"
# }
# y = json.dumps(x, indent=2, separators=(".", " = "), sort_keys=True)
# print(y)

# x = '{ "name": "John", "age": 23, "P_language": "Python" }'
