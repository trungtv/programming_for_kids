# Bài giảng 5: Câu chuyện tương tác

## 📋 Thông tin bài học
- **Thời gian**: 90 phút
- **Độ tuổi**: 8-11 tuổi
- **Trình độ**: Cơ bản đến trung bình
- **Mục tiêu**: Tạo câu chuyện tương tác với nhiều nhân vật và tình huống

## 🎯 Mục tiêu học tập

### Kiến thức
- Hiểu cách tạo câu chuyện có cốt truyện
- Biết cách sử dụng broadcast để đồng bộ
- Hiểu khái niệm tương tác và lựa chọn

### Kỹ năng
- Viết kịch bản câu chuyện
- Thiết kế nhân vật và cảnh
- Lập trình logic câu chuyện

### Thái độ
- Phát triển khả năng sáng tạo
- Rèn luyện kỹ năng viết
- Khuyến khích làm việc nhóm

## 🧠 Nội dung bài học

## 📚 PHẦN LÝ THUYẾT (45 phút)

### Phần 1: Khái niệm câu chuyện tương tác qua hoạt động không máy tính (25 phút)

#### Hoạt động khởi động - "Kể chuyện tương tác"
- **Hoạt động**: Học sinh kể chuyện và cho bạn chọn kết thúc
- **Câu hỏi**: "Các em thích câu chuyện nào nhất? Tại sao?"
- **Kết nối**: "Hôm nay chúng ta sẽ tạo câu chuyện tương tác bằng Scratch"
- **Mục tiêu**: Hiểu khái niệm câu chuyện tương tác

#### Khái niệm câu chuyện tương tác qua ví dụ thực tế
- **Cốt truyện**: Có mở đầu, thân bài, kết thúc
- **Nhân vật**: Nhân vật chính và nhân vật phụ
- **Tương tác**: Người đọc có thể lựa chọn
- **Kết thúc**: Nhiều kết thúc khác nhau

#### Hoạt động thực hành - "Viết kịch bản câu chuyện"
- **Hoạt động**: Học sinh viết kịch bản câu chuyện trên giấy
- **Yêu cầu**: Có mở đầu, thân bài, kết thúc và tương tác
- **Mục tiêu**: Có ý tưởng câu chuyện trước khi làm trên Scratch
- **Kết quả**: Hiểu cấu trúc câu chuyện tương tác

### Phần 2: Khái niệm broadcast qua hoạt động không máy tính (20 phút)

#### Hoạt động không máy tính - "Đồng bộ hoạt động"
- **Hoạt động**: Học sinh đóng vai nhân vật, đồng bộ hoạt động
- **Mục tiêu**: Hiểu khái niệm đồng bộ và broadcast
- **Quy tắc**: Khi một nhân vật nói, các nhân vật khác phải im lặng
- **Kết quả**: Nhận ra cần đồng bộ hoạt động giữa các nhân vật

#### Bài toán: Thiết kế câu chuyện tương tác
- **Nhân vật chính**: 1-2 nhân vật
- **Nhân vật phụ**: 2-3 nhân vật
- **Cảnh**: Nhiều cảnh khác nhau
- **Tương tác**: Người đọc có thể lựa chọn

#### Hoạt động không máy tính - "Lập kế hoạch lập trình"
- **Hoạt động**: Học sinh viết các bước để tạo câu chuyện
- **Bước 1**: Tạo nhân vật và cảnh
- **Bước 2**: Viết kịch bản cho từng nhân vật
- **Bước 3**: Lập trình broadcast để đồng bộ
- **Bước 4**: Thêm tương tác và lựa chọn
- **Bước 5**: Test và chỉnh sửa

## 💻 PHẦN THỰC HÀNH SCRATCH (45 phút)

### Phần 3: Tạo nhân vật và cảnh trên Scratch (15 phút)

#### Lập trình trong Scratch với hướng dẫn từng bước
```scratch
# Bước 1: Tạo nhân vật chính
1. Chọn "Choose a Sprite" → "Animals" → chọn mèo
2. Đặt tên: "NhanVatChinh"
3. Đặt ở giữa màn hình
4. Điều chỉnh kích thước phù hợp

# Bước 2: Tạo nhân vật phụ
1. Chọn "Choose a Sprite" → "Animals" → chọn chó
2. Đặt tên: "NhanVatPhu"
3. Đặt ở cạnh màn hình
4. Điều chỉnh kích thước phù hợp

# Bước 3: Tạo cảnh
1. Chọn "Choose a Backdrop" → "Nature" → chọn rừng
2. Hoặc vẽ cảnh đơn giản
```

#### Hoạt động mở rộng - "Tùy chỉnh nhân vật"
- **Hoạt động**: Thay đổi màu sắc và kích thước nhân vật
- **Mục tiêu**: Hiểu cách tùy chỉnh nhân vật
- **Thử thách**: Tạo nhân vật độc đáo

### Phần 4: Lập trình logic câu chuyện (20 phút)

