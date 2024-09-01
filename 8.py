nested_list=[[1,2],[3,4,5],[5,6,7]]

def flattened_list(nested_list):
    Flattened=[]
    for i in nested_list:
            if isinstance(i,list):
                Flattened.extend(i)
    return list(set(Flattened))

print(flattened_list(nested_list))