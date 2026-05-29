print("--- EMERGENCY TRIAGE SYSTEM ---")

heart_rate = float(input("Enter patient's heart rate (bpm): "))

if heart_rate > 120:
    print(f"Priority: RED - Critical condition! Immediate action required.")
elif heart_rate > 100:
    print(f"Priority: YELLOW - Abnormal. Monitor closely.")
elif heart_rate < 60:
    print(f"Priority: BLUE - Bradycardia. Require ultrasound.")
else:
    print(f"Priority: GREEN - Stable. Please wait in the lobby.")
print(f"Triage process completed.")

# Chạy từ trên xuống
# Gặp điều kiện đúng đầu tiên ->chạy và thoát
# Các elif phía dưới -> bị bỏ qua
#Lỗi Sai logic ở thứ tự điều kiện 