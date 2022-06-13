x=int(input("Enter the Number"))
o=[]
e=[]
l=[]
for i in range(x):
    y=int(input("Enter list of numbers"))
    l.append(y)
    print("The number of lists L is ",l)
for j in l:
    if j%2 == 0:
        e.append(j)
    else:
        o.append(j)
print("List of even numbers is",e)
print("List of odd numbers is",o)
