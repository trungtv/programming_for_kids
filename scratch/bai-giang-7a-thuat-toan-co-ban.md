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
- Biết cách sắp xếp đơn giản

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

### Phần 5: Tạo game "Sắp xếp số" trên Scratch (15 phút)

#### Hoạt động không máy tính - "Sắp xếp học sinh theo chiều cao"
- **Hoạt động**: Yêu cầu học sinh đứng thành hàng theo chiều cao từ thấp đến cao
- **Mục tiêu**: Hiểu thuật toán sắp xếp bằng cách so sánh và đổi chỗ
- **Quy tắc**: Chỉ được so sánh 2 người cạnh nhau, nếu sai thứ tự thì đổi chỗ

#### Bài toán: Sắp xếp điểm số từ cao đến thấp
- **Input**: Danh sách điểm [8, 9, 7, 10, 6]
- **Output**: Danh sách đã sắp xếp [10, 9, 8, 7, 6]
- **Ví dụ**: Sắp xếp điểm của lớp từ cao đến thấp

#### Thuật toán sắp xếp qua ví dụ thực tế
```
Bước 1: So sánh điểm đầu tiên (8) với điểm thứ hai (9)
Bước 2: Vì 8 < 9, đổi chỗ: [9, 8, 7, 10, 6]
Bước 3: So sánh điểm thứ hai (8) với điểm thứ ba (7)
Bước 4: Vì 8 > 7, giữ nguyên: [9, 8, 7, 10, 6]
Bước 5: Tiếp tục cho đến hết danh sách
```

#### Lập trình trong Scratch với hiệu ứng trực quan
```scratch
Khi cờ xanh được nhấn
đặt [So1 v] thành [8]
đặt [So2 v] thành [9]
đặt [So3 v] thành [7]
nói [Trước khi sắp xếp: ] + [So1 v] + [, ] + [So2 v] + [, ] + [So3 v] trong (3) giây
lặp lại (3) lần
nếu <[So1 v] > [So2 v]> thì
phát âm thanh [pop v]
đặt [Temp v] thành [So1 v]
đặt [So1 v] thành [So2 v]
đặt [So2 v] thành [Temp v]
nói [Đã đổi chỗ số 1 và số 2] trong (2) giây
nếu <[So2 v] > [So3 v]> thì
phát âm thanh [pop v]
đặt [Temp v] thành [So2 v]
đặt [So2 v] thành [So3 v]
đặt [So3 v] thành [Temp v]
nói [Đã đổi chỗ số 2 và số 3] trong (2) giây
nói [Sau khi sắp xếp: ] + [So1 v] + [, ] + [So2 v] + [, ] + [So3 v] trong (3) giây
```

#### Hoạt động mở rộng - "Sắp xếp 5 số"
- **Hoạt động**: Mở rộng thuật toán cho 5 số
- **Mục tiêu**: Hiểu cách thuật toán hoạt động với nhiều phần tử hơn
- **Thử thách**: Tìm cách tối ưu hóa thuật toán

## 🎯 Tổng kết và đánh giá (10 phút)

### Tổng kết kiến thức
- **Thuật toán**: Các bước rõ ràng để giải quyết vấn đề
- **Tìm số lớn nhất**: So sánh từng phần tử và cập nhật kết quả
- **Đếm**: Duyệt qua danh sách và đếm theo điều kiện
- **Sắp xếp**: So sánh và đổi chỗ để sắp xếp theo thứ tự
- **Ứng dụng**: Thuật toán có mặt khắp nơi trong cuộc sống

### Đánh giá học sinh
- **Hiểu thuật toán**: Có thể giải thích các bước của thuật toán
- **Áp dụng thực tế**: Tìm được ví dụ thuật toán trong cuộc sống
- **Lập trình Scratch**: Tạo được chương trình tìm max, đếm và sắp xếp
- **Tư duy logic**: Phân tích và giải quyết vấn đề có hệ thống

## 🎨 Hoạt động mở rộng

### Cấp độ 1: Thêm tính năng cơ bản
- **Giao diện tương tác**: Tạo nút để nhập dữ liệu mới
- **Hiệu ứng trực quan**: Thêm màu sắc và animation khi thực hiện thuật toán
- **Âm thanh**: Tạo âm thanh khác nhau cho từng loại thuật toán

### Cấp độ 2: Tính năng nâng cao
- **Sắp xếp nhiều phần tử**: Mở rộng thuật toán cho 10 số
- **Tìm kiếm thông minh**: Tìm kiếm với nhiều điều kiện
- **So sánh hiệu suất**: So sánh tốc độ của các thuật toán khác nhau

### Cấp độ 3: Sáng tạo
- **Game thuật toán**: Tạo trò chơi sắp xếp thẻ bài
- **Thuật toán riêng**: Thiết kế thuật toán giải quyết vấn đề thực tế
- **Dự án tích hợp**: Kết hợp tìm max, đếm và sắp xếp trong một dự án

## 📝 Bài tập về nhà

### Bài tập bắt buộc
1. **Tìm điểm cao nhất**: Viết thuật toán tìm điểm cao nhất trong 7 điểm số
2. **Đếm học sinh khá**: Tạo chương trình đếm số học sinh có điểm >= 7
3. **Sắp xếp tên**: Sắp xếp danh sách tên học sinh theo thứ tự ABC

### Bài tập nâng cao
1. **Tìm điểm thấp nhất**: Sửa đổi thuật toán để tìm điểm thấp nhất
2. **Đếm nhiều loại**: Đếm đồng thời số học sinh giỏi, khá, trung bình
3. **Sắp xếp ngược**: Sắp xếp danh sách từ thấp đến cao

### Bài tập sáng tạo
1. **Game điểm số**: Tạo game cho phép nhập điểm và hiển thị thống kê
2. **Thuật toán riêng**: Thiết kế thuật toán giải quyết vấn đề trong lớp học
3. **Dự án tích hợp**: Kết hợp tất cả thuật toán đã học vào một dự án lớn

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