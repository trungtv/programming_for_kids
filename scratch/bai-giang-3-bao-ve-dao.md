# Bài giảng 3: Trò chơi "Bảo vệ đảo"

## 📋 Thông tin bài học
- **Thời gian**: 120 phút
- **Độ tuổi**: 10-11 tuổi
- **Trình độ**: Trung bình đến nâng cao
- **Mục tiêu**: Tạo trò chơi phòng thủ với hệ thống điểm số và level

## 🎯 Mục tiêu học tập

### Kiến thức
- Hiểu cách sử dụng biến số và danh sách
- Biết cách tạo hệ thống điểm số
- Hiểu khái niệm clone và quản lý nhiều đối tượng

### Kỹ năng
- Lập trình trò chơi phức tạp
- Quản lý nhiều nhân vật cùng lúc
- Tạo hệ thống game logic

### Thái độ
- Phát triển tư duy chiến thuật
- Rèn luyện tính kiên trì
- Khuyến khích sáng tạo và cải tiến

## 🧠 Nội dung bài học

## 📚 PHẦN LÝ THUYẾT (60 phút)

### Phần 1: Khái niệm trò chơi phòng thủ qua hoạt động không máy tính (30 phút)

#### Hoạt động khởi động - "Trò chơi bảo vệ thành"
- **Hoạt động**: Học sinh chơi trò chơi bảo vệ thành trong lớp
- **Quy tắc**: Một nhóm bảo vệ, một nhóm tấn công
- **Mục tiêu**: Hiểu khái niệm phòng thủ và tấn công
- **Kết quả**: Nhận ra trò chơi cần có mục tiêu, luật chơi và hệ thống điểm

#### Khái niệm trò chơi phòng thủ qua ví dụ thực tế
- **Mục tiêu**: Bảo vệ một vị trí khỏi kẻ thù
- **Cách chơi**: Sử dụng vũ khí để tiêu diệt kẻ thù
- **Hệ thống điểm**: Điểm số dựa trên số kẻ thù tiêu diệt
- **Level**: Độ khó tăng dần theo thời gian

#### Hoạt động thực hành - "Thiết kế trò chơi trên giấy"
- **Hoạt động**: Học sinh vẽ phác thảo trò chơi bảo vệ đảo
- **Yêu cầu**: Có đảo, tàu địch, đạn, hệ thống điểm
- **Mục tiêu**: Có ý tưởng thiết kế trước khi làm trên Scratch
- **Kết quả**: Hiểu các thành phần cần thiết của trò chơi phòng thủ

### Phần 2: Khái niệm clone và quản lý đối tượng qua hoạt động không máy tính (30 phút)

#### Hoạt động không máy tính - "Tạo nhiều tàu địch"
- **Hoạt động**: Học sinh đóng vai tàu địch, xuất hiện từng người một
- **Mục tiêu**: Hiểu khái niệm tạo nhiều đối tượng giống nhau
- **Quy tắc**: Mỗi người di chuyển độc lập, có tốc độ khác nhau
- **Kết quả**: Nhận ra cần quản lý nhiều đối tượng cùng lúc

#### Bài toán: Thiết kế trò chơi "Bảo vệ đảo"
- **Nhân vật**: Đảo (cố định), tàu địch (di chuyển), đạn (bắn)
- **Hệ thống**: Điểm số, level, thời gian
- **Tương tác**: Nhấn chuột để bắn đạn
- **Mục tiêu**: Tiêu diệt tàu địch, không để chúng đến đảo

#### Hoạt động không máy tính - "Lập kế hoạch lập trình"
- **Hoạt động**: Học sinh viết các bước để tạo trò chơi
- **Bước 1**: Tạo hình nền biển và đảo
- **Bước 2**: Tạo tàu địch và lập trình di chuyển
- **Bước 3**: Tạo đạn và lập trình bắn
- **Bước 4**: Tạo hệ thống điểm và level
- **Bước 5**: Thêm điều kiện thắng/thua

## 💻 PHẦN THỰC HÀNH SCRATCH (60 phút)

### Phần 3: Tạo hình nền và đảo trên Scratch (15 phút)

#### Lập trình trong Scratch với hướng dẫn từng bước
```scratch
# Bước 1: Tạo hình nền
1. Chọn "Choose a Backdrop" → "Nature" → chọn biển
2. Hoặc vẽ hình nền biển đơn giản

# Bước 2: Tạo đảo
1. Chọn "Choose a Sprite" → "Nature" → chọn đảo
2. Đặt tên: "Dao"
3. Đặt ở giữa màn hình
4. Điều chỉnh kích thước phù hợp
```

#### Hoạt động mở rộng - "Tùy chỉnh đảo"
- **Hoạt động**: Thay đổi màu sắc và kích thước đảo
- **Mục tiêu**: Hiểu cách tùy chỉnh nhân vật
- **Thử thách**: Tạo đảo có nhiều màu sắc

### Phần 4: Tạo tàu địch và hệ thống clone (20 phút)

#### Lập trình trong Scratch với hiệu ứng trực quan
```scratch
# Tạo tàu địch
1. Chọn "Choose a Sprite" → "Transportation" → chọn tàu
2. Đặt tên: "TauDich"
3. Đặt ở cạnh trái màn hình

# Lập trình di chuyển tàu địch
Khi cờ xanh được nhấn
ẩn
chờ (2) giây
tạo bản sao của [TauDich v]

Khi tôi là bản sao
hiện
đặt x thành (-240)
đặt y thành (số ngẫu nhiên từ (-180) đến (180))
hướng về phía (90 vòng độ)
lặp lại (50) lần
  di chuyển (3) bước
  chờ (0.1) giây
xóa bản sao này
```

