# Bài giảng 2.3: Cấu trúc dữ liệu Python - Dictionary, Tuple và Set

## 📋 Thông tin bài học
- **Thời gian**: 90 phút
- **Độ tuổi**: 11-12 tuổi
- **Trình độ**: Trung bình
- **Mục tiêu**: Hiểu và sử dụng các cấu trúc dữ liệu Python cơ bản

## 🎯 Mục tiêu học tập

### Kiến thức
- Hiểu khái niệm cấu trúc dữ liệu và tầm quan trọng
- Nắm vững Dictionary (từ điển) và ứng dụng
- Hiểu Tuple (bộ) và Set (tập hợp)
- Biết cách chọn cấu trúc dữ liệu phù hợp

### Kỹ năng
- Phân tích và thiết kế cấu trúc dữ liệu
- Áp dụng các cấu trúc dữ liệu vào lập trình Python
- Sử dụng các phương thức và hàm built-in
- Debug và tối ưu hóa code với cấu trúc dữ liệu

### Thái độ
- Phát triển tư duy tổ chức dữ liệu
- Rèn luyện tính cẩn thận với cấu trúc dữ liệu
- Khuyến khích tư duy sáng tạo với dữ liệu

## 🧠 Nội dung bài học

## 📚 PHẦN LÝ THUYẾT (45 phút)

### Phần 1: Khái niệm cấu trúc dữ liệu qua hoạt động không máy tính (25 phút)

#### Hoạt động khởi động - "Kết nối với Scratch"
- **Hoạt động**: Nhắc lại bài 6 về cấu trúc dữ liệu trong Scratch (danh sách Pokemon)
- **Câu hỏi**: "Chúng ta đã học cách tổ chức dữ liệu như thế nào trong Scratch?"
- **Kết nối**: "Hôm nay chúng ta sẽ học cách tổ chức dữ liệu phức tạp hơn trong Python"
- **Mục tiêu**: Kết nối kiến thức Scratch với Python

#### Khái niệm cấu trúc dữ liệu qua ví dụ thực tế
- **Định nghĩa**: Cấu trúc dữ liệu là cách tổ chức và lưu trữ dữ liệu trong máy tính
- **Ví dụ**: Danh sách học sinh, từ điển tra cứu, bộ tọa độ
- **Input**: Dữ liệu thô (tên, điểm, địa chỉ...)
- **Output**: Dữ liệu có cấu trúc (dễ tìm kiếm, sắp xếp, xử lý)
- **Ứng dụng**: Quản lý thông tin, tìm kiếm nhanh, phân tích dữ liệu

#### Hoạt động thực hành - "Tổ chức thông tin học sinh"
- **Hoạt động**: Học sinh tổ chức thông tin của 3 bạn trong lớp
- **Mục tiêu**: Hiểu khái niệm cấu trúc dữ liệu qua trải nghiệm thực tế
- **Quy tắc**: Mỗi học sinh có tên, tuổi, điểm số, địa chỉ
- **Kết quả**: Nhận ra cần cách tổ chức dữ liệu hiệu quả

### Phần 2: Dictionary (Từ điển) qua hoạt động không máy tính (20 phút)

#### Hoạt động không máy tính - "Từ điển tra cứu"
- **Hoạt động**: Học sinh sử dụng từ điển tiếng Anh để tra nghĩa từ
- **Mục tiêu**: Hiểu cách Dictionary hoạt động
- **Quy tắc**: Từ (key) → Nghĩa (value), tra nhanh theo từ
- **Kết quả**: Nhận ra Dictionary giúp tìm kiếm nhanh

#### Bài toán: Quản lý điểm số học sinh
- **Input**: Tên học sinh và điểm số
- **Output**: Dictionary {tên: điểm}
- **Ví dụ**: {"An": 8, "Bình": 9, "Cường": 7}

#### Dictionary qua ví dụ thực tế
```
Từ điển điểm số:
- "An" → 8 điểm
- "Bình" → 9 điểm  
- "Cường" → 7 điểm

Tìm điểm của "Bình": tra từ điển → 9 điểm
Thêm học sinh mới: "Dũng" → 10 điểm
```

#### Hoạt động không máy tính - "So sánh với danh sách"
- **Hoạt động**: So sánh cách tìm điểm bằng danh sách và từ điển
- **Mục tiêu**: Hiểu ưu điểm của Dictionary
- **Kết quả**: Nhận ra Dictionary tìm kiếm nhanh hơn

## 💻 PHẦN THỰC HÀNH PYTHON (45 phút)

