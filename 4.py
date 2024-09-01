l=[1,2,2,3,4,5]
l1=[]
def duplicate(l):
    for i in l:
        if l.count(i)>1 and i not in l1:
            l1.append(i)
    return l1

print(duplicate(l))