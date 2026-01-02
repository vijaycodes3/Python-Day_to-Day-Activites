'''
set:

A set is a mutable,uordered collection of unique


'''
'''
s={1,5.5,(1,2),'python',True}
print(s)

st={1,1,2,2,3,3}
print(st)

set_1={34,6,1,95}
print(set_1)

#a=set(map(int,input().split()))
#print(a)

marks={'a':12,'b':13,'c':14}
print(set(marks))

##### SET OPERATIONS######

####OPERATORS#####

#in , not in can be used
#is , is not also be used

#some operators are used for special set operations like union
#union operation--  (|)
a={1,2,6,3,4}
b={5,1,2,6,7,8}
print(a|b)

#intersection - &

print(a&b)


#difference - (-)
#it is used to get the elements present only in first set
print(a-b)

#symmetric difference-   ^
#it is used to get elements that are not common to both the sets
print(a^b)
'''
'''

sup_set={1,2,3,4,5,6,7}
sub_set={2,4,6}

print(sup_set>=sub_set)####(>=)---returns whether a rhs is subset of lhs
print(sup_set!=sub_set)

#set methods-methods defined inside set class
#we have to use mthods as set_obj.fun_name()
example={1,2,3,4}

#add()
example.add(5)
print(example)

#update()-adds a group of elements
example.update({10,20,30})
print(example)

#remove(ele)--for removing elements-raises keyerror if element doesnt exist
example.remove(5)
print(example)

#discard(ele)-none
example.discard(3)
print(example)

#pop()-removes an orbitary element

example.pop()
print(example)

#clear()-an empty set
example.clear()
print(example)
'''
'''
s={}
s=set()
s=list(),str()'''

set1={1,3,5,8}
set2={2,4,6,8}
#union()
print(set1.union(set2))
#intersection()
#intersection_update()
print(set1.intersection(set2))
#difference()
print(set1.difference(set2))
#symmetric_difference()
print(set1.symmetric_difference(set2))

#issuperset(),issubset(),isdisjoint()
print(set1.issubset(set2))
print(set1.issuperset(set2))
print(set1.isdisjoint(set2))
