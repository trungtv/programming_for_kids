# Bài giảng 3.5: Thuật toán xử lý chuỗi - Tìm kiếm, đếm và chuyển đổi

## 📋 Thông tin bài học
- **Thời gian**: 90 phút
- **Độ tuổi**: 11-12 tuổi
- **Trình độ**: Trung bình
- **Mục tiêu**: Hiểu và áp dụng thuật toán xử lý chuỗi trong Python

## 🎯 Mục tiêu học tập

### Kiến thức
- Hiểu khái niệm chuỗi và các thao tác cơ bản
- Nắm vững thuật toán tìm kiếm trong chuỗi
- Hiểu thuật toán đếm ký tự và từ
- Biết cách chuyển đổi chuỗi (upper, lower, reverse)

### Kỹ năng
- Phân tích và thiết kế thuật toán xử lý chuỗi
- Áp dụng thuật toán chuỗi vào lập trình Python
- Sử dụng vòng lặp và điều kiện với chuỗi
- Debug và tối ưu hóa code xử lý chuỗi

### Thái độ
- Phát triển tư duy logic với dữ liệu văn bản
- Rèn luyện tính cẩn thận với chuỗi
- Khuyến khích tư duy sáng tạo với văn bản

## 🧠 Nội dung bài học

## 📚 PHẦN LÝ THUYẾT (45 phút)

### Phần 1: Khái niệm chuỗi qua hoạt động không máy tính (25 phút)

#### Hoạt động khởi động - "Kết nối với tìm kiếm"
- **Hoạt động**: Nhắc lại bài 2 về thuật toán tìm kiếm trong danh sách số
- **Câu hỏi**: "Chúng ta đã học cách tìm số trong danh sách như thế nào?"
- **Kết nối**: "Hôm nay chúng ta sẽ học cách tìm kiếm trong văn bản"
- **Mục tiêu**: Kết nối thuật toán tìm kiếm với xử lý chuỗi

#### Khái niệm chuỗi qua ví dụ thực tế
- **Định nghĩa**: Chuỗi là một dãy các ký tự được sắp xếp theo thứ tự
- **Ví dụ**: Tên học sinh "Nguyễn Văn An", địa chỉ "123 Đường ABC"
- **Input**: Chuỗi "Hello World" và ký tự cần tìm "o"
- **Output**: Vị trí của ký tự (4) hoặc "không tìm thấy"
- **Ứng dụng**: Tìm kiếm trong tài liệu, xử lý văn bản, phân tích dữ liệu

#### Hoạt động thực hành - "Tìm chữ cái trong từ"
- **Hoạt động**: Học sinh tìm chữ cái "a" trong từ "banana"
- **Mục tiêu**: Hiểu khái niệm chuỗi qua trải nghiệm thực tế
- **Quy tắc**: Đếm từng ký tự từ trái sang phải
- **Kết quả**: Nhận ra chuỗi có thể tìm kiếm và đếm

### Phần 2: Thuật toán tìm kiếm trong chuỗi qua hoạt động không máy tính (20 phút)

#### Hoạt động không máy tính - "Tìm từ trong câu"
- **Hoạt động**: Học sinh tìm từ "Python" trong câu "Tôi học Python lập trình"
- **Mục tiêu**: Hiểu cách thuật toán tìm kiếm chuỗi hoạt động
- **Quy tắc**: So sánh từng ký tự một cách tuần tự
- **Kết quả**: Nhận ra tìm kiếm chuỗi phức tạp hơn tìm kiếm số

#### Bài toán: Tìm tên học sinh trong danh sách
- **Input**: Chuỗi "Nguyễn Văn An, Trần Thị Bình, Lê Văn Cường" và tên cần tìm "Bình"
- **Output**: Vị trí của tên (15) hoặc "không tìm thấy"
- **Ví dụ**: Tìm học sinh trong danh sách lớp

