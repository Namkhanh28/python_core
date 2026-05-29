max_attemps =5
status =False 
correct_num =50
for i in range(1,6,1):
    input_num =int(input(f"Lượt đón {i} :"))
    if(input_num < correct_num):
        print(f"")