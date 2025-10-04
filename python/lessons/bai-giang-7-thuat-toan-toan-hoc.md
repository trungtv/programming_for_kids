# Bài giảng 7: Thuật toán toán học - Số nguyên tố, giai thừa và Fibonacci

## 📋 Thông tin bài học
- **Thời gian**: 90 phút
- **Độ tuổi**: 11-12 tuổi
- **Trình độ**: Nâng cao
- **Mục tiêu**: Hiểu và áp dụng thuật toán toán học trong Python

## 🎯 Mục tiêu học tập

### Kiến thức
- Hiểu khái niệm số nguyên tố và cách kiểm tra
- Nắm vững thuật toán tính giai thừa
- Hiểu dãy Fibonacci và cách tính
- Biết cách áp dụng thuật toán toán học vào thực tế

### Kỹ năng
- Phân tích và thiết kế thuật toán toán học
- Áp dụng thuật toán toán học vào lập trình Python
- Sử dụng vòng lặp và điều kiện cho tính toán
- Debug và tối ưu hóa code toán học

### Thái độ
- Phát triển tư duy logic toán học
- Rèn luyện tính cẩn thận với số học
- Khuyến khích tư duy sáng tạo với toán học

## 🧠 Nội dung bài học

## 📚 PHẦN LÝ THUYẾT (45 phút)

### Phần 1: Khái niệm số nguyên tố qua hoạt động không máy tính (25 phút)

#### Hoạt động khởi động - "Kết nối với toán học"
- **Hoạt động**: Nhắc lại bài 3.5 về xử lý chuỗi
- **Câu hỏi**: "Chúng ta đã học cách xử lý văn bản như thế nào?"
- **Kết nối**: "Hôm nay chúng ta sẽ học cách xử lý số học"
- **Mục tiêu**: Kết nối xử lý chuỗi với xử lý số học

#### Khái niệm số nguyên tố qua ví dụ thực tế
- **Định nghĩa**: Số nguyên tố là số tự nhiên lớn hơn 1, chỉ chia hết cho 1 và chính nó
- **Ví dụ**: 2, 3, 5, 7, 11, 13, 17, 19, 23, 29...
- **Input**: Số cần kiểm tra (ví dụ: 17)
- **Output**: True (là số nguyên tố) hoặc False (không phải)
- **Ứng dụng**: Mã hóa, bảo mật, toán học thuần túy

#### Hoạt động thực hành - "Tìm số nguyên tố"
- **Hoạt động**: Học sinh kiểm tra các số từ 2 đến 20 xem số nào là nguyên tố
- **Mục tiêu**: Hiểu khái niệm số nguyên tố qua trải nghiệm thực tế
- **Quy tắc**: Chia số cho các số từ 2 đến số đó-1, nếu không chia hết thì là nguyên tố
- **Kết quả**: Nhận ra số nguyên tố có tính chất đặc biệt

### Phần 2: Thuật toán tính giai thừa qua hoạt động không máy tính (20 phút)

#### Hoạt động không máy tính - "Tính giai thừa bằng tay"
- **Hoạt động**: Học sinh tính 5! = 5 × 4 × 3 × 2 × 1 = 120
- **Mục tiêu**: Hiểu cách thuật toán tính giai thừa hoạt động
- **Quy tắc**: Nhân số với tất cả số nhỏ hơn nó
- **Kết quả**: Nhận ra giai thừa tăng rất nhanh

#### Bài toán: Tính số cách sắp xếp
- **Input**: Số học sinh (ví dụ: 5)
- **Output**: Số cách sắp xếp (5! = 120)
- **Ví dụ**: Sắp xếp 5 học sinh thành hàng

#### Thuật toán tính giai thừa qua ví dụ thực tế
```
5! = 5 × 4 × 3 × 2 × 1
Bước 1: Kết quả = 1
Bước 2: Kết quả = 1 × 5 = 5
Bước 3: Kết quả = 5 × 4 = 20
Bước 4: Kết quả = 20 × 3 = 60
Bước 5: Kết quả = 60 × 2 = 120
Bước 6: Kết quả = 120 × 1 = 120
```

#### Hoạt động không máy tính - "Dãy Fibonacci"
- **Hoạt động**: Học sinh viết dãy Fibonacci: 1, 1, 2, 3, 5, 8, 13...
- **Mục tiêu**: Hiểu quy luật của dãy Fibonacci
- **Quy tắc**: Mỗi số bằng tổng của 2 số trước đó
- **Kết quả**: Nhận ra dãy Fibonacci có quy luật đặc biệt

## 💻 PHẦN THỰC HÀNH PYTHON (45 phút)

### Phần 3: Tạo chương trình "Kiểm tra số nguyên tố" trên Python (25 phút)

#### Bước 1: Tạo file Python mới
```python
# Tạo file: kiem_tra_so_nguyen_to.py
# Mục tiêu: Kiểm tra số nguyên tố
```

