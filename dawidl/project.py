###
# BMI Calculator
#
height = input('Enter your height in cm: ')
weight = input('Enter your weight in kg: ')
height = int(height)
weight = int(weight)
bmi = weight / (height/100)**2
bmi = round(bmi,2)
print('Your BMI is', bmi)
print('Check on the Internet if your BMI is ok!!')


###
# The program simulates five dice rolls.
#
import random
print("Dice rolling simulator")
for i in range(5):
    dice_roll = random.randint(1,6)
    print(dice_roll, end=" ")
    
    



# — dodawanie liczb; łączenie (konkatenacja) sekwencji (stringi, listy, tuple).
# — mnożenie liczb; powielanie sekwencji (np. string * n, list * n).
# ** — potęgowanie (x ** y = x do potęgi y).
# / — dzielenie rzeczywiste (zwraca float).
# // — dzielenie całkowite (floor division) — wynik zaokrąglony w dół do najbliższej liczby całkowitej.
# % — reszta z dzielenia (modulo).
# — porównanie większe (zwraca True/False).

# <= — porównanie mniejsze lub równe (zwraca True/False).

# # Dodawanie / konkatenacja
# 1 + 2           # 3
# "ab" + "cd"     # "abcd"
# [1,2] + [3]     # [1,2,3]

# # Mnożenie / powielanie
# 3 * 4           # 12
# "ab" * 3        # "ababab"
# [0] * 4         # [0,0,0,0]

# # Potęgowanie
# 2 ** 3          # 8

# # Dzielenie
# 7 / 2           # 3.5
# 7 // 2          # 3

# # Modulo
# 7 % 2           # 1

# # Porównania
# 5 > 3           # True
# 5 <= 5          # True


company = "ABC Data"
phone = "555-123-009"
employees = 25
remote_work = True
big_company = employees > 100
income = 4500000
income_per_person = income / employees

###
# A program that calculates the sum of two numbers.
# Modify the program to calculate the sum of three numbers.
#
number1 = 71
number2 = 14
number3 = 13
result = number1 + number2 + number3
print('Number 1: ', number1)
print('Number 2: ', number2)
print('Number 3: ', number3)
print('The result of summation: ', result)


###
# A program for swapping two varable values
#
x = 7
y = 34
z = 0 # additional, auxiliary variable
print("Before swapping: x=", x, "y=", y)

# swap the values
z = x
x = y
y = z

print("After swapping: x=", x, "y=", y)


###
# A program that, for a given speed in km/h,
# prints the speed in m/s
#
speed_kmh = 70
speed_ms = 70 * 0.2778
print(speed_kmh, "km/h = ", speed_ms, "m/s")


###
# A program that calculates the length of the diagonal
# of a rectangle with sides a and b.
#
import math
a = 5
b = 8
diagonal = math.sqrt(a**2 + b**2) 
print(diagonal)


##ludnosc

###
# A program that calculates and prints:
# - the number of people and percentage of the total
#   population living in the Northern Hemisphere
# - the number of people and percentage of the total
#   population living in the Southern Hemisphere
#
total = 8000000000
north = 7200000000
south = total - north
print("World population: ", total)
print("Northern Hemisphere: ", north)
print("Southern Hemisphere: ", south)
print("Northern Hemisphere in %: ", north/total*100)
print("Southern Hemisphere in %: ", south/total*100)

###
# A program that calculates and prints
# the average grade of a student
#
math = 5
art = 4
music = 5
history = 3
average = math + art - music + history / 4
print("Average grade is", average)


# ...existing code...
###
# Printing student's personal data
#
name = "Adam"
age = "18"
height = "180"
after = int(age) + 6

print(f"My name is {name}.")
print(f"I am {age} years old, and my height is {height} cm.")
print(f"In 6 years I will be {after} years old.")
# ...existing code...

###
# Write a program that calculates and prints
# the income of a family per person. To print the results
# in a readable form, use f-strings.
#
father_income = 5450
mother_income = 4920
family_members = 5
total_income = father_income + mother_income
income_per_person = total_income / family_members
print(f'Total family income is {total_income}, and income per person is {income_per_person}.')

a = 3
b = 5
print(f'{a}+{b}={a+b}')
print(f'{a}-{b}={a-b}')
print(f'{a}*{b}={a*b}')
print(f'{a}/{b}= {a/b}')  