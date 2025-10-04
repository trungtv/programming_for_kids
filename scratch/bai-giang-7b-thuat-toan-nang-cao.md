# Bài giảng 7B: Thuật toán nâng cao - Tính toán và tích hợp

## 📋 Thông tin bài học
- **Thời gian**: 90 phút
- **Độ tuổi**: 10-11 tuổi
- **Trình độ**: Nâng cao
- **Mục tiêu**: Học thuật toán tính toán và tích hợp để chuẩn bị cho Python

## 🎯 Mục tiêu học tập

### Kiến thức
- Hiểu thuật toán tính tổng và trung bình
- Biết cách tích hợp nhiều thuật toán
- Hiểu cách tối ưu hóa thuật toán

### Kỹ năng
- Thiết kế hệ thống tích hợp nhiều thuật toán
- Debug và tối ưu hóa code phức tạp
- Tạo dự án hoàn chỉnh

### Thái độ
- Phát triển tư duy logic nâng cao
- Rèn luyện tính kiên trì và cẩn thận
- Khuyến khích tư duy sáng tạo

## 🧠 Nội dung bài học

## 📚 PHẦN LÝ THUYẾT (45 phút)

### Phần 1: Ôn tập và kết nối với bài 7A (15 phút)

#### Hoạt động khởi động - "Nhớ lại thuật toán từ bài 7A"
- **Hoạt động**: Học sinh nhắc lại 3 thuật toán đã học trong bài 7A
- **Câu hỏi**: "Chúng ta đã học những thuật toán nào trong bài trước?"
- **Kết nối**: "Hôm nay chúng ta sẽ học cách kết hợp các thuật toán đó"
- **Mục tiêu**: Củng cố kiến thức và chuẩn bị cho bài mới

#### Ôn tập nhanh các thuật toán đã học
- **Tìm số lớn nhất**: So sánh từng phần tử và cập nhật kết quả
- **Đếm số phần tử**: Duyệt qua danh sách và đếm theo điều kiện
- **Sắp xếp**: So sánh và đổi chỗ để sắp xếp theo thứ tự

#### Giới thiệu bài mới - "Thuật toán tính toán"
- **Tính tổng**: Cộng dồn các số trong danh sách
- **Tính trung bình**: Tổng chia cho số lượng phần tử
- **Dự án tích hợp**: Kết hợp tất cả thuật toán đã học

### Phần 2: Thuật toán tính tổng qua trò chơi "Xây tháp" (30 phút)

#### Hoạt động không máy tính - "Xây tháp bằng khối LEGO"
- **Hoạt động**: Xây tháp 5 tầng bằng khối LEGO
- **Quy tắc**: Tầng 1 có 1 khối, tầng 2 có 2 khối, tầng 3 có 3 khối...
- **Mục tiêu**: Hiểu thuật toán tính tổng qua hoạt động thực tế

#### Bài toán: Tính tổng điểm của lớp
- **Input**: Danh sách điểm [8, 9, 7, 10, 6]
- **Output**: Tổng điểm = 8+9+7+10+6 = 40
- **Ví dụ**: Tính tổng điểm của cả lớp

#### Thuật toán tính tổng qua ví dụ thực tế
```
Bước 1: Khởi tạo tổng = 0
Bước 2: Thêm điểm học sinh 1 (8) vào tổng → tổng = 8
Bước 3: Thêm điểm học sinh 2 (9) vào tổng → tổng = 17
Bước 4: Thêm điểm học sinh 3 (7) vào tổng → tổng = 24
Bước 5: Tiếp tục cho đến hết danh sách
```

#### Hoạt động không máy tính - "Tính điểm trung bình"
- **Hoạt động**: Học sinh tính điểm trung bình bằng cách chia tổng cho số học sinh
- **Mục tiêu**: Hiểu thuật toán tính trung bình
- **Quy tắc**: Tổng điểm ÷ Số học sinh = Điểm trung bình
- **Kết quả**: Nhận ra trung bình là tổng chia cho số lượng

#### Bài toán: Tính điểm trung bình của lớp
- **Input**: Tổng điểm = 40, Số học sinh = 5
- **Output**: Điểm trung bình = 40 ÷ 5 = 8
- **Ví dụ**: Tính điểm trung bình của lớp

