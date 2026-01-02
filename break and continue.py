#break is a keyword to exit the loop early
'''
lst=[11,45,23,40,15]
a=1
for i in lst:
    print(f'Iteration: {a}')
    a+=1
    if i%2==0:
        print(i)
        break
'''
#continue is a keyword used to skip the steps present after it in current iteration
'''
a=1
for i in lst:
    if i%2==0:
        continue
    print(f'Iteration: {a}')
    print(i)
    a+=1
'''
#write a program to print a number is prime or not   
'''
number=int(input())
count=0
for i in range(1,number+1):
    if number%i==0:
        count+=1
if count>2:
      print(" Not prime number")
else:
     print("prime")
'''
#else with loops
#else block of code will get executed if the loop never breaks
lst=[12,32,34,54]
for i in lst:
    if i==20:
        print('present')
        break
else:
    print("not present")

