"""Anonymous functions:
These functions dont have any names 
These are defined using lambda keyword.Hence these are also called as lambda functions
These should always have a single line of code
These are generally used as helper functions for the working of other builtin functions like
map(),filter(),sorted(),etc

syntax:
lambda arguments : return_object
The return keyword is not necessary .the value present after the colon will be automatically returned.
"""''''''
#lambda function for summing up two numbers
'''func= lambda x,y:x+y
print(func(3,10))'''
#lambda function to find the length of the given string
'''f=lambda s :len(s)
print(f(s=input()))'''
#write a lambda function to find a number is even or odd
'''num=lambda a:a%2==0
if num(6==0):
    print("even")
else:
    print("odd")
#using lambda we can write the above code as 

f=lambda b:"even" if b%2==0 else "odd"
print(f(10))'''

#map()---
'''lst=[12,6,90,3]
result=list(map(lambda l:l*2,lst))
print(result)

def double(n):
    return n*2
print(list(map(double,lst)))

res=list(map(lambda l:"E" if l%2==0 else "o",lst))
print(res)'''
#filter()----
#count the number of words in the given list that have a minimum of 5 characters
'''lst1=["python",'abc','code','program']
res1=list(filter(lambda c:len(c)>=5,lst1))
print(len(res1))
'''
#count the number of palindrome strings in the given list
'''lst2=["aba","cbc","vijay"]
res2=list(filter(lambda d:d==d[::-1],lst2))
print(len(res2))'''

#sorted()----
lst3=['cat','ball','donkey','apple']
print(sorted(lst3,key=lambda s:len(s)))#according the length 
#sorted the above words according to their last characters
print(sorted(lst3,key=lambda s:s[-1]))