# Bài Giảng 6B: Thuật Toán Nâng Cao

## 📋 Thông tin bài học
- **Thời gian**: 90 phút (2 tiết)
- **Độ tuổi**: Lớp 4-5 (9-11 tuổi)
- **Mức độ**: Nâng cao
- **Mục tiêu**: Học thuật toán đếm, thống kê và tính toán để chuẩn bị cho Python

## 🎯 Mục tiêu học tập

### Kiến thức
- Hiểu thuật toán đếm và phân loại
- Biết cách tính toán và thống kê dữ liệu
- Hiểu cách kết hợp nhiều thuật toán

### Kỹ năng
- Thiết kế thuật toán phức tạp
- Debug và tối ưu hóa code nâng cao
- Tạo dự án tích hợp nhiều thuật toán

### Thái độ
- Phát triển tư duy logic nâng cao
- Rèn luyện tính kiên trì và cẩn thận
- Khuyến khích tư duy sáng tạo

## 🧠 Nội dung bài học

### Phần 1: Ôn tập và kết nối (15 phút)

#### Hoạt động khởi động - "Nhớ lại thuật toán"
- **Hoạt động**: Học sinh nhắc lại thuật toán sắp xếp và tìm kiếm đã học
- **Mục tiêu**: Củng cố kiến thức từ bài 6A
- **Kết quả**: Đảm bảo học sinh hiểu rõ các thuật toán cơ bản

#### Kết nối với bài trước
- **Sắp xếp**: Bubble Sort cho 3-5 số
- **Tìm kiếm**: Linear Search để tìm số lớn nhất/nhỏ nhất
- **Chuẩn bị**: Áp dụng vào các bài toán phức tạp hơn

#### Giới thiệu bài mới
- **Thuật toán đếm**: Đếm số lượng theo điều kiện
- **Thuật toán tính toán**: Tính tổng, trung bình, giai thừa
- **Dự án tổng hợp**: Kết hợp tất cả thuật toán đã học

### Phần 2: Thuật toán đếm và thống kê qua trò chơi "Đếm đồ vật" (30 phút)

#### Hoạt động không máy tính - "Đếm số bạn nam và nữ trong lớp"
- **Hoạt động**: Học sinh đứng thành hàng, đếm số bạn nam và nữ
- **Quy tắc**: Đi từ đầu đến cuối hàng, đếm từng người một
- **Mục tiêu**: Hiểu thuật toán đếm và phân loại

#### Bài toán: Đếm số học sinh giỏi trong lớp
- **Input**: Danh sách điểm [8, 9, 7, 10, 6, 9, 8, 7]
- **Output**: Số học sinh có điểm >= 8 (4 học sinh)
- **Ví dụ**: Thống kê số học sinh đạt loại giỏi

#### Thuật toán đếm qua ví dụ thực tế
```
Bước 1: Khởi tạo biến đếm = 0
Bước 2: Xem điểm của bạn đầu tiên (8)
Bước 3: Vì 8 >= 8, tăng biến đếm lên 1
Bước 4: Xem điểm của bạn tiếp theo (9)
Bước 5: Vì 9 >= 8, tăng biến đếm lên 2
Bước 6: Tiếp tục cho đến hết danh sách
```

#### Vẽ sơ đồ thuật toán
```
[Start] → [Đặt đếm = 0] → [Xem điểm tiếp theo]
    ↓
[Điểm >= 8?] → [Có: Tăng đếm lên 1] → [Không: Giữ nguyên đếm]
    ↓
[Còn điểm nào?] → [Có: Tiếp tục] → [Không: Hiển thị kết quả]
```

#### Lập trình trong Scratch với hiệu ứng trực quan
```scratch
Khi cờ xanh được nhấn
đặt [DanhSachDiem v] thành [8,9,7,10,6,9,8,7]
nói [Danh sách điểm lớp: ] + [DanhSachDiem v] trong (3) giây
chờ (2) giây
đặt [DemHocSinhGioi v] thành (0)
đặt [ViTri v] thành (1)
nói [Bắt đầu đếm học sinh giỏi (điểm >= 8)...] trong (2) giây
```

#### Thuật toán đếm với hiệu ứng âm thanh
```scratch
lặp lại (8) lần
nếu <(mục (ViTri) của [DanhSachDiem v]) >= [8]> thì
phát âm thanh [pop v]
thay đổi [DemHocSinhGioi v] bởi (1)
nói [Điểm ] + (mục (ViTri) của [DanhSachDiem v]) + [ - Đạt loại giỏi!] trong (2) giây
nếu không
nói [Điểm ] + (mục (ViTri) của [DanhSachDiem v]) + [ - Chưa đạt loại giỏi] trong (1) giây
thay đổi [ViTri v] bởi (1)
chờ (1) giây
nói [Tổng số học sinh giỏi: ] + [DemHocSinhGioi v] + [ học sinh] trong (3) giây
```

