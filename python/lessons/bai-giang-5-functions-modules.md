# Bài giảng 5: Functions và Modules Python - Lập trình modular

## 📋 Thông tin bài học
- **Thời gian**: 90 phút
- **Độ tuổi**: 11-12 tuổi
- **Trình độ**: Trung bình đến nâng cao
- **Mục tiêu**: Hiểu và sử dụng Functions và Modules trong Python

## 🎯 Mục tiêu học tập

### Kiến thức
- Hiểu khái niệm Function và tầm quan trọng
- Nắm vững cách tạo và sử dụng Functions
- Hiểu Modules và cách tổ chức code
- Biết cách tái sử dụng code hiệu quả

### Kỹ năng
- Phân tích và thiết kế Functions
- Áp dụng Functions vào lập trình Python
- Sử dụng Parameters và Return values
- Tạo Modules và import functions

### Thái độ
- Phát triển tư duy modular programming
- Rèn luyện tính cẩn thận với code structure
- Khuyến khích tư duy tái sử dụng code

## 🧠 Nội dung bài học

## 📚 PHẦN LÝ THUYẾT (45 phút)

### Phần 1: Khái niệm Function qua hoạt động không máy tính (25 phút)

#### Hoạt động khởi động - "Kết nối với thuật toán"
- **Hoạt động**: Nhắc lại bài 2.5 về thuật toán sắp xếp
- **Câu hỏi**: "Chúng ta đã học cách sắp xếp như thế nào?"
- **Kết nối**: "Hôm nay chúng ta sẽ học cách tạo công thức sắp xếp có thể dùng lại"
- **Mục tiêu**: Kết nối thuật toán với Functions

#### Khái niệm Function qua ví dụ thực tế
- **Định nghĩa**: Function là một khối code có thể gọi lại nhiều lần
- **Ví dụ**: Máy tính bỏ túi - mỗi phím là một function
- **Input**: Parameters (tham số đầu vào)
- **Process**: Thực hiện các bước xử lý
- **Output**: Return value (giá trị trả về)
- **Ứng dụng**: Tái sử dụng code, tổ chức code rõ ràng

#### Hoạt động thực hành - "Công thức nấu ăn"
- **Hoạt động**: Học sinh viết công thức nấu món ăn đơn giản
- **Mục tiêu**: Hiểu khái niệm Function qua trải nghiệm thực tế
- **Quy tắc**: Công thức có nguyên liệu (input), các bước (process), kết quả (output)
- **Kết quả**: Nhận ra Function giống như công thức có thể dùng lại

### Phần 2: Parameters và Return values qua hoạt động không máy tính (20 phút)

#### Hoạt động không máy tính - "Máy tính đơn giản"
- **Hoạt động**: Học sinh đóng vai máy tính với các phép tính
- **Mục tiêu**: Hiểu cách Function nhận input và trả output
- **Quy tắc**: Người A nói "5 + 3", người B trả lời "8"
- **Kết quả**: Nhận ra Function cần input và cho output

#### Bài toán: Tính diện tích hình chữ nhật
- **Input**: Chiều dài và chiều rộng
- **Process**: Diện tích = dài × rộng
- **Output**: Diện tích
- **Ví dụ**: Tính diện tích phòng học

#### Function qua ví dụ thực tế
```
Function: tinh_dien_tich(dai, rong)
Input: dai = 5, rong = 3
Process: dien_tich = 5 × 3 = 15
Output: 15

Function: tinh_dien_tich(dai, rong)
Input: dai = 8, rong = 4
Process: dien_tich = 8 × 4 = 32
Output: 32
```

#### Hoạt động không máy tính - "So sánh với code cũ"
- **Hoạt động**: So sánh cách tính diện tích với và không có Function
- **Mục tiêu**: Hiểu ưu điểm của Functions
- **Kết quả**: Nhận ra Functions giúp code ngắn gọn và dễ hiểu

## 💻 PHẦN THỰC HÀNH PYTHON (45 phút)

### Phần 3: Tạo Functions cơ bản trên Python (25 phút)

#### Bước 1: Tạo file Python mới
```python
# Tạo file: functions_co_ban.py
# Mục tiêu: Tạo và sử dụng Functions cơ bản
```