### Phần 3: Tạo chương trình "Quản lý học sinh với Dictionary" trên Python (25 phút)

#### Bước 1: Tạo file Python mới
```python
# Tạo file: quan_ly_hoc_sinh.py
# Mục tiêu: Sử dụng Dictionary để quản lý học sinh
```

#### Bước 2: Lập trình Dictionary cơ bản
```python
def tao_danh_sach_hoc_sinh():
    """
    Tạo danh sách học sinh với Dictionary
    """
    print("=== TẠO DANH SÁCH HỌC SINH ===")
    
    # Tạo Dictionary rỗng
    hoc_sinh = {}
    
    # Thêm học sinh
    hoc_sinh["An"] = 8
    hoc_sinh["Bình"] = 9
    hoc_sinh["Cường"] = 7
    hoc_sinh["Dũng"] = 10
    
    print(f"Danh sách học sinh: {hoc_sinh}")
    return hoc_sinh

def tim_diem_hoc_sinh(hoc_sinh, ten):
    """
    Tìm điểm của học sinh
    """
    print(f"Tìm điểm của học sinh: {ten}")
    
    if ten in hoc_sinh:
        diem = hoc_sinh[ten]
        print(f"Học sinh {ten} có điểm: {diem}")
        return diem
    else:
        print(f"Không tìm thấy học sinh {ten}")
        return None

def them_hoc_sinh_moi(hoc_sinh, ten, diem):
    """
    Thêm học sinh mới
    """
    print(f"Thêm học sinh mới: {ten} - {diem} điểm")
    
    hoc_sinh[ten] = diem
    print(f"Đã thêm! Danh sách mới: {hoc_sinh}")
    return hoc_sinh

def hien_thi_tat_ca_hoc_sinh(hoc_sinh):
    """
    Hiển thị tất cả học sinh
    """
    print("=== DANH SÁCH TẤT CẢ HỌC SINH ===")
    
    for ten, diem in hoc_sinh.items():
        print(f"Học sinh: {ten} - Điểm: {diem}")
    
    print(f"Tổng số học sinh: {len(hoc_sinh)}")

def tim_hoc_sinh_gioi(hoc_sinh, diem_chuan=8):
    """
    Tìm học sinh giỏi (điểm >= diem_chuan)
    """
    print(f"Tìm học sinh giỏi (điểm >= {diem_chuan})")
    
    hoc_sinh_gioi = {}
    for ten, diem in hoc_sinh.items():
        if diem >= diem_chuan:
            hoc_sinh_gioi[ten] = diem
    
    print(f"Học sinh giỏi: {hoc_sinh_gioi}")
    return hoc_sinh_gioi

# Chương trình chính
if __name__ == "__main__":
    # Tạo danh sách học sinh
    danh_sach = tao_danh_sach_hoc_sinh()
    
    print("\n" + "="*50)
    
    # Tìm điểm học sinh
    tim_diem_hoc_sinh(danh_sach, "Bình")
    tim_diem_hoc_sinh(danh_sach, "Nam")  # Không tồn tại
    
    print("\n" + "="*50)
    
    # Thêm học sinh mới
    them_hoc_sinh_moi(danh_sach, "Nam", 6)
    
    print("\n" + "="*50)
    
    # Hiển thị tất cả
    hien_thi_tat_ca_hoc_sinh(danh_sach)
    
    print("\n" + "="*50)
    
    # Tìm học sinh giỏi
    hoc_sinh_gioi = tim_hoc_sinh_gioi(danh_sach, 8)
```

#### Hoạt động mở rộng - "Dictionary lồng nhau"
- **Hoạt động**: Tạo Dictionary chứa thông tin đầy đủ của học sinh
- **Mục tiêu**: Hiểu cách sử dụng Dictionary phức tạp
- **Thử thách**: Tạo hệ thống quản lý lớp học hoàn chỉnh

#### Giải thích các khái niệm Python quan trọng:
```python
# Tạo Dictionary:
hoc_sinh = {}  # Dictionary rỗng
hoc_sinh = {"An": 8, "Bình": 9}  # Dictionary với dữ liệu

# Truy cập giá trị:
diem = hoc_sinh["An"]  # Truy cập theo key

# Kiểm tra key tồn tại:
if "An" in hoc_sinh:  # Kiểm tra key có tồn tại

# Duyệt Dictionary:
for ten, diem in hoc_sinh.items():  # Duyệt key và value
for ten in hoc_sinh.keys():         # Chỉ duyệt key
for diem in hoc_sinh.values():      # Chỉ duyệt value

# Thêm/sửa giá trị:
hoc_sinh["Nam"] = 6  # Thêm hoặc sửa
```

