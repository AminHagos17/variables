#Amin Hagos
#16-09-2014
#Development Exercises - Task 3

height_inches = int(input("please enter your height in inches: "))
weight_stone = int(input("please enter your weight in stone: "))

height_cm = height_inches * 2.54
weight_kg = weight_stone * 6.364

print("your height converted from inches into centimetres is {0} and your weight coverted from stones into kilograms is {1}!".format(height_cm,weight_kg))
