playlist = ["See You Again", "Faded", "Attention"]

while True:
    choice = input('''
==================================================
          MUSIC MANAGEMENT SYSTEM
==================================================
1. Thêm bài hát mới vào cuối danh sách
2. Chèn bài hát yêu thích lên đầu danh sách
3. Xóa một bài hát
4. Sắp xếp danh sách theo ABC
5. Nghe thử 3 bài đầu
0. Thoát
==================================================
Mời bạn chọn chức năng (0-5): ''')

    
    if not choice.isdigit():
        print(" Lựa chọn không hợp lệ, vui lòng nhập số!")
        continue

    choice = int(choice)
    if choice == 1:
        song = input("Nhập tên bài hát mới: ")
        if song == "":
            print(" Tên bài hát không được để trống!")
        else:
            playlist.append(song)
            print(" Đã thêm bài hát!")

    elif choice == 2:
        song = input("Nhập bài hát yêu thích: ")
        if song == "":
            print(" Tên bài hát không hợp lệ!")
        else:
            playlist.insert(0, song)
            print(" Đã thêm vào đầu danh sách!")

    elif choice == 3:
        song = input("Nhập tên bài hát cần xóa: ")
        if song in playlist:
            playlist.remove(song)
            print(" Đã xóa bài hát!")
        else:
            print(" Không tìm thấy bài hát!")

    elif choice == 4:
        playlist.sort()
        print(" Đã sắp xếp danh sách!")

    elif choice == 5:
        print("\n🎧 3 bài hát đầu tiên:")
        if len(playlist) == 0:
            print("Danh sách trống!")
        else:
            for song in playlist[:3]:
                print("-", song)

    elif choice == 0:
        print("👋 Thoát chương trình!")
        break

    else:
        print(" Chọn từ 0 đến 5 thôi!")

    print(" Playlist hiện tại:")
    for i, song in enumerate(playlist, start=1):
        print(f"{i}. {song}")