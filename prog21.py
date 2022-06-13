d={}
while True :
    print(d)
    ch=int(input("Enter your choice\n 1. Registration\n 2. Login\n 3. Update\n 4. Delete"))
    
    if ch==1:
        usr=input("Enter username")
        if usr in d.keys():
            print("uername exsists")
        else:
            pwd=input("enter password")
            d[usr]=pwd
    
    if ch==2:
        usr=input("Enter username")
        if usr in d.keys():
            pwd=input("enter password")
            if d[usr]==pwd:
                print("Login Successfull")
            else:
                print("Incorrect password")
        else:
            print("Username dosen't exsists please register")
    if ch==3:
        usr=input("Enter username")
        if usr in d.keys():
            pwd=input("enter password")
            if d[usr]==pwd:
                print("Login Successfull")
                upwd=input("Enter new password")
                d[usr]=upwd
            else:
                print("Incorrect password")
        else:
            print("Username dosen't exsists please register")
    if ch==4:
        usr=input("Enter username")
        if usr in d.keys():
            pwd=input("enter password")
            if d[usr]==pwd:
                del d[usr]
                print("Deleted sucessfully")
            else:
              print("Incorrect password")
        else:
            print("Username dosen't exsists please register")  
