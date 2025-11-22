# Bài giảng 7A: Thuật toán tìm số lớn nhất và nhỏ nhất

## 📋 Thông tin bài học
- **Thời gian**: 90 phút
- **Độ tuổi**: 10-11 tuổi
- **Trình độ**: Trung bình
- **Mục tiêu**: Hiểu và áp dụng thuật toán tìm số lớn nhất, nhỏ nhất trong danh sách

## 🎯 Mục tiêu học tập

### Kiến thức
- Hiểu khái niệm thuật toán tìm kiếm
- Nắm vững thuật toán tìm số lớn nhất (max)
- Nắm vững thuật toán tìm số nhỏ nhất (min)
- Biết cách tìm cả max và min trong cùng một lần duyệt

### Kỹ năng
- Phân tích và giải quyết vấn đề có hệ thống
- Áp dụng thuật toán tìm kiếm vào lập trình Scratch
- Sử dụng biến và vòng lặp hiệu quả
- Debug và tối ưu hóa code

### Thái độ
- Phát triển tư duy logic
- Rèn luyện tính kiên trì
- Khuyến khích tư duy phản biện

## 🧠 Nội dung bài học

## 📚 PHẦN LÝ THUYẾT (45 phút)

### Phần 1: Khái niệm thuật toán qua hoạt động không máy tính (20 phút)

#### Hoạt động khởi động - "Kết nối với cấu trúc dữ liệu"
- **Hoạt động**: Nhắc lại bài 6 về cấu trúc dữ liệu (danh sách Pokemon)
- **Câu hỏi**: "Chúng ta đã học cách tổ chức dữ liệu như thế nào?"
- **Kết nối**: "Hôm nay chúng ta sẽ học cách tìm số lớn nhất và nhỏ nhất trong danh sách"
- **Mục tiêu**: Kết nối cấu trúc dữ liệu với thuật toán tìm kiếm

#### Khái niệm thuật toán qua ví dụ thực tế
- **Định nghĩa**: Thuật toán là tập hợp các bước rõ ràng để giải quyết một vấn đề
- **Ví dụ**: Tìm bạn cao nhất trong lớp
- **Input**: Danh sách chiều cao của các bạn
- **Process**: So sánh từng bạn, giữ lại bạn cao nhất
- **Output**: Bạn cao nhất trong lớp
- **Đặc điểm**: Các bước phải rõ ràng, có thứ tự, có thể lặp lại

#### Hoạt động thực hành - "Tìm bạn cao nhất và thấp nhất"
- **Hoạt động**: Học sinh đứng thành hàng, tìm bạn cao nhất và thấp nhất
- **Mục tiêu**: Thực hành thuật toán tìm max và min
- **Kết quả**: Hiểu cách so sánh và cập nhật kết quả

### Phần 2: Thuật toán tìm số lớn nhất (15 phút)

#### Hoạt động không máy tính - "Tìm bạn cao nhất trong lớp"
- **Hoạt động**: Học sinh đứng thành hàng, tìm bạn cao nhất
- **Mục tiêu**: Hiểu thuật toán tìm số lớn nhất
- **Quy tắc**: So sánh từng cặp, giữ lại người cao hơn
- **Kết quả**: Nhận ra thuật toán tìm max có thể áp dụng cho số

#### Bài toán: Tìm điểm cao nhất trong lớp
- **Input**: Danh sách điểm [8, 9, 7, 10, 6]
- **Output**: Điểm cao nhất (10)
- **Ví dụ**: Tìm học sinh có điểm cao nhất trong lớp

#### Thuật toán tìm số lớn nhất qua ví dụ thực tế
```
Bước 1: Giả sử điểm đầu tiên là cao nhất (8)
Bước 2: So sánh với điểm tiếp theo (9)
Bước 3: Vì 9 > 8, cập nhật điểm cao nhất = 9
Bước 4: So sánh với điểm tiếp theo (7)
Bước 5: Vì 7 < 9, giữ nguyên điểm cao nhất = 9
Bước 6: So sánh với điểm tiếp theo (10)
Bước 7: Vì 10 > 9, cập nhật điểm cao nhất = 10
Bước 8: So sánh với điểm tiếp theo (6)
Bước 9: Vì 6 < 10, giữ nguyên điểm cao nhất = 10
Bước 10: Kết quả: Điểm cao nhất là 10
```

#### Hoạt động không máy tính - "Mô phỏng thuật toán"
- **Hoạt động**: Học sinh mô phỏng thuật toán bằng cách so sánh từng cặp số
- **Mục tiêu**: Hiểu rõ từng bước của thuật toán
- **Kết quả**: Nhận ra cần so sánh tất cả các phần tử

### Phần 3: Thuật toán tìm số nhỏ nhất (10 phút)