#### Thuật toán tìm kiếm chuỗi qua ví dụ thực tế
```
Bước 1: Bắt đầu từ vị trí đầu tiên (0)
Bước 2: So sánh ký tự tại vị trí 0 ("N") với ký tự đầu của "Bình" ("B")
Bước 3: Vì "N" ≠ "B", chuyển sang vị trí tiếp theo (1)
Bước 4: Tiếp tục cho đến khi tìm thấy hoặc hết chuỗi
```

#### Hoạt động không máy tính - "Đếm số lần xuất hiện"
- **Hoạt động**: Học sinh đếm số lần chữ "a" xuất hiện trong từ "banana"
- **Mục tiêu**: Hiểu thuật toán đếm trong chuỗi
- **Kết quả**: Nhận ra đếm chuỗi cần duyệt qua từng ký tự

## 💻 PHẦN THỰC HÀNH PYTHON (45 phút)

### Phần 3: Tạo chương trình "Tìm kiếm trong chuỗi" trên Python (25 phút)

#### Bước 1: Tạo file Python mới
```python
# Tạo file: tim_kiem_chuoi.py
# Mục tiêu: Tìm kiếm ký tự và từ trong chuỗi
```

#### Bước 2: Lập trình thuật toán tìm kiếm ký tự
```python
def tim_ky_tu(chuoi, ky_tu_can_tim):
    """
    Tìm kiếm ký tự trong chuỗi
    Trả về danh sách các vị trí nếu tìm thấy, [] nếu không tìm thấy
    """
    print(f"Đang tìm kiếm '{ky_tu_can_tim}' trong chuỗi: '{chuoi}'")
    
    vi_tri_tim_thay = []
    
    # Duyệt qua từng ký tự
    for i in range(len(chuoi)):
        print(f"Kiểm tra vị trí {i}: '{chuoi[i]}'")
        
        # Nếu tìm thấy
        if chuoi[i] == ky_tu_can_tim:
            vi_tri_tim_thay.append(i)
            print(f"Tìm thấy '{ky_tu_can_tim}' tại vị trí {i}!")
    
    if vi_tri_tim_thay:
        print(f"Tìm thấy '{ky_tu_can_tim}' tại các vị trí: {vi_tri_tim_thay}")
    else:
        print(f"Không tìm thấy '{ky_tu_can_tim}' trong chuỗi")
    
    return vi_tri_tim_thay

def dem_ky_tu(chuoi, ky_tu_can_dem):
    """
    Đếm số lần xuất hiện của ký tự trong chuỗi
    """
    print(f"Đang đếm '{ky_tu_can_dem}' trong chuỗi: '{chuoi}'")
    
    so_lan_xuat_hien = 0
    
    # Duyệt qua từng ký tự
    for ky_tu in chuoi:
        if ky_tu == ky_tu_can_dem:
            so_lan_xuat_hien += 1
    
    print(f"'{ky_tu_can_dem}' xuất hiện {so_lan_xuat_hien} lần")
    return so_lan_xuat_hien

# Chương trình chính
if __name__ == "__main__":
    # Chuỗi mẫu
    chuoi_mau = "Hello World"
    
    # Tìm kiếm ký tự 'l'
    vi_tri = tim_ky_tu(chuoi_mau, 'l')
    
    # Đếm ký tự 'l'
    so_lan = dem_ky_tu(chuoi_mau, 'l')
    
    print(f"\nKết quả: Ký tự 'l' xuất hiện {so_lan} lần tại các vị trí {vi_tri}")
```

#### Hoạt động mở rộng - "Tìm kiếm không phân biệt hoa thường"
- **Hoạt động**: Tìm kiếm "hello" trong "Hello World" (không phân biệt hoa thường)
- **Mục tiêu**: Hiểu cách xử lý chuỗi linh hoạt
- **Thử thách**: Tìm kiếm từ đầy đủ trong câu

#### Giải thích các khái niệm Python quan trọng:
```python
# Duyệt qua chuỗi:
for i in range(len(chuoi)):  # Duyệt qua chỉ số
    print(chuoi[i])          # Truy cập ký tự tại vị trí i

for ky_tu in chuoi:         # Duyệt qua từng ký tự
    print(ky_tu)             # Truy cập trực tiếp ký tự

# So sánh ký tự:
if chuoi[i] == ky_tu_can_tim:  # So sánh ký tự

# Thêm vào danh sách:
vi_tri_tim_thay.append(i)      # Thêm phần tử vào cuối danh sách
```

