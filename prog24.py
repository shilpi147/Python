with open("mytest.txt","r")as fb:
    y=fb.readlines()
    y[-2]="my age is 26\n"
    print(y)
with open("mytest.txt","w")as fb:
    fb.writelines(y)
