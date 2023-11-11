from divide import divide
import random

print("Hello World!")

# Other type casting methods are:
# 1) ord(): Which returns an integer that represents the underlining unicode character.
print(ord("r"))
print(type(ord("r")))
# returns 114 and int

# 2) hex(): Which converts the given integer to an hexidecimal string.
print(hex(456))
print(type(hex(456)))
# returns 0x1c8 and str

# 2) oct(): Which converts the given integer to a string that represents the octane number.
print(oct(456))
print(type(oct(456)))
# returns 0x1c8 and str

# DIFFERENT METHODS OF PRINTING VALUES
# 1) Basic print
print("Boy")
# It outputs "Boy on the CLI"

# 2) If a sep argument is included
print(2, 3, sep=", ")
# It outputs "2, 3"

# 3) Direct formating is allowed inside the print statement
name = input("Enter your name: ")
print("My name is {}.".format(name))
# It outputs "My name is {name}"

# 4) Multiple arguments
print(2, 3)
# It outputs "2 3"


# there is an isinstance function that takes in two arguments and checks where the first argument is of the type written in the second argument.
# it returns true or false.
print(isinstance(45, int))
# returns True

# the round function takes two arguments. The first argument is the variable or calculation you want to round. The second argument is the number of decimal places.
print(round(34.34/7, 2))
# returns 4.91

# types of variable scope(LEGB)
# 1. Local Scope
# 2. Enclosing Scope
# 3. Global Scope: Variables in global scope are accessible anywhere in the code.
# 4. Builtin Scope
# A practice can be shown below:
# Assign a global variable
global_variable = 10

# create a function that adds local variable to global variable


def add_global_to_local():
    # assign a local variable
    local_variable = 5
    return global_variable + local_variable


# create a function that check the scope of a variable
def check_variable_scope(variable_name):
    # assigns enclosed_variable to value of the variable_name
    enclosed_variable = variable_name
    # a function that checks the type of variable with a local_variable that differentiates enclosed_variable and local_variable.

    def check_variable(local_variable=False):
        # checks if check_variable is a global variable
        if enclosed_variable in globals():
            return "{} is a global variable".format(variable_name)
        # checks if a variable is an enclosed variable
        if enclosed_variable in locals() and local_variable:
            return "{} is an enclosed variable".format(variable_name)
        # checks if a variable is a local variable
        elif enclosed_variable in locals():
            return "{} is a local variable".format(variable_name)
    # Controls the flow by assigning local_variable=True if the variable is already a local variable
    if enclosed_variable in locals():
        return check_variable(local_variable=True)
    return check_variable()


# checks what type of variable scope does global variable belong to.
print(check_variable_scope("global_variable"))
# returns global_variable is a global variable

# checks what type of variable scope does local_variable belong to.
print(check_variable_scope("local_variable"))
# returns local_variable is a local variable

# checks what type of variable does enclosed_varaible belong to.
print(check_variable_scope("enclosed_variable"))
# returns variable_name is an enclosed variable

# Data structures in python can be divided into:
# 1. Built-in data structures:
# a. List
# b. Tuple
# c. String
# d. Dictionary
# e. Set
# f. Integer

# 2. User-Defined data structures:
# a. Stack
# b. Tree
# c. Graph
# d. Queue
# e. Linked List
# f. HashMap

# LIST
mixed_list = ["Akachukwu", "is", "a", "king"]
# print all the items in the list
print(*mixed_list)
# returns Akachukwu is a king
mixed_list.insert(3, "good")
print(mixed_list)
# returns ['Akachukwu', 'is', 'a', 'good', 'king']
mixed_list.extend(["but", "he", "loves", "playing", "."])
print(mixed_list)
# returns ['Akachukwu', 'is', 'a', 'good', 'king', 'but', 'he', 'loves', 'playing', '.']

# TUPLE
mixed_tuple = tuple(mixed_list)
print(mixed_tuple.count("."))
# returns 1

# SET
set_1 = {1, 2, 3, 4}
set_2 = {2, 4, 5, 6}
print(set_1.union(set_2))  # return {1, 2, 3, 4, 5, 6}
print(set_1 | set_2)  # return {1, 2, 3, 4, 5, 6}
print(set_1.intersection(set_2))  # return {2, 4}
print(set_1 & set_2)  # return {2, 4}
print(set_1.difference(set_2))  # return {1, 3}
print(set_1 - set_2)  # return {1, 3}
print(set_1.symmetric_difference(set_2))  # return {1, 3, 5, 6}
print(set_1 ^ set_2)  # return {1, 3, 5, 6}

# DICTIONARY
my_dict = {"name": "Chukwumam Akachukwu David", "age": 21, "class": "year 4"}
for key, value in my_dict.items():
    print(key, value, sep=": ")

# Args and Kwargs
# *args can be used to receive any amount of non-keyword arguments.


def sum_of(*args):
    sum = 0
    for x in args:
        sum += x
    return sum


print(sum_of(5, 3, 4, 6, 7, 5, 3, 2))  # returns 35

# *kwargs is similar to a dictionary and can be used to receive any amount of keyword arguments.


def sum_of(**kwargs):
    sum = 0
    for k, v in kwargs.items():
        sum += v
    return sum


print(sum_of(shoe=12500, trouser=5000, shirt=2500))  # returns 20000

# For Error and Exception check the divide module

# Fuck it I started working with classes
division = divide("Basic division", "divide", "basic")
print(division.divide_numbers())
print(division)

# managing files
# This is a method of writing files using the with statement
with open("introduce.txt", "w") as file:
    file.write("This is the introduction line. \nMy name is Chukwumam Akachukwu David. \nI am a boy.\nI am 21 years old. \nI love Reahanat Chukwumam. \nThis is another line. \n")

# This is a method of reading files  There are other methods like read() and readline().
# read() reads the whole file from last stop to the end while read line reads only a line of the file.
file = open("introduce.txt", "r+")
for line in file.readlines():
    new_line = line.replace("\n", "")
    print(new_line)
file.write("This is the introduction line. \nMy name is Chukwumam Akachukwu David. \nI am a boy.\nI am 21 years old. \nI love Reahanat Chukwumam. \nThis is another line. \nI rewrote the whole introduction because the pointer has shifted to the end of the file so it appears twice. \n")
print(file.read(40)) # write the first 40 characters in the file.
file.close()

# To add more lines to an existing file use a instead of w when opening the file.
# writelines writes a list or takes a list as input to be written in the file
try:
    file = open("introduce.txt", "a")
    file.writelines(["I am a done writing.\n", "Are you sure I am done?\n",
                    "I don't think I am done\n", "Ok now I am done writing.\n"])
    file.close()
except FileNotFoundError as e:
    print(e)

# readlines converts the lines to a list.
file = open("introduce.txt", "r")
print(file.readline(10)) # write the first 10 characters in the first line
file.readline()
body = file.readlines()
print(len(body))
print(random.choice(body))
file.close()