### Phần 4: Tạo chương trình "Chuyển đổi chuỗi" trên Python (20 phút)

#### Bước 1: Tạo file Python mới
```python
# Tạo file: chuyen_doi_chuoi.py
# Mục tiêu: Chuyển đổi chuỗi (upper, lower, reverse)
```

#### Bước 2: Lập trình thuật toán chuyển đổi chuỗi
```python
def chuyen_thanh_hoa(chuoi):
    """
    Chuyển chuỗi thành chữ hoa
    """
    print(f"Chuỗi gốc: '{chuoi}'")
    
    chuoi_hoa = ""
    for ky_tu in chuoi:
        if 'a' <= ky_tu <= 'z':  # Nếu là chữ thường
            chuoi_hoa += chr(ord(ky_tu) - 32)  # Chuyển thành chữ hoa
        else:
            chuoi_hoa += ky_tu  # Giữ nguyên
    
    print(f"Chuỗi chữ hoa: '{chuoi_hoa}'")
    return chuoi_hoa

def chuyen_thanh_thuong(chuoi):
    """
    Chuyển chuỗi thành chữ thường
    """
    print(f"Chuỗi gốc: '{chuoi}'")
    
    chuoi_thuong = ""
    for ky_tu in chuoi:
        if 'A' <= ky_tu <= 'Z':  # Nếu là chữ hoa
            chuoi_thuong += chr(ord(ky_tu) + 32)  # Chuyển thành chữ thường
        else:
            chuoi_thuong += ky_tu  # Giữ nguyên
    
    print(f"Chuỗi chữ thường: '{chuoi_thuong}'")
    return chuoi_thuong

def dao_nguoc_chuoi(chuoi):
    """
    Đảo ngược chuỗi
    """
    print(f"Chuỗi gốc: '{chuoi}'")
    
    chuoi_dao_nguoc = ""
    for i in range(len(chuoi) - 1, -1, -1):  # Duyệt ngược
        chuoi_dao_nguoc += chuoi[i]
    
    print(f"Chuỗi đảo ngược: '{chuoi_dao_nguoc}'")
    return chuoi_dao_nguoc

def dem_tu(chuoi):
    """
    Đếm số từ trong chuỗi
    """
    print(f"Chuỗi gốc: '{chuoi}'")
    
    so_tu = 0
    trong_tu = False
    
    for ky_tu in chuoi:
        if ky_tu != ' ' and ky_tu != '\t' and ky_tu != '\n':  # Không phải khoảng trắng
            if not trong_tu:  # Bắt đầu từ mới
                so_tu += 1
                trong_tu = True
        else:  # Gặp khoảng trắng
            trong_tu = False
    
    print(f"Số từ trong chuỗi: {so_tu}")
    return so_tu

# Chương trình chính
if __name__ == "__main__":
    # Chuỗi mẫu
    chuoi_mau = "Hello World Python"
    
    # Chuyển đổi chuỗi
    chuoi_hoa = chuyen_thanh_hoa(chuoi_mau)
    chuoi_thuong = chuyen_thanh_thuong(chuoi_mau)
    chuoi_dao_nguoc = dao_nguoc_chuoi(chuoi_mau)
    so_tu = dem_tu(chuoi_mau)
    
    print(f"\n=== KẾT QUẢ TỔNG HỢP ===")
    print(f"Chuỗi gốc: '{chuoi_mau}'")
    print(f"Chữ hoa: '{chuoi_hoa}'")
    print(f"Chữ thường: '{chuoi_thuong}'")
    print(f"Đảo ngược: '{chuoi_dao_nguoc}'")
    print(f"Số từ: {so_tu}")
```

