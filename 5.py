#Write a Python program to filter list elements between both 1 and 20 inclusive which are even nos

def even_numbers_between_1_and_20():
    L=[]
    for i in range(1,21):
        if i%2==0:
            L.append(i)
    return L

print(even_numbers_between_1_and_20())
