
def int_split(a):
    tab=[]
    while a>0:
        tab.append(a%2)
        a=a//2
    return tab