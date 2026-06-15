blood_inventory = [
    "BL001-Nguyen Van A-O+-250-31/12/2026",
    "BL002-Tran Thi B-A--350-15/11/2026",
    "BL003-Le Van C-AB+-250-20/10/2026"
]


def split_blood_info(blood_bag):
    """
    Xử lý trường hợp nhóm máu có dấu -
    Ví dụ:
    BL002-Tran Thi B-A--350-15/11/2026
    """
    parts = blood_bag.split("-")

    bag_id = parts[0]
    donor = parts[1]

    if parts[2] in ["A", "B", "AB", "O"] and parts[3] == "":
        blood_group = parts[2] + "-"
        volume = parts[4]
        expiry = parts[5]
    else:
        blood_group = parts[2]
        volume = parts[3]
        expiry = parts[4]

    return bag_id, donor, blood_group, volume, expiry


def display_inventory(inventory):
    print("\n--- DANH SÁCH KHO MÁU ---")

    if len(inventory) == 0:
        print("Kho máu hiện chưa có túi máu nào.")
        return

    print(
        f"{'Mã Túi':<8} | {'Người Hiến':<20} | {'Nhóm Máu':<10} | {'Thể Tích':<10} | {'Ngày Hết Hạn'}"
    )
    print("-" * 75)

    total_volume = 0

    for blood_bag in inventory:
        bag_id, donor, blood_group, volume, expiry = split_blood_info(
            blood_bag
        )

        total_volume += int(volume)

        print(
            f"{bag_id:<8} | {donor:<20} | {blood_group:<10} | {volume + ' ml':<10} | {expiry}"
        )

    print("-" * 75)
    print(f"Tổng thể tích máu trong kho: {total_volume} ml.")


def add_blood_bag(inventory):
    print("\n--- NHẬP TÚI MÁU MỚI ---")

    bag_id = input("Nhập mã túi máu mới: ").strip().upper()

    if bag_id == "":
        print("\nLỗi: Mã túi máu không được để trống!")
        return

    for blood_bag in inventory:
        current_id = split_blood_info(blood_bag)[0]

        if current_id == bag_id:
            print(f"\nLỗi: Mã túi máu {bag_id} đã tồn tại! Vui lòng nhập mã khác.")
            return

    donor = input("Nhập tên người hiến: ").strip().title()

    if donor == "":
        print("\nLỗi: Tên người hiến không được để trống!")
        return

    blood_group = input("Nhập nhóm máu: ").strip().upper()

    volume = input("Nhập thể tích (ml): ").strip()

    if not volume.isdigit():
        print("\nLỗi: Thể tích phải là số nguyên lớn hơn 0!")
        return

    volume = int(volume)

    if volume <= 0:
        print("\nLỗi: Thể tích phải là số nguyên lớn hơn 0!")
        return

    expiry = input("Nhập ngày hết hạn (DD/MM/YYYY): ").strip()

    new_bag = "-".join(
        [
            bag_id,
            donor,
            blood_group,
            str(volume),
            expiry
        ]
    )

    inventory.append(new_bag)

    print(f"\nThành công: Đã nhập túi máu {bag_id} vào kho!")
    print("\nSau khi chuẩn hóa, dữ liệu được lưu vào list là:")
    print(new_bag)


def update_expiry(inventory):
    print("\n--- GIA HẠN / SỬA NGÀY HẾT HẠN ---")

    bag_id = input(
        "Nhập mã túi máu cần cập nhật: "
    ).strip().upper()

    if bag_id == "":
        print("\nLỗi: Mã túi máu không được để trống!")
        return

    for index in range(len(inventory)):
        current_id = split_blood_info(inventory[index])[0]

        if current_id == bag_id:

            parts = inventory[index].split("-")

            new_expiry = input(
                "Nhập ngày hết hạn mới: "
            ).strip()

            parts[-1] = new_expiry

            inventory[index] = "-".join(parts)

            print(
                f"\nThành công: Đã cập nhật ngày hết hạn cho túi máu {bag_id}!"
            )
            return

    print(f"\nLỗi: Không tìm thấy túi máu {bag_id} trong kho!")


def remove_blood_bag(inventory):
    print("\n--- XUẤT / HỦY TÚI MÁU ---")

    bag_id = input(
        "Nhập mã túi máu cần xuất/hủy: "
    ).strip().upper()

    if bag_id == "":
        print("\nLỗi: Mã túi máu không được để trống!")
        return

    for index in range(len(inventory)):
        current_id = split_blood_info(inventory[index])[0]

        if current_id == bag_id:
            inventory.pop(index)

            print(
                f"\nThành công: Đã xuất túi máu {bag_id} khỏi kho!"
            )
            return

    print(f"\nLỗi: Không tìm thấy túi máu {bag_id} trong kho!")


def main():
    while True:
        print("\n=== HỆ THỐNG QUẢN LÝ KHO MÁU RIKKEI ===")
        print("1. Xem danh sách túi máu trong kho")
        print("2. Nhập túi máu mới")
        print("3. Gia hạn / Sửa ngày hết hạn")
        print("4. Xuất / Hủy túi máu")
        print("5. Thoát chương trình")
        print("========================================")

        choice = input("Chọn chức năng (1-5): ").strip()

        match choice:
            case "1":
                display_inventory(blood_inventory)

            case "2":
                add_blood_bag(blood_inventory)

            case "3":
                update_expiry(blood_inventory)

            case "4":
                remove_blood_bag(blood_inventory)

            case "5":
                print(
                    "\nCảm ơn bác sĩ đã sử dụng hệ thống. Hẹn gặp lại!"
                )
                break

            case _:
                print(
                    "\nLựa chọn không hợp lệ, vui lòng nhập số từ 1-5!"
                )


main()