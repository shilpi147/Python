import random
c=0
print("Welcome")
while True :
    c=c+1
    x=int(input("Enter  number"))
    y=(random.randint(0,100))
    print("random number",y)
    if x==y:
        print("Your Guess is right")
        break
    else:
        print("Try again !!")
    print("All done")
    if(c==5):
        print("Limit Reached !!")
        break
print("Exit")
