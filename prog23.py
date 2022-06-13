with open("mytest.txt","r")as fb:
    y=(fb.read())
    print(len(y.split("\n")))
with open("mytest.txt","w")as fb:
    for i in range(20):
        fb.write(f"my age is{i}\n")
