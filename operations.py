
def int_split(a):
    tab=[]
    while a>0:
        tab.append(a%2)
        a=a//2
    return tab

def int_split_nr(a,b):
    tab = int_split(a)
    c=len(tab)
    for i in range(b-c):
        tab.append(0)
    print(tab)
    return tab