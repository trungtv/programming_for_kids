# Bài giảng 2.5: Biến số cơ bản

## 📋 Thông tin bài học
- **Thời gian**: 45 phút
- **Độ tuổi**: 8-9 tuổi
- **Trình độ**: Cơ bản đến trung bình
- **Mục tiêu**: Làm quen với biến số và cách sử dụng trong Scratch

## 🎯 Mục tiêu học tập

### Kiến thức
- Hiểu khái niệm biến số là gì
- Biết cách tạo và sử dụng biến số trong Scratch
- Hiểu cách biến số lưu trữ và thay đổi giá trị

### Kỹ năng
- Tạo biến số trong Scratch
- Sử dụng biến số để đếm và tính toán
- Hiển thị giá trị biến số trên màn hình

### Thái độ
- Phát triển tư duy logic toán học
- Rèn luyện tính chính xác
- Khuyến khích thử nghiệm và khám phá

## 🧠 Nội dung bài học

## 📚 PHẦN LÝ THUYẾT (25 phút)

### Phần 1: Khái niệm biến số qua hoạt động không máy tính (15 phút)

#### Hoạt động khởi động - "Hộp đựng đồ"
- **Hoạt động**: Giáo viên cầm một hộp và hỏi: "Hộp này đựng gì?"
- **Câu hỏi**: "Hộp có thể đựng những gì?"
- **Kết nối**: "Hôm nay chúng ta sẽ học về 'hộp' đặc biệt trong máy tính"
- **Mục tiêu**: Hiểu biến số như một "hộp" để chứa thông tin

#### Khái niệm biến số qua ví dụ thực tế
- **Hộp điểm số**: Có thể chứa 8, 9, 10...
- **Hộp tên**: Có thể chứa "An", "Bình", "Châu"...
- **Hộp tuổi**: Có thể chứa 8, 9, 10...
- **Hộp màu sắc**: Có thể chứa "đỏ", "xanh", "vàng"...

#### Hoạt động thực hành - "Đếm số bạn trong lớp"
- **Hoạt động**: Học sinh đếm số bạn nam và nữ trong lớp
- **Mục tiêu**: Thực hành sử dụng biến số để đếm
- **Quy tắc**: Đi từ đầu đến cuối lớp, đếm từng người một
- **Kết quả**: Hiểu cách biến số giúp theo dõi thông tin

#### Bài toán: Hiểu biến số
- **Tên biến**: Nhãn dán trên hộp (ví dụ: "điểm", "tuổi")
- **Giá trị**: Nội dung trong hộp (ví dụ: 8, "An")
- **Thay đổi**: Có thể thay đổi nội dung trong hộp
- **Ví dụ**: Hộp "điểm" có thể chứa 5, sau đó thay đổi thành 8

### Phần 2: Khái niệm đếm và tính toán qua hoạt động không máy tính (10 phút)

#### Hoạt động không máy tính - "Đếm số lần vỗ tay"
- **Hoạt động**: Học sinh vỗ tay và đếm số lần
- **Mục tiêu**: Hiểu cách đếm và tăng giá trị
- **Quy tắc**: Mỗi lần vỗ tay, tăng số đếm lên 1
- **Kết quả**: Nhận ra đếm là tăng giá trị lên 1

#### Bài toán: Đếm số lần nhấn phím
- **Mục tiêu**: Mỗi lần nhấn phím cách, tăng điểm số lên 1
- **Ví dụ**: Nhấn 3 lần → điểm số = 3
- **Ứng dụng**: Game đếm điểm, thống kê

#### Hoạt động không máy tính - "Tính tổng điểm"
- **Hoạt động**: Học sinh tính tổng điểm của 3 bài kiểm tra
- **Mục tiêu**: Hiểu cách sử dụng biến số để tính toán
- **Quy tắc**: Cộng từng điểm một vào tổng
- **Kết quả**: Nhận ra biến số có thể dùng để tính toán

## 💻 PHẦN THỰC HÀNH SCRATCH (20 phút)

### Phần 3: Tạo biến số đầu tiên trên Scratch (10 phút)

#### Lập trình trong Scratch với hướng dẫn từng bước
```scratch
# Bước 1: Tạo biến số đầu tiên
1. Mở Scratch và tạo dự án mới
2. Chọn "Variables" (Biến số) trong menu
3. Nhấn "Make a Variable" (Tạo biến số)
4. Đặt tên: "DiemSo"
5. Chọn "For all sprites" (Cho tất cả nhân vật)

# Bước 2: Hiển thị và thay đổi giá trị
Khi cờ xanh được nhấn
đặt [DiemSo v] thành (5)
nói [Điểm số của tôi là: ] + [DiemSo v] trong (3) giây
```

#### Hoạt động mở rộng - "Thay đổi điểm số"
- **Hoạt động**: Học sinh thay đổi giá trị biến số và quan sát
- **Mục tiêu**: Hiểu cách thay đổi giá trị biến số
- **Thử thách**: Thử các giá trị khác nhau (1, 10, 100)

