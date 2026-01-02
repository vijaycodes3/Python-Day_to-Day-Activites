''''''''''#Recursion:
"""
It is a programming technique where a function calls itself
to solve smaller instances of the same kind

Syntax:
def fun_name(par):
    base case
    recursive call

base case:
It tells where the recursive call should stop 
without base case,we get RecursionError which tells max recursion depth exceeded
recursive call:
function calls itself by passing some smaller arguments

Recursion is used when we need to back track in our problem.
A problem that can be solved using loops can be solved using recursion 
also but recursion technque stores all the function calls in a Stack which can be used for backtracking
"""'''
#printing python n times
'''def p(n):
    for i in range(n):
        print("python")
p(3)
def printing(n):
    if n==0:
        return
    print("python")
    printing(n-1)
printing(5)'''

#write a recursive function to find the sum of natural numbers till given n
'''def natural(n):
    if n==1:
        return 1
    return n + natural(n-1)
print(natural(100))'''

#write a program to print the factorial of  a given number
'''def fact(n):
    if n==1:
        return 1
    return n*fact(n-1)
print(fact(6))'''

#write a program to find the nth fibonacci term
#zeroth term and the first term of the series are 0,1 respectively
#every other term in the series is the sum of the two previous terms
#0,1,1,2,3,5,8'''''''
def fibonacci(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)
print(fibonacci(5))