# Bài Giảng 9: Giới Thiệu Python Cơ Bản

## 📋 Thông tin bài học
- **Thời gian**: 120 phút (3 tiết)
- **Độ tuổi**: Lớp 5 (10-11 tuổi)
- **Mức độ**: Trung bình đến nâng cao
- **Mục tiêu**: Làm quen với Python và chuyển đổi từ Scratch

## 🎯 Mục tiêu học tập

### Kiến thức
- Hiểu cú pháp cơ bản của Python
- Biết cách sử dụng biến và kiểu dữ liệu
- Hiểu các cấu trúc điều khiển trong Python

### Kỹ năng
- Viết chương trình Python đơn giản
- Chuyển đổi code từ Scratch sang Python
- Sử dụng môi trường lập trình Python

### Thái độ
- Phát triển tư duy lập trình văn bản
- Rèn luyện tính cẩn thận với cú pháp
- Khuyến khích tư duy logic


## 🐍 Nội dung bài học

### Phần 1: Giới thiệu Python (20 phút)

#### Hoạt động khởi động
- Hỏi: "Các em có biết Python là gì không?"
- Giải thích: "Python là ngôn ngữ lập trình văn bản"
- So sánh: "Scratch vs Python"

#### Tại sao học Python?
- **Dễ học**: Cú pháp đơn giản, gần với ngôn ngữ tự nhiên
- **Mạnh mẽ**: Có thể làm nhiều việc khác nhau
- **Phổ biến**: Được sử dụng rộng rãi trong thực tế
- **Tương lai**: Chuẩn bị cho việc học lập trình chuyên sâu

#### Cài đặt và chạy Python
```python
# Kiểm tra Python đã cài đặt
python --version

# Chạy Python
python
```

### Phần 2: Cú pháp cơ bản (30 phút)

#### In ra màn hình
```python
# Scratch: nói [Hello World] trong (2) giây
# Python:
print("Hello World")
print("Xin chào các bạn!")
```

#### Biến số
```python
# Scratch: đặt [ten v] thành [An]
# Python:
ten = "An"
tuoi = 10
diem = 8.5

print("Tên:", ten)
print("Tuổi:", tuoi)
print("Điểm:", diem)
```

#### Kiểu dữ liệu
```python
# Số nguyên
so_nguyen = 10
print(type(so_nguyen))  # <class 'int'>

# Số thập phân
so_thap_phan = 3.14
print(type(so_thap_phan))  # <class 'float'>

# Chuỗi
chuoi = "Xin chào"
print(type(chuoi))  # <class 'str'>

# Boolean
dung_sai = True
print(type(dung_sai))  # <class 'bool'>
```

### Phần 3: Cấu trúc điều khiển (30 phút)

#### Điều kiện if/else
```python
# Scratch: nếu <[tuoi v] > [18]> thì
# Python:
tuoi = 15

if tuoi >= 18:
    print("Bạn đã trưởng thành")
else:
    print("Bạn còn nhỏ")
```

#### Vòng lặp for
```python
# Scratch: lặp lại (5) lần
# Python:
for i in range(5):
    print("Lần thứ:", i + 1)
```

#### Vòng lặp while
```python
# Scratch: lặp lại cho đến khi <[dem v] = [10]>
# Python:
dem = 0
while dem < 10:
    print("Đếm:", dem)
    dem = dem + 1
```

### Phần 4: Chuyển đổi từ Scratch sang Python (25 phút)

#### Ví dụ 1: Chương trình chào hỏi
```python
# Scratch:
# Khi cờ xanh được nhấn
# nói [Xin chào! Tên tôi là An] trong (3) giây

# Python:
print("Xin chào! Tên tôi là An")
```

#### Ví dụ 2: Tính tổng hai số
```python
# Scratch:
# đặt [so1 v] thành (5)
# đặt [so2 v] thành (3)
# đặt [tong v] thành ([so1 v] + [so2 v])
# nói [Tổng là: ] + [tong v] trong (2) giây

# Python:
so1 = 5
so2 = 3
tong = so1 + so2
print("Tổng là:", tong)
```

#### Ví dụ 3: Kiểm tra số chẵn/lẻ
```python
# Scratch:
# nếu <([so v] mod (2)) = [0]> thì
# nói [Số chẵn] trong (2) giây
# nếu không
# nói [Số lẻ] trong (2) giây

# Python:
so = 8
if so % 2 == 0:
    print("Số chẵn")
else:
    print("Số lẻ")
```

### Phần 5: Danh sách trong Python (15 phút)