#### Hoạt động không máy tính - "Tìm bạn thấp nhất trong lớp"
- **Hoạt động**: Học sinh đứng thành hàng, tìm bạn thấp nhất
- **Mục tiêu**: Hiểu thuật toán tìm số nhỏ nhất
- **Quy tắc**: So sánh từng cặp, giữ lại người thấp hơn
- **Kết quả**: Nhận ra thuật toán tìm min tương tự như tìm max

#### Bài toán: Tìm điểm thấp nhất trong lớp
- **Input**: Danh sách điểm [8, 9, 7, 10, 6]
- **Output**: Điểm thấp nhất (6)
- **Ví dụ**: Tìm học sinh có điểm thấp nhất trong lớp

#### Thuật toán tìm số nhỏ nhất qua ví dụ thực tế
```
Bước 1: Giả sử điểm đầu tiên là thấp nhất (8)
Bước 2: So sánh với điểm tiếp theo (9)
Bước 3: Vì 9 > 8, giữ nguyên điểm thấp nhất = 8
Bước 4: So sánh với điểm tiếp theo (7)
Bước 5: Vì 7 < 8, cập nhật điểm thấp nhất = 7
Bước 6: So sánh với điểm tiếp theo (10)
Bước 7: Vì 10 > 7, giữ nguyên điểm thấp nhất = 7
Bước 8: So sánh với điểm tiếp theo (6)
Bước 9: Vì 6 < 7, cập nhật điểm thấp nhất = 6
Bước 10: Kết quả: Điểm thấp nhất là 6
```

## 💻 PHẦN THỰC HÀNH SCRATCH (45 phút)

### Phần 4: Tạo game "Tìm số lớn nhất" trên Scratch (20 phút)

#### Bước 1: Tạo các biến cần thiết
```scratch
# Tạo các biến sau:
1. Biến "DanhSachDiem" - danh sách điểm số (List)
2. Biến "DiemCaoNhat" - lưu điểm cao nhất
3. Biến "ViTri" - chỉ số vị trí hiện tại
```

#### Bước 2: Lập trình thuật toán tìm số lớn nhất
```scratch
Khi cờ xanh được nhấn
# Khởi tạo danh sách điểm
xóa tất cả trong [DanhSachDiem v]
thêm [8] vào [DanhSachDiem v]
thêm [9] vào [DanhSachDiem v]
thêm [7] vào [DanhSachDiem v]
thêm [10] vào [DanhSachDiem v]
thêm [6] vào [DanhSachDiem v]

# Hiển thị danh sách
nói [Danh sách điểm: ] + [DanhSachDiem v] trong (3) giây
chờ (1) giây

# Khởi tạo: Giả sử điểm đầu tiên là cao nhất
đặt [DiemCaoNhat v] thành (mục (1) của [DanhSachDiem v])
đặt [ViTri v] thành (2)
nói [Bắt đầu tìm điểm cao nhất...] trong (2) giây
nói [Giả sử điểm đầu tiên ] + (mục (1) của [DanhSachDiem v]) + [ là cao nhất] trong (2) giây

# Duyệt qua các phần tử còn lại
lặp lại ((chiều dài của [DanhSachDiem v]) - (1)) lần
  nếu <(mục (ViTri) của [DanhSachDiem v]) > [DiemCaoNhat v]> thì
    đặt [DiemCaoNhat v] thành (mục (ViTri) của [DanhSachDiem v])
    phát âm thanh [pop v]
    nói [Tìm thấy điểm cao hơn: ] + [DiemCaoNhat v] + [ tại vị trí ] + [ViTri v] trong (2) giây
  nếu không
    nói [Điểm ] + (mục (ViTri) của [DanhSachDiem v]) + [ không lớn hơn ] + [DiemCaoNhat v] trong (1) giây
  thay đổi [ViTri v] bởi (1)
  chờ (0.5) giây

# Kết quả
nói [=== KẾT QUẢ ===] trong (2) giây
nói [Điểm cao nhất trong danh sách là: ] + [DiemCaoNhat v] trong (3) giây
```

#### Hoạt động mở rộng - "Tìm vị trí của số lớn nhất"
- **Hoạt động**: Thay đổi thuật toán để tìm cả giá trị và vị trí của số lớn nhất
- **Mục tiêu**: Hiểu cách lưu trữ thông tin bổ sung
- **Thử thách**: Tìm tất cả các vị trí có giá trị lớn nhất (nếu có nhiều số bằng nhau)

### Phần 5: Tạo game "Tìm số nhỏ nhất" trên Scratch (15 phút)

