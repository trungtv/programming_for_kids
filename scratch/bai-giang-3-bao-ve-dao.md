# Bài Giảng 3: Trò Chơi "Bảo Vệ Đảo"

## 📋 Thông tin bài học
- **Thời gian**: 90 phút (2 tiết)
- **Độ tuổi**: Lớp 5 (10-11 tuổi)
- **Mức độ**: Trung bình đến nâng cao
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


## 🎮 Nội dung bài học

### Phần 1: Giới thiệu và thiết kế game (15 phút)

#### Hoạt động khởi động
- Cho học sinh xem video trò chơi "Bảo vệ đảo" hoàn chỉnh
- Hỏi: "Các em đã chơi trò chơi phòng thủ chưa?"
- Giải thích mục tiêu: Tạo trò chơi bảo vệ đảo khỏi kẻ thù

#### Thiết kế game
- **Luật chơi**: Bảo vệ đảo khỏi tàu địch
- **Cách chơi**: Nhấn chuột để bắn đạn
- **Mục tiêu**: Tiêu diệt tàu địch, không để chúng đến đảo
- **Hệ thống điểm**: +10 điểm mỗi tàu bị tiêu diệt

### Phần 2: Tạo hình nền và đảo (10 phút)

#### Bước 1: Tạo hình nền
1. Chọn "Choose a Backdrop" → "Nature" → chọn biển
2. Hoặc vẽ hình nền biển đơn giản

#### Bước 2: Tạo đảo
1. Chọn "Choose a Sprite" → "Nature" → chọn đảo
2. Đặt tên: "Dao"
3. Đặt ở giữa màn hình
4. Thêm hiệu ứng bảo vệ

### Phần 3: Tạo hệ thống bắn đạn (20 phút)

#### Bước 1: Tạo đạn pháo
1. Chọn "Choose a Sprite" → "Things" → chọn đạn
2. Đặt tên: "Dan"
3. Thu nhỏ kích thước

#### Bước 2: Lập trình bắn đạn
```scratch
Khi nhấn phím [space v]
tạo bản sao của [Dan v]

Khi tôi là bản sao
đi tới [Dao v]
hướng về phía [con trỏ chuột v]
lặp lại cho đến khi <chạm [cạnh v]?>
di chuyển (15) bước
```

#### Bước 3: Thêm âm thanh bắn
```scratch
Khi nhấn phím [space v]
phát âm thanh [laser v]
```

### Phần 4: Tạo tàu địch (25 phút)

#### Bước 1: Tạo tàu địch
1. Chọn "Choose a Sprite" → "Transportation" → chọn tàu
2. Đặt tên: "TauDich"
3. Điều chỉnh kích thước phù hợp

#### Bước 2: Lập trình tàu địch
```scratch
Khi nhấn phím [s v]
tạo bản sao của [TauDich v]

Khi tôi là bản sao
đi tới [cạnh trái v]
hướng về phía (90 vòng độ)
lặp lại cho đến khi <chạm [Dao v]?> hoặc <chạm [Dan v]?>
di chuyển (3) bước
```

#### Bước 3: Xử lý khi tàu bị tiêu diệt
```scratch
Khi tôi là bản sao
nếu <chạm [Dan v]?> thì
phát âm thanh [explosion v]
thay đổi [DiemSo v] bởi (10)
xóa bản sao này
```

#### Bước 4: Xử lý khi tàu đến đảo
```scratch
Khi tôi là bản sao
nếu <chạm [Dao v]?> thì
thay đổi [MangSong v] bởi (-1)
phát âm thanh [hurt v]
xóa bản sao này
```

### Phần 5: Tạo hệ thống điểm số và mạng sống (15 phút)

#### Bước 1: Tạo biến điểm số
1. Chọn "Variables" → "Make a Variable"
2. Đặt tên: "DiemSo"
3. Đặt giá trị ban đầu: 0

#### Bước 2: Tạo biến mạng sống
1. Chọn "Variables" → "Make a Variable"
2. Đặt tên: "MangSong"
3. Đặt giá trị ban đầu: 3

#### Bước 3: Hiển thị điểm số và mạng sống
```scratch
Khi cờ xanh được nhấn
đặt [DiemSo v] thành (0)
đặt [MangSong v] thành (3)
```

