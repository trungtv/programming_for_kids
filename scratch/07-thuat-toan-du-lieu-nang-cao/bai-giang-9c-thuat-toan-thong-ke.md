# Bài giảng 9C: Thuật toán thống kê nâng cao

## 📋 Thông tin bài học
- **Thời gian**: 90 phút
- **Độ tuổi**: 10-11 tuổi
- **Trình độ**: Nâng cao
- **Mục tiêu**: Áp dụng thuật toán vào phân tích dữ liệu phức tạp (mở rộng từ Bài 7C)

## 🎯 Mục tiêu học tập

### Kiến thức
- Hiểu cách tính trung bình theo nhóm (mở rộng từ tính trung bình cơ bản ở Bài 7C)
- Nắm vững đếm theo điều kiện phức tạp (mở rộng từ Bài 7B)
- Hiểu cách tính tổng có điều kiện (ví dụ: chỉ tính tổng điểm của học sinh giỏi)
- Biết cách tìm khoảng cách giữa 2 số
- Hiểu các khái niệm thống kê nâng cao: độ lệch, phân phối

### Kỹ năng
- Thiết kế thuật toán tính toán có điều kiện
- Phân tích và thống kê dữ liệu phức tạp
- Kết hợp nhiều thuật toán thống kê
- Tạo hệ thống phân tích dữ liệu hoàn chỉnh

### Thái độ
- Phát triển tư duy phân tích dữ liệu
- Rèn luyện tính cẩn thận và chính xác
- Khuyến khích tư duy hệ thống

## 🧠 Nội dung bài học

## 📚 PHẦN LÝ THUYẾT (45 phút)

### Phần 1: Ôn tập và kết nối với Bài 7B và 7C (10 phút)

#### Hoạt động khởi động - "Nhớ lại tính tổng và trung bình cơ bản"
- **Hoạt động**: Nhắc lại Bài 7C về tính tổng và trung bình cơ bản
- **Câu hỏi**: "Chúng ta đã học cách tính tổng và trung bình như thế nào?"
- **Kết nối**: "Hôm nay chúng ta sẽ học tính tổng và trung bình có điều kiện, phức tạp hơn"
- **Mục tiêu**: Củng cố kiến thức và chuẩn bị cho bài mới

#### Ôn tập nhanh về tính tổng và trung bình cơ bản
- **Tính tổng cơ bản**: Cộng tất cả các số trong danh sách
- **Tính trung bình cơ bản**: Tổng chia cho số lượng phần tử
- **Đếm cơ bản**: Đếm số phần tử trong danh sách

### Phần 2: Tính tổng có điều kiện (15 phút)

#### Hoạt động không máy tính - "Tính tổng điểm của học sinh giỏi"
- **Hoạt động**: Học sinh được phát danh sách điểm [8, 9, 7, 10, 6, 8, 9]
- **Câu hỏi**: "Hãy tính tổng điểm của các học sinh giỏi (điểm >= 8)"
- **Bước 1**: Duyệt qua từng điểm
- **Bước 2**: Kiểm tra điều kiện (điểm >= 8)
- **Bước 3**: Nếu thỏa điều kiện, cộng vào tổng
- **Kết quả**: 8 + 9 + 10 + 8 + 9 = 44
- **Mục tiêu**: Hiểu tính tổng có điều kiện qua trải nghiệm thực tế

#### Khái niệm tính tổng có điều kiện qua ví dụ thực tế
- **Định nghĩa**: Tính tổng chỉ các phần tử thỏa một điều kiện nào đó
- **Ví dụ thực tế**: 
  - Tính tổng điểm của học sinh giỏi
  - Tính tổng tiền mua đồ chơi (chỉ đồ chơi > 100.000đ)
  - Tính tổng số Pokemon loại nước
- **Ứng dụng**: Phân tích dữ liệu có điều kiện, thống kê theo nhóm

