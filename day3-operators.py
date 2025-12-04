'''
operators: operators are either special symbols or reserved words used to operate on operands.
in python,these are the different types of operators.
1.arthmetic
2.relational
3.logical
4.membership
5.identity
6.assignment
7.bitwise operators
'''
#1.Arithmetic operators
'''
these are special symbols
+ --addition
- --subtraction
* --multiplication
/ --division
//--floor division
% -- modulus
** --exponentiation
'''
'''
a=90
b=50
c=a+b # 90+50
print(c)
'''
#input is a function used to take input from the user
a=int(input('enter first number:'))
b=int(input('enter second number:'))
print('addition:',a+b)
print('subtraction:',a-b)
print('multiple:',a*b)
print('division:',a/b)
print('modulus:',a%b)
print('floor division:',a//b)
print('exponentiation:',a**b)

##2.Relational operators:
'''
these are special symbols
they always return boolean values based on the comparision made
> --greater than
< --less than
>= -- greater than or equal to
<= --less than or equal to
== --equal to
!= --not equal to '''
x=int(input("enter a number:"))
y=int(input("enter a number:"))
print(x>y)
print(x<y)
print(x>=y)
print(x<=y)
print(x==y)
print(x!=y)

''' A person should work for min of 5 hrs a day.His clock stores the time he worked as seconds.
check out whether the requirement is satisfied for the given day.
output should be true or false
input: one line which is seconds in his clock
'''
sec=int(input("enter seconds:"))
hrs_sec=5*60*60
print(sec >= hrs_sec)

'''Two lines of input are given .check whether the second number is a square root of first number'''
a=25
b=5
print(a**1//)

#Logical Operators
'''
and: True if both operands are truthy; returns the first falsy operand or the last value if all truthy.

or: True if any operand is truthy; returns the first truthy operand or the last value if all falsy.

not: Unary operator; returns True if operand is falsy, otherwise False.

Notes on truthiness: 0, 0.0, '', None, [], {}, (), and False are considered falsy. Everything else is truthy.

Short-circuiting:

In a and b, if a is falsy, b is not evaluated and a is returned.

In a or b, if a is truthy, b is not evaluated and a is returned.
'''
#4.Membership operators
'''
in: Checks whether a value is a member of a container (strings, lists, tuples, sets, dict keys). Returns boolean.

not in: Negation of in.

Examples:

'x' in 'xyz' → True

3 in [1,2,3] → True

'key' in {'key': 1} → True (checks keys)
'''

#5.Identity Operators
'''
is: True if two references point to the same object (same memory id).

is not: Negation of is.

Important: is checks identity, not value equality. Use == to compare values, is when you need to check None or identical singletons.

Recommended pattern for None-check: if x is None: (preferred over if x == None:)
'''
'''
Logical operators
print('Logical operators:')
print( True and False ) # False
print( 0 or 'fallback' ) # 'fallback' (first truthy or last)
print( [] and 'no' ) # [] (falsy returned)
print( not 0 ) # True


# Membership
print('\nMembership:')
print('a' in 'cat') # True
print(3 in [1,2,3]) # True
print('k' not in {'k':1}) # False (k is a key)


# Identity
print('\nIdentity:')
a = [1,2,3]
b = a
c = [1,2,3]
print(a is b) # True (same object)
print(a is c) # False (different objects with same contents)
print(a == c) # True (values equal)


# Use is for None checks
x = None
print(x is None) # True
'''

#6.Assignment Operators
'''

Assignment operators are used to assign values to variables. Python supports both simple and compound assignment operators.

Basic Assignment

a = b → Assigns value of b to a.

Compound Assignment Operators

These operators perform an operation and then assign the result back to the variable.

Operator	Meaning	Example	Equivalent To
+=	Add and assign	x += 5	x = x + 5
-=	Subtract and assign	x -= 2	x = x - 2
*=	Multiply and assign	x *= 3	x = x * 3
/=	Divide and assign	x /= 2	x = x / 2
//=	Floor-divide and assign	x //= 2	x = x // 2
%=	Modulo and assign	x %= 3	x = x % 3
**=	Exponent and assign	x **= 2	x = x ** 2
&=	Bitwise AND and assign	x &= y	x = x & y
`	=`	Bitwise OR and assign	`x	= y`	`x = x	y`
^=	Bitwise XOR and assign	x ^= y	x = x ^ y
<<=	Left-shift and assign	x <<= 1	x = x << 1
>>=	Right-shift and assign	x >>= 1	x = x >> 1

Examples
x = 10
x += 5 # 15
x *= 2 # 30
x -= 4 # 26
x //= 3 # 8
x **= 2 # 64
'''

#7.Bitwise Operators
'''
These are usedfor bit level operations

these are symbols

&  - bitwise and
|  - bitwise or
^  - bitwise xor
~  - bitwise not
>> - right shift
<< - left shift
'''
'''
1.bitwise and:

It works similar to logical and
it compares bits at specific positions in both the operands
and decides what should be the position in the resultant
if both the bits are 1 then the resultatant will be 1 ,else 0
'''
a=5#0101
b=3#0011
#0001
print(a & b)

'''
2.bitwise or:

In the resultant,the bit at any specific  position will be 1 if any of the two bits
number consideration are 1, else 0
'''
x=5
y=3
print(x | y)
'''
3.bitwise XOR:

if the both bits are different then it will be 1,else 0

'''
v=5
u=6
print(v ^ u)
'''
4.bitwise not:

This is an unary operator
It inverses the bits present in the number

~n= -n-1
'''
aa=6
print(~aa)
print(~-5)
'''
5.leftshift (<<)
'''
q=100
print(q<<1)#a*2^n
print(q<<5)#a*2^n

'''
6.rightshift
this operator is used to move all the bits to right by given number of positions
the result of a >> n will be a // 2^n
'''
p=100
print(p>>3)