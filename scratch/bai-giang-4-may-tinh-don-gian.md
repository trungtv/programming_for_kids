# Bài giảng 4: Máy tính đơn giản

## 📋 Thông tin bài học
- **Thời gian**: 90 phút
- **Độ tuổi**: 9-11 tuổi
- **Trình độ**: Trung bình
- **Mục tiêu**: Tạo máy tính đơn giản với các phép toán cơ bản

## 🎯 Mục tiêu học tập

### Kiến thức
- Hiểu cách sử dụng biến số và phép toán
- Biết cách tạo giao diện người dùng
- Hiểu khái niệm input và output

### Kỹ năng
- Thiết kế giao diện đơn giản
- Lập trình logic tính toán
- Xử lý dữ liệu đầu vào

### Thái độ
- Phát triển tư duy logic toán học
- Rèn luyện tính chính xác
- Khuyến khích ứng dụng thực tế

## 🧠 Nội dung bài học

## 📚 PHẦN LÝ THUYẾT (45 phút)

### Phần 1: Khái niệm máy tính qua hoạt động không máy tính (25 phút)

#### Hoạt động khởi động - "Máy tính thật"
- **Hoạt động**: Học sinh quan sát máy tính thật và thảo luận
- **Câu hỏi**: "Máy tính hoạt động như thế nào?"
- **Kết nối**: "Hôm nay chúng ta sẽ tạo máy tính đơn giản bằng Scratch"
- **Mục tiêu**: Hiểu chức năng cơ bản của máy tính

#### Khái niệm máy tính qua ví dụ thực tế
- **Input**: Dữ liệu đầu vào (số, phép toán)
- **Process**: Xử lý tính toán
- **Output**: Kết quả đầu ra
- **Giao diện**: Màn hình hiển thị và nút bấm

#### Hoạt động thực hành - "Thiết kế máy tính trên giấy"
- **Hoạt động**: Học sinh vẽ phác thảo máy tính trên giấy
- **Yêu cầu**: Có màn hình hiển thị, nút số 0-9, nút phép toán
- **Mục tiêu**: Có ý tưởng thiết kế trước khi làm trên Scratch
- **Kết quả**: Hiểu các thành phần cần thiết của máy tính

### Phần 2: Khái niệm phép toán qua hoạt động không máy tính (20 phút)

#### Hoạt động không máy tính - "Tính toán bằng tay"
- **Hoạt động**: Học sinh tính toán các phép toán cơ bản
- **Phép cộng**: 5 + 3 = 8
- **Phép trừ**: 10 - 4 = 6
- **Phép nhân**: 2 × 3 = 6
- **Phép chia**: 8 ÷ 2 = 4
- **Mục tiêu**: Hiểu cách thực hiện các phép toán

#### Bài toán: Thiết kế máy tính đơn giản
- **Màn hình hiển thị**: Hiển thị số và kết quả
- **Nút số**: 0-9 để nhập số
- **Nút phép toán**: +, -, ×, ÷ để chọn phép toán
- **Nút đặc biệt**: = để tính kết quả, C để xóa

#### Hoạt động không máy tính - "Lập kế hoạch lập trình"
- **Hoạt động**: Học sinh viết các bước để tạo máy tính
- **Bước 1**: Tạo hình nền và màn hình hiển thị
- **Bước 2**: Tạo nút số và nút phép toán
- **Bước 3**: Lập trình logic tính toán
- **Bước 4**: Thêm nút đặc biệt (=, C)
- **Bước 5**: Test và debug

## 💻 PHẦN THỰC HÀNH SCRATCH (45 phút)

### Phần 3: Tạo giao diện máy tính trên Scratch (15 phút)

#### Lập trình trong Scratch với hướng dẫn từng bước
```scratch
# Bước 1: Tạo hình nền
1. Chọn "Choose a Backdrop" → "Other" → chọn màu xám
2. Hoặc vẽ hình nền đơn giản

# Bước 2: Tạo màn hình hiển thị
1. Chọn "Choose a Sprite" → "Things" → chọn hình chữ nhật
2. Đặt tên: "ManHinh"
3. Đặt ở trên cùng màn hình
4. Điều chỉnh kích thước phù hợp

# Bước 3: Tạo nút số
1. Chọn "Choose a Sprite" → "Things" → chọn hình tròn
2. Đặt tên: "NutSo"
3. Tạo nhiều nút cho số 0-9
4. Đặt ở giữa màn hình
```

#### Hoạt động mở rộng - "Tùy chỉnh giao diện"
- **Hoạt động**: Thay đổi màu sắc và kích thước nút
- **Mục tiêu**: Hiểu cách tùy chỉnh giao diện
- **Thử thách**: Tạo giao diện đẹp mắt

### Phần 4: Lập trình logic tính toán (20 phút)

