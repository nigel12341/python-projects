import math
import time


op = ""
num1 = ""
num2 = ""
name = ""
path = './name.txt'

if name == "":
    print("Welcome, please enter your name")
    name = input("")
    file = open("name.txt", "w")
    file.write(name)
    file.close()


def calc():
    file = open("name.txt", "r")
    print("welcome", name, "to advanced calculator")
    print("first select the operation: +, *, -, power, squareroot, tan, areacircle, pythagorean, rectvol")
    op = input("")
    if op == "+":
        print("now select value 1")
        num1 = int(input())
        print("now select value 2")
        num2 = int(input())
        print(num1 + num2)
        time.sleep(5)
        calc()
    elif op == "*":
        print("now select value 1")
        num1 = int(input())
        print("now select value 2")
        num2 = int(input())
        print(num1 * num2)
        time.sleep(5)
        calc()
    elif op == "*":
        print("now select value 1")
        num1 = int(input())
        print("now select value 2")
        num2 = int(input())
        print(num1 * num2)
        time.sleep(5)
        calc()
    elif op == "-":
        print("now select value 1")
        num1 = int(input())
        print("now select value 2")
        num2 = int(input())
        print(num1 - num2)
        time.sleep(5)
        calc()
    elif op == "power":
        print("now select value 1")
        num1 = int(input())
        print("now select value 2")
        num2 = int(input())
        print(math.pow(num1, num2))
        time.sleep(5)
        calc()
    elif op == "squareroot":
        print("now select value 1")
        num1 = int(input())
        print(math.sqrt(num1))
        time.sleep(5)
        calc()
    elif op == "tan":
        print("now select value 1")
        num1 = int(input())
        print(math.tan(num1))
        time.sleep(5)
        calc()
    elif op == "pi":
        print(math.pi)
        time.sleep(5)
        calc()
    elif op == "areacircle":
        print("now select value 1")
        num1 = int(input())
        print(math.pi*num1*num1)
        time.sleep(5)
        calc()
    elif op == "pythagorean":
        print("now select value 1")
        num1 = int(input())
        print("now select value 2")
        num2 = int(input())
        num1_ = math.pow(num1, 2)
        num2_ = math.pow(num2, 2)
        step2 = num1_ + num2_
        print(math.sqrt(step2))
        time.sleep(5)
        calc()
    elif op == "rectvol":
        print("now select value 1")
        num1 = int(input())
        print("now select value 2")
        num2 = int(input())
        print("Now select value 3")
        num3 = int(input())
        print(num1 * num2 * num3)
        time.sleep(5)
        calc()
    else:
        print("Error")

calc()
