#Loops:
'''  
It is a programming structure used to repeat a block of code at a particular point
There are 2 types of loops in python
1.for loop - runs based on number of iterations
2.while loop - runs based on truthiness of a condition
'''
#For loop
'''
The loop runs equal times as number of elements present in the given iterable
the variable will store one element at a time from the given iterable,
moving forward consecutively starting from first element

syntax:
  for variable in iterable:
      with indentation block of code
'''
'''
lst=[1,2,3,4,5]
for i in lst:#1,2,3,4,5
    print("i")
'''
'''
a=input()
for i in a:
    print(i)

list1=['v','i','j','a','y']
for i in list1:
    print(i)

l=[11,22,33,44,55]
count=0
for i in l:
    count=count+1
print(count)
'''
'''
# sum of the list
l1=[1,2,3,4,5]
s=0
for i in l1:
    s+=i
print(s)

#average of the elements of the list
l2=[1,2,3,4,5]
length=0
total=0
for i in l2:
    length+=1
    total+=i
print(total//length)
#find the number of vowels present  in the given string
s="abaabced"
vowels="aeiou"
c=0
for i in s:
     if i in vowels:
         c+=1
print(c)
#program to print number of even and number of odds in a given list
l3=list(map(int,input().split()))
even_count=0
odd_count=0
for i in l3:
    if i%2==0:
        even_count+=1
    else:
        odd_count+=1
print("even numbers count is:",even_count)
print("odd numbers count is",odd_count)
'''
'''
#program to print multiplication table
number=int(input())
for i in range(1,11):
    product=number*i
    #print(number,'x',i,"=",product)
    print(f"{number} x {i} = {product} ")
    #print("{} x {} = {}".format(number,i,product))
#program to find max element in the given list
'''
'''
#maximum element in the list
a=list(map(int,input().split()))
ele=a[0]
for i in a:
    if i>ele:
        ele=i
print(ele)

#min element and its index
b=list(map(int,input().split()))
lst=b[0]
index=-1
max_index=0
for i in b:
    index+=1
    if i<lst:
        lst=i
        max_index=index
print(lst)
print(max_index)
'''
#write a program to print the second largest item in the list
'''
lst1=[13,23,45,3]
n=len(lst1)
for i in range(0,n):
    print(lst1[i])


d={'a':1,'b':2,'c':3}
for i in d:
    print(i)
for j in d.values():
    print(j)
for k in d.items():
    print(k)
for key,value in d.items():
    print(f'Key:{key}, Value:{value}')
'''
'''
l=list(map(int,input().split()))
a=l[0]
index=-1
min_index=0
for i in l:
    index+=1
    if i<a:
        a=i
        min_index=index
print(min_index)
'''
''' 
#write a program to find the second maximum element in the list
a=list(map(int,input().split()))
ele=a[0]
ele2=a[0]
#ele2=a[0]
for i in a:
    if i>ele:
        ele2=ele
        ele=i
    elif i>ele2 and i!=ele:
        ele2=i
print(ele2)
'''
sec=list(map(int,input().split()))
e1=sec[0]
e2=sec[0]
for i in sec:
    if i<e1:
        e2=e1
        e1=i
    elif i<e2 and i!=e1:
        e2=i
print(e2)