### Phần 4: Tạo chương trình "Tuple và Set" trên Python (20 phút)

#### Bước 1: Tạo file Python mới
```python
# Tạo file: tuple_va_set.py
# Mục tiêu: Sử dụng Tuple và Set
```

#### Bước 2: Lập trình Tuple và Set
```python
def su_dung_tuple():
    """
    Sử dụng Tuple để lưu trữ dữ liệu không thay đổi
    """
    print("=== SỬ DỤNG TUPLE ===")
    
    # Tạo Tuple tọa độ
    toa_do_a = (3, 4)
    toa_do_b = (1, 2)
    
    print(f"Tọa độ điểm A: {toa_do_a}")
    print(f"Tọa độ điểm B: {toa_do_b}")
    
    # Tính khoảng cách
    khoang_cach = ((toa_do_a[0] - toa_do_b[0])**2 + (toa_do_a[1] - toa_do_b[1])**2)**0.5
    print(f"Khoảng cách giữa A và B: {khoang_cach:.2f}")
    
    # Tuple điểm số
    diem_toan = (8, 9, 7, 10, 6)
    print(f"Điểm toán: {diem_toan}")
    print(f"Điểm cao nhất: {max(diem_toan)}")
    print(f"Điểm thấp nhất: {min(diem_toan)}")
    
    return toa_do_a, toa_do_b

def su_dung_set():
    """
    Sử dụng Set để loại bỏ trùng lặp
    """
    print("\n=== SỬ DỤNG SET ===")
    
    # Danh sách có trùng lặp
    danh_sach_trung_lap = [1, 2, 3, 2, 4, 3, 5, 1]
    print(f"Danh sách có trùng lặp: {danh_sach_trung_lap}")
    
    # Chuyển thành Set để loại bỏ trùng lặp
    set_khong_trung = set(danh_sach_trung_lap)
    print(f"Set không trùng lặp: {set_khong_trung}")
    
    # Set các môn học
    mon_hoc_lop_5a = {"Toán", "Tiếng Việt", "Khoa học", "Lịch sử"}
    mon_hoc_lop_5b = {"Toán", "Tiếng Việt", "Địa lý", "Mỹ thuật"}
    
    print(f"Môn học lớp 5A: {mon_hoc_lop_5a}")
    print(f"Môn học lớp 5B: {mon_hoc_lop_5b}")
    
    # Tìm môn học chung
    mon_chung = mon_hoc_lop_5a.intersection(mon_hoc_lop_5b)
    print(f"Môn học chung: {mon_chung}")
    
    # Tìm môn học khác biệt
    mon_khac_biet = mon_hoc_lop_5a.symmetric_difference(mon_hoc_lop_5b)
    print(f"Môn học khác biệt: {mon_khac_biet}")
    
    # Tất cả môn học
    tat_ca_mon = mon_hoc_lop_5a.union(mon_hoc_lop_5b)
    print(f"Tất cả môn học: {tat_ca_mon}")
    
    return set_khong_trung, mon_hoc_lop_5a, mon_hoc_lop_5b

def so_sanh_cac_cau_truc():
    """
    So sánh các cấu trúc dữ liệu
    """
    print("\n=== SO SÁNH CÁC CẤU TRÚC DỮ LIỆU ===")
    
    # List (danh sách)
    danh_sach = [1, 2, 3, 2, 4]
    print(f"List: {danh_sach} - Có thể thay đổi, có trùng lặp")
    
    # Tuple (bộ)
    bo_du_lieu = (1, 2, 3, 2, 4)
    print(f"Tuple: {bo_du_lieu} - Không thể thay đổi, có trùng lặp")
    
    # Set (tập hợp)
    tap_hop = {1, 2, 3, 4}
    print(f"Set: {tap_hop} - Có thể thay đổi, không trùng lặp")
    
    # Dictionary (từ điển)
    tu_dien = {"a": 1, "b": 2, "c": 3}
    print(f"Dictionary: {tu_dien} - Key-Value pairs")

# Chương trình chính
if __name__ == "__main__":
    # Sử dụng Tuple
    toa_do_a, toa_do_b = su_dung_tuple()
    
    # Sử dụng Set
    set_khong_trung, mon_5a, mon_5b = su_dung_set()
    
    # So sánh các cấu trúc
    so_sanh_cac_cau_truc()
    
    print(f"\n=== KẾT QUẢ TỔNG HỢP ===")
    print(f"Tọa độ A: {toa_do_a}")
    print(f"Tọa độ B: {toa_do_b}")
    print(f"Set không trùng lặp: {set_khong_trung}")
    print(f"Môn học lớp 5A: {mon_5a}")
    print(f"Môn học lớp 5B: {mon_5b}")
```