#### Bước 2: Lập trình thuật toán kiểm tra số nguyên tố
```python
def kiem_tra_so_nguyen_to(so):
    """
    Kiểm tra xem một số có phải là số nguyên tố không
    """
    print(f"Đang kiểm tra số {so} có phải là số nguyên tố không...")
    
    # Số nhỏ hơn 2 không phải số nguyên tố
    if so < 2:
        print(f"{so} không phải là số nguyên tố (nhỏ hơn 2)")
        return False
    
    # Kiểm tra từ 2 đến căn bậc hai của số
    for i in range(2, int(so ** 0.5) + 1):
        print(f"Kiểm tra {so} có chia hết cho {i} không?")
        if so % i == 0:
            print(f"Có! {so} chia hết cho {i}, nên không phải số nguyên tố")
            return False
        else:
            print(f"Không, {so} không chia hết cho {i}")
    
    print(f"{so} là số nguyên tố!")
    return True

def tim_so_nguyen_to_trong_khoang(bat_dau, ket_thuc):
    """
    Tìm tất cả số nguyên tố trong một khoảng
    """
    print(f"Tìm số nguyên tố từ {bat_dau} đến {ket_thuc}")
    
    so_nguyen_to = []
    for so in range(bat_dau, ket_thuc + 1):
        if kiem_tra_so_nguyen_to(so):
            so_nguyen_to.append(so)
    
    print(f"Các số nguyên tố trong khoảng [{bat_dau}, {ket_thuc}]: {so_nguyen_to}")
    return so_nguyen_to

# Chương trình chính
if __name__ == "__main__":
    # Kiểm tra một số cụ thể
    so_can_kiem_tra = 17
    ket_qua = kiem_tra_so_nguyen_to(so_can_kiem_tra)
    
    # Tìm số nguyên tố trong khoảng
    print("\n" + "="*50)
    so_nguyen_to = tim_so_nguyen_to_trong_khoang(2, 20)
    
    print(f"\nKết quả: Tìm thấy {len(so_nguyen_to)} số nguyên tố")
```

#### Hoạt động mở rộng - "Tối ưu hóa thuật toán"
- **Hoạt động**: So sánh thuật toán kiểm tra từ 2 đến n-1 với thuật toán kiểm tra đến căn bậc hai
- **Mục tiêu**: Hiểu cách tối ưu hóa thuật toán
- **Thử thách**: Tạo thuật toán kiểm tra số nguyên tố nhanh nhất

#### Giải thích các khái niệm Python quan trọng:
```python
# Vòng lặp với range:
for i in range(2, int(so ** 0.5) + 1):  # Duyệt từ 2 đến căn bậc hai

# Phép chia lấy dư:
if so % i == 0:  # Kiểm tra chia hết

# Lũy thừa:
so ** 0.5  # Căn bậc hai

# Chuyển đổi kiểu:
int(so ** 0.5)  # Chuyển float thành int
```

### Phần 4: Tạo chương trình "Tính giai thừa và Fibonacci" trên Python (20 phút)

#### Bước 1: Tạo file Python mới
```python
# Tạo file: tinh_giai_thua_fibonacci.py
# Mục tiêu: Tính giai thừa và dãy Fibonacci
```

#### Bước 2: Lập trình thuật toán tính giai thừa và Fibonacci
```python
def tinh_giai_thua(n):
    """
    Tính giai thừa của n: n! = n × (n-1) × ... × 1
    """
    print(f"Đang tính {n}!...")
    
    if n < 0:
        print("Giai thừa không được định nghĩa cho số âm!")
        return None
    
    if n == 0 or n == 1:
        print(f"{n}! = 1")
        return 1
    
    ket_qua = 1
    print(f"Bắt đầu với kết quả = 1")
    
    for i in range(1, n + 1):
        ket_qua *= i
        print(f"Bước {i}: kết quả = {ket_qua}")
    
    print(f"{n}! = {ket_qua}")
    return ket_qua

def tinh_fibonacci(n):
    """
    Tính số Fibonacci thứ n
    """
    print(f"Đang tính số Fibonacci thứ {n}...")
    
    if n <= 0:
        print("Số Fibonacci phải lớn hơn 0!")
        return None
    
    if n == 1 or n == 2:
        print(f"F({n}) = 1")
        return 1
    
    # Khởi tạo 2 số đầu tiên
    f1 = 1  # F(1)
    f2 = 1  # F(2)
    
    print(f"F(1) = 1")
    print(f"F(2) = 1")
    
    # Tính từ F(3) đến F(n)
    for i in range(3, n + 1):
        f_tiep_theo = f1 + f2
        print(f"F({i}) = F({i-1}) + F({i-2}) = {f2} + {f1} = {f_tiep_theo}")
        
        # Cập nhật cho lần tiếp theo
        f1 = f2
        f2 = f_tiep_theo
    
    print(f"F({n}) = {f2}")
    return f2

def in_day_fibonacci(n):
    """
    In n số đầu tiên của dãy Fibonacci
    """
    print(f"In {n} số đầu tiên của dãy Fibonacci:")
    
    if n <= 0:
        print("Số lượng phải lớn hơn 0!")
        return []
    
    day_fibonacci = []
    
    if n >= 1:
        day_fibonacci.append(1)
        print("F(1) = 1")
    
    if n >= 2:
        day_fibonacci.append(1)
        print("F(2) = 1")
    
    # Tính các số tiếp theo
    for i in range(3, n + 1):
        f_tiep_theo = day_fibonacci[i-2] + day_fibonacci[i-3]
        day_fibonacci.append(f_tiep_theo)
        print(f"F({i}) = {f_tiep_theo}")
    
    print(f"Dãy Fibonacci: {day_fibonacci}")
    return day_fibonacci

# Chương trình chính
if __name__ == "__main__":
    # Tính giai thừa
    print("=== TÍNH GIAI THỪA ===")
    giai_thua_5 = tinh_giai_thua(5)
    
    print("\n" + "="*50)
    
    # Tính số Fibonacci
    print("=== TÍNH SỐ FIBONACCI ===")
    fib_10 = tinh_fibonacci(10)
    
    print("\n" + "="*50)
    
    # In dãy Fibonacci
    print("=== DÃY FIBONACCI ===")
    day_fib = in_day_fibonacci(10)
    
    print(f"\n=== KẾT QUẢ TỔNG HỢP ===")
    print(f"5! = {giai_thua_5}")
    print(f"F(10) = {fib_10}")
    print(f"Dãy Fibonacci 10 số đầu: {day_fib}")
```

