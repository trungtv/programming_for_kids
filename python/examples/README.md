# 🎮 Ví Dụ Code Python Mẫu

## 📋 Giới thiệu
Các ví dụ này minh họa cách sử dụng Python để tạo ra các chương trình thực tế.

## 🚀 Ví dụ cơ bản

### 1. Hello World
```python
# hello-world.py
print("Xin chào thế giới!")
print("Tôi đang học Python!")

# Kết quả:
# Xin chào thế giới!
# Tôi đang học Python!
```

### 2. Tính toán đơn giản
```python
# calculator.py
# Tính chu vi và diện tích hình chữ nhật
chieu_dai = 5
chieu_rong = 3

chu_vi = 2 * (chieu_dai + chieu_rong)
dien_tich = chieu_dai * chieu_rong

print(f"Chu vi hình chữ nhật: {chu_vi}")
print(f"Diện tích hình chữ nhật: {dien_tich}")

# Kết quả:
# Chu vi hình chữ nhật: 16
# Diện tích hình chữ nhật: 15
```

### 3. Kiểm tra điều kiện
```python
# grade-checker.py
# Kiểm tra điểm số
diem = float(input("Nhập điểm của bạn: "))

if diem >= 8:
    print("Xếp loại: Giỏi")
elif diem >= 6.5:
    print("Xếp loại: Khá")
elif diem >= 5:
    print("Xếp loại: Trung bình")
else:
    print("Xếp loại: Yếu")
```

## 🎮 Ví dụ nâng cao

### 4. Game đoán số
```python
# number-guessing-game.py
import random

print("Chào mừng đến với game đoán số!")
print("Tôi đã chọn một số từ 1 đến 100")
print("Hãy đoán xem đó là số gì!")

# Máy tính chọn số ngẫu nhiên
so_bi_mat = random.randint(1, 100)
so_lan_doan = 0

while True:
    # Người chơi nhập số đoán
    so_doan = int(input("Nhập số bạn đoán: "))
    so_lan_doan += 1
    
    # Kiểm tra kết quả
    if so_doan == so_bi_mat:
        print(f"Chúc mừng! Bạn đã đoán đúng sau {so_lan_doan} lần!")
        break
    elif so_doan < so_bi_mat:
        print("Số của bạn nhỏ hơn số bí mật!")
    else:
        print("Số của bạn lớn hơn số bí mật!")
```

### 5. Quản lý học sinh
```python
# student-manager.py
# Quản lý danh sách học sinh
danh_sach_hoc_sinh = []

def them_hoc_sinh():
    ten = input("Nhập tên học sinh: ")
    tuoi = int(input("Nhập tuổi: "))
    lop = input("Nhập lớp: ")
    
    hoc_sinh = {
        "ten": ten,
        "tuoi": tuoi,
        "lop": lop
    }
    
    danh_sach_hoc_sinh.append(hoc_sinh)
    print(f"Đã thêm học sinh {ten} vào danh sách!")

def hien_thi_danh_sach():
    print("\n=== DANH SÁCH HỌC SINH ===")
    for i, hs in enumerate(danh_sach_hoc_sinh, 1):
        print(f"{i}. {hs['ten']} - {hs['tuoi']} tuổi - Lớp {hs['lop']}")

def tim_kiem_hoc_sinh():
    ten_tim = input("Nhập tên học sinh cần tìm: ")
    tim_thay = False
    
    for hs in danh_sach_hoc_sinh:
        if ten_tim.lower() in hs['ten'].lower():
            print(f"Tìm thấy: {hs['ten']} - {hs['tuoi']} tuổi - Lớp {hs['lop']}")
            tim_thay = True
    
    if not tim_thay:
        print("Không tìm thấy học sinh!")

# Menu chính
while True:
    print("\n=== QUẢN LÝ HỌC SINH ===")
    print("1. Thêm học sinh")
    print("2. Hiển thị danh sách")
    print("3. Tìm kiếm học sinh")
    print("4. Thoát")
    
    lua_chon = input("Chọn chức năng (1-4): ")
    
    if lua_chon == "1":
        them_hoc_sinh()
    elif lua_chon == "2":
        hien_thi_danh_sach()
    elif lua_chon == "3":
        tim_kiem_hoc_sinh()
    elif lua_chon == "4":
        print("Cảm ơn bạn đã sử dụng chương trình!")
        break
    else:
        print("Lựa chọn không hợp lệ!")
```

## 🎨 Ví dụ sáng tạo