#### Lập trình trong Scratch với hiệu ứng trực quan
```scratch
# Nhân vật chính - Mở đầu câu chuyện
Khi cờ xanh được nhấn
nói [Xin chào! Tôi là chú mèo] trong (2) giây
gửi tin nhắn [bat_dau] cho tất cả

# Nhân vật phụ - Phản hồi
Khi nhận tin nhắn [bat_dau]
nói [Xin chào! Tôi là chú chó] trong (2) giây
gửi tin nhắn [phản_hoi] cho tất cả

# Nhân vật chính - Tiếp tục câu chuyện
Khi nhận tin nhắn [phản_hoi]
nói [Chúng ta cùng đi phiêu lưu nhé!] trong (2) giây
gửi tin nhắn [lua_chon] cho tất cả

# Tương tác - Lựa chọn
Khi nhận tin nhắn [lua_chon]
nói [Bạn muốn đi đâu?] trong (2) giây
nói [Nhấn A: Đi vào rừng, B: Đi ra biển] trong (3) giây
```

#### Hoạt động mở rộng - "Thêm nhiều tương tác"
- **Hoạt động**: Thêm nhiều lựa chọn và kết thúc khác nhau
- **Mục tiêu**: Hiểu cách tạo câu chuyện phức tạp
- **Thử thách**: Tạo câu chuyện có nhiều nhánh

### Phần 5: Thêm tương tác và hoàn thiện (10 phút)

#### Lập trình trong Scratch với hiệu ứng trực quan
```scratch
# Lựa chọn A - Đi vào rừng
Khi nhấn phím [a v]
nói [Chúng ta đi vào rừng!] trong (2) giây
gửi tin nhắn [vao_rung] cho tất cả

# Lựa chọn B - Đi ra biển
Khi nhấn phím [b v]
nói [Chúng ta đi ra biển!] trong (2) giây
gửi tin nhắn [ra_bien] cho tất cả

# Kết thúc câu chuyện
Khi nhận tin nhắn [vao_rung]
nói [Chúng ta đã về nhà an toàn!] trong (2) giây

Khi nhận tin nhắn [ra_bien]
nói [Chúng ta đã về nhà an toàn!] trong (2) giây
```

#### Hoạt động mở rộng - "Thêm âm thanh và hiệu ứng"
- **Hoạt động**: Thêm âm thanh và hiệu ứng cho câu chuyện
- **Mục tiêu**: Hiểu cách tạo câu chuyện sinh động
- **Thử thách**: Tạo câu chuyện có âm thanh nền

## 🎯 Tổng kết và đánh giá (10 phút)

### Tổng kết kiến thức
- **Câu chuyện tương tác**: Câu chuyện có thể tương tác và lựa chọn
- **Broadcast**: Đồng bộ hoạt động giữa các nhân vật
- **Tương tác**: Người đọc có thể lựa chọn và ảnh hưởng đến câu chuyện
- **Cốt truyện**: Có mở đầu, thân bài, kết thúc

### Đánh giá học sinh
- **Viết kịch bản**: Viết được kịch bản câu chuyện có cốt truyện
- **Thiết kế nhân vật**: Tạo được nhân vật phù hợp với câu chuyện
- **Lập trình logic**: Lập trình được logic câu chuyện
- **Tư duy sáng tạo**: Tạo được câu chuyện độc đáo và thú vị

## 🎨 Hoạt động mở rộng

### Cấp độ 1: Thêm tính năng cơ bản
- **Nhiều nhân vật**: Thêm nhiều nhân vật phụ
- **Âm thanh**: Thêm âm thanh và hiệu ứng
- **Hiệu ứng**: Thêm animation cho nhân vật

### Cấp độ 2: Tính năng nâng cao
- **Nhiều cảnh**: Tạo nhiều cảnh khác nhau
- **Nhiều kết thúc**: Tạo nhiều kết thúc khác nhau
- **Lưu tiến trình**: Lưu tiến trình đọc câu chuyện

### Cấp độ 3: Sáng tạo
- **Câu chuyện dài**: Tạo câu chuyện dài với nhiều chương
- **Game câu chuyện**: Tạo game dựa trên câu chuyện
- **Chia sẻ**: Chia sẻ câu chuyện với bạn bè

## 📝 Bài tập về nhà

### Bài tập bắt buộc
1. **Hoàn thành câu chuyện**: Tạo câu chuyện tương tác hoàn chỉnh
2. **Thêm tương tác**: Có ít nhất 3 lựa chọn khác nhau
3. **Tùy chỉnh**: Thay đổi nhân vật và cảnh

### Bài tập nâng cao
1. **Câu chuyện dài**: Tạo câu chuyện dài với nhiều chương
2. **Nhiều kết thúc**: Tạo nhiều kết thúc khác nhau
3. **Âm thanh**: Thêm âm thanh và hiệu ứng

### Bài tập sáng tạo
1. **Câu chuyện cá nhân**: Tạo câu chuyện về bản thân
2. **Câu chuyện nhóm**: Tạo câu chuyện cùng bạn bè
3. **Chia sẻ**: Chia sẻ câu chuyện với bạn bè và gia đình

## 🔧 Tài nguyên hỗ trợ

### Tài liệu tham khảo
- **Scratch Storytelling**: Hướng dẫn tạo câu chuyện
- **Interactive Story Design**: Thiết kế câu chuyện tương tác
- **Character Development**: Phát triển nhân vật

### Công cụ hỗ trợ
- **Scratch Editor**: Môi trường lập trình trực quan
- **Sprite Library**: Thư viện nhân vật và hình nền
- **Sound Library**: Thư viện âm thanh miễn phí

### Đánh giá và phản hồi
- **Rubric đánh giá**: Tiêu chí đánh giá câu chuyện tương tác
- **Peer Review**: Đánh giá lẫn nhau giữa học sinh
- **Portfolio**: Tập hợp các dự án và bài tập của học sinh