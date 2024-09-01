lst=[12,23,12,24,46,49,23]
element_count={}
unique_list=[]
#List of count of Elements
for element in lst:
    if element in element_count:
        element_count[element]+=1
    else:
        element_count[element]=1
        unique_list.append(element)



for element,count in element_count.items():
    print(f"The count of {element} is :",count)

print(f"The Unique list is : {unique_list}")