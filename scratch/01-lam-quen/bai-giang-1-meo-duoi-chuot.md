# Bài giảng 1: Trò chơi "Mèo đuổi chuột"

## 📋 Thông tin bài học
- **Thời gian**: 60 phút
- **Độ tuổi**: 8-9 tuổi
- **Trình độ**: Cơ bản
- **Mục tiêu**: Tạo trò chơi đơn giản với chuyển động và tương tác

## 🎯 Mục tiêu học tập

### Kiến thức
- Hiểu cách sử dụng khối lệnh chuyển động
- Biết cách sử dụng cảm biến phím bấm
- Hiểu khái niệm điều kiện và vòng lặp

### Kỹ năng
- Tạo nhân vật và hình nền
- Lập trình chuyển động cho nhân vật
- Thêm âm thanh và hiệu ứng

### Thái độ
- Phát triển tư duy logic
- Rèn luyện tính kiên trì
- Khuyến khích sáng tạo

## 🧠 Nội dung bài học

## 📚 PHẦN LÝ THUYẾT (30 phút)

### Phần 1: Khái niệm chuyển động qua hoạt động không máy tính (15 phút)

#### Hoạt động khởi động - "Trò chơi đuổi bắt"
- **Hoạt động**: Học sinh chơi trò đuổi bắt trong lớp
- **Quy tắc**: Một bạn làm mèo, một bạn làm chuột, mèo đuổi chuột
- **Mục tiêu**: Hiểu khái niệm chuyển động và tương tác
- **Kết quả**: Nhận ra trò chơi cần có nhân vật, luật chơi và cách điều khiển

#### Khái niệm chuyển động qua ví dụ thực tế
- **Chuyển động**: Di chuyển từ vị trí này sang vị trí khác
- **Hướng**: Lên, xuống, trái, phải
- **Tốc độ**: Nhanh hay chậm
- **Điều khiển**: Sử dụng phím để điều khiển nhân vật

#### Hoạt động thực hành - "Mô phỏng chuyển động"
- **Hoạt động**: Học sinh đứng tại chỗ, mô phỏng chuyển động theo lệnh
- **Lệnh**: "Bước sang phải", "Bước lên trên", "Xoay người"
- **Mục tiêu**: Hiểu các khái niệm chuyển động cơ bản
- **Kết quả**: Chuẩn bị cho việc lập trình chuyển động trên Scratch

### Phần 2: Thiết kế trò chơi qua hoạt động không máy tính (15 phút)

#### Hoạt động không máy tính - "Thiết kế trò chơi trên giấy"
- **Hoạt động**: Học sinh vẽ nhân vật mèo và chuột trên giấy
- **Mục tiêu**: Hiểu cách thiết kế nhân vật và hình nền
- **Quy tắc**: Mèo to hơn chuột, có màu sắc khác nhau
- **Kết quả**: Có ý tưởng về nhân vật trước khi tạo trên Scratch

#### Bài toán: Thiết kế trò chơi "Mèo đuổi chuột"
- **Nhân vật**: Mèo (to, màu cam) và Chuột (nhỏ, màu xám)
- **Hình nền**: Sân cỏ hoặc phòng khách
- **Luật chơi**: Mèo đuổi chuột, chuột chạy trốn
- **Cách chơi**: Dùng phím mũi tên điều khiển chuột

#### Hoạt động không máy tính - "Lập kế hoạch lập trình"
- **Hoạt động**: Học sinh viết các bước để tạo trò chơi
- **Bước 1**: Tạo nhân vật mèo và chuột
- **Bước 2**: Tạo hình nền
- **Bước 3**: Lập trình chuyển động cho chuột
- **Bước 4**: Lập trình mèo đuổi chuột
- **Bước 5**: Thêm điều kiện thắng/thua

## 💻 PHẦN THỰC HÀNH SCRATCH (30 phút)

### Phần 3: Tạo nhân vật và hình nền trên Scratch (10 phút)

#### Lập trình trong Scratch với hướng dẫn từng bước
```scratch
# Bước 1: Tạo nhân vật Mèo
1. Xóa nhân vật mặc định (Sprite1)
2. Chọn "Choose a Sprite" → "Animals" → chọn mèo
3. Đặt tên: "Meo"
4. Điều chỉnh kích thước phù hợp

# Bước 2: Tạo nhân vật Chuột
1. Chọn "Choose a Sprite" → "Animals" → chọn chuột
2. Đặt tên: "Chuot"
3. Điều chỉnh kích thước nhỏ hơn mèo

# Bước 3: Tạo hình nền
1. Chọn "Choose a Backdrop" → "Nature" → chọn sân cỏ
2. Hoặc vẽ hình nền đơn giản
```

#### Hoạt động mở rộng - "Tùy chỉnh nhân vật"
- **Hoạt động**: Thay đổi màu sắc và kích thước nhân vật
- **Mục tiêu**: Hiểu cách tùy chỉnh nhân vật
- **Thử thách**: Tạo nhân vật độc đáo của riêng mình

### Phần 4: Lập trình chuyển động cho Chuột (10 phút)

