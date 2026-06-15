
raw_logs = []
processed_logs = []

def clean_logs(input_text):
    """
    Làm sạch log:
    - Xóa ký tự đặc biệt !@#$
    - Tách thành list bằng dấu ;
    """
    table = str.maketrans("", "", "!@#$")
    cleaned = input_text.translate(table)

    logs = [log.strip() for log in cleaned.split(";") if log.strip() != ""]
    return logs

def filter_logs(logs):
    """
    Lọc log chứa ERROR hoặc CRITICAL (không phân biệt hoa thường)
    """
    return [log for log in logs if "error" in log.lower() or "critical" in log.lower()]

def mask_ips(logs):
   
    result = []

    for log in logs:
        words = log.split()
        new_words = []

        for word in words:
            if "." in word:  
                parts = word.split(".")
                if len(parts) == 4:
                    word = ".".join(parts[:2] + ["*", "*"])
            new_words.append(word)

        result.append(" ".join(new_words))

    return result


# ===============================
# 4. MENU
# ===============================
def main():
    global raw_logs, processed_logs

    while True:
        print("""
============= SECURITY LOG ANALYZER =============
1. Nhập và làm sạch dữ liệu Log thô
2. Lọc các Log cảnh báo mức độ cao (ERROR/CRITICAL)
3. Mã hóa địa chỉ IP (Masking)
4. Đóng hệ thống
=================================================
        """)

        choice = input("Chọn chức năng (1-4): ")
        if choice == "1":
            data = input("Nhập chuỗi log (cách nhau ;): ")
            raw_logs = clean_logs(data)
            print(f"Đã lưu {len(raw_logs)} log.")

        elif choice == "2":
            if not raw_logs:
                print("Chưa có dữ liệu log!")
                continue

            processed_logs = filter_logs(raw_logs)

            print(f"Tìm thấy {len(processed_logs)} cảnh báo:")
            for log in processed_logs:
                print("-", log)

        elif choice == "3":
            if not processed_logs:
                print("Chưa có dữ liệu log nguy hiểm!")
                continue

            masked = mask_ips(processed_logs)

            print("Báo cáo an toàn:")
            for i, log in enumerate(masked, 1):
                print(f"{i}. {log}")

        elif choice == "4":
            print("Đóng hệ thống...")
            break

        else:
            print("Lựa chọn không hợp lệ!")

main()