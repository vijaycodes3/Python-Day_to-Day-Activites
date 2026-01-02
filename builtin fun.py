#enum(),zip()
lst=[11,23,42,31,13,14]
for k,v in enumerate (lst):
    if v==31:
        print(k)
lst1=[11,58,31,14]
lst2=[12,6,9]
new=[]
for i in range(len(lst2)):
    new.append((lst1[i],lst2[i]))
print(new)
for i in zip(lst1,lst2):
    print(i)