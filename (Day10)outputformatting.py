#output formatting


'''
TYPES

comma based
modulo operator based
formatted string literals
format method of string class

'''
#1.comma based:
'''
we give multiple objects with commas in print function.
name=input()
age=int(input())
print(name,'is',age,'years old')


b=int(input())
length=int(input())
print("Area of the triangle is:",0.5*b*length)
'''
#2.modulo operator based
'''
we use format specifiers in string and pass values that have to be replced with those
syntax:
string with format specifier'%(values following proper order)
%d-int format specifier
%s-string
%f-float
%.nf-float with n digits after decimal point,it can be used for round off
'''
'''
name1=input()
age1=int(input())
print('%s is %d years old'%(name1,age1))
num=31.5378
print('The rounded off number is: %.2f' %(num,))

'''

#3.Formatted string literals
'''
We use 'f' at the beginning the string and plce holders in the string
{}-brackets are used as placeholders
syntax:
f'string with placeholders and values to be embedded'
'''

'''
name2=input()
age2=int(input())
print(f'{name2} is {age2} years old ')
'''

#4.Format method in string class
'''
'''
name3=input()
age3=int(input())
op='{1} is {0} years old'

print(op.format(age3,name3))
