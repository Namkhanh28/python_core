
while True:
    s=input()
    if s=="True"or s=="False":
        print("BOOL")
    elif s.isdigit():
        print("INT")
    elif s.count(".")==1:
        parts=s.split(".")
        if parts[0].isdigit() and parts[1].isdigit():
            print("FLOAT")
        else:
            print("STRING")
    else:
        print("STRING")