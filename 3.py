#Separate Integers and 
#Characters from a given string

a="str12prad23"

def sep_int_and_string(a):
    a1=""
    a2=""
    for i in a:
        if i.isdigit():
            a1+=i
        else:
            a2+=i
    return a1,a2

print(sep_int_and_string(a))


