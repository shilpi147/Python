
try:
    x=-1
    if x<1:
        raise Exception("x is less than 1")
except Exception as e:
    print("Error !",e)
