'''FUNCTION:-
A Function is a reusable block of code to do a specific task

Syntax of defining a function:

def fun_name():
        block of code with intention
        return obj

def - keyword used to define function
fun_name can be anything following naming convention
parameters - variables used for passing  values to the func
return - keyword used to be return a value from the function
to the point where it was called
NOTE:-
Function definition will not execute the function body.
Function call will execute the function body
 Syntax for function call:
fun_name(arg1,arg2,arg3,...)
During func cll ,We use the values to the parameters and these
actual values are called as arguments.

return statement in any function is optional . None will be returned
dy de…
'''

def greet(name):
    print("Hello", name)

greet("Vijay")
greet("Python")







'''
Arguments:-
Arguments are the actual values passed to parameters
There are different ways to pass arguments.
1.Positional arguments
2.Default arguments
3.Keyword arguments

#positional arguments.
Arguments are passed with the help of positions of parameters order has to be necessarily followed
Arguments are passed while making the function call

def info(batch, subject):
    print(f'Batch: {batch}')
    print(f'Subject:{subject}')
info('PFS-43','Python')


#Default arguments:-

#Arguments will be passed during function definition only if we pass any arguments
during function call, the defaults will be over written by the passed values

#There can be a combination of default and non default arguments Defaults
should always come after non
default parameters.

def info(batch ,subject = 'python'):
    print(f'Batch:{batch}')
    print(f'Subject:{subject}')
info('PFS')

#Keyword Arguments:-
We pass arguments while making function call
To pass arguments, we use the names of the functions
Order of parameters need not be followed while passing args

#def info(batch, subject):
    print(f'Batch: {batch}')
    print(f'Subject:{subject}')
info(subject = 'Python',batch = 'PFS-43')

Scope of a variable:
It refers to the part of the program where a variable can be accessed.
There are mainly two types of scope.
1.Local scope:
    If a variable is defined inside a function, it is said to exist in local scope
It cannot be accessed outside the function
2.Global scope:
    If a variable is defined outside of every function and usually at the top, it is said
    to exist in global scope
    It can be reterived every where in the program but to update we need to mention that
    it is a global variable using global keyword.

###
b = 5
def example():
    global b
    print(b)
    b += 10
    a =10
    print(a)
example()
print(b)
###
Passing mutable and immutable objects to funs:
In case of mutable objects, the changes made exist outside
the fun, whose behaviour is similar to pass by value
###
def modify (a):
    print(f'Inside fun before modi: {a}')
    a += 10
    print(f'Inside fun after modi: {a}')
num = 10
modify(num)
print(num)
###
def modify(l):
    print(l)
    l.append(10)
    print(l)
lst = [1,2]
modify(lst)
print(lst)
'''
'''
Variable length arguments:-

In this case,A function accepts any number of arguments during function call

1.Variable length positional arguments.
we use * operator to pack all the arguments into a tuple with the name following the * operator

2.variable length keyword arguments
we use ** operator to pack all the arguments into a dictionary with the name following the ** operator

'''
'''
def example(*args):
    for i in args:
        print(i)
example(1)
print()
example(1,2,3,4,5)
'''
'''
def example(**kwargs):
    print(type(kwargs))
    for i in kwargs:
        print(i,kwargs[i])
example(name='Bob',place='Hyderabad')
print()
example(name='Bob',place='Hyderabad',phone=9876543210)'''
#write a function that accepts any number of integers as arguments and calculate the average of those integers
'''def average_calculator(*args):
    total=0
    length=0
    for i in args:
        total+=i
        length+=1
    avg=total//length
    print(avg)
average_calculator(1,2,3,4,5,6)'''
#write a function bill_calculator() that takes two details of any number of products(product name and price),
#prints the bill in a formatted way with individual prices and total price
'''def bill_calculator(**kwargs):
    t=0
    for i in kwargs:
        t+=kwargs[i]
        print(i,kwargs[i])
    print(t)
bill_calculator(shoe=1000,shirt=2000)

def bc(**details):
    bill=0
    i=1
    for key,value in details.items():
        print(f'{key}-{value}')
        bill+=value
        i+=1
    print(f"Total:{bill}")
bc(shoe=1000,shirt=3000,pant=9876)
'''