#### Bước 4: Kiểm tra game over
```scratch
Khi cờ xanh được nhấn
lặp lại cho đến khi <[MangSong v] = [0]>
nếu <[MangSong v] = [0]> thì
nói [Game Over! Điểm số: ] + [DiemSo v] trong (3) giây
dừng [tất cả v]
```

### Phần 6: Thêm tính năng nâng cao (5 phút)

#### Bước 1: Thêm power-up
```scratch
Khi cờ xanh được nhấn
lặp lại mãi mãi
chờ (30) giây
tạo bản sao của [PowerUp v]
```

#### Bước 2: Tăng tốc độ bắn
```scratch
Khi tôi là bản sao của [PowerUp v]
nếu <chạm [Dao v]?> thì
phát âm thanh [power up v]
xóa bản sao này
```

## 🎨 Hoạt động mở rộng

### Cấp độ 1: Thêm tính năng cơ bản
- Thêm nhiều loại tàu địch
- Tạo hiệu ứng nổ khi tiêu diệt
- Thêm âm thanh nền

### Cấp độ 2: Tính năng nâng cao
- Tạo hệ thống level
- Thêm boss cuối level
- Tạo shop mua vũ khí

### Cấp độ 3: Sáng tạo
- Thiết kế chủ đề game khác
- Thêm multiplayer
- Tạo hệ thống ranking

## 📝 Bài tập về nhà

### Bài tập bắt buộc
1. Hoàn thành trò chơi cơ bản
2. Thêm ít nhất 2 loại tàu địch khác nhau
3. Tạo hệ thống điểm cao (high score)

### Bài tập nâng cao
1. Thêm hệ thống level với độ khó tăng dần
2. Tạo boss với nhiều giai đoạn
3. Thiết kế giao diện menu game

## 🔍 Đánh giá

### Tiêu chí đánh giá
| Tiêu chí | Điểm | Mô tả |
|----------|------|-------|
| Game logic | 4 | Trò chơi hoạt động đúng, có hệ thống điểm |
| Tính năng | 3 | Có ít nhất 3 tính năng khác nhau |
| Sáng tạo | 2 | Có yếu tố độc đáo và sáng tạo |
| Code quality | 2 | Code rõ ràng, có comment |
| Trình bày | 1 | Demo mượt mà, giải thích tốt |
| Tổng cộng | 12 | |

### Cách đánh giá
- **Quan sát**: Giáo viên quan sát quá trình lập trình
- **Sản phẩm**: Kiểm tra trò chơi hoàn chỉnh
- **Code review**: Kiểm tra chất lượng code
- **Trình bày**: Học sinh demo và giải thích logic

## 🚀 Lưu ý quan trọng

### Cho giáo viên
- Giải thích kỹ khái niệm clone
- Hướng dẫn cách debug khi có lỗi
- Khuyến khích học sinh thử nghiệm
- Chuẩn bị sẵn code mẫu để hỗ trợ

### Cho học sinh
- Hiểu rõ logic game trước khi code
- Test thường xuyên để phát hiện lỗi
- Không ngại thử nghiệm tính năng mới
- Lưu dự án thường xuyên

## 💡 Mẹo hay

### Tối ưu hiệu suất
- Sử dụng clone thay vì tạo nhiều sprite
- Xóa clone khi không cần thiết
- Sử dụng biến để quản lý trạng thái

### Game balance
- Điều chỉnh tốc độ và sát thương hợp lý
- Tạo độ khó tăng dần
- Thêm phần thưởng để tạo động lực

### Debug hiệu quả
- Sử dụng "say" để debug
- Kiểm tra từng phần một
- Test với các trường hợp khác nhau

## 📚 Tài liệu tham khảo

- [Scratch Game Development](https://scratch.mit.edu/explore/projects/games)
- [Scratch Clone Tutorial](https://scratch.mit.edu/tutorials)
- [Game Design Principles](https://scratch.mit.edu/studios/104)

---

**Tác giả**: AI & Trần Việt Trung (BKHN)  
**Ngày tạo**: 04/10/2025  
**Phiên bản**: 1.0