#### Bước 2: Lập trình Functions cơ bản
```python
def chao_hoi(ten):
    """
    Function chào hỏi
    Input: ten (string) - Tên người
    Output: None - Chỉ in ra màn hình
    """
    print(f"Xin chào {ten}!")
    print("Chúc bạn học Python vui vẻ!")

def tinh_dien_tich_hcn(dai, rong):
    """
    Function tính diện tích hình chữ nhật
    Input: dai (number), rong (number)
    Output: dien_tich (number)
    """
    print(f"Tính diện tích hình chữ nhật: {dai} × {rong}")
    dien_tich = dai * rong
    print(f"Diện tích = {dien_tich}")
    return dien_tich

def tinh_chu_vi_hcn(dai, rong):
    """
    Function tính chu vi hình chữ nhật
    Input: dai (number), rong (number)
    Output: chu_vi (number)
    """
    print(f"Tính chu vi hình chữ nhật: ({dai} + {rong}) × 2")
    chu_vi = (dai + rong) * 2
    print(f"Chu vi = {chu_vi}")
    return chu_vi

def kiem_tra_so_chan(so):
    """
    Function kiểm tra số chẵn
    Input: so (number)
    Output: True/False
    """
    print(f"Kiểm tra số {so} có phải số chẵn không?")
    if so % 2 == 0:
        print(f"{so} là số chẵn")
        return True
    else:
        print(f"{so} là số lẻ")
        return False

def tim_so_lon_nhat(so1, so2, so3):
    """
    Function tìm số lớn nhất trong 3 số
    Input: so1, so2, so3 (numbers)
    Output: so_lon_nhat (number)
    """
    print(f"Tìm số lớn nhất trong: {so1}, {so2}, {so3}")
    
    so_lon_nhat = so1
    if so2 > so_lon_nhat:
        so_lon_nhat = so2
    if so3 > so_lon_nhat:
        so_lon_nhat = so3
    
    print(f"Số lớn nhất là: {so_lon_nhat}")
    return so_lon_nhat

# Chương trình chính
if __name__ == "__main__":
    print("=== DEMO FUNCTIONS CƠ BẢN ===\n")
    
    # Sử dụng function chào hỏi
    chao_hoi("An")
    chao_hoi("Bình")
    
    print("\n" + "="*50)
    
    # Sử dụng function tính diện tích
    dien_tich1 = tinh_dien_tich_hcn(5, 3)
    dien_tich2 = tinh_dien_tich_hcn(8, 4)
    
    print(f"\nKết quả: Diện tích 1 = {dien_tich1}, Diện tích 2 = {dien_tich2}")
    
    print("\n" + "="*50)
    
    # Sử dụng function tính chu vi
    chu_vi1 = tinh_chu_vi_hcn(5, 3)
    chu_vi2 = tinh_chu_vi_hcn(8, 4)
    
    print(f"\nKết quả: Chu vi 1 = {chu_vi1}, Chu vi 2 = {chu_vi2}")
    
    print("\n" + "="*50)
    
    # Sử dụng function kiểm tra số chẵn
    kiem_tra_so_chan(8)
    kiem_tra_so_chan(7)
    
    print("\n" + "="*50)
    
    # Sử dụng function tìm số lớn nhất
    so_lon_nhat1 = tim_so_lon_nhat(5, 8, 3)
    so_lon_nhat2 = tim_so_lon_nhat(10, 2, 9)
    
    print(f"\nKết quả: Số lớn nhất 1 = {so_lon_nhat1}, Số lớn nhất 2 = {so_lon_nhat2}")
```

#### Hoạt động mở rộng - "Functions với nhiều parameters"
- **Hoạt động**: Tạo Function tính điểm trung bình của nhiều môn
- **Mục tiêu**: Hiểu cách sử dụng nhiều parameters
- **Thử thách**: Tạo Function với default parameters

#### Giải thích các khái niệm Python quan trọng:
```python
# Định nghĩa function:
def ten_function(parameter1, parameter2):
    # Code xử lý
    return ket_qua

# Gọi function:
ket_qua = ten_function(gia_tri1, gia_tri2)

# Function không có return:
def in_thong_tin(ten):
    print(f"Tên: {ten}")
    # Không có return (trả về None)

# Function có return:
def tinh_toan(a, b):
    ket_qua = a + b
    return ket_qua
```

### Phần 4: Tạo Modules và tổ chức code (20 phút)

#### Bước 1: Tạo file Module
```python
# Tạo file: toan_hoc.py
# Mục tiêu: Module chứa các functions toán học
```

#### Bước 2: Lập trình Module toán học
```python
# File: toan_hoc.py
"""
Module toán học - chứa các functions tính toán cơ bản
"""

def cong(a, b):
    """Cộng hai số"""
    return a + b

def tru(a, b):
    """Trừ hai số"""
    return a - b

def nhan(a, b):
    """Nhân hai số"""
    return a * b

def chia(a, b):
    """Chia hai số"""
    if b != 0:
        return a / b
    else:
        print("Lỗi: Không thể chia cho 0!")
        return None

def luy_thua(a, b):
    """Tính lũy thừa a^b"""
    return a ** b

def can_bac_hai(a):
    """Tính căn bậc hai"""
    if a >= 0:
        return a ** 0.5
    else:
        print("Lỗi: Không thể tính căn bậc hai của số âm!")
        return None

def tinh_dien_tich_hinh_tron(ban_kinh):
    """Tính diện tích hình tròn"""
    import math
    return math.pi * ban_kinh ** 2

def tinh_chu_vi_hinh_tron(ban_kinh):
    """Tính chu vi hình tròn"""
    import math
    return 2 * math.pi * ban_kinh
```

