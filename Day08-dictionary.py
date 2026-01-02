'''
Dictionary---A dictionary is a mutable,ordered collection of key-value pairs
where keys are unique,immutable and values can be of any data




'''
'''
d={'a':1,100:'abcd',(1,2):['a','b']}
print(d)

emp_d={}
print(type(emp_d))


#dictionary input

lst=[(1,'a'),(2,'b')]
print(dict(lst))

#eval()
print(eval('3+5'))
print(type(eval('[1,2,3,4]')))


dic=eval(input('enter a dictionary: '))
print(dic)
print(type(dic))

#Dictioanary operations:

dict_1={'a':1}
dict_2={'b':2}
print(dict_1 | dict_2)

#in,not in always checks in keys only,not on values

marks={'Bob':80,'john':100,100:1}
print(100 in marks)'''
'''
#is,is not can be used

#built-in functions

values={100:23,200:34,23:3}
a=len(values)
b=min(values)
c=max(values)
print(a,b,c)

#accessing values in dictionary
#values are accessed using keys


marks={'bob':80,'john':100}
print(marks['john'])

#we can use key based indexing for reassigning the values also

marks['john']=900
print(marks['john'])


#we can use this to insert new key value pairs in dictionary

'''
#-----------------------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------------------
'''
@@Dictionary class functions

methods for adding new elements

update()-adds new key value pairs at the end of an existing dictionary


'''
'''
marks={'bob':80,'john':100}
marks.update({'lilly':75,'rose':55})
print(marks)

#methods for removing elemnts

#pop(key)
marks.pop('john')
print(marks)

#popitem()
marks.popitem()
print(marks)

#clear()--it is going to make a dictionary an empty dictionary
#marks.clear()
#print(marks)

#methods for accessing values
marks1={'bob':80,'john':100}

#get()-safer way to access values using keys
print(marks1.get('bob'))
print(marks1['bob'])
print(marks1.get('charles'))
#print(marks1['charles'])

#keys()--
print(marks1.keys())
#values()--
print(marks1.values())
#items
print(marks1.items())
'''

marks2={'bob':80,'john':100}
keys=marks2.keys()
values=marks2.values()

print(keys)
print(values)
marks2['charles']=70#---directly assinging as a key  value pair without need to reassign the dictionary
print(keys)
print(values)
'''
a=eval(input())
print(sum(a.values())/len(a.values()))
'''
marks3 = eval(input("Enter marks dictionary: "))     # Example: {"math":90,"eng":80,"sci":70}
print(sum(marks3.values()) / len(marks3))
