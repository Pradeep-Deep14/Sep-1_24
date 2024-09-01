l=[1,2,3,4,5,6,7,8,9]
l1=[]
l2=[]
for i in l:
    l1.insert(0,i)
print(l1)


for i in range(len(l)-1,-1,-1):
    l2.append(l[i])
print(l2)

