#Two pair sum divisible by 
a= [1,2,3,4,5,6]
k=5
n=len(a)
pairs=0
for i in range(n-1):
    first=a[i]
    for j in range(i+1,n):
        sec=a[j]
        if (first+sec)%k==0:
            pairs+=1
print(pairs)
'''
#print diagonal sum of  a matrix
x=int(input())
s=0
matrix=[]
for i in range(x):
    l=list(map(int,input().split()))
    matrix.append(l)
for row in range(x):
    for col in range(x):
        if row==col:
            s+=matrix[row][col]
print(s)

#3.frequency counting using dictionary 
'''
'''
str1=input()
freq={}
for i in str1:
    if i in freq:
        freq[i]+=1
    else:
        freq[i]=1
for key,value in freq.items():
    print(f'{key}:{value}')
'''

n=987654
count=0
while n>0:
    a=n%10
    count=count*10+a
    n=n//10
print(count)