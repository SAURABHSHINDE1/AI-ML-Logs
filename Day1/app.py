
# day 1st first program 
print("hello its miii")


# variables in python 
# a variable is a container that stores data values.
a = 5
b = "hello"
c = 45.78
print(a)
print(b)
print(c)

# data types in python

# int
d = 20
print(type(d))

# float
e = 45.67
print(type(e))

# str
f = "saurabh"
print(type(f))

# bool also T and F are capitalized
# True and False
g = True
print(type(g))

# none type
h = None
print(type(h))



# keywords in python
# keywords are reserved words in python that have special meaning and cannot be used as variable names.
# some keywords are: if, else, elif, while, for, def, return, import, from, as, class, try, except, finally, with, lambda, pass, break, continue, global, nonlocal, assert, yield, raise, del, in, is, not, or, and.

# style guide
# use meaningful variable names. 
# # use snake_case for variable and function names. 
# most preferred style in python is snake_case.  
my_variable = 10
print(my_variable)

# use CamelCase for class names.

myVariableName = 20
print(myVariableName)


# pascal case for constants.
MY_Constant = 30
print(MY_Constant)


# operators in python
# operators are special symbols that perform operations on variables and values.
# arithmetic operators: +, -, *, /, %, //, **
x = 10
y = 3
print(x + y) # addition
print(x - y) # subtraction
print(x * y)  # multiplication
print(x / y) # division
print(x % y)  # modulus
print(x ** y)  # exponentiation


# Realational/comparison operators: ==, !=, >, <, >=, <=
print(x == y)  # equal to
print(x != y)  # not equal to
print(x > y)   # greater than
print(x < y)   # less than
print(x >= y)  # greater than or equal to
print(x <= y)  # less than or equal to

# assignment operators: =, +=, -=, *=, /=, %=, //=, **=
z = 5
z += 2  # z = z + 2
print(z)
z -= 2  # z = z - 2
print(z)
z *= 2  # z = z * 2
print(z)
z /= 2  # z = z / 2
print(z)
z %= 2  # z = z % 2
print(z)


# logical operators: and, or, not
print(x > 5 and y < 5)  # and
print(x > 5 or y > 5)   # or
ab = False
print(not ab)       # not


# operators precedence
'''
1. Parentheses ()
2. Exponentiation (**)
3. Multiplication (*), Division (/), Floor Division (//), Modulus (%)
4. Addition (+), Subtraction (-)
5. Relational/Comparison Operators (==, !=, >, <, >=, <=)
6. Logical Operators (and, or, not)

'''

# type conversion in python
# type conversion is the process of converting one data type to another.
# implicit type conversion
p = 10
q = 5.5
r = p + q  # p is converted to float
print(r)
print(type(r))
# explicit type conversion
s = "20"
t = int(s)  # str to int
print(t)
print(type(t))
u = float(s)  # str to float
print(u)
print(type(u))
v = str(p)  # int to str
print(v)
print(type(v))
w = str(q)  # float to str
print(w)
print(type(w))

# input in python
name = input("Enter your name: ")
print("Hello, " + name )

# int input
age = int(input("Enter your age: "))
print("You are " + str(age) + " years old.")

# float input
height = float(input("Enter your height in meters: "))
print("You are " + str(height) + " meters tall.")

# avrage of two numbers

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

avg = (num1 + num2) / 2

print("The average of is", avg)

# end of day 1st program