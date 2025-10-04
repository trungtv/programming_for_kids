# Bài giảng 7A: Thuật toán cơ bản - Tìm số lớn nhất và đếm

## 📋 Thông tin bài học
- **Thời gian**: 90 phút
- **Độ tuổi**: 10-11 tuổi
- **Trình độ**: Trung bình
- **Mục tiêu**: Hiểu thuật toán cơ bản và áp dụng vào Scratch

## 🎯 Mục tiêu học tập

### Kiến thức
- Hiểu khái niệm thuật toán
- Nắm vững thuật toán tìm số lớn nhất
- Hiểu thuật toán đếm số phần tử
- Biết cách áp dụng thuật toán vào thực tế

### Kỹ năng
- Phân tích và giải quyết vấn đề có hệ thống
- Áp dụng thuật toán vào lập trình Scratch
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
- **Kết nối**: "Hôm nay chúng ta sẽ học cách xử lý dữ liệu đã tổ chức"
- **Mục tiêu**: Kết nối cấu trúc dữ liệu với thuật toán

#### Khái niệm thuật toán qua ví dụ thực tế
- **Định nghĩa**: Thuật toán là tập hợp các bước rõ ràng để giải quyết một vấn đề
- **Ví dụ**: Công thức làm bánh sandwich
- **Input**: Nguyên liệu (bánh mì, bơ, thịt, rau)
- **Process**: Các bước chế biến (phết bơ, đặt thịt...)
- **Output**: Bánh sandwich hoàn chỉnh
- **Đặc điểm**: Các bước phải rõ ràng, có thứ tự, có thể lặp lại

#### Hoạt động thực hành - "Hướng dẫn bạn đi từ lớp đến thư viện"
- **Hoạt động**: Học sinh viết hướng dẫn chi tiết từ lớp đến thư viện
- **Mục tiêu**: Thực hành chia nhỏ vấn đề thành các bước
- **Kết quả**: Hiểu tầm quan trọng của thuật toán trong cuộc sống

### Phần 2: Thuật toán đơn giản - Tìm số lớn nhất và đếm (25 phút)

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
Bước 6: Tiếp tục cho đến hết danh sách
```

#### Hoạt động không máy tính - "Đếm số bạn trong lớp"
- **Hoạt động**: Học sinh đếm số bạn nam và nữ trong lớp
- **Mục tiêu**: Hiểu thuật toán đếm đơn giản
- **Quy tắc**: Đi từ đầu đến cuối lớp, đếm từng người một
- **Kết quả**: Nhận ra thuật toán đếm có thể áp dụng cho nhiều tình huống

#### Bài toán: Đếm số học sinh giỏi
- **Input**: Danh sách điểm [8, 9, 7, 10, 6]
- **Output**: Số học sinh có điểm >= 8 (3 học sinh)
- **Ví dụ**: Đếm số bạn đạt loại giỏi trong lớp

#### Thuật toán đếm qua ví dụ thực tế
```
Bước 1: Khởi tạo biến đếm = 0
Bước 2: Xem điểm của bạn đầu tiên (8)
Bước 3: Vì 8 >= 8, tăng biến đếm lên 1
Bước 4: Xem điểm của bạn tiếp theo (9)
Bước 5: Vì 9 >= 8, tăng biến đếm lên 2
Bước 6: Tiếp tục cho đến hết danh sách
```

## 💻 PHẦN THỰC HÀNH SCRATCH (45 phút)

### Phần 3: Tạo game "Tìm số lớn nhất" trên Scratch (15 phút)

#### Lập trình trong Scratch với hiệu ứng trực quan
```scratch
Khi cờ xanh được nhấn
đặt [DanhSachDiem v] thành [8,9,7,10,6]
nói [Danh sách điểm: ] + [DanhSachDiem v] trong (3) giây
đặt [DiemCaoNhat v] thành [8]
đặt [ViTri v] thành [1]
nói [Bắt đầu tìm điểm cao nhất...] trong (2) giây
lặp lại (4) lần
  nếu <[DiemCaoNhat v] < [DanhSachDiem v]> thì
    đặt [DiemCaoNhat v] thành [DanhSachDiem v]
    nói [Tìm thấy điểm cao hơn: ] + [DiemCaoNhat v] trong (2) giây
  thay đổi [ViTri v] bởi (1)