#### Hoạt động mở rộng - "Thay đổi tốc độ tàu"
- **Hoạt động**: Thay đổi tốc độ di chuyển của tàu địch
- **Mục tiêu**: Hiểu cách điều chỉnh độ khó trò chơi
- **Thử thách**: Tạo tàu địch có tốc độ khác nhau

### Phần 5: Tạo đạn và hệ thống bắn (15 phút)

#### Lập trình trong Scratch với hiệu ứng trực quan
```scratch
# Tạo đạn
1. Chọn "Choose a Sprite" → "Things" → chọn đạn
2. Đặt tên: "Dan"
3. Đặt ở giữa màn hình

# Lập trình bắn đạn
Khi nhấn chuột
tạo bản sao của [Dan v]

Khi tôi là bản sao
hiện
đặt x thành (0)
đặt y thành (0)
hướng về phía (con trỏ chuột v)
lặp lại (30) lần
  di chuyển (10) bước
  chờ (0.05) giây
xóa bản sao này
```

#### Hoạt động mở rộng - "Thêm âm thanh bắn"
- **Hoạt động**: Thêm âm thanh khi bắn đạn
- **Mục tiêu**: Hiểu cách thêm âm thanh vào trò chơi
- **Thử thách**: Tạo âm thanh khác nhau cho các loại đạn

### Phần 6: Tạo hệ thống điểm và điều kiện thắng/thua (10 phút)

#### Lập trình trong Scratch với hiệu ứng trực quan
```scratch
# Tạo biến số điểm
1. Chọn "Variables" → "Make a Variable"
2. Đặt tên: "Diem"
3. Chọn "For all sprites"

# Kiểm tra va chạm và tính điểm
Khi tôi là bản sao của [Dan v]
nếu <chạm [TauDich v]?> thì
thay đổi [Diem v] bởi (10)
phát âm thanh [pop v]
xóa bản sao này

# Kiểm tra điều kiện thua
Khi tôi là bản sao của [TauDich v]
nếu <chạm [Dao v]?> thì
nói [Game Over! Điểm số: ] + [Diem v] trong (3) giây
dừng [tất cả v]
```

#### Hoạt động mở rộng - "Thêm hệ thống level"
- **Hoạt động**: Tạo hệ thống level với độ khó tăng dần
- **Mục tiêu**: Hiểu cách tạo trò chơi có nhiều level
- **Thử thách**: Tạo level boss với tàu địch đặc biệt

## 🎯 Tổng kết và đánh giá (20 phút)

### Tổng kết kiến thức
- **Trò chơi phòng thủ**: Bảo vệ một vị trí khỏi kẻ thù
- **Clone**: Tạo nhiều đối tượng giống nhau
- **Hệ thống điểm**: Theo dõi thành tích của người chơi
- **Tương tác**: Sử dụng chuột để điều khiển

### Đánh giá học sinh
- **Tạo trò chơi**: Tạo được trò chơi phòng thủ hoàn chỉnh
- **Sử dụng clone**: Sử dụng clone để tạo nhiều đối tượng
- **Hệ thống điểm**: Tạo được hệ thống điểm số
- **Tư duy logic**: Hiểu được luồng hoạt động của trò chơi

## 🎨 Hoạt động mở rộng

### Cấp độ 1: Thêm tính năng cơ bản
- **Nhiều loại đạn**: Tạo đạn có sức mạnh khác nhau
- **Âm thanh**: Thêm âm thanh nền và hiệu ứng
- **Hiệu ứng**: Thêm animation khi tàu địch bị tiêu diệt

### Cấp độ 2: Tính năng nâng cao
- **Nhiều loại tàu**: Tạo tàu địch có tốc độ và sức mạnh khác nhau
- **Hệ thống level**: Tạo nhiều level với độ khó tăng dần
- **Power-up**: Thêm vật phẩm tăng sức mạnh

### Cấp độ 3: Sáng tạo
- **Trò chơi mới**: Tạo trò chơi phòng thủ với chủ đề khác
- **Multiplayer**: Tạo trò chơi nhiều người chơi
- **AI**: Tạo tàu địch có trí tuệ nhân tạo

## 📝 Bài tập về nhà

### Bài tập bắt buộc
1. **Hoàn thành trò chơi**: Tạo trò chơi bảo vệ đảo hoàn chỉnh
2. **Thêm âm thanh**: Thêm âm thanh nền và hiệu ứng
3. **Tùy chỉnh**: Thay đổi màu sắc và kích thước nhân vật

### Bài tập nâng cao
1. **Nhiều loại tàu**: Tạo tàu địch có tốc độ khác nhau
2. **Hệ thống level**: Tạo hệ thống level với độ khó tăng dần
3. **Power-up**: Thêm vật phẩm tăng sức mạnh

### Bài tập sáng tạo
1. **Trò chơi mới**: Tạo trò chơi phòng thủ với chủ đề khác
2. **Câu chuyện**: Viết câu chuyện cho trò chơi
3. **Chia sẻ**: Chia sẻ trò chơi với bạn bè và gia đình

## 🔧 Tài nguyên hỗ trợ

### Tài liệu tham khảo
- **Scratch Game Design**: Hướng dẫn thiết kế trò chơi
- **Clone Management**: Quản lý clone trong Scratch
- **Game Logic**: Logic trò chơi cơ bản

### Công cụ hỗ trợ
- **Scratch Editor**: Môi trường lập trình trực quan
- **Sprite Library**: Thư viện nhân vật và hình nền
- **Sound Library**: Thư viện âm thanh miễn phí

### Đánh giá và phản hồi
- **Rubric đánh giá**: Tiêu chí đánh giá trò chơi phòng thủ
- **Peer Review**: Đánh giá lẫn nhau giữa học sinh
- **Portfolio**: Tập hợp các dự án và bài tập của học sinh