#### Tạo và sử dụng danh sách
```python
# Scratch: thêm (1) vào [DanhSach v]
# Python:
danh_sach = [1, 2, 3, 4, 5]
print("Danh sách:", danh_sach)

# Thêm phần tử
danh_sach.append(6)
print("Sau khi thêm:", danh_sach)

# Truy cập phần tử
print("Phần tử đầu tiên:", danh_sach[0])
print("Phần tử cuối:", danh_sach[-1])
```

#### Vòng lặp với danh sách
```python
# Scratch: lặp lại (độ dài của [DanhSach v]) lần
# Python:
danh_sach = [10, 20, 30, 40, 50]

for so in danh_sach:
    print("Số:", so)

# Hoặc sử dụng range
for i in range(len(danh_sach)):
    print("Vị trí", i, ":", danh_sach[i])
```

## 🎨 Hoạt động mở rộng

### Cấp độ 1: Thêm tính năng cơ bản
- Tạo chương trình tính diện tích hình chữ nhật
- Tạo chương trình kiểm tra điểm số
- Thêm giao diện nhập dữ liệu

### Cấp độ 2: Tính năng nâng cao
- Tạo chương trình quản lý danh sách học sinh
- Tạo chương trình tính toán phức tạp
- Sử dụng hàm trong Python

### Cấp độ 3: Sáng tạo
- Tạo game đơn giản bằng Python
- Thiết kế chương trình riêng
- Áp dụng vào bài toán thực tế

## 📝 Bài tập về nhà

### Bài tập bắt buộc
1. Viết chương trình Python tính chu vi hình chữ nhật
2. Tạo chương trình kiểm tra số chia hết cho 3
3. Viết chương trình in ra các số từ 1 đến 10

### Bài tập nâng cao
1. Tạo chương trình quản lý điểm số học sinh
2. Viết chương trình tìm số lớn nhất trong danh sách
3. Tạo chương trình tính giai thừa

## 🔍 Đánh giá

### Tiêu chí đánh giá
| Tiêu chí | Điểm | Mô tả |
|----------|------|-------|
| Hiểu cú pháp Python | 3 | Viết code đúng cú pháp |
| Chuyển đổi từ Scratch | 3 | Chuyển đổi chính xác |
| Tạo chương trình | 2 | Code hoạt động đúng |
| Sáng tạo | 1 | Có yếu tố độc đáo |
| Trình bày | 1 | Giải thích rõ ràng |
| Tổng cộng | 10 | |

### Cách đánh giá
- **Quan sát**: Giáo viên quan sát quá trình học
- **Sản phẩm**: Kiểm tra chương trình Python
- **Trình bày**: Học sinh demo và giải thích
- **Phản hồi**: Nhận xét từ bạn cùng lớp

## 🚀 Lưu ý quan trọng

### Cho giáo viên
- Giải thích kỹ sự khác biệt giữa Scratch và Python
- Sử dụng ví dụ cụ thể để minh họa
- Khuyến khích học sinh thử nghiệm
- Chuẩn bị nhiều bài tập thực hành

### Cho học sinh
- Chú ý đến cú pháp Python
- Test kỹ từng chương trình
- Không ngại thử nghiệm với code mới
- Lưu file thường xuyên

## 💡 Mẹo hay

### Học Python hiệu quả
- Bắt đầu với các chương trình đơn giản
- Thực hành thường xuyên
- Đọc code của người khác

### Tránh lỗi thường gặp
- Chú ý đến indentation (thụt lề)
- Kiểm tra dấu ngoặc và dấu phẩy
- Sử dụng tên biến có ý nghĩa

### Debug hiệu quả
- Đọc kỹ thông báo lỗi
- Test từng phần một
- Sử dụng print() để debug

## 🔗 So sánh Scratch vs Python

### Điểm tương đồng
| Scratch | Python |
|---------|--------|
| Biến số | Variables |
| Vòng lặp | for/while loops |
| Điều kiện | if/else |
| Danh sách | Lists |

### Điểm khác biệt
| Scratch | Python |
|---------|--------|
| Kéo thả | Viết code |
| Giao diện đồ họa | Giao diện văn bản |
| Tự động | Cần chú ý cú pháp |
| Dễ học | Linh hoạt hơn |

## 📚 Tài liệu tham khảo

- [Python Official Website](https://python.org)
- [Python Tutorial for Beginners](https://python.org/tutorial)
- [Scratch to Python Guide](https://scratch.mit.edu)

---

**Tác giả**: AI & Trần Việt Trung (BKHN)  
**Ngày tạo**: 04/10/2025  
**Phiên bản**: 1.0