#### Hoạt động mở rộng - "Thống kê đầy đủ"
- **Hoạt động**: Đếm số học sinh giỏi, khá, trung bình, yếu
- **Mục tiêu**: Hiểu cách sử dụng nhiều điều kiện trong thuật toán
- **Thử thách**: Tạo biểu đồ trực quan cho thống kê

### Phần 3: Thuật toán tính toán qua trò chơi "Xây tháp" (30 phút)

#### Hoạt động không máy tính - "Xây tháp bằng khối LEGO"
- **Hoạt động**: Xây tháp 5 tầng bằng khối LEGO
- **Quy tắc**: Tầng 1 có 1 khối, tầng 2 có 2 khối, tầng 3 có 3 khối...
- **Mục tiêu**: Hiểu thuật toán tính tổng và giai thừa

#### Bài toán: Tính tổng điểm của lớp
- **Input**: Số học sinh n = 5
- **Output**: Tổng điểm từ 1 đến 5 = 1+2+3+4+5 = 15
- **Ví dụ**: Tính tổng điểm của 5 học sinh đầu tiên

#### Thuật toán tính tổng qua ví dụ thực tế
```
Bước 1: Khởi tạo tổng = 0
Bước 2: Thêm điểm học sinh 1 (1) vào tổng → tổng = 1
Bước 3: Thêm điểm học sinh 2 (2) vào tổng → tổng = 3
Bước 4: Thêm điểm học sinh 3 (3) vào tổng → tổng = 6
Bước 5: Tiếp tục cho đến học sinh thứ 5
```

#### Lập trình trong Scratch với hiệu ứng trực quan
```scratch
Khi cờ xanh được nhấn
đặt [SoHocSinh v] thành (5)
nói [Tính tổng điểm của ] + [SoHocSinh v] + [ học sinh đầu tiên] trong (3) giây
chờ (2) giây
đặt [TongDiem v] thành (0)
đặt [i v] thành (1)
nói [Bắt đầu tính tổng...] trong (2) giây
```

#### Thuật toán tính tổng với hiệu ứng âm thanh
```scratch
lặp lại ([SoHocSinh v]) lần
phát âm thanh [pop v]
thay đổi [TongDiem v] bởi ([i v])
nói [Học sinh ] + [i v] + [ có điểm ] + [i v] + [. Tổng hiện tại: ] + [TongDiem v] trong (2) giây
thay đổi [i v] bởi (1)
chờ (1) giây
nói [Tổng điểm của ] + [SoHocSinh v] + [ học sinh là: ] + [TongDiem v] trong (3) giây
```

#### Hoạt động mở rộng - "Tính điểm trung bình"
- **Hoạt động**: Tính điểm trung bình của lớp
- **Mục tiêu**: Hiểu cách kết hợp nhiều thuật toán
- **Thử thách**: Tạo chương trình tính toán đầy đủ

### Phần 4: Dự án tổng hợp - "Hệ thống quản lý điểm số" (15 phút)

#### Mô tả dự án
- **Mục tiêu**: Tạo hệ thống quản lý điểm số hoàn chỉnh
- **Tính năng**: Nhập điểm, sắp xếp, tìm kiếm, thống kê, tính toán
- **Kết quả**: Chương trình Scratch hoàn chỉnh

#### Thiết kế hệ thống
```
1. Nhập danh sách điểm số
2. Sắp xếp điểm từ cao đến thấp
3. Tìm điểm cao nhất và thấp nhất
4. Đếm số học sinh theo loại
5. Tính điểm trung bình
6. Hiển thị báo cáo tổng hợp
```

#### Lập trình tích hợp
```scratch
Khi cờ xanh được nhấn
nói [=== HỆ THỐNG QUẢN LÝ ĐIỂM SỐ ===] trong (3) giây
chờ (2) giây

# Nhập dữ liệu
đặt [DanhSachDiem v] thành [8,9,7,10,6,9,8,7]
nói [Danh sách điểm: ] + [DanhSachDiem v] trong (3) giây
chờ (2) giây

# Sắp xếp
nói [Đang sắp xếp điểm từ cao đến thấp...] trong (2) giây
# [Code sắp xếp từ bài 6A]

# Tìm kiếm
nói [Đang tìm điểm cao nhất và thấp nhất...] trong (2) giây
# [Code tìm kiếm từ bài 6A]

# Thống kê
nói [Đang thống kê số học sinh theo loại...] trong (2) giây
# [Code đếm từ phần 2]

# Tính toán
nói [Đang tính điểm trung bình...] trong (2) giây
# [Code tính tổng từ phần 3]

# Báo cáo
nói [=== BÁO CÁO TỔNG HỢP ===] trong (3) giây
nói [Điểm cao nhất: ] + [DiemCaoNhat v] trong (2) giây
nói [Điểm thấp nhất: ] + [DiemThapNhat v] trong (2) giây
nói [Số học sinh giỏi: ] + [DemHocSinhGioi v] trong (2) giây
nói [Điểm trung bình: ] + [DiemTrungBinh v] trong (2) giây
```

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
1. **Thống kê lớp học**: Tạo chương trình đếm số học sinh theo loại
2. **Tính điểm trung bình**: Tính điểm trung bình của lớp
3. **Hệ thống đơn giản**: Tạo hệ thống quản lý điểm cơ bản