#### Thuật toán tính trung bình qua ví dụ thực tế
```
Bước 1: Tính tổng điểm (40)
Bước 2: Đếm số học sinh (5)
Bước 3: Chia tổng cho số học sinh (40 ÷ 5 = 8)
Bước 4: Kết quả là điểm trung bình (8)
```

## 💻 PHẦN THỰC HÀNH SCRATCH (45 phút)

### Phần 3: Tạo game "Tính tổng điểm" trên Scratch (15 phút)

#### Lập trình trong Scratch với hiệu ứng trực quan
```scratch
Khi cờ xanh được nhấn
đặt [DanhSachDiem v] thành [8,9,7,10,6]
nói [Danh sách điểm: ] + [DanhSachDiem v] trong (3) giây
đặt [TongDiem v] thành [0]
đặt [ViTri v] thành [1]
nói [Bắt đầu tính tổng điểm...] trong (2) giây
lặp lại (5) lần
  thay đổi [TongDiem v] bởi [DanhSachDiem v]
  nói [Điểm ] + [DanhSachDiem v] + [. Tổng hiện tại: ] + [TongDiem v] trong (2) giây
  thay đổi [ViTri v] bởi (1)
nói [Tổng điểm của lớp: ] + [TongDiem v] trong (3) giây
```

#### Hoạt động mở rộng - "Tính tổng với điều kiện"
- **Hoạt động**: Chỉ tính tổng điểm của học sinh giỏi (>= 8)
- **Mục tiêu**: Hiểu cách kết hợp đếm và tính tổng
- **Thử thách**: Tính tổng điểm của từng loại học sinh

### Phần 4: Tạo game "Tính điểm trung bình" trên Scratch (15 phút)

#### Lập trình trong Scratch với hiệu ứng trực quan
```scratch
Khi cờ xanh được nhấn
đặt [DanhSachDiem v] thành [8,9,7,10,6]
nói [Danh sách điểm: ] + [DanhSachDiem v] trong (3) giây
đặt [TongDiem v] thành [0]
đặt [SoHocSinh v] thành [5]
đặt [ViTri v] thành [1]
nói [Bắt đầu tính điểm trung bình...] trong (2) giây
lặp lại (5) lần
  thay đổi [TongDiem v] bởi [DanhSachDiem v]
  thay đổi [ViTri v] bởi (1)
đặt [DiemTrungBinh v] thành ([TongDiem v] / [SoHocSinh v])
nói [Tổng điểm: ] + [TongDiem v] + [. Số học sinh: ] + [SoHocSinh v] trong (3) giây
nói [Điểm trung bình: ] + [DiemTrungBinh v] trong (3) giây
```

#### Hoạt động mở rộng - "So sánh với điểm trung bình"
- **Hoạt động**: Đếm số học sinh trên/below điểm trung bình
- **Mục tiêu**: Hiểu cách sử dụng kết quả tính toán
- **Thử thách**: Tạo báo cáo thống kê hoàn chỉnh

### Phần 5: Dự án tích hợp - "Hệ thống quản lý điểm số" (15 phút)

#### Mô tả dự án
- **Mục tiêu**: Tạo hệ thống quản lý điểm số hoàn chỉnh
- **Tính năng**: Sắp xếp, tìm kiếm, đếm, tính tổng, tính trung bình
- **Kết quả**: Chương trình Scratch tích hợp tất cả thuật toán đã học

#### Thiết kế hệ thống
```
1. Nhập danh sách điểm số
2. Sắp xếp điểm từ cao đến thấp (từ bài 6A)
3. Tìm điểm cao nhất và thấp nhất (từ bài 6A)
4. Đếm số học sinh theo loại (từ bài 6A)
5. Tính tổng điểm (bài mới)
6. Tính điểm trung bình (bài mới)
7. Hiển thị báo cáo tổng hợp
```

