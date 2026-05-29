#for biến_chạy in range(start ,stop ,step):

#IN ra các số từ 0-5 
for i in range(1,6,1):
    print(i)
for i in range(1,5,1):
    print(i)
for i in range(-5,-1,-1):
    print(i)
for i in range(1,21,1):
    if i % 3 ==0 :
        print(f"Số {i} chia hết cho 3")
    if i%5==0:
        print(f'Số {i} chia hết cho 5')
    if i%5==0 and  i % 3 ==0 :
        print(f'Số {i} chia hết cho cả 3 và 5')
