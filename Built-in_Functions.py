"""

1️⃣ Basic Operators (built-in)
Operator	Example	Result
+	5 + 3	8
-	5 - 3	2
*	5 * 3	15
/	5 / 2	2.5
//	5 // 2	2 (floor division)
%	5 % 2	1 (remainder)
**	5 ** 2	25 (power)


2️⃣ Built-in Functions

abs(x) → absolute value

round(x, n) → round to n decimals

pow(x, y) → x raised to the power y (same as x**y)

print(abs(-10))     # 10
print(round(3.1415, 2))  # 3.14
print(pow(2, 3))    # 8


3️⃣ math Module Functions
import math
print(math.sqrt(16))     # 4.0
print(math.ceil(4.2))    # 5
print(math.floor(4.8))   # 4
print(math.factorial(5)) # 120
print(math.log(10))      # natural log
print(math.sin(math.pi/2))  # 1.0


sqrt(x) → square root

ceil(x) → smallest integer ≥ x

floor(x) → largest integer ≤ x

factorial(x) → x!

log(x) → natural log

sin(x), cos(x), tan(x) → trigonometry


✅ Built-in max() and min()

On numbers directly

print(max(10, 5, 20))  # 20
print(min(10, 5, 20))  # 5


On a list or tuple

nums = [4, 8, 1, 9, 2]
print(max(nums))  # 9
print(min(nums))  # 1

tup = (10, 15, 5)
print(max(tup))  # 15
print(min(tup))  # 5


With strings (compares alphabetically)

words = ["apple", "banana", "cherry"]
print(max(words))  # cherry
print(min(words))  # apple


"""