### 6. Câu chuyện tương tác
```python
# interactive-story.py
# Câu chuyện phiêu lưu trong rừng

print("=== CUỘC PHIÊU LƯU TRONG RỪNG ===")
print("Bạn đang đi bộ trong rừng và gặp một con đường rẽ.")
print("Bạn có thể đi về phía trái hoặc phải.")

lua_chon1 = input("Bạn chọn đi về phía nào? (trái/phải): ")

if lua_chon1.lower() == "trái":
    print("\nBạn đi về phía trái và gặp một con sông.")
    print("Bạn có thể bơi qua sông hoặc tìm cách khác.")
    
    lua_chon2 = input("Bạn sẽ làm gì? (bơi/tìm): ")
    
    if lua_chon2.lower() == "bơi":
        print("Bạn bơi qua sông và tìm thấy một kho báu!")
        print("Kết thúc: Bạn đã thành công!")
    else:
        print("Bạn tìm thấy một cây cầu và đi qua an toàn.")
        print("Kết thúc: Bạn đã thành công!")
        
elif lua_chon1.lower() == "phải":
    print("\nBạn đi về phía phải và gặp một hang động.")
    print("Bạn có thể vào hang hoặc đi tiếp.")
    
    lua_chon2 = input("Bạn sẽ làm gì? (vào/tiếp): ")
    
    if lua_chon2.lower() == "vào":
        print("Trong hang có một con gấu đang ngủ!")
        print("Bạn phải chạy ra ngoài và bị thương.")
        print("Kết thúc: Cuộc phiêu lưu kết thúc!")
    else:
        print("Bạn đi tiếp và tìm thấy một ngôi làng.")
        print("Kết thúc: Bạn đã được cứu!")
        
else:
    print("Lựa chọn không hợp lệ! Cuộc phiêu lưu kết thúc.")
```

### 7. Game tính nhanh
```python
# math-game.py
import random
import time

print("=== GAME TÍNH NHANH ===")
print("Bạn sẽ có 10 câu hỏi toán học")
print("Hãy trả lời nhanh nhất có thể!")

diem = 0
tong_cau = 10

for i in range(tong_cau):
    # Tạo câu hỏi ngẫu nhiên
    so1 = random.randint(1, 20)
    so2 = random.randint(1, 20)
    phep_tinh = random.choice(['+', '-', '*'])
    
    if phep_tinh == '+':
        ket_qua_dung = so1 + so2
        cau_hoi = f"{so1} + {so2} = ?"
    elif phep_tinh == '-':
        ket_qua_dung = so1 - so2
        cau_hoi = f"{so1} - {so2} = ?"
    else:
        ket_qua_dung = so1 * so2
        cau_hoi = f"{so1} × {so2} = ?"
    
    print(f"\nCâu {i+1}/{tong_cau}: {cau_hoi}")
    
    # Đo thời gian trả lời
    thoi_gian_bat_dau = time.time()
    tra_loi = input("Trả lời: ")
    thoi_gian_ket_thuc = time.time()
    
    thoi_gian_tra_loi = thoi_gian_ket_thuc - thoi_gian_bat_dau
    
    try:
        tra_loi = int(tra_loi)
        if tra_loi == ket_qua_dung:
            diem += 1
            print(f"Đúng! Thời gian: {thoi_gian_tra_loi:.1f} giây")
        else:
            print(f"Sai! Đáp án đúng là: {ket_qua_dung}")
    except ValueError:
        print("Vui lòng nhập số!")

# Kết quả cuối cùng
print(f"\n=== KẾT QUẢ ===")
print(f"Bạn đã trả lời đúng {diem}/{tong_cau} câu")
print(f"Điểm số: {diem}/{tong_cau}")

if diem >= 8:
    print("Xuất sắc! Bạn rất giỏi toán!")
elif diem >= 6:
    print("Tốt! Hãy cố gắng thêm!")
else:
    print("Hãy luyện tập thêm nhé!")
```

## 📚 Cách sử dụng

### Chạy ví dụ
```bash
# Chạy từng file
python hello-world.py
python calculator.py
python number-guessing-game.py
```

### Thực hành
1. **Đọc và hiểu** code mẫu
2. **Chạy thử** để xem kết quả
3. **Sửa đổi** để tạo phiên bản riêng
4. **Thêm tính năng** mới

### Học hỏi
- Chú ý đến cú pháp Python
- Hiểu logic của chương trình
- Học cách sử dụng thư viện
- Áp dụng vào dự án riêng

## 💡 Gợi ý mở rộng

### Thêm tính năng
- Lưu điểm số cao nhất
- Thêm âm thanh và hiệu ứng
- Tạo giao diện đẹp hơn
- Thêm nhiều câu hỏi

### Tạo biến thể
- Game đoán từ thay vì số
- Quản lý thư viện sách
- Tạo câu chuyện dài hơn
- Game đố vui

---

**🌟 Hãy thử nghiệm và sáng tạo với các ví dụ này!**