#### Hoạt động mở rộng - "So sánh hiệu suất"
- **Hoạt động**: So sánh thời gian tính giai thừa và Fibonacci với các giá trị khác nhau
- **Mục tiêu**: Hiểu cách đánh giá hiệu suất thuật toán toán học
- **Thử thách**: Tạo thuật toán tính Fibonacci nhanh nhất

## 🎯 Tổng kết và đánh giá (10 phút)

### Tổng kết kiến thức
- **Số nguyên tố**: Số chỉ chia hết cho 1 và chính nó
- **Giai thừa**: Tích của tất cả số từ 1 đến n
- **Dãy Fibonacci**: Mỗi số bằng tổng của 2 số trước đó
- **Thuật toán toán học**: Cần độ chính xác cao và tối ưu hóa
- **Ứng dụng**: Mã hóa, bảo mật, toán học thuần túy

### Đánh giá học sinh
- **Hiểu thuật toán**: Có thể giải thích các bước của thuật toán toán học
- **Áp dụng thực tế**: Tìm được ví dụ ứng dụng toán học trong cuộc sống
- **Lập trình Python**: Tạo được chương trình toán học hoạt động
- **Tư duy logic**: Phân tích và thiết kế thuật toán toán học

## 🎨 Hoạt động mở rộng

### Cấp độ 1: Thêm tính năng cơ bản
- **Giao diện tương tác**: Tạo menu để chọn loại tính toán
- **Hiệu ứng trực quan**: Thêm màu sắc khi hiển thị kết quả
- **Âm thanh**: Tạo âm thanh khác nhau cho từng loại tính toán

### Cấp độ 2: Tính năng nâng cao
- **Tính toán phức tạp**: Tính giai thừa và Fibonacci với số lớn
- **Tối ưu hóa**: Sử dụng thuật toán nhanh nhất
- **So sánh hiệu suất**: Đo thời gian thực thi của các thuật toán

### Cấp độ 3: Sáng tạo
- **Game toán học**: Tạo trò chơi đoán số nguyên tố
- **Thuật toán riêng**: Thiết kế thuật toán toán học mới
- **Dự án tích hợp**: Kết hợp toán học với các thuật toán đã học

## 📝 Bài tập về nhà

### Bài tập bắt buộc
1. **Kiểm tra số nguyên tố**: Viết thuật toán kiểm tra số nguyên tố
2. **Tính giai thừa**: Tạo chương trình tính giai thừa
3. **Dãy Fibonacci**: Viết chương trình tính dãy Fibonacci

### Bài tập nâng cao
1. **Tính toán phức tạp**: Tính giai thừa và Fibonacci với số lớn
2. **Tối ưu hóa**: Tìm thuật toán nhanh nhất cho từng bài toán
3. **Ứng dụng thực tế**: Tạo chương trình giải bài toán thực tế

### Bài tập sáng tạo
1. **Game toán học**: Tạo game đoán số nguyên tố với giao diện đẹp
2. **Thuật toán riêng**: Thiết kế thuật toán toán học độc đáo
3. **Dự án tích hợp**: Kết hợp toán học với sắp xếp và tìm kiếm

## 🔧 Tài nguyên hỗ trợ

### Tài liệu tham khảo
- **Python Programming**: Hướng dẫn lập trình Python cơ bản
- **Mathematical Algorithms**: Thuật toán toán học cơ bản
- **Number Theory**: Lý thuyết số cho học sinh

### Công cụ hỗ trợ
- **Python Editor**: Môi trường lập trình Python
- **Mathematical Simulator**: Mô phỏng thuật toán toán học
- **Debugging Tools**: Công cụ gỡ lỗi và tối ưu hóa

### Đánh giá và phản hồi
- **Rubric đánh giá**: Tiêu chí đánh giá kỹ năng toán học
- **Peer Review**: Đánh giá lẫn nhau giữa học sinh
- **Portfolio**: Tập hợp các dự án và bài tập của học sinh
