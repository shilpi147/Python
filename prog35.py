'''l=[1,2,3]
m=["one","two","three"]
d={}
d={k:v for k,v in zip(m,l)}
print(d)'''


'''l=(i**2 for i in range(10))
print(list(l))
print(list(l))'''


'''l=[i for i in range(20)]
for i in l:
    print(i)
    if i>4:
        break
print("after for loop")
for i in l:
    print(i)'''


'''l=(i**2 for i in range(20))
print(next(l))'''

'''l=(i**2 for i in range(20))
for i in range(3):
    print(next(l))
print("Outside")
print(next(l))'''

'''# A simple generator function
def my_gen():
    n = 1
    print('This is printed first')
    # Generator function contains yield statements
    yield n

    n += 1
    print('This is printed second')
    yield n

    n += 1
    print('This is printed at last')
    yield n
a = my_gen()
for i in a :
    print(i)
x=next(a)
print(x)
y=next(a)
print(y)
z=next(a)
print(z)
b=next(a)
print(b)'''



'''def gen():
    for i in range (10):
        yield i
x=gen()
for j in x:
    print(j)'''

from itertools import count
for i in count():
        print(i)
