'''dict
a={'a':1,'b':2}
b=str(a)
print(str(a))
print(list(a))
print(tuple(a))
print(set(a))
print(bool(a))
'''


lst=[[1,2],[2,3]]
print(dict(lst))
lst1=[1,2,34,34]
#print(dict(lst1))
"""
🔷 What is Type Conversion?
Type conversion means changing one data type into another.

Example:

x = "10"     # string
y = int(x)   # integer
print(y + 5) # 15
Without conversion:

"10" + 5   # ❌ ERROR
🔷 Why Type Conversion is Needed (Real Life)
🧠 Real-world thinking
User input → always string

File data → string

API response → string / JSON

Environment variables → string

👉 But calculations need numbers

So we convert.

🔷 Types of Type Conversion
1️⃣ Implicit Type Conversion (Automatic)
Python converts smaller → larger type automatically.

a = 10       # int
b = 2.5      # float

c = a + b    # int → float
print(c)     # 12.5
📌 Rule:

int → float → complex
❌ Python will NOT do unsafe conversion:

"10" + 5   # ERROR
2️⃣ Explicit Type Conversion (Type Casting)
Programmer manually converts type.

Common functions:
Function	Converts to
int()	Integer
float()	Float
str()	String
bool()	Boolean
list()	List
tuple()	Tuple
set()	Set
dict()	Dictionary
🔷 int() Conversion (Most Important)
int("10")      # 10
int(10.7)      # 10 (decimal removed)
❌ Invalid:

int("10.5")    # ERROR
int("abc")     # ERROR
Real-world use:
age = int(input("Enter age: "))
🔷 float() Conversion
float("10")     # 10.0
float(5)        # 5.0
❌ Invalid:

float("abc")
🔷 str() Conversion (Very Common)
x = 100
print("Value is " + str(x))
Real-world:
Logging

Printing messages

Writing to files

🔷 bool() Conversion (INTERVIEW FAVORITE ⭐)
Truthy & Falsy Values
bool(0)        # False
bool(1)        # True
bool("")       # False
bool("python") # True
bool([])       # False
bool([1])      # True
📌 Rule:

Empty → False

Zero → False

None → False

Everything else → True

🔷 list(), tuple(), set() Conversion
String → List
list("abc")   # ['a','b','c']
List → Tuple
tuple([1,2,3])
List → Set (remove duplicates)
set([1,2,2,3])
🔷 dict() Conversion
From list of tuples
dict([("a",1),("b",2)])
Real-world:
Database results

API responses

🔷 REAL-WORLD USE CASES 🔥
1️⃣ User Input Calculator
a = int(input("Enter a: "))
b = int(input("Enter b: "))
print(a + b)
2️⃣ File Data Processing
line = "100"
price = int(line)
total = price * 5
3️⃣ Environment Variables (DevOps ⭐)
import os
port = int(os.getenv("PORT", 8080))
4️⃣ API / JSON Handling
import json

data = '{"age": "25"}'
obj = json.loads(data)

age = int(obj["age"])
5️⃣ Boolean Flags (Feature Toggle)
DEBUG = bool(int(os.getenv("DEBUG", 0)))
🔷 COMMON ERRORS (INTERVIEW TRAPS ⚠️)
❌ ValueError
int("abc")
❌ TypeError
"10" + 5
❌ Logical error
bool("False")  # True 😱
✔ Correct way:

flag = "False"
flag = flag.lower() == "true"
🔷 INTERVIEW QUESTIONS & ANSWERS
❓ What is type conversion?
👉 Changing one data type to another.

❓ Difference between implicit and explicit conversion?
Implicit	Explicit
Automatic	Manual
Safe	Programmer controlled
❓ Why input() returns string?
👉 To avoid unsafe automatic conversion.

❓ What is type casting?
👉 Manual type conversion using functions.

❓ Can int() convert float?
👉 Yes, decimal part is removed.

❓ What values are False in bool()?
👉 0, 0.0, "", [], (), {}, None

❓ Is bool("False") False?
👉 ❌ No, it's True.

❓ Why Python doesn’t auto convert string to int?
👉 To avoid ambiguity and runtime bugs.

❓ Can we convert list to dict?
👉 Yes, if elements are key-value pairs.

❓ Which type conversion is risky?
👉 String → number (can cause ValueError)

❓ How to safely convert?
try:
    x = int(s)
except ValueError:
    x = 0
"""