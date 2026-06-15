import logging
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)
logger = logging.getLogger(__name__)
def show_devices(devices_list: list) -> None:
    logger.debug(f"Đang thực hiện truy vấn hiển thị danh sách {len(devices_list)} thiết bị.")
    if not devices_list:
        print("Hệ thống hiện chưa có thiết bị giám sát nào!")
        return
    print("--- DANH SÁCH THIẾT BỊ GIÁM SÁT ---")
    header = f"{'MÃ TB':<7} | {'VỊ TRÍ PHÂN XƯỞNG':<20} | {'CHỈ SỐ CŨ':>10} | {'CHỈ SỐ MỚI':>10} | {'TRẠNG THÁI':<10}"
    print(header)
    for dev in devices_list:
        print(f"{dev['id']:<7} | {dev['location']:<20} | {dev['old_index']:>10.1f} | {dev['new_index']:>10.1f} | {dev['status']:<10}")
def update_indices(devices_list: list) -> None:
    logger.debug("Bắt đầu quy trình cập nhật chỉ số điện (Check-in).")
    device_id = input("Nhập mã thiết bị (id): ").strip()
    target_device = None
    for dev in devices_list:
        if dev["id"] == device_id:
            target_device = dev
            break
    if not target_device:
        print("[Lỗi] (ERR-E01): Mã thiết bị này không tồn tại trong danh sách hệ thống!")
        return
    while True:
        try:
            old_val = float(input("Nhập chỉ số cũ: "))
            if old_val < 0:
                print("[Lỗi] (ERR-E03): Định dạng không hợp lệ! Chỉ số điện phải là số lớn hơn hoặc bằng 0!")
                continue
            break
        except ValueError:
            logger.error("[Lỗi]: Kỹ thuật viên nhập sai định dạng số tại ô chỉ số điện")
            print("[Lỗi] (ERR-E03): Định dạng không hợp lệ! Chỉ số điện phải là số lớn hơn hoặc bằng 0!")
    while True:
        try:
            new_val = float(input("Nhập chỉ số mới: "))
            if new_val < 0:
                print("[Lỗi] (ERR-E03): Định dạng không hợp lệ! Chỉ số điện phải là số lớn hơn hoặc bằng 0!")
                continue
            if new_val < old_val:
                print("[Lỗi] (ERR-E02): Số liệu lỗi! Chỉ số mới không được nhỏ hơn chỉ số cũ!")
                continue
            break
        except ValueError:
            logger.error("[Lỗi]: Kỹ thuật viên nhập sai định dạng số tại ô chỉ số điện")
            print("[Lỗi] (ERR-E03): Định dạng không hợp lệ! Chỉ số điện phải là số lớn hơn hoặc bằng 0!")
    target_device["old_index"] = old_val
    target_device["new_index"] = new_val
    
    logger.info(f"[Thành công]: Đã check-in số liệu cho thiết bị {device_id}")
    print(f"[Thành công]: Cập nhật số liệu thành công cho thiết bị {device_id}.")
def trigger_overload_alert(devices_list: list) -> None:
    print("--- KÍCH HOẠT TRẠNG THÁI CẢNH BÁO ---")
    device_id = input("Nhập mã thiết bị cần duyệt: ").strip()
    target_device = None
    for dev in devices_list:
        if dev["id"] == device_id:
            target_device = dev
            break
    if not target_device:
        print("[Lỗi] (ERR-E01): Mã thiết bị này không tồn tại trong danh sách hệ thống!")
        return
    consumption = target_device["new_index"] - target_device["old_index"]
    print(f"Tìm thấy thiết bị tại: {target_device['location']} (Lượng tiêu thụ: {consumption:.0f} kWh)")

    if consumption > 5000:
        if target_device["status"] == "Normal":
            target_device["status"] = "Overload"
            logger.warning(f"[Cảnh báo]: Thiết bị {device_id} đã vượt ngưỡng tiêu thụ an toàn, chuyển sang OVERLOAD!")
            print(f"[Thành công]! Thiết bị {device_id} đã được kích hoạt trạng thái OVERLOAD!")
        elif target_device["status"] == "Overload":
            print("[Lỗi] (ERR-E04): Thao tác bị hủy! Thiết bị này đã được kích hoạt trạng thái OVERLOAD từ trước!")
    else:
        print(f"Thiết bị {device_id} hoạt động bình thường, không vượt ngưỡng an toàn.")
def calculate_energy_financials(devices_list: list) -> tuple:
    logger.debug(f"Đang tính toán chi phí năng lượng cho {len(devices_list)} thiết bị.")
    if not devices_list:
        return (0.0, 0.0, 0.0)
    total_kwh = 0.0
    for dev in devices_list:
        total_kwh += (dev["new_index"] - dev["old_index"])
    base_cost = total_kwh * 3000
    if total_kwh >= 50000:
        discount_percent = 3.0
    else:
        discount_percent = 0.0
    final_cost = base_cost * (1 - discount_percent / 100)
    return (total_kwh, discount_percent, final_cost)
def main():
    devices = [
        {"id": "M01", "location": "Mechanical Shop A", "old_index": 1200.0, "new_index": 4500.0, "status": "Normal"},
        {"id": "M02", "location": "Assembly Line B", "old_index": 2300.0, "new_index": 8500.0, "status": "Overload"}
    ]
    while True:
        print("SMART ENERGY MONITOR - PHÒNG CƠ ĐIỆN")
        print("1. Xem danh sách thiết bị giám sát")
        print("2. Cập nhật chỉ số điện tiêu thụ (Check-in)")
        print("3. Kích hoạt trạng thái cảnh báo quá tải")
        print("4. Tính tổng lượng điện & Chi phí năng lượng")
        print("5. Thoát chương trình")
        choice = input("Mời chọn chức năng (1-5): ").strip()
        if choice == '1':
            show_devices(devices)
        elif choice == '2':
            update_indices(devices)
        elif choice == '3':
            trigger_overload_alert(devices)
        elif choice == '4':
            tong_kwh, discount, tong_tien = calculate_energy_financials(devices)
            print("--- BÁO CÁO TÀI CHÍNH NĂNG LƯỢNG ---")
            print(f" Tổng lượng điện tiêu thụ thực tế: {tong_kwh:,.0f} kWh")
            print(f" Tỷ lệ chiết khấu áp dụng cho nhà máy: {discount:.0f}%")
            print(f" Tổng chi phí năng lượng phải trả sau chiết khấu: {tong_tien:,.0f} VND")
        elif choice == '5':
            print("Cảm ơn bạn đã sử dụng phần mềm Smart Energy Monitor!")
            print("[Chương trình kết thúc]")
            break
        else:
            logger.error("[Lỗi]: Kỹ thuật viên nhập sai định dạng số tại ô lựa chọn Menu")
            print("[Lỗi] (ERR-E05): Lựa chọn sai! Vui lòng nhập đúng số thứ tự chức năng từ 1 đến 5!")
if __name__ == "__main__":
    main()