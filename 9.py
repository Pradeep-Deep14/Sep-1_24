nested_list=[1,[1,2],3,[3,4,5],7,6,[5,6,7]]

def flattened_list(nested_list):
    Flattened=[]
    seen=set()

    for sublist in nested_list:
        if isinstance(sublist,list):
            for item in sublist:
                if item not in seen:
                    Flattened.append(item)
                    seen.add(item)
    return Flattened

print(flattened_list(nested_list))

#Nested to Flattened and remove duplicates