#### Hoạt động mở rộng - "Cấu trúc dữ liệu lồng nhau"
- **Hoạt động**: Tạo Dictionary chứa List và Tuple
- **Mục tiêu**: Hiểu cách kết hợp các cấu trúc dữ liệu
- **Thử thách**: Tạo hệ thống quản lý trường học

## 🎯 Tổng kết và đánh giá (10 phút)

### Tổng kết kiến thức
- **Cấu trúc dữ liệu**: Cách tổ chức và lưu trữ dữ liệu
- **Dictionary**: Key-Value pairs, tìm kiếm nhanh
- **Tuple**: Dữ liệu không thay đổi, tọa độ, điểm số
- **Set**: Loại bỏ trùng lặp, phép toán tập hợp
- **Ứng dụng**: Quản lý thông tin, tìm kiếm, phân tích dữ liệu

### Đánh giá học sinh
- **Hiểu cấu trúc dữ liệu**: Có thể giải thích sự khác biệt giữa các cấu trúc
- **Áp dụng thực tế**: Tìm được ví dụ sử dụng cấu trúc dữ liệu trong cuộc sống
- **Lập trình Python**: Tạo được chương trình sử dụng Dictionary, Tuple, Set
- **Tư duy logic**: Chọn được cấu trúc dữ liệu phù hợp cho bài toán

## 🎨 Hoạt động mở rộng

### Cấp độ 1: Thêm tính năng cơ bản
- **Giao diện tương tác**: Tạo menu để chọn loại cấu trúc dữ liệu
- **Hiệu ứng trực quan**: Thêm màu sắc khi hiển thị dữ liệu
- **Âm thanh**: Tạo âm thanh khác nhau cho từng loại thao tác

### Cấp độ 2: Tính năng nâng cao
- **Cấu trúc lồng nhau**: Dictionary chứa List và Tuple
- **Xử lý dữ liệu phức tạp**: Đọc và ghi file với cấu trúc dữ liệu
- **Tối ưu hóa**: So sánh hiệu suất của các cấu trúc dữ liệu

### Cấp độ 3: Sáng tạo
- **Game cấu trúc dữ liệu**: Tạo trò chơi sử dụng các cấu trúc dữ liệu
- **Thuật toán riêng**: Thiết kế thuật toán sử dụng cấu trúc dữ liệu mới
- **Dự án tích hợp**: Kết hợp cấu trúc dữ liệu với các thuật toán đã học

## 📝 Bài tập về nhà

### Bài tập bắt buộc
1. **Quản lý học sinh**: Tạo Dictionary quản lý điểm số lớp
2. **Tọa độ**: Sử dụng Tuple lưu trữ tọa độ các điểm
3. **Loại bỏ trùng lặp**: Sử dụng Set loại bỏ số trùng lặp

### Bài tập nâng cao
1. **Cấu trúc lồng nhau**: Tạo Dictionary chứa thông tin đầy đủ học sinh
2. **Phép toán tập hợp**: So sánh danh sách môn học của các lớp
3. **Tối ưu hóa**: So sánh hiệu suất tìm kiếm giữa List và Dictionary

### Bài tập sáng tạo
1. **Game cấu trúc dữ liệu**: Tạo game sử dụng các cấu trúc dữ liệu
2. **Thuật toán riêng**: Thiết kế thuật toán sử dụng cấu trúc dữ liệu độc đáo
3. **Dự án tích hợp**: Kết hợp cấu trúc dữ liệu với sắp xếp và tìm kiếm

## 🔧 Tài nguyên hỗ trợ

### Tài liệu tham khảo
- **Python Programming**: Hướng dẫn lập trình Python cơ bản
- **Data Structures**: Cấu trúc dữ liệu trong Python
- **Python Collections**: Các kiểu dữ liệu collection trong Python

### Công cụ hỗ trợ
- **Python Editor**: Môi trường lập trình Python
- **Data Structure Simulator**: Mô phỏng cấu trúc dữ liệu
- **Debugging Tools**: Công cụ gỡ lỗi và tối ưu hóa

### Đánh giá và phản hồi
- **Rubric đánh giá**: Tiêu chí đánh giá kỹ năng cấu trúc dữ liệu
- **Peer Review**: Đánh giá lẫn nhau giữa học sinh
- **Portfolio**: Tập hợp các dự án và bài tập của học sinh
