

import logging


def main():
    import logging
    logging.basicConfig(
    filename="arena_tickets.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
ticket_db = [
    {"ticket_id": "T01", "buyer_name": "Nguyen Van A", "price": 500.0, "status": "Booked", "seat": ("A", 1)},
    {"ticket_id": "T02", "buyer_name": "Tran Thi B", "price": 300.0, "status": "Cancelled", "seat": ("B", 5)},
    {"ticket_id": "T03", "buyer_name": "Le Van C", "price": 500.0, "status": "Booked", "seat": ("A", 2)}
]
def display(tickets):
    logging.info("User viewed ticket list.")
    
    if not tickets:
        print("Hiện chưa có vé nào trong hệ thống.")
        return

    print("\n--- DANH SÁCH VÉ ---")
    print(
        f"{'Mã Vé':<8}|{'Tên Khách Hàng':<20}|{'Giá Vé':<10}|{'Chỗ Ngồi':<12}|{'Trạng Thái'}"
    )
    print("-" * 70)

    for ticket in tickets:
        try:
            seat = f"{ticket['seat'][0]}-{ticket['seat'][1]}"
            status = ticket["status"]
            if status == "Cancelled":
                status += " [ĐÃ HỦY]"

            print(
                f"{ticket['ticket_id']:<8}|"
                f"{ticket['buyer_name']:<20}|"
                f"{ticket['price']:<10}|"
                f"{seat:<12}|"
                f"{status}"
            )

        except KeyError as error:
            print(
                "Lỗi: Một vé đang bị thiếu dữ liệu, vui lòng kiểm tra lại."
            )
            logging.error(
                f"Missing key while displaying ticket: {error}"
            )

    print("-" * 70)
def input_price():
    while True:
        try:
            price = float(input("Nhập giá vé: "))

            if price <= 0:
                print(
                    "Giá vé phải lớn hơn 0. Vui lòng nhập lại."
                )
                continue

            return price

        except ValueError:
            print(
                "Giá vé phải là số. Vui lòng nhập lại."
            )
            logging.warning(
                "Invalid price input while booking ticket"
            )
def input_seat_number():
    while True:
        try:
            seat_number = int(
                input("Nhập số ghế: ")
            )

            if seat_number <= 0:
                print(
                    "Số ghế phải lớn hơn 0."
                )
                continue

            return seat_number

        except ValueError:
            print(
                "Số ghế phải là số nguyên. Vui lòng nhập lại."
            )
def book_ticket(tickets):
    print("\n--- ĐẶT VÉ MỚI ---")

    ticket_id = input(
        "Nhập mã vé: "
    ).strip().upper()

    for ticket in tickets:
        if ticket["ticket_id"] == ticket_id:
            print(
                f"Lỗi: Mã vé {ticket_id} đã tồn tại."
            )

            logging.warning(
                f"Duplicate ticket ID entered: {ticket_id}"
            )
            return

    buyer_name = input(
        "Nhập tên khách hàng: "
    ).strip()

    price = input_price()

    row = input(
        "Nhập khu vực ghế: "
    ).strip().upper()

    seat_number = input_seat_number()

    new_ticket = {
        "ticket_id": ticket_id,
        "buyer_name": buyer_name,
        "price": price,
        "status": "Booked",
        "seat": (row, seat_number)
    }

    tickets.append(new_ticket)

    print(
        f"Thành công: Đã đặt vé {ticket_id} cho khách hàng {buyer_name}."
    )

    logging.info(
        f"Booked new ticket {ticket_id} for {buyer_name}"
    )

if __name__=='__main__':
    main()
    while True:
        choice = ('''
=== HỆ THỐNG QUẢN LÝ VÉ RIKKEI ESPORTS ===
1. Xem danh sách vé đã bán
2. Đặt vé mới
3. Đổi chỗ ngồi (Cập nhật vé)
4. Hủy vé
5. Báo cáo doanh thu
6. Thoát chương trình
======================================== 
Chọn chức năng (1-6):''').strip()
        match choice:
            case'1':
                display(ticket_db)
                pass
            case'2':
                pass
            case'3':
                pass
            case'4':
                pass
            case'5':
                pass
            case'6':
                print("Thoát chương trình")
                break
            case _ :
                print("Nhập đúng lựa chọn")
