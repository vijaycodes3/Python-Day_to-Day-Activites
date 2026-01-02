'''
n=int(input())
for i in range(n):
    print('*'*n)

l=int(input())
b=int(input())
for i in range(b):
    print('*'*l)
'''
'''
n=int(input())
for i in range(n):
    if i==0 or i==n-1:
        print("*"*n)
    else:
        print("*"+" "*(n-2)+"*")
r=int(input())
c=int(input())
for i in range(r):
    for j in range(c):
        if i==0 or i==r-1 or j==0 or j==c-1:
            print("*",end="")
        else:
            print(" ",end="")
    print()'''
'''
a=int(input())
for i in range(a):
    for j in range(i+1):
        if i==0 or i==a-1 or j==0 or j==i:
            print("*",end="")
        else:
            print(" ",end="")
    print()
'''
"""v=int(input())
for i in range(v):
    for j in range(i+1):
        if i==j or i==v-1 or j==0 or j==i:
            print("*",end="")
        else:
            print(" ",end="")
    print()"""

'''
a=[1,2,3,4,5]
for i in range(len(a)):
    print(f"index {i}: {a[i]}")
'''
'''
v=int(input())
for i in range(v):
    for j in range(i+1):
        if i==j or i==v-1 or j==0 or j==i:
            print("*",end="")
        else:
            print(" ",end="")
    print()
'''
'''
inp=int(input())
for i in range(inp):
        print((" "*i)+"*"*(inp-i))
'''
'''
n1=int(input())
a=n1//2
for i in range(0,n1):
    if i==a:
        print("*"*n1)
    else:
        print("*"+" "*(n1-2)+"*")

n2=int(input())
for i in range(1,n2+1):
    print("*"*i+" "*(n2+1))
'''
'''
n3=int(input())
for i in range(n3+1):
    print(str(i)*i)
'''
'''
n4=int(input())
for i in range(1,n4+1):
    row=''
    for j in range(1,i+1):
        row+=str(j)
    print(row)
'''
'''
n4=int(input())
for i in range(1,n4+1):
    row=''
    for j in range(1,i+1):
        row+=chr(96+i)
    print(row)
'''
"""n6=int(input())
for i in range(1,n6+1):
    print(" "*(n6-i)+"* "*i)
for i in range(n6):
    print("* "*n6)"""
"""for i in range(1,n6+1):
    print(" "*i+"* "*(n6-i)+" "*i)"""
  





'''
#Right sided triangle(Decreasing space,Increasing star)
n=5
for i in range(n):
    for j in range(i,n):
        print(' ',end=' ')
    for j in range(i+1):
        print('*',end=' ')
    print()

#left sided triangle(increasing space,decreasing star)
n=5
for i in range(n):
    for j in range(i+1):
        print(" ",end=' ')
    for j in range(i,n):
        print("*",end=" ")
    print()'''
#increasing triangle pattern
"""n=5
for i in range(n):
    for j in range(i+1):
        print("*",end=' ')
    print()"""
#decreasing triangle pattern
"""n=5
for i in range(n):
    for j in range(i,n):
        print("*",end=" ")
    print()"""
#hill pattern
"""n=5
for i in range(n-1):
    for j in range(i,n):
        print(" ",end=' ')
    for j in range(i+1):
        print("*",end=' ')
    for j in range(i):
        print("*",end=" ")
    print()"""
#reverse hill pattern
"""n=5
for i in range(n):
    for j in range(i+1):
        print(" ",end=" ")
    for j in range(i,n-1):
        print("*",end=" ")
    for j in range(i,n):
        print("*",end=" ")
    print()"""
#1 12 123 1234 12345 
'''n=int(input())
for i in range(1,n+1):
    for j in range(i):
        print(j+1,end="")
    print()
'''

#12345 1234 123 12 1
'''n=int(input())
for i in range(n):
    for j in range(n-i):
        print(j+1,end="")
    print()'''
#A AB ABC ABCD ABCDE
'''n=int(input())
for i in range(1,n+1):
    for j in range(i):
        print(chr(65+j)+' ',end='')
    print()'''

#ABCDE ABCD ABC AB A
'''n=int(input())
for i in range(n):
    for j in range(n-i):
        print(chr(65+j)+'',end="")
    print()'''
#A
#A B 
#A B C
#A B
#A
'''n=int(input())
for i in range(1,n+1):
    for j in range(i):
        print(chr(65+j)+' ',end='')
    print()
for i in range(1,n+1):
    for j in range(n-i):
        print(chr(65+j)+' ',end='')
    print()'''


#     A
#   A   B
# A   B   C
#A  B   C   D
'''n=int(input())
for i in range(n):
    print(" "*(n-i-1),end='')
    for j in range(i+1):
        print(chr(65+j)+"",end=' ')
    print()'''

'''n=int(input())
for i in range(n):
    print(" "*i,end="")
    for j in range(n-i):
        print(chr(65+j)+'',end=" ")
    print()
'''
'''    A B C D E
        A B C D
         A B C
          A B
           A
           A 
          A B
         A B C
        A B C D
       A B C D E
'''
'''n=int(input())
for i in range(n):
    print(" "*i,end="")
    for j in range(n-i):
        print(chr(65+j),end=" ")
    print()
for i in range(n-1):
    print(" "*(n-i-1),end='')
    for j in range(i+1):
        print(chr(65+j),end=" ")
    print()'''
'''
   D
  D C
 D C B
D C B A
'''
'''n=int(input())
for i in range(n):
    print(' '*(n-i-1),end='')
    for j in range(i+1):
        print(chr(65+n-j-1),end=' ')
    print()'''

'''
   *
  * *
 * * *
* * * *
'''
'''n=int(input())
for i in range(n):
        print(" "*(n-i-1)+'* '*(i+1),end=' ')
        print()'''
n=5
for i in range(n):
    for j in range(i,n):
        print(' ',end=' ')
    for j in range(i+1):
        print('*',end=' ')
    print()


for i in range(n-1):
    print(" "*(n-i-1),end='')
    for j in range(i+1):
        print(chr(65+j),end=" ")
    print()

for i in range(n):
    print(chr(65+i)*(i+1))

for i in range(n):
    print(" "*(n-i-1)+((str(i+1))+" ")*(i+1))