# -*- coding: utf-8 -*-
"""calculator1python.py

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/12B0OffwCatNPuIsoagCzJjOpoYUMdYzi
"""



1class Calculator:

    def add( x, y):
        return x + y

    def subtract( x, y):
        return x - y

    def multiply( x, y):
        return x * y

    def divide( x, y):
        if y == 0:
            return "Error: Cannot divide by zero!"
        else:
            return x / y


a=int(input("enter the first number"))
b=int(input("enter the second number"))
print("a + b =", Calculator.add(a, b))
print("a - b =", Calculator.subtract(a, b))
print("a * b =", Calculator.multiply(a, b))
print("a / b =", Calculator.divide(a, b))