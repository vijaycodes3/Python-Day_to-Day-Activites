#while loop
'''
It is a condition based loop
The loop runs  until the given condition is true
sytax:
while condition:
    with indentation the block of code
Initialization of a variable and updating that variable inside the loop 
are necessary fo the working of while loop
it leads to an infinite loop if the variable is not updated inside the loop body

i=0
while i<3:
    print('Hello World!')
    i+=1
'''
'''
n1=int(input())
i=1
s=0
while i<n1+1:
    s+=i
    i+=1
print(s)
'''
'''
#program to find the factorial of a given number
n=5
total=1
i=1
while i<=n:
    total*=i
    i+=1

print(total)

m=5
total1=1
i=m
while i>=1:
    total1*=i
    i-=1
print(total1)

#print each element present in the given list,in a new line
l=[1,2,3,4,5]
a=l[0]
while a in l:
    print(a)
    a+=1
i=0
s=0
n=len(l)
while i<n:
    print(l[i])
    s+=l[i]
    i+=1
print(s)
'''

#find the sum of the digits present in the given integer input
#123=1+2+3=6
#123%10=3
#123//10=12
'''start=0
n=123
while n>0:
    a=n%10
    start+=a
    n//=10
print(start)
'''