#### Lập trình trong Scratch với hiệu ứng trực quan
```scratch
# Tạo biến số
1. Chọn "Variables" → "Make a Variable"
2. Đặt tên: "So1", "So2", "PhepToan", "KetQua"

# Lập trình nút số
Khi nhấn [NutSo v]
nếu <[PhepToan v] = [0]> thì
  đặt [So1 v] thành ([So1 v] * 10 + [số của nút])
  nói [So1 v] trong (1) giây
nếu không
  đặt [So2 v] thành ([So2 v] * 10 + [số của nút])
  nói [So2 v] trong (1) giây

# Lập trình nút phép toán
Khi nhấn [NutPhepToan v]
đặt [PhepToan v] thành [phép toán tương ứng]
nói [PhepToan v] trong (1) giây

# Lập trình nút bằng
Khi nhấn [NutBang v]
nếu <[PhepToan v] = [+]> thì
  đặt [KetQua v] thành ([So1 v] + [So2 v])
nếu <[PhepToan v] = [-]> thì
  đặt [KetQua v] thành ([So1 v] - [So2 v])
nếu <[PhepToan v] = [×]> thì
  đặt [KetQua v] thành ([So1 v] * [So2 v])
nếu <[PhepToan v] = [÷]> thì
  đặt [KetQua v] thành ([So1 v] / [So2 v])
nói [KetQua v] trong (2) giây
```

#### Hoạt động mở rộng - "Thêm phép toán khác"
- **Hoạt động**: Thêm phép toán bình phương, căn bậc hai
- **Mục tiêu**: Hiểu cách mở rộng chức năng máy tính
- **Thử thách**: Tạo máy tính khoa học đơn giản

### Phần 5: Thêm nút đặc biệt và hoàn thiện (10 phút)

#### Lập trình trong Scratch với hiệu ứng trực quan
```scratch
# Nút xóa (C)
Khi nhấn [NutXoa v]
đặt [So1 v] thành (0)
đặt [So2 v] thành (0)
đặt [PhepToan v] thành (0)
đặt [KetQua v] thành (0)
nói [Đã xóa] trong (1) giây

# Nút xóa tất cả
Khi nhấn [NutXoaTatCa v]
đặt [So1 v] thành (0)
đặt [So2 v] thành (0)
đặt [PhepToan v] thành (0)
đặt [KetQua v] thành (0)
nói [Đã xóa tất cả] trong (1) giây
```

#### Hoạt động mở rộng - "Thêm tính năng đặc biệt"
- **Hoạt động**: Thêm nút lưu kết quả, nút nhớ
- **Mục tiêu**: Hiểu cách tạo tính năng nâng cao
- **Thử thách**: Tạo máy tính có lịch sử tính toán

## 🎯 Tổng kết và đánh giá (10 phút)

### Tổng kết kiến thức
- **Máy tính**: Thiết bị xử lý dữ liệu đầu vào và tạo kết quả
- **Giao diện**: Màn hình hiển thị và nút bấm
- **Logic tính toán**: Sử dụng biến số và phép toán
- **Input/Output**: Dữ liệu đầu vào và kết quả đầu ra

### Đánh giá học sinh
- **Tạo giao diện**: Tạo được giao diện máy tính đẹp mắt
- **Lập trình logic**: Lập trình được logic tính toán
- **Xử lý dữ liệu**: Xử lý được dữ liệu đầu vào
- **Tư duy logic**: Hiểu được cách máy tính hoạt động

## 🎨 Hoạt động mở rộng

### Cấp độ 1: Thêm tính năng cơ bản
- **Nhiều phép toán**: Thêm phép toán bình phương, căn bậc hai
- **Âm thanh**: Thêm âm thanh khi nhấn nút
- **Hiệu ứng**: Thêm animation khi tính toán

### Cấp độ 2: Tính năng nâng cao
- **Máy tính khoa học**: Thêm các hàm toán học
- **Lịch sử**: Lưu lịch sử tính toán
- **Nút nhớ**: Thêm nút nhớ kết quả

### Cấp độ 3: Sáng tạo
- **Máy tính cá nhân**: Tạo máy tính với giao diện riêng
- **Ứng dụng thực tế**: Tạo máy tính cho mục đích cụ thể
- **Chia sẻ**: Chia sẻ máy tính với bạn bè

## 📝 Bài tập về nhà

### Bài tập bắt buộc
1. **Hoàn thành máy tính**: Tạo máy tính đơn giản hoàn chỉnh
2. **Thêm âm thanh**: Thêm âm thanh khi nhấn nút
3. **Tùy chỉnh**: Thay đổi màu sắc và kích thước nút

### Bài tập nâng cao
1. **Máy tính khoa học**: Thêm các hàm toán học
2. **Lịch sử**: Lưu lịch sử tính toán
3. **Nút nhớ**: Thêm nút nhớ kết quả

### Bài tập sáng tạo
1. **Máy tính cá nhân**: Tạo máy tính với giao diện riêng
2. **Ứng dụng thực tế**: Tạo máy tính cho mục đích cụ thể
3. **Chia sẻ**: Chia sẻ máy tính với bạn bè và gia đình

## 🔧 Tài nguyên hỗ trợ

### Tài liệu tham khảo
- **Scratch Calculator Tutorial**: Hướng dẫn tạo máy tính
- **Math Operations**: Các phép toán cơ bản
- **User Interface Design**: Thiết kế giao diện người dùng

### Công cụ hỗ trợ
- **Scratch Editor**: Môi trường lập trình trực quan
- **Math Blocks**: Khối lệnh toán học trong Scratch
- **Variable Blocks**: Khối lệnh biến số

### Đánh giá và phản hồi
- **Rubric đánh giá**: Tiêu chí đánh giá máy tính Scratch
- **Peer Review**: Đánh giá lẫn nhau giữa học sinh
- **Portfolio**: Tập hợp các dự án và bài tập của học sinh