### Bài tập nâng cao
1. **Thống kê nâng cao**: Tính độ lệch chuẩn và phân phối điểm
2. **Tìm kiếm thông minh**: Tìm học sinh có điểm trong khoảng nhất định
3. **Dự án sáng tạo**: Thiết kế hệ thống quản lý thư viện

## 🔍 Đánh giá

### Tiêu chí đánh giá
| Tiêu chí | Điểm | Mô tả |
|----------|------|-------|
| Hiểu thuật toán | 3 | Giải thích được các bước thuật toán |
| Lập trình đúng | 3 | Code hoạt động chính xác |
| Tích hợp thuật toán | 2 | Kết hợp nhiều thuật toán |
| Sáng tạo | 1 | Có yếu tố độc đáo |
| Trình bày | 1 | Giải thích rõ ràng |
| **Tổng cộng** | **10** | |

### Cách đánh giá
- **Quan sát**: Giáo viên quan sát quá trình tư duy
- **Sản phẩm**: Kiểm tra hệ thống hoàn chỉnh
- **Trình bày**: Học sinh demo và giải thích
- **Phản hồi**: Nhận xét từ bạn cùng lớp

## 🚀 Lưu ý quan trọng

### Cho giáo viên
- Khuyến khích học sinh tích hợp nhiều thuật toán
- Giải thích cách kết hợp các thuật toán
- Tạo không khí học tập tích cực
- Chuẩn bị nhiều ví dụ thực tế

### Cho học sinh
- Hiểu cách kết hợp các thuật toán
- Test kỹ từng phần trước khi tích hợp
- Không ngại thử nghiệm và sai lầm
- Lưu dự án thường xuyên

## 💡 Mẹo hay

### Tích hợp thuật toán
- **Modular programming**: Chia thành các phần nhỏ
- **Test từng phần**: Kiểm tra từng thuật toán trước khi tích hợp
- **Sử dụng biến chung**: Dùng biến để chia sẻ dữ liệu giữa các thuật toán

### Debug hiệu quả
- **Sử dụng "say"**: Thêm lệnh nói để theo dõi giá trị biến
- **Kiểm tra từng bước**: Debug từng phần một thay vì toàn bộ
- **Test với các trường hợp**: Kiểm tra với dữ liệu khác nhau

### Tối ưu hóa
- **Giảm số bước**: Tìm cách làm thuật toán ngắn gọn hơn
- **Sử dụng biến tạm**: Dùng biến tạm để lưu giá trị trung gian
- **Tránh lặp lại**: Không lặp lại các phép tính không cần thiết

## 🔗 Chuẩn bị cho Python

### Khái niệm tương đồng
- **Biến**: Scratch variables ↔ Python variables
- **Vòng lặp**: Scratch loops ↔ Python for/while
- **Điều kiện**: Scratch if/else ↔ Python if/else
- **Danh sách**: Scratch lists ↔ Python lists

### Chuẩn bị cho Python
- Hiểu cú pháp cơ bản
- Làm quen với môi trường lập trình
- Thực hành với các bài toán đơn giản

## 📚 Tài liệu tham khảo

- [Unplugged Activities for Teaching Algorithms](https://missmorenakos.com/education/algorithm-activities/)
- [Teaching Algorithmic Thinking](https://codinginmathclass.wordpress.com/2014/09/10/how-to-teach-algorithmic-thinking/)
- [Computational Thinking in Scratch](https://www.lifeinthetechlab.com/teacher/compThinking/)
- [Scratch Algorithm Projects](https://scratch.mit.edu/explore/projects/algorithms)
- [Introduction to Algorithms](https://scratch.mit.edu/tutorials)
- [Python for Kids](https://python.org)

---

**Tác giả**: AI & Trần Việt Trung (BKHN)  
**Ngày tạo**: 04/10/2025  
**Phiên bản**: 1.0