#### Lập trình trong Scratch với hiệu ứng trực quan
```scratch
# Chuyển động sang phải
Khi nhấn phím [mũi tên phải v]
di chuyển (10) bước
hướng về phía (90 vòng độ)

# Chuyển động sang trái
Khi nhấn phím [mũi tên trái v]
di chuyển (-10) bước
hướng về phía (-90 vòng độ)

# Chuyển động lên trên
Khi nhấn phím [mũi tên lên v]
thay đổi y bởi (10)

# Chuyển động xuống dưới
Khi nhấn phím [mũi tên xuống v]
thay đổi y bởi (-10)
```

#### Hoạt động mở rộng - "Thay đổi tốc độ"
- **Hoạt động**: Thay đổi số bước di chuyển (5, 15, 20)
- **Mục tiêu**: Hiểu cách điều chỉnh tốc độ
- **Thử thách**: Tạo chế độ chạy nhanh/chậm

### Phần 5: Lập trình cho Mèo và điều kiện thắng/thua (10 phút)

#### Lập trình trong Scratch với hiệu ứng trực quan
```scratch
# Mèo đuổi chuột
Mãi mãi
hướng về phía [Chuot v]
di chuyển (5) bước
phát âm thanh [meow v]

# Kiểm tra khi mèo bắt được chuột
Mãi mãi
nếu <chạm [Chuot v]?> thì
nói [Mèo đã bắt được chuột!] trong (2) giây
dừng [tất cả v]
```

#### Hoạt động mở rộng - "Thêm tính năng"
- **Hoạt động**: Thêm điểm số và âm thanh nền
- **Mục tiêu**: Hiểu cách mở rộng trò chơi
- **Thử thách**: Tạo hệ thống level

## 🎯 Tổng kết và đánh giá (10 phút)

### Tổng kết kiến thức
- **Chuyển động**: Di chuyển nhân vật theo các hướng khác nhau
- **Điều khiển**: Sử dụng phím để điều khiển nhân vật
- **Tương tác**: Nhân vật có thể tương tác với nhau
- **Điều kiện**: Kiểm tra điều kiện để thay đổi trạng thái trò chơi

### Đánh giá học sinh
- **Tạo nhân vật**: Có thể tạo và tùy chỉnh nhân vật
- **Lập trình chuyển động**: Tạo được chuyển động cơ bản
- **Điều khiển**: Sử dụng phím để điều khiển nhân vật
- **Tư duy logic**: Hiểu được luồng hoạt động của trò chơi

## 🎨 Hoạt động mở rộng

### Cấp độ 1: Thêm tính năng cơ bản
- **Điểm số**: Thêm hệ thống điểm khi chuột sống sót
- **Âm thanh**: Thêm âm thanh nền và hiệu ứng
- **Tốc độ**: Thay đổi tốc độ di chuyển của nhân vật

### Cấp độ 2: Tính năng nâng cao
- **Nhiều chuột**: Tạo thêm nhiều chuột để mèo đuổi
- **Chướng ngại vật**: Thêm vật cản trên đường
- **Hệ thống level**: Tăng độ khó theo từng level

### Cấp độ 3: Sáng tạo
- **Nhân vật mới**: Thay đổi thành nhân vật khác
- **Câu chuyện**: Tạo câu chuyện cho trò chơi
- **Hiệu ứng đặc biệt**: Thêm animation và hiệu ứng

## 📝 Bài tập về nhà

### Bài tập bắt buộc
1. **Hoàn thành trò chơi**: Tạo trò chơi mèo đuổi chuột hoàn chỉnh
2. **Thêm âm thanh**: Thêm ít nhất 2 âm thanh khác nhau
3. **Tùy chỉnh**: Thay đổi màu sắc và kích thước nhân vật

### Bài tập nâng cao
1. **Nhân vật phụ**: Tạo thêm 1 nhân vật phụ trong trò chơi
2. **Hệ thống điểm**: Thêm hệ thống điểm số và thời gian
3. **Màn hình**: Tạo màn hình bắt đầu và kết thúc

### Bài tập sáng tạo
1. **Trò chơi mới**: Tạo trò chơi tương tự với nhân vật khác
2. **Câu chuyện**: Viết câu chuyện cho trò chơi
3. **Chia sẻ**: Chia sẻ trò chơi với bạn bè và gia đình

## 🔧 Tài nguyên hỗ trợ

### Tài liệu tham khảo
- **Scratch Programming**: Hướng dẫn lập trình Scratch cơ bản
- **Game Design**: Nguyên lý thiết kế trò chơi đơn giản
- **Animation Basics**: Khái niệm hoạt hình cơ bản

### Công cụ hỗ trợ
- **Scratch Editor**: Môi trường lập trình trực quan
- **Sprite Library**: Thư viện nhân vật và hình nền
- **Sound Library**: Thư viện âm thanh miễn phí

### Đánh giá và phản hồi
- **Rubric đánh giá**: Tiêu chí đánh giá trò chơi Scratch
- **Peer Review**: Đánh giá lẫn nhau giữa học sinh
- **Portfolio**: Tập hợp các dự án và bài tập của học sinh