#### Bước 3: Sử dụng Module
```python
# Tạo file: su_dung_module.py
# Mục tiêu: Sử dụng Module toán học

# Import toàn bộ module
import toan_hoc

# Import specific functions
from toan_hoc import cong, tru, nhan, chia

def demo_module():
    """
    Demo sử dụng Module toán học
    """
    print("=== DEMO MODULE TOÁN HỌC ===\n")
    
    # Sử dụng functions từ module
    print("Sử dụng import toan_hoc:")
    ket_qua1 = toan_hoc.cong(5, 3)
    ket_qua2 = toan_hoc.nhan(4, 6)
    print(f"5 + 3 = {ket_qua1}")
    print(f"4 × 6 = {ket_qua2}")
    
    print("\n" + "="*50)
    
    # Sử dụng functions đã import
    print("Sử dụng from toan_hoc import:")
    ket_qua3 = cong(10, 5)
    ket_qua4 = tru(10, 5)
    print(f"10 + 5 = {ket_qua3}")
    print(f"10 - 5 = {ket_qua4}")
    
    print("\n" + "="*50)
    
    # Sử dụng functions phức tạp
    print("Sử dụng functions phức tạp:")
    dien_tich = toan_hoc.tinh_dien_tich_hinh_tron(3)
    chu_vi = toan_hoc.tinh_chu_vi_hinh_tron(3)
    print(f"Diện tích hình tròn (r=3): {dien_tich:.2f}")
    print(f"Chu vi hình tròn (r=3): {chu_vi:.2f}")
    
    print("\n" + "="*50)
    
    # Xử lý lỗi
    print("Xử lý lỗi:")
    ket_qua_chia = chia(10, 0)
    ket_qua_can = toan_hoc.can_bac_hai(-4)

# Chương trình chính
if __name__ == "__main__":
    demo_module()
```

#### Hoạt động mở rộng - "Tạo Module riêng"
- **Hoạt động**: Tạo Module quản lý học sinh
- **Mục tiêu**: Hiểu cách tổ chức code thành modules
- **Thử thách**: Tạo hệ thống modules hoàn chỉnh

## 🎯 Tổng kết và đánh giá (10 phút)

### Tổng kết kiến thức
- **Function**: Khối code có thể gọi lại nhiều lần
- **Parameters**: Dữ liệu đầu vào của function
- **Return values**: Dữ liệu trả về của function
- **Modules**: Cách tổ chức code thành các file riêng biệt
- **Import**: Cách sử dụng functions từ modules khác

### Đánh giá học sinh
- **Hiểu Functions**: Có thể giải thích khái niệm function và cách hoạt động
- **Áp dụng thực tế**: Tìm được ví dụ sử dụng functions trong cuộc sống
- **Lập trình Python**: Tạo được functions và modules hoạt động
- **Tư duy modular**: Tổ chức code thành các phần có thể tái sử dụng

## 🎨 Hoạt động mở rộng

### Cấp độ 1: Thêm tính năng cơ bản
- **Giao diện tương tác**: Tạo menu để chọn functions
- **Hiệu ứng trực quan**: Thêm màu sắc khi hiển thị kết quả
- **Âm thanh**: Tạo âm thanh khác nhau cho từng loại function

### Cấp độ 2: Tính năng nâng cao
- **Functions phức tạp**: Tạo functions với nhiều parameters
- **Error handling**: Xử lý lỗi trong functions
- **Documentation**: Viết docstring chi tiết cho functions

### Cấp độ 3: Sáng tạo
- **Game functions**: Tạo game sử dụng nhiều functions
- **Module riêng**: Thiết kế hệ thống modules hoàn chỉnh
- **Dự án tích hợp**: Kết hợp functions với các thuật toán đã học

## 📝 Bài tập về nhà

### Bài tập bắt buộc
1. **Functions cơ bản**: Tạo functions tính toán đơn giản
2. **Functions với parameters**: Tạo functions nhận nhiều tham số
3. **Modules**: Tạo module chứa các functions liên quan

### Bài tập nâng cao
1. **Functions phức tạp**: Tạo functions với logic phức tạp
2. **Error handling**: Xử lý lỗi trong functions
3. **Tối ưu hóa**: Tối ưu hóa performance của functions

### Bài tập sáng tạo
1. **Game functions**: Tạo game sử dụng nhiều functions
2. **Module riêng**: Thiết kế hệ thống modules độc đáo
3. **Dự án tích hợp**: Kết hợp functions với cấu trúc dữ liệu và thuật toán

## 🔧 Tài nguyên hỗ trợ

### Tài liệu tham khảo
- **Python Programming**: Hướng dẫn lập trình Python cơ bản
- **Functions in Python**: Functions và cách sử dụng
- **Python Modules**: Modules và cách tổ chức code

### Công cụ hỗ trợ
- **Python Editor**: Môi trường lập trình Python
- **Function Simulator**: Mô phỏng hoạt động của functions
- **Debugging Tools**: Công cụ gỡ lỗi và tối ưu hóa

### Đánh giá và phản hồi
- **Rubric đánh giá**: Tiêu chí đánh giá kỹ năng functions
- **Peer Review**: Đánh giá lẫn nhau giữa học sinh
- **Portfolio**: Tập hợp các dự án và bài tập của học sinh
