'''
CONDITIONALS STATEMENTS:
    They are programming structures which interrupt the normal flow of the program
    and help in executing certain lines of code based on conditions.

    There are different types of conditional statements in python
    they are:
    1.if statement
    2.if-else statement
    3.if-elif_elif...else statement

'''
#if statement
"""
'''
  It executes a block of code when the condition results in boolean True
  In case of False the condition goes to the next statement present after if

  syntax:
  if boolean:
     indented block of code

  Indentation:The space present at the beginning of the any line is called as indentation
  The standard practice is to provide one tab space
  All the lines enclosed as a block of code should be with the same indentation
'''
#Code:

n=int(input('enter a number: '))
if n>0:
    doubled_n=2*n
    print(doubled_n) 
print('completed')

"""
#2.if-else statement
"""
'''
It adds an alternate path to if conditional statement.
if the given condition results in boolean True,if block of code will be executed
if the given condition results in boolean False,else block of code will be executed

syntax:
if cond:
    if block
else:
    else block
'''
num=int(input())
if num>0:
    print("positive")
else:
    print("Negative")
"""
'''
name=input("Enter a name: ")
if name==name[::-1]:
    print((f"{name}it is a pallindrome"))
else:
    print("Not a pallindrome")
'''
'''
marks=eval(input())
s=input()
if s in marks:
    print(marks[s])
else:
    print("no")
'''
'''
bill=int(input())
dis=bool(int(input()))
if bill>2000:
    if dis:
        print("No Discount")
    else:
        print("10% Discount")
else:
    print("No Discount")
'''
'''
x=int(input())
if x%2 == 0:
    if x%4==0:
        print("Even and Divisible")
    else:
        print("even and not divisible")
else:
    print('not even')
'''
'''
ebill=350
bill=0
if ebill>100:
    ebill=ebill-100
    bill+=100*1
    if ebill>200:
        ebill=ebill-200
        bill+=200*2
        if ebill>0:
            bill+=ebill*3
print(bill)
'''
'''
units=int(input())
if units<=100:
    bill=units
if units>100 and units<=300:
    bill=100+(units-100)*2
if units>300:
    bill=500+(units-300)*3
print(bill)
'''

'''
total=int(input())
if total>20000:
    disc=total*(15/100)
    print(total-disc)
elif total>10000:
    disc=total*(10/100)
    print(total-disc)
elif total>5000:
    disc=total*(5/100)
    print(total-disc)
elif total>1000:
    disc=total-100
    print(total-disc)
else:
    print(total)
'''
'''
marks=int(input())
if marks>=90:
    print("Grade A")
elif marks>=80:
    print("Grade B")
elif marks>=70:
    print("Grade C")
elif marks>=60:
    print("Grade D")
else:
    print("Student has failed ")
'''

#program to print the largest of three numbers
a=int(input())
b=int(input())
c=int(input())
if a>b and a>c:
    print(f"{a} is the largest number")
elif b>a and b>c:
    print(f"{b} is the largest number")
else:
    print(f"{c} is the largest number")


