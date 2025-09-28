                        # Day 02



                        # function 

"""

def welcome():
    print(f"Welcome to the world of function")

welcome()



def parameter(name):
    print(f"You write this {name} name.")

# parameter("Rakib")
parameter(input("Write your name: "))



def sum(a, b):
    a = int(a)
    b = int(b)
    print(f"{a} + {b} = {a+b}")

sum(input("Enter the first number: "), input("Enter the second number: "))



# work of default parameter

def default(a = "Rakib"):
    return a

print(f"Default = {default()}")

print(f"not default = {default('Shanto')}") 



# arguments

def student_info(name, roll, age):
    print(f"Name = {name}, \nRoll = {roll}, \nAge = {age}")

student_info(roll=3871, name='Rakib', age='25')




def add_all_numbers(*numbers):
    return sum(numbers)

print(f"Summation = {add_all_numbers(1, 2, 3, 4, 5)}")


# exercise

def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False
    
print(is_even(int(input("Enter a number: "))))

"""

# bonus exercise

def add_list(num):
    # return print(max(num))
    l = len(add_list)
    

# print(add_list([1,2,3,4,5]))
add_list(list(map(int, input('Enter a list of numbers seperated by commas: ').split(','))))

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