nói [Điểm cao nhất là: ] + [DiemCaoNhat v] trong (3) giây
```

#### Hoạt động mở rộng - "Tìm số nhỏ nhất"
- **Hoạt động**: Thay đổi thuật toán để tìm số nhỏ nhất
- **Mục tiêu**: Hiểu cách điều chỉnh thuật toán cho các mục đích khác nhau
- **Thử thách**: Tìm cả số lớn nhất và nhỏ nhất trong cùng một lần duyệt

### Phần 4: Tạo game "Đếm số học sinh giỏi" trên Scratch (15 phút)

#### Lập trình trong Scratch với hiệu ứng trực quan
```scratch
Khi cờ xanh được nhấn
đặt [DanhSachDiem v] thành [8,9,7,10,6]
nói [Danh sách điểm: ] + [DanhSachDiem v] trong (3) giây
đặt [SoHocSinhGioi v] thành [0]
đặt [ViTri v] thành [1]
nói [Bắt đầu đếm học sinh giỏi...] trong (2) giây
lặp lại (5) lần
  nếu <[DanhSachDiem v] >= [8]> thì
    thay đổi [SoHocSinhGioi v] bởi (1)
    nói [Tìm thấy học sinh giỏi!] trong (1) giây
  thay đổi [ViTri v] bởi (1)
nói [Số học sinh giỏi: ] + [SoHocSinhGioi v] trong (3) giây
```

#### Hoạt động mở rộng - "Đếm với điều kiện khác"
- **Hoạt động**: Thay đổi điều kiện đếm (ví dụ: điểm >= 9)
- **Mục tiêu**: Hiểu cách điều chỉnh điều kiện trong thuật toán
- **Thử thách**: Đếm nhiều loại học sinh cùng lúc (giỏi, khá, trung bình)

## 🎯 Tổng kết và đánh giá (10 phút)

### Tổng kết kiến thức
- **Thuật toán**: Các bước rõ ràng để giải quyết vấn đề
- **Tìm số lớn nhất**: So sánh từng phần tử và cập nhật kết quả
- **Đếm**: Duyệt qua danh sách và đếm theo điều kiện
- **Ứng dụng**: Thuật toán có mặt khắp nơi trong cuộc sống

### Đánh giá học sinh
- **Hiểu thuật toán**: Có thể giải thích các bước của thuật toán
- **Áp dụng thực tế**: Tìm được ví dụ thuật toán trong cuộc sống
- **Lập trình Scratch**: Tạo được chương trình tìm max và đếm
- **Tư duy logic**: Phân tích và giải quyết vấn đề có hệ thống

## 🎨 Hoạt động mở rộng

### Cấp độ 1: Thêm tính năng cơ bản
- **Giao diện tương tác**: Tạo nút để nhập dữ liệu mới
- **Hiệu ứng trực quan**: Thêm màu sắc và animation khi thực hiện thuật toán
- **Âm thanh**: Tạo âm thanh khác nhau cho từng loại thuật toán

### Cấp độ 2: Tính năng nâng cao
- **Tìm kiếm thông minh**: Tìm kiếm với nhiều điều kiện
- **Đếm phức tạp**: Đếm nhiều loại cùng lúc
- **So sánh hiệu suất**: So sánh tốc độ của các thuật toán khác nhau

### Cấp độ 3: Sáng tạo
- **Game thuật toán**: Tạo trò chơi tìm số và đếm
- **Thuật toán riêng**: Thiết kế thuật toán giải quyết vấn đề thực tế
- **Dự án tích hợp**: Kết hợp tìm max và đếm trong một dự án

## 📝 Bài tập về nhà

### Bài tập bắt buộc
1. **Tìm điểm cao nhất**: Viết thuật toán tìm điểm cao nhất trong 7 điểm số
2. **Đếm học sinh khá**: Tạo chương trình đếm số học sinh có điểm >= 7
3. **Tìm số nhỏ nhất**: Sửa đổi thuật toán để tìm điểm thấp nhất

### Bài tập nâng cao
1. **Đếm nhiều loại**: Đếm đồng thời số học sinh giỏi, khá, trung bình
2. **Tìm kiếm thông minh**: Tìm số lớn thứ hai trong danh sách
3. **Thống kê cơ bản**: Tính tổng và trung bình điểm số

### Bài tập sáng tạo
1. **Game điểm số**: Tạo game cho phép nhập điểm và hiển thị thống kê
2. **Thuật toán riêng**: Thiết kế thuật toán giải quyết vấn đề trong lớp học
3. **Dự án tích hợp**: Kết hợp tìm max và đếm vào một dự án lớn

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