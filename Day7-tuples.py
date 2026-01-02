'''
Tuple:
 A tuple is an immutable,ordered collection of heterogeneous
 elements enclosed in round brackets


 '''
'''
t=(1,23.4,True,'python',[1,2],(3,4),{5,6},{'a':1})
#print(t)
empty_tple=()
#tuple with single element
s_t=(1,)
#implicit tuple creation
tup=1,2,3,4,5
print(type(tup))

#tuple input
s='python'
print(tuple(s))

#a b c d e f
tu=tuple(input().split())
print(tu, type(tu))

#1 2 3 4 5
int_t=tuple(map(int,input().split()))

#tuple operations
#operators: +,*,in not in,is,is not
#builtin functions
#min(),max(),sorted(),len(),sum()
#indexing and slicing---same as string and list classes


#tuple methods
#count(ele) -returns the number of occurences of a particular ele
#index(ele)-returns the index of a particular element
#NO other methods of modification are there as tuple is immutable
'''
#understanding the immutability nature of tuple--if an mutable object exists as a tuple element ,
#changes can be made to that object but entire replacement of that object with other object is not supported

t=(1,[2,34,34],'python')
#t[0]=6
'''
lst=[[1,2],[3,4]]
print(lst[0][1])'''

t[1][1]=12
print(t)

#t[1]=[2,12,34]---it is not possible

##tuple unpacking
tup=('vijay',123456,'PFS-43')#there should be balance between the variables and the elements presnt in the tuple
name,id_num,batch=tup
print(name,id_num,batch)