#### Thuật toán tính tổng có điều kiện qua ví dụ
```
Danh sách điểm: [8, 9, 7, 10, 6, 8, 9]
Điều kiện: Điểm >= 8

Duyệt qua từng điểm:
- 8: 8 >= 8 → Đúng, cộng vào tổng (tổng = 8)
- 9: 9 >= 8 → Đúng, cộng vào tổng (tổng = 17)
- 7: 7 >= 8 → Sai, bỏ qua
- 10: 10 >= 8 → Đúng, cộng vào tổng (tổng = 27)
- 6: 6 >= 8 → Sai, bỏ qua
- 8: 8 >= 8 → Đúng, cộng vào tổng (tổng = 35)
- 9: 9 >= 8 → Đúng, cộng vào tổng (tổng = 44)

Kết quả: Tổng điểm học sinh giỏi = 44
```

### Phần 3: Tính trung bình theo nhóm (10 phút)

#### Hoạt động không máy tính - "Tính trung bình điểm của từng lớp"
- **Hoạt động**: Học sinh được phát danh sách điểm theo lớp
  - Lớp A: [8, 9, 7, 10]
  - Lớp B: [6, 8, 9, 7]
- **Câu hỏi**: "Tính trung bình điểm của từng lớp"
- **Lớp A**: (8 + 9 + 7 + 10) / 4 = 8.5
- **Lớp B**: (6 + 8 + 9 + 7) / 4 = 7.5
- **Mục tiêu**: Hiểu tính trung bình theo nhóm

#### Thuật toán tính trung bình theo nhóm
```
Danh sách lớp A: [8, 9, 7, 10]
Bước 1: Tính tổng = 8 + 9 + 7 + 10 = 34
Bước 2: Đếm số phần tử = 4
Bước 3: Trung bình = 34 / 4 = 8.5

Danh sách lớp B: [6, 8, 9, 7]
Bước 1: Tính tổng = 6 + 8 + 9 + 7 = 30
Bước 2: Đếm số phần tử = 4
Bước 3: Trung bình = 30 / 4 = 7.5
```

### Phần 4: Tìm khoảng cách giữa 2 số (10 phút)

#### Hoạt động không máy tính - "Tìm khoảng cách giữa 2 điểm"
- **Hoạt động**: Học sinh được phát 2 số: 8 và 10
- **Câu hỏi**: "Khoảng cách giữa 8 và 10 là bao nhiêu?"
- **Cách tính**: |10 - 8| = 2
- **Mục tiêu**: Hiểu khái niệm khoảng cách

#### Khái niệm khoảng cách qua ví dụ thực tế
- **Định nghĩa**: Khoảng cách giữa 2 số = |số lớn - số nhỏ|
- **Ví dụ thực tế**: 
  - Khoảng cách giữa điểm cao nhất và thấp nhất
  - Khoảng cách giữa 2 vị trí trên bản đồ
  - Khoảng cách giữa 2 thời điểm

## 💻 PHẦN THỰC HÀNH (45 phút)

### Phần 1: Tạo game "Tính tổng có điều kiện" (15 phút)

#### Bước 1: Tạo các biến và danh sách
```scratch
# Tạo các biến sau:
1. Biến "i" - chỉ số vị trí hiện tại
2. Biến "tong" - tổng điểm
3. List "DanhSachDiem" - danh sách điểm
```

#### Bước 2: Lập trình tính tổng có điều kiện
```scratch
Khi cờ xanh được nhấn
xóa tất cả trong [DanhSachDiem v]
thêm [8] vào [DanhSachDiem v]
thêm [9] vào [DanhSachDiem v]
thêm [7] vào [DanhSachDiem v]
thêm [10] vào [DanhSachDiem v]
thêm [6] vào [DanhSachDiem v]
thêm [8] vào [DanhSachDiem v]
thêm [9] vào [DanhSachDiem v]
nói [Danh sách điểm: ] + [DanhSachDiem v] trong (3) giây

# Tính tổng điểm của học sinh giỏi (>= 8)
đặt [tong v] thành [0]
đặt [i v] thành [1]
lặp lại (chiều dài của [DanhSachDiem v]) lần
  nếu <(mục (i) của [DanhSachDiem v]) >= [8]> thì
    thay đổi [tong v] bởi (mục (i) của [DanhSachDiem v])
  thay đổi [i v] bởi (1)

nói [Tổng điểm học sinh giỏi (>= 8): ] + [tong v] trong (5) giây
```

### Phần 2: Tạo game "Tính trung bình theo nhóm" (15 phút)