### Phần 4: Sử dụng biến số để đếm trên Scratch (10 phút)

#### Lập trình trong Scratch với hiệu ứng trực quan
```scratch
# Đếm số lần nhấn phím
Khi cờ xanh được nhấn
đặt [DiemSo v] thành (0)
nói [Bắt đầu đếm! Nhấn phím cách để tăng điểm] trong (3) giây

Khi nhấn phím [cách v]
thay đổi [DiemSo v] bởi (1)
nói [Điểm số: ] + [DiemSo v] trong (1) giây

# Tính tổng điểm
Khi cờ xanh được nhấn
đặt [DiemSo v] thành (0)
đặt [TongDiem v] thành (0)
nói [Nhấn phím cách để thêm điểm] trong (3) giây

Khi nhấn phím [cách v]
thay đổi [DiemSo v] bởi (1)
thay đổi [TongDiem v] bởi ([DiemSo v])
nói [Điểm hiện tại: ] + [DiemSo v] + [. Tổng: ] + [TongDiem v] trong (2) giây
```

#### Hoạt động mở rộng - "Đếm với nhiều phím"
- **Hoạt động**: Tạo biến số cho từng phím (A, S, D)
- **Mục tiêu**: Hiểu cách sử dụng nhiều biến số
- **Thử thách**: Tạo game đếm điểm đơn giản

## 🎯 Tổng kết và đánh giá (10 phút)

### Tổng kết kiến thức
- **Biến số**: Như một hộp để chứa thông tin
- **Tên biến**: Nhãn dán trên hộp để phân biệt
- **Giá trị**: Nội dung trong hộp có thể thay đổi
- **Đếm**: Tăng giá trị biến số lên 1
- **Tính toán**: Sử dụng biến số trong phép toán

### Đánh giá học sinh
- **Hiểu biến số**: Có thể giải thích khái niệm biến số
- **Tạo biến số**: Tạo được biến số trong Scratch
- **Sử dụng đúng**: Sử dụng biến số để đếm và tính toán
- **Tư duy logic**: Hiểu được cách biến số hoạt động

## 🎨 Hoạt động mở rộng

### Cấp độ 1: Thêm tính năng cơ bản
- **Hiển thị đẹp**: Thay đổi màu sắc và kích thước biến số
- **Âm thanh**: Thêm âm thanh khi thay đổi giá trị
- **Hiệu ứng**: Thêm animation khi biến số thay đổi

### Cấp độ 2: Tính năng nâng cao
- **Nhiều biến số**: Tạo biến số cho điểm, thời gian, level
- **Tính toán**: Sử dụng biến số trong phép toán
- **Điều kiện**: Sử dụng biến số trong điều kiện if/else

### Cấp độ 3: Sáng tạo
- **Game đếm điểm**: Tạo game đơn giản với hệ thống điểm
- **Máy tính đơn giản**: Sử dụng biến số để tính toán
- **Thống kê**: Đếm và hiển thị thống kê đơn giản

## 📝 Bài tập về nhà

### Bài tập bắt buộc
1. **Đếm số lần nhấn**: Tạo chương trình đếm số lần nhấn phím cách
2. **Tính tổng**: Tạo chương trình tính tổng từ 1 đến 10
3. **Hiển thị thông tin**: Tạo chương trình hiển thị tên và tuổi

### Bài tập nâng cao
1. **Game đếm**: Tạo game đếm điểm với nhiều phím
2. **Máy tính đơn giản**: Tạo máy tính cộng trừ đơn giản
3. **Thống kê**: Đếm số học sinh nam và nữ trong lớp

### Bài tập sáng tạo
1. **Game điểm số**: Tạo game đếm điểm với nhiều tính năng
2. **Máy tính cá nhân**: Tạo máy tính với giao diện đẹp
3. **Dự án tích hợp**: Kết hợp biến số với các bài học trước

## 🔧 Tài nguyên hỗ trợ

### Tài liệu tham khảo
- **Scratch Variables Tutorial**: Hướng dẫn sử dụng biến số
- **Teaching Variables to Kids**: Phương pháp dạy biến số cho trẻ em
- **Scratch Programming for Kids**: Lập trình Scratch cho trẻ em

### Công cụ hỗ trợ
- **Scratch Editor**: Môi trường lập trình trực quan
- **Variable Blocks**: Khối lệnh biến số trong Scratch
- **Debugging Tools**: Công cụ gỡ lỗi và kiểm tra giá trị

### Đánh giá và phản hồi
- **Rubric đánh giá**: Tiêu chí đánh giá kỹ năng sử dụng biến số
- **Peer Review**: Đánh giá lẫn nhau giữa học sinh
- **Portfolio**: Tập hợp các dự án và bài tập của học sinh