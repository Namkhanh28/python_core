# Do anh Sofm chi co 2 phan tu thoi nen khi khong tim thay p[2] => sap
# # Các tên biến như ds, p, t, m, r, b quá ngắn và khó hiểu, nên đổi thành player_records, record, name, matches, mmr, bonus để dễ đọc và bảo trì.

player_records = [
    ("Levi", 120, 2500),   
    ("SofM", 150),            
    ("Optimus", 100, "N/A")   
]

def calculate_bonus(matches: int, mmr: int) -> float:
    return (matches * 10) + (int(mmr) * 0.5)

def process_players(records: list):
    print("--- BẢNG TÍNH THƯỞNG RP ---")
    for record in records:
        name = record[0]
        try:
            matches = record[1]
            mmr = record[2]
            bonus = calculate_bonus(matches, mmr)
            print(f"Tuyển thủ {name} nhận được {bonus} RP")
            
        except IndexError:
            print(f"Tuyển thủ {name}: Lỗi - Hồ sơ bị thiếu thông tin!")
            continue
            
        except ValueError:
            print(f"Tuyển thủ {name}: Lỗi - Dữ liệu MMR không hợp lệ!")
            continue
process_players(player_records)