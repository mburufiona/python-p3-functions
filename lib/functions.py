#!/usr/bin/env python3

def greet_programmer():
    print("Hello, programmer!")

greet_programmer()  

def greet(name):
    print(f"Hello, {name}!")

greet("Fiona")

def greet_with_default(name="programmer"):
    print(f"Hello, {name}!")

greet_with_default()

def add(num1=45, num2=55):
    return num1 + num2

add()


def halve(number):
    return number / 2

halve(10)