#### Bước 1: Tạo danh sách cho từng nhóm
```scratch
# Tạo danh sách cho lớp A và lớp B
List "LopA": [8, 9, 7, 10]
List "LopB": [6, 8, 9, 7]
```

#### Bước 2: Lập trình tính trung bình theo nhóm
```scratch
# Tính trung bình lớp A
đặt [tongA v] thành [0]
đặt [i v] thành [1]
lặp lại (chiều dài của [LopA v]) lần
  thay đổi [tongA v] bởi (mục (i) của [LopA v])
  thay đổi [i v] bởi (1)
đặt [trungBinhA v] thành ((tongA) / (chiều dài của [LopA v]))
nói [Trung bình lớp A: ] + [trungBinhA v] trong (3) giây

# Tính trung bình lớp B (tương tự)
```

### Phần 3: Tạo game "Tìm khoảng cách" (15 phút)

#### Bước 1: Tìm số lớn nhất và nhỏ nhất
```scratch
# Sử dụng thuật toán từ Bài 7A
đặt [max v] thành (mục (1) của [DanhSachDiem v])
đặt [min v] thành (mục (1) của [DanhSachDiem v])
# [Code tìm max và min từ Bài 7A]
```

#### Bước 2: Tính khoảng cách
```scratch
đặt [khoangCach v] thành ((max) - (min))
nói [Khoảng cách giữa điểm cao nhất và thấp nhất: ] + [khoangCach v] trong (5) giây
```

## 🎨 Hoạt động mở rộng

### Cấp độ 1: Thêm tính năng cơ bản
- **Tính tổng với nhiều điều kiện**: Điểm >= 8 và <= 10
- **Tính trung bình có điều kiện**: Trung bình điểm của học sinh giỏi
- **Tìm khoảng cách giữa nhiều số**: Khoảng cách lớn nhất trong danh sách

### Cấp độ 2: Tính năng nâng cao
- **Thống kê theo nhiều nhóm**: So sánh trung bình của nhiều lớp
- **Phân tích phân phối**: Đếm số học sinh ở từng mức điểm
- **Độ lệch chuẩn**: Tính độ phân tán của dữ liệu

### Cấp độ 3: Sáng tạo
- **Hệ thống phân tích điểm số**: Tạo hệ thống phân tích hoàn chỉnh
- **Báo cáo thống kê**: Tạo báo cáo với nhiều chỉ số
- **Dự án tích hợp**: Kết hợp với các bài học khác

## 📝 Tổng kết kiến thức

### Kiến thức đã học
- **Tính tổng có điều kiện**: Chỉ tính tổng các phần tử thỏa điều kiện
- **Tính trung bình theo nhóm**: Tính trung bình cho từng nhóm riêng
- **Tìm khoảng cách**: Khoảng cách giữa 2 số
- **Thống kê nâng cao**: Kết hợp nhiều thuật toán thống kê

### Kỹ năng đã rèn luyện
- Thiết kế thuật toán tính toán có điều kiện
- Phân tích và thống kê dữ liệu phức tạp
- Kết hợp nhiều thuật toán thống kê
- Tạo hệ thống phân tích dữ liệu

## 🎯 Đánh giá học sinh

### Tiêu chí đánh giá
- **Hiểu thuật toán**: Có thể giải thích các bước tính tổng có điều kiện
- **Lập trình Scratch**: Tạo được hệ thống thống kê nâng cao
- **Tư duy phân tích**: Phân tích được dữ liệu phức tạp
- **Sáng tạo**: Tạo được dự án tích hợp

## 🔗 Liên kết

- **Bài trước**: [Bài 9B: Sắp xếp nâng cao - Insertion Sort](bai-giang-9b-sap-xep-nang-cao.md)
- **Bài tiếp theo**: [Bài 10A: Mô phỏng nhiều đối tượng tương tác](../08-mo-phong-nang-cao/bai-giang-10a-mo-phong-nhieu-doi-tuong.md)
- **Bài liên quan**: 
  - [Bài 7B: Thuật toán đếm](../05-thuat-toan/bai-giang-7b-thuat-toan-dem.md)
  - [Bài 7C: Thuật toán tính toán](../05-thuat-toan/bai-giang-7c-thuat-toan-tinh-toan.md)
- **Về topic**: [README.md](README.md)

---

**🌟 Chúc các em học tốt và sáng tạo!**

