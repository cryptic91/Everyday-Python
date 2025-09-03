                        # Day 01



                        # basic 

# Data types: int, float, str, bool, list, tuple, dict, set
# Type casting: int(), float(), str()
# Basic operators: + - * / // % **
# Comparison & logical operators: == != > < >= <= and or not

"""
name = "Rakib"
age = 25
height = 1.75

# print('Name: ',name,'\n','Height: ',height,'\n','Age: ',age)
print(f"Name: {name}\nAge: {age}\nHeight: {height}")       # It's better

"""

                        # list (changeable)

"""
fruits = ['apple', 'mango', 'jackfruit']
print(fruits)

fruits.append('orange')
print(fruits)

fruits[0] = "guava"
print(fruits)

"""

                        # tuple (unchangeable)

"""                        
colors = ('red', 'green', 'yellow')
print(colors)
print(colors[2])

"""

                        # Dictionaries

"""
personal_info = {
    "name" : "Rakib",
    "age" : 25,
    "working python" : True,
}

print(personal_info["working python"])

print(f"before -> {personal_info['name']}")
personal_info["name"] = "Rakibul"
print(f"after  -> {personal_info['name']}")

"""


                        # conditions

"""

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a>b:
    if a>c:
        print(f"{a} is the biggest number!")
    else:
        print(f"{c} is the biggest number!")
elif b>a:
    if b>c:
        print(f"{b} is the biggest number!")
    else:
        print(f"{c} is the biggest number!")
else:
    print(f"something is happening wrong!!!")

"""


                        # loop 

"""

rolls = [1, 2, 3, 4, 5, 6]

for roll in rolls:
    print(f"{roll}")


i = 1
while i <= 5: 
    print(f"{i}")
    i += 1


print("Sum of 1 to 20 numbers: ")
j = 1
sum = 0
while j<=20:
    sum += j
    j += 1
print(f"{sum}") 


start = int(input("Input the starting number: "))
end = int(input("Input the ending number: "))
r = end - start
s = 0

for a in range(start, end+1):
    s += a
print(s)


print('count 3 from 0')
for x in range (3):
    print(x)

print('number from 1 to 4')
for x in range (1, 5):
    print(x)

print('odd number')
for x in range (1 , 10, 2):
    print(x)

print('printing reverse')
for x in range (10 , 0, -1):
    print(x)


"""


                        # input 

"""

age = int(input("Enter your age: "))
print(age)

height = input("Enter your height: ")
print(height)
print(type(height))
height = float(height)
print(height)
print(type(height))

num1, num2 = map(int, input("Enter two number with a space between them: ").split())
print('numbers are', num1, '&', num2)
print(f"Summation = {num1+num2}")

"""



                        # loop 

# """



# """


                        # loop 

# """



# """


                        # loop 

# """



# """

# echo "# Everyday-Python" >> README.md
# git init
# git add README.md
# git commit -m "first commit"
# git branch -M main
# git remote add origin https://github.com/cryptic91/Everyday-Python.git
# git push -u origin main


# git remote add origin https://github.com/cryptic91/Everyday-Python.git
# git branch -M main
# git push -u origin main