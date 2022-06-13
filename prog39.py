'''a=10
b=20
def add():
    z=a+b
    return z
x=add()
print(x)'''

'''c = 1 # global variable
    
def add():
    #global c
    c=0
    c = c + 2 # increment c by 2
    print(c)

add()'''


'''def foo():
    global x 
    x = 20
    print("in foo",x)#20

    def bar():
        #global x
        #print("inbarc",x)#123
        x = 2500
        print("in bar",x)
    
    print("Before calling bar: ", x)#20
    print("Calling bar now")
    bar()
    print("After calling bar: ", x)#2500
    
    
x = 123
foo()
print("x in main : ", x)#2500    123'''




'''def outer_function():
    global a
    a = 20
    print("outer function",a) #20      30
    def inner_function():
        global a
        a = 30
        print('inner function a =',a)#30     20
    
    
    print("a",a) 

    inner_function()
    
    print(' a =',a)#10     30   20
     
a = 10 #globl
outer_function()
print('a =',a)#10    30'''



'''def outer_function():
    #global a
    a =10
    #hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh
    print("firsr",a) #10
    a = 20
    def inner_function():
        #global a
        print("innerfunt",a)#10
        a = 30
        print('inner a =',a)#30

    inner_function()
    print('outer a =',a) #20        30 
     
a = 10
print("a",a) #20 
####################################
outer_function()
print('main a =',a)'''

def calc_factorial(x):
    """This is a recursive function
    to find the factorial of an integer"""
    print("executing",x)

    #if x == 1:
        #return 1
        #pass
    #else:
    return (x * calc_factorial(x-1))

num = 4
print("The factorial of", num, "is", calc_factorial(num))
print(calc_factorial.__doc__)

















