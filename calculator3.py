Python 3.14.8 (tags/v3.14.8:8e6e75d, Sep 30 2026, 18:19:33) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.

while True:
    print("======== SIMPLE CALCULATOR ========")

    a = float(input("Enter the first number: "))
    o1 = input("Enter the first operator (+, -, *, /, **, %): ")
    b = float(input("Enter the second number: "))
    o2 = input("Enter the second operator (+, -, *, /, **, %): ")
...     c = float(input("Enter the third number: "))
... 
...     if o1 == "+":
...         x = a + b
...     elif o1 == "-":
...         x = a - b
...     elif o1 == "*":
...         x = a * b
...     elif o1 == "/":
...         x = a / b if b != 0 else None
...     elif o1 == "**":
...         x = a ** b
...     elif o1 == "%":
...         x = a % b if b != 0 else None
...     else:
...         print("Invalid first operator!")
...         x = None
... 
...     if x is not None:
...         if o2 == "+":
...             result = x + c
...         elif o2 == "-":
...             result = x - c
...         elif o2 == "*":
...             result = x * c
...         elif o2 == "/":
...             result = x / c if c != 0 else None
...         elif o2 == "**":
...             result = x ** c
...         elif o2 == "%":
...             result = x % c if c != 0 else None
...         else:
...             print("Invalid second operator!")
...             result = None
... 
...         if result is not None:
...             print("Result =", result)
... 
...     choice = input("Do you want to calculate again? (yes/no): ")
... 
...     if choice.lower() != "yes":
...         print("Calculator closed. Thank you!")
...         break
