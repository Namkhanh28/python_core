transportation_list = [
    {
        "ma_xe": "X001",
        "chu_xe": "Nguyễn Quảng An ",
        "loai_xe ": "Ô tô",
       
    },
    {
        "ma_xe": "X002",
        "chu_xe": "Nguyễn Văn An",
        "loai_xe": "Xe máy",
    }
]
while True:
    choice = int(input('''Quản lí bãi đỗ xe
                   1, Thêm xe mới vào bãi 
                   2,Hiển thi danh sách xe trong bãi 
                   3,Tìm kiếm xe theo mã id
                   4,Xóa xe khỏi bãi 
                   5,Thoát chương trình
                    Nhập lựa chọn ?'''))
    match choice :
        case '1':
            find = False 
            xe_id = input("Nhập mã xe bạn gửi")
            for index,xe in enumerate(transportation_list):
                if xe_id == xe["ma_xe"]:
                    print(" Xe đã có trong bãi")
                    find =True
                    break
                if not find:
                    xe = input("Nhập loai xe ").strip()
                if xe == "" :
                    print("Nhập đầy đủ thông tin")
                    boss = input("Nhập tên chủ xe").strip()
                if boss == "" :
                    print("Nhập đầy đủ thông tin")
                new_transpost = {
                    transportation_list["ma_xe"] = index,
                    transportation_list["loai_xe"]= xe ,
                    transportation_list["chu_xe"]=boss
                    }
                transportation_list.append(new_transpost)
        case '2':
            if transportation_list==[]:
                print("Bãi xe đang trống")
            else:
                for xe in transportation_list:
                    print(f" Chủ xe :{transportation_list["ma_xe"]} | {transportation_list["loai_xe"]}| {transportation_list["chu_xe"]}")
       
        
        