#### Hoạt động mở rộng - "Xử lý chuỗi nâng cao"
- **Hoạt động**: Tạo chương trình kiểm tra chuỗi palindrome
- **Mục tiêu**: Hiểu cách kết hợp nhiều thuật toán chuỗi
- **Thử thách**: Tạo chương trình mã hóa đơn giản

## 🎯 Tổng kết và đánh giá (10 phút)

### Tổng kết kiến thức
- **Chuỗi**: Dãy các ký tự được sắp xếp theo thứ tự
- **Tìm kiếm chuỗi**: Duyệt qua từng ký tự để tìm kiếm
- **Đếm chuỗi**: Đếm số lần xuất hiện của ký tự hoặc từ
- **Chuyển đổi chuỗi**: Upper, lower, reverse, đếm từ
- **Ứng dụng**: Xử lý văn bản, tìm kiếm tài liệu, phân tích dữ liệu

### Đánh giá học sinh
- **Hiểu thuật toán**: Có thể giải thích các bước của thuật toán chuỗi
- **Áp dụng thực tế**: Tìm được ví dụ xử lý chuỗi trong cuộc sống
- **Lập trình Python**: Tạo được chương trình xử lý chuỗi hoạt động
- **Tư duy logic**: Phân tích và thiết kế thuật toán chuỗi

## 🎨 Hoạt động mở rộng

### Cấp độ 1: Thêm tính năng cơ bản
- **Giao diện tương tác**: Tạo menu để chọn loại xử lý chuỗi
- **Hiệu ứng trực quan**: Thêm màu sắc khi hiển thị kết quả
- **Âm thanh**: Tạo âm thanh khác nhau cho từng loại xử lý

### Cấp độ 2: Tính năng nâng cao
- **Xử lý chuỗi phức tạp**: Xử lý chuỗi có dấu câu và ký tự đặc biệt
- **Tìm kiếm thông minh**: Tìm kiếm không phân biệt hoa thường
- **So sánh chuỗi**: So sánh và sắp xếp chuỗi

### Cấp độ 3: Sáng tạo
- **Game chuỗi**: Tạo trò chơi đoán từ
- **Thuật toán riêng**: Thiết kế thuật toán xử lý chuỗi mới
- **Dự án tích hợp**: Kết hợp xử lý chuỗi với các thuật toán đã học

## 📝 Bài tập về nhà

### Bài tập bắt buộc
1. **Tìm kiếm chuỗi**: Viết thuật toán tìm kiếm từ trong câu
2. **Đếm ký tự**: Tạo chương trình đếm số lần xuất hiện của mỗi chữ cái
3. **Chuyển đổi chuỗi**: Viết chương trình chuyển đổi chuỗi hoàn chỉnh

### Bài tập nâng cao
1. **Xử lý chuỗi phức tạp**: Xử lý chuỗi có dấu câu và ký tự đặc biệt
2. **Tìm kiếm thông minh**: Tìm kiếm không phân biệt hoa thường
3. **Tối ưu hóa**: Tìm cách giảm số lần duyệt chuỗi

### Bài tập sáng tạo
1. **Game chuỗi**: Tạo game đoán từ với giao diện đẹp
2. **Thuật toán riêng**: Thiết kế thuật toán xử lý chuỗi độc đáo
3. **Dự án tích hợp**: Kết hợp xử lý chuỗi với sắp xếp và tìm kiếm

## 🔧 Tài nguyên hỗ trợ

### Tài liệu tham khảo
- **Python Programming**: Hướng dẫn lập trình Python cơ bản
- **String Processing**: Công cụ xử lý chuỗi trong Python
- **Text Analysis**: Phân tích văn bản cơ bản

### Công cụ hỗ trợ
- **Python Editor**: Môi trường lập trình Python
- **String Simulator**: Mô phỏng xử lý chuỗi
- **Debugging Tools**: Công cụ gỡ lỗi và tối ưu hóa

### Đánh giá và phản hồi
- **Rubric đánh giá**: Tiêu chí đánh giá kỹ năng xử lý chuỗi
- **Peer Review**: Đánh giá lẫn nhau giữa học sinh
- **Portfolio**: Tập hợp các dự án và bài tập của học sinh