#### Lập trình tích hợp
```scratch
Khi cờ xanh được nhấn
nói [=== HỆ THỐNG QUẢN LÝ ĐIỂM SỐ ===] trong (3) giây
chờ (2) giây

# Nhập dữ liệu
đặt [DanhSachDiem v] thành [8,9,7,10,6]
nói [Danh sách điểm: ] + [DanhSachDiem v] trong (3) giây
chờ (2) giây

# Sắp xếp (từ bài 7A)
nói [Đang sắp xếp điểm từ cao đến thấp...] trong (2) giây
# [Code sắp xếp từ bài 7A]

# Tìm kiếm (từ bài 7A)
nói [Đang tìm điểm cao nhất và thấp nhất...] trong (2) giây
# [Code tìm kiếm từ bài 7A]

# Đếm (từ bài 7A)
nói [Đang đếm số học sinh theo loại...] trong (2) giây
# [Code đếm từ bài 7A]

# Tính tổng (bài mới)
nói [Đang tính tổng điểm...] trong (2) giây
# [Code tính tổng từ phần 3]

# Tính trung bình (bài mới)
nói [Đang tính điểm trung bình...] trong (2) giây
# [Code tính trung bình từ phần 4]

# Báo cáo
nói [=== BÁO CÁO TỔNG HỢP ===] trong (3) giây
nói [Điểm cao nhất: ] + [DiemCaoNhat v] trong (2) giây
nói [Điểm thấp nhất: ] + [DiemThapNhat v] trong (2) giây
nói [Số học sinh giỏi: ] + [DemHocSinhGioi v] trong (2) giây
nói [Tổng điểm: ] + [TongDiem v] trong (2) giây
nói [Điểm trung bình: ] + [DiemTrungBinh v] trong (2) giây
```

## 🎯 Tổng kết và đánh giá (10 phút)

### Tổng kết kiến thức
- **Tính tổng**: Cộng dồn các số trong danh sách
- **Tính trung bình**: Tổng chia cho số lượng phần tử
- **Tích hợp thuật toán**: Kết hợp nhiều thuật toán trong một hệ thống
- **Tối ưu hóa**: Sử dụng lại code và biến chung

### Đánh giá học sinh
- **Hiểu thuật toán**: Có thể giải thích các bước tính tổng và trung bình
- **Tích hợp**: Kết hợp được nhiều thuật toán trong một dự án
- **Lập trình Scratch**: Tạo được hệ thống quản lý điểm hoàn chỉnh
- **Tư duy hệ thống**: Thiết kế và phát triển dự án có cấu trúc

## 🎨 Hoạt động mở rộng

### Cấp độ 1: Thêm tính năng cơ bản
- **Giao diện tương tác**: Tạo nút để nhập dữ liệu mới
- **Hiệu ứng trực quan**: Thêm màu sắc và animation
- **Âm thanh**: Tạo âm thanh khác nhau cho từng chức năng

### Cấp độ 2: Tính năng nâng cao
- **Lưu trữ dữ liệu**: Lưu danh sách điểm vào file
- **Tìm kiếm thông minh**: Tìm học sinh theo tên và điểm
- **Biểu đồ trực quan**: Tạo biểu đồ cột cho thống kê

### Cấp độ 3: Sáng tạo
- **Game thuật toán**: Tạo trò chơi quiz về thuật toán
- **Thuật toán riêng**: Thiết kế thuật toán giải quyết vấn đề thực tế
- **Dự án tích hợp**: Kết hợp với các bài học khác

## 📝 Bài tập về nhà

### Bài tập bắt buộc
1. **Tính tổng điểm**: Viết thuật toán tính tổng điểm của 7 học sinh
2. **Tính điểm trung bình**: Tính điểm trung bình của lớp
3. **Hệ thống đơn giản**: Tạo hệ thống quản lý điểm cơ bản

### Bài tập nâng cao
1. **Tính tổng có điều kiện**: Chỉ tính tổng điểm của học sinh giỏi
2. **Thống kê nâng cao**: Tính độ lệch chuẩn và phân phối điểm
3. **Dự án sáng tạo**: Thiết kế hệ thống quản lý thư viện

## 🔧 Tài nguyên hỗ trợ

### Tài liệu tham khảo
- **Scratch Programming**: Hướng dẫn lập trình Scratch nâng cao
- **Algorithm Integration**: Cách tích hợp nhiều thuật toán
- **System Design**: Thiết kế hệ thống đơn giản

### Công cụ hỗ trợ
- **Scratch Editor**: Môi trường lập trình trực quan
- **Algorithm Simulator**: Mô phỏng thuật toán tích hợp
- **Debugging Tools**: Công cụ gỡ lỗi và tối ưu hóa

### Đánh giá và phản hồi
- **Rubric đánh giá**: Tiêu chí đánh giá kỹ năng tích hợp thuật toán
- **Peer Review**: Đánh giá lẫn nhau giữa học sinh
- **Portfolio**: Tập hợp các dự án và bài tập của học sinh