#### Bước 1: Lập trình thuật toán tìm số nhỏ nhất
```scratch
Khi nhấn phím [m v]
# Khởi tạo danh sách điểm
xóa tất cả trong [DanhSachDiem v]
thêm [8] vào [DanhSachDiem v]
thêm [9] vào [DanhSachDiem v]
thêm [7] vào [DanhSachDiem v]
thêm [10] vào [DanhSachDiem v]
thêm [6] vào [DanhSachDiem v]

# Hiển thị danh sách
nói [Danh sách điểm: ] + [DanhSachDiem v] trong (3) giây
chờ (1) giây

# Khởi tạo: Giả sử điểm đầu tiên là thấp nhất
đặt [DiemThapNhat v] thành (mục (1) của [DanhSachDiem v])
đặt [ViTri v] thành (2)
nói [Bắt đầu tìm điểm thấp nhất...] trong (2) giây
nói [Giả sử điểm đầu tiên ] + (mục (1) của [DanhSachDiem v]) + [ là thấp nhất] trong (2) giây

# Duyệt qua các phần tử còn lại
lặp lại ((chiều dài của [DanhSachDiem v]) - (1)) lần
  nếu <(mục (ViTri) của [DanhSachDiem v]) < [DiemThapNhat v]> thì
    đặt [DiemThapNhat v] thành (mục (ViTri) của [DanhSachDiem v])
    phát âm thanh [pop v]
    nói [Tìm thấy điểm thấp hơn: ] + [DiemThapNhat v] + [ tại vị trí ] + [ViTri v] trong (2) giây
  nếu không
    nói [Điểm ] + (mục (ViTri) của [DanhSachDiem v]) + [ không thấp hơn ] + [DiemThapNhat v] trong (1) giây
  thay đổi [ViTri v] bởi (1)
  chờ (0.5) giây

# Kết quả
nói [=== KẾT QUẢ ===] trong (2) giây
nói [Điểm thấp nhất trong danh sách là: ] + [DiemThapNhat v] trong (3) giây
```

#### Hoạt động mở rộng - "So sánh thuật toán"
- **Hoạt động**: So sánh điểm khác biệt giữa tìm max và tìm min
- **Mục tiêu**: Hiểu cách điều chỉnh điều kiện so sánh
- **Thử thách**: Viết một hàm có thể tìm cả max và min

### Phần 6: Tìm cả số lớn nhất và nhỏ nhất trong một lần duyệt (10 phút)

#### Bài toán: Tìm điểm cao nhất và thấp nhất cùng lúc
- **Input**: Danh sách điểm [8, 9, 7, 10, 6]
- **Output**: Điểm cao nhất (10) và điểm thấp nhất (6)
- **Lợi ích**: Tiết kiệm thời gian, chỉ cần duyệt danh sách một lần

#### Lập trình tìm cả max và min
```scratch
Khi nhấn phím [b v]
# Khởi tạo danh sách điểm
xóa tất cả trong [DanhSachDiem v]
thêm [8] vào [DanhSachDiem v]
thêm [9] vào [DanhSachDiem v]
thêm [7] vào [DanhSachDiem v]
thêm [10] vào [DanhSachDiem v]
thêm [6] vào [DanhSachDiem v]

# Hiển thị danh sách
nói [Danh sách điểm: ] + [DanhSachDiem v] trong (3) giây
chờ (1) giây

# Khởi tạo: Giả sử điểm đầu tiên là cả max và min
đặt [DiemCaoNhat v] thành (mục (1) của [DanhSachDiem v])
đặt [DiemThapNhat v] thành (mục (1) của [DanhSachDiem v])
đặt [ViTri v] thành (2)
nói [Bắt đầu tìm điểm cao nhất và thấp nhất...] trong (2) giây

# Duyệt qua các phần tử còn lại
lặp lại ((chiều dài của [DanhSachDiem v]) - (1)) lần
  # Kiểm tra max
  nếu <(mục (ViTri) của [DanhSachDiem v]) > [DiemCaoNhat v]> thì
    đặt [DiemCaoNhat v] thành (mục (ViTri) của [DanhSachDiem v])
    phát âm thanh [pop v]
    nói [Tìm thấy điểm cao hơn: ] + [DiemCaoNhat v] trong (1) giây
  
  # Kiểm tra min
  nếu <(mục (ViTri) của [DanhSachDiem v]) < [DiemThapNhat v]> thì
    đặt [DiemThapNhat v] thành (mục (ViTri) của [DanhSachDiem v])
    phát âm thanh [pop v]
    nói [Tìm thấy điểm thấp hơn: ] + [DiemThapNhat v] trong (1) giây
  
  thay đổi [ViTri v] bởi (1)
  chờ (0.5) giây

# Kết quả
nói [=== KẾT QUẢ ===] trong (2) giây
nói [Điểm cao nhất: ] + [DiemCaoNhat v] trong (2) giây
nói [Điểm thấp nhất: ] + [DiemThapNhat v] trong (2) giây
nói [Khoảng cách: ] + ([DiemCaoNhat v] - [DiemThapNhat v]) trong (2) giây
```

#### Hoạt động mở rộng - "Tối ưu hóa thuật toán"
- **Hoạt động**: So sánh hiệu suất giữa tìm riêng và tìm chung
- **Mục tiêu**: Hiểu tầm quan trọng của tối ưu hóa
- **Thử thách**: Tìm số lớn thứ hai trong danh sách

## 🎯 Tổng kết và đánh giá (10 phút)

### Tổng kết kiến thức
- **Thuật toán tìm max**: So sánh từng phần tử và cập nhật kết quả
- **Thuật toán tìm min**: Tương tự max nhưng so sánh ngược lại
- **Tối ưu hóa**: Có thể tìm cả max và min trong một lần duyệt
- **Ứng dụng**: Tìm kiếm có mặt khắp nơi trong cuộc sống

### Đánh giá học sinh
- **Hiểu thuật toán**: Có thể giải thích các bước của thuật toán tìm max/min
- **Áp dụng thực tế**: Tìm được ví dụ tìm kiếm trong cuộc sống
- **Lập trình Scratch**: Tạo được chương trình tìm max và min
- **Tư duy logic**: Phân tích và giải quyết vấn đề có hệ thống

## 🎨 Hoạt động mở rộng

### Cấp độ 1: Thêm tính năng cơ bản
- **Giao diện tương tác**: Tạo nút để nhập dữ liệu mới
- **Hiệu ứng trực quan**: Thêm màu sắc và animation khi tìm kiếm
- **Âm thanh**: Tạo âm thanh khác nhau khi tìm thấy max/min

### Cấp độ 2: Tính năng nâng cao
- **Tìm số lớn thứ hai**: Tìm số lớn thứ hai trong danh sách
- **Tìm nhiều giá trị**: Tìm tất cả các số lớn nhất (nếu có nhiều số bằng nhau)
- **Tìm theo điều kiện**: Tìm số lớn nhất trong các số chẵn

### Cấp độ 3: Sáng tạo
- **Game tìm kiếm**: Tạo trò chơi tìm số lớn nhất/nhỏ nhất
- **Thuật toán riêng**: Thiết kế thuật toán tìm kiếm mới
- **Dự án tích hợp**: Kết hợp tìm max/min với các thuật toán khác

## 📝 Bài tập về nhà

### Bài tập bắt buộc
1. **Tìm điểm cao nhất**: Viết thuật toán tìm điểm cao nhất trong 7 điểm số
2. **Tìm điểm thấp nhất**: Viết thuật toán tìm điểm thấp nhất trong 7 điểm số
3. **Tìm cả hai**: Tạo chương trình tìm cả điểm cao nhất và thấp nhất cùng lúc

### Bài tập nâng cao
1. **Tìm số lớn thứ hai**: Tìm số lớn thứ hai trong danh sách
2. **Tìm vị trí**: Tìm cả giá trị và vị trí của số lớn nhất/nhỏ nhất
3. **Tìm theo điều kiện**: Tìm số lớn nhất trong các số chẵn

### Bài tập sáng tạo
1. **Game điểm số**: Tạo game cho phép nhập điểm và hiển thị max/min
2. **Thuật toán riêng**: Thiết kế thuật toán tìm kiếm độc đáo
3. **Dự án tích hợp**: Kết hợp tìm max/min với các bài học khác

## 🔧 Tài nguyên hỗ trợ

### Tài liệu tham khảo
- **Scratch Programming**: Hướng dẫn lập trình Scratch cơ bản
- **Algorithm Visualization**: Công cụ minh họa thuật toán
- **Unplugged Activities**: Hoạt động không máy tính cho thuật toán

### Công cụ hỗ trợ
- **Scratch Editor**: Môi trường lập trình trực quan
- **Algorithm Simulator**: Mô phỏng thuật toán
- **Debugging Tools**: Công cụ gỡ lỗi và tối ưu hóa

### Đánh giá và phản hồi
- **Rubric đánh giá**: Tiêu chí đánh giá kỹ năng thuật toán
- **Peer Review**: Đánh giá lẫn nhau giữa học sinh
- **Portfolio**: Tập hợp các dự án và bài tập của học sinh

## 🔗 Kết nối với bài học khác

### Kiến thức liên quan
- **Bài 6**: Cấu trúc dữ liệu - Sử dụng danh sách (List)
- **Bài 7B**: Thuật toán đếm - Đếm số phần tử theo điều kiện
- **Bài 7C**: Thuật toán tính toán - Tính tổng và trung bình

### Chuẩn bị cho bài tiếp theo
- Hiểu cách duyệt qua danh sách
- Nắm vững so sánh và cập nhật giá trị
- Sẵn sàng học thuật toán đếm (Bài 7B)

---

**Tác giả**: AI & Trần Việt Trung (BKHN)  
**Ngày tạo**: 04/10/2025  
**Phiên bản**: 1.0

