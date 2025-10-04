# Bài Giảng 5: Câu Chuyện Tương Tác

## 📋 Thông tin bài học
- **Thời gian**: 90 phút (2 tiết)
- **Độ tuổi**: Lớp 3-5 (8-11 tuổi)
- **Mức độ**: Cơ bản đến trung bình
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


## 📖 Nội dung bài học

### Phần 1: Giới thiệu và lên ý tưởng (15 phút)

#### Hoạt động khởi động
- Cho học sinh xem video câu chuyện tương tác mẫu
- Hỏi: "Các em thích câu chuyện nào nhất? Tại sao?"
- Giải thích mục tiêu: Tạo câu chuyện tương tác của riêng mình

#### Lên ý tưởng câu chuyện
- **Chủ đề**: Cuộc phiêu lưu của một nhân vật
- **Nhân vật chính**: 1-2 nhân vật
- **Nhân vật phụ**: 2-3 nhân vật
- **Cốt truyện**: Có mở đầu, thân bài, kết thúc
- **Tương tác**: Người đọc có thể lựa chọn

#### Ví dụ câu chuyện: "Cuộc phiêu lưu của chú mèo"
- **Mở đầu**: Chú mèo đi dạo trong rừng
- **Thân bài**: Gặp nhiều tình huống khác nhau
- **Kết thúc**: Về nhà an toàn

### Phần 2: Viết kịch bản (15 phút)

#### Bước 1: Tạo cấu trúc câu chuyện
```
Cảnh 1: Mở đầu
- Nhân vật: Mèo
- Hành động: Đi dạo
- Tương tác: Chọn hướng đi

Cảnh 2: Gặp bạn
- Nhân vật: Mèo, Chó
- Hành động: Trò chuyện
- Tương tác: Chọn câu trả lời

Cảnh 3: Thử thách
- Nhân vật: Mèo, Cá
- Hành động: Giải cứu
- Tương tác: Chọn cách giải quyết
```

#### Bước 2: Viết lời thoại
- **Mèo**: "Xin chào! Tôi đang đi dạo."
- **Chó**: "Chào bạn! Bạn có muốn chơi không?"
- **Cá**: "Cứu tôi! Tôi bị mắc kẹt!"

### Phần 3: Tạo nhân vật và cảnh (20 phút)

#### Bước 1: Tạo nhân vật chính
1. Chọn "Choose a Sprite" → "Animals" → chọn mèo
2. Đặt tên: "Meo"
3. Thêm costume khác nhau cho các cảnh

#### Bước 2: Tạo nhân vật phụ
1. Tạo sprite chó: "Cho"
2. Tạo sprite cá: "Ca"
3. Tạo sprite chim: "Chim"

#### Bước 3: Tạo cảnh
1. Cảnh 1: Rừng
2. Cảnh 2: Công viên
3. Cảnh 3: Hồ nước

### Phần 4: Lập trình câu chuyện (30 phút)

#### Bước 1: Tạo broadcast
1. Chọn "Events" → "broadcast"
2. Tạo các broadcast:
   - "BatDau"
   - "Canh1"
   - "Canh2"
   - "Canh3"
   - "KetThuc"

#### Bước 2: Lập trình cảnh mở đầu
```scratch
Khi nhận được [BatDau v]
nói [Chào mừng đến với câu chuyện của tôi!] trong (2) giây
chờ (1) giây
phát âm thanh [BatDau v]
```

#### Bước 3: Lập trình cảnh 1
```scratch
Khi nhận được [Canh1 v]
đi tới [Rung v]
nói [Tôi là chú mèo. Hôm nay tôi sẽ đi dạo.] trong (3) giây
chờ (1) giây
nói [Bạn muốn tôi đi hướng nào?] trong (2) giây
```

#### Bước 4: Tạo tương tác
```scratch
Khi nhấn phím [1 v]
nói [Tôi sẽ đi về phía trái.] trong (2) giây
phát âm thanh [Canh2 v]

Khi nhấn phím [2 v]
nói [Tôi sẽ đi về phía phải.] trong (2) giây
phát âm thanh [Canh3 v]
```

#### Bước 5: Lập trình cảnh 2
```scratch
Khi nhận được [Canh2 v]
đi tới [CongVien v]
nói [Ồ! Tôi gặp bạn chó.] trong (2) giây
chờ (1) giây
nói [Chó: Chào bạn! Bạn có muốn chơi không?] trong (3) giây
```

#### Bước 6: Lập trình cảnh 3
```scratch
Khi nhận được [Canh3 v]
đi tới [HoNuoc v]
nói [Tôi nghe thấy tiếng kêu cứu!] trong (2) giây
chờ (1) giây
nói [Cá: Cứu tôi! Tôi bị mắc kẹt!] trong (3) giây
```

### Phần 5: Thêm tính năng nâng cao (10 phút)

#### Bước 1: Thêm âm thanh nền
```scratch
Khi cờ xanh được nhấn
lặp lại mãi mãi
phát âm thanh [NhacNen v]
chờ (10) giây
```

#### Bước 2: Thêm hiệu ứng chuyển cảnh
```scratch
Khi nhận được [Canh2 v]
thay đổi hiệu ứng [màu v] bởi (25)
chờ (0.5) giây
thay đổi hiệu ứng [màu v] bởi (0)
```

#### Bước 3: Thêm kết thúc
```scratch
Khi nhận được [KetThuc v]
nói [Cảm ơn bạn đã đọc câu chuyện của tôi!] trong (3) giây
phát âm thanh [KetThuc v]
```

## 🎨 Hoạt động mở rộng

### Cấp độ 1: Thêm tính năng cơ bản
- Thêm nhiều cảnh hơn
- Tạo nhiều lựa chọn
- Thêm âm thanh cho từng nhân vật

### Cấp độ 2: Tính năng nâng cao
- Tạo hệ thống điểm số
- Thêm minigame trong câu chuyện
- Tạo nhiều kết thúc khác nhau

### Cấp độ 3: Sáng tạo
- Tạo câu chuyện theo chủ đề khác
- Thêm animation phức tạp
- Tạo câu chuyện có nhiều phần

## 📝 Bài tập về nhà

### Bài tập bắt buộc
1. Hoàn thành câu chuyện với ít nhất 3 cảnh
2. Thêm ít nhất 2 lựa chọn tương tác
3. Thêm âm thanh cho từng nhân vật

### Bài tập nâng cao
1. Tạo câu chuyện với nhiều kết thúc
2. Thêm minigame trong câu chuyện
3. Thiết kế câu chuyện theo phong cách riêng

## 🔍 Đánh giá

### Tiêu chí đánh giá
| Tiêu chí | Điểm | Mô tả |
|----------|------|-------|
| Cốt truyện | 3 | Có mở đầu, thân bài, kết thúc rõ ràng |
| Tương tác | 2 | Có ít nhất 2 lựa chọn tương tác |
| Nhân vật | 2 | Nhân vật có tính cách và lời thoại |
| Kỹ thuật | 2 | Sử dụng broadcast và logic đúng |
| Sáng tạo | 1 | Có yếu tố độc đáo và sáng tạo |
| Tổng cộng | 10 | |

### Cách đánh giá
- **Kịch bản**: Kiểm tra cốt truyện và lời thoại
- **Quan sát**: Giáo viên quan sát quá trình tạo
- **Sản phẩm**: Kiểm tra câu chuyện hoàn chỉnh
- **Trình bày**: Học sinh kể câu chuyện

## 🚀 Lưu ý quan trọng

### Cho giáo viên
- Khuyến khích học sinh sáng tạo
- Hướng dẫn cách viết kịch bản
- Tạo không khí học tập vui vẻ
- Chuẩn bị template kịch bản

### Cho học sinh
- Không ngại thể hiện ý tưởng
- Viết kịch bản trước khi lập trình
- Thử nghiệm nhiều tình huống khác nhau
- Lưu dự án thường xuyên

## 💡 Mẹo hay

### Viết kịch bản hay
- Tạo nhân vật có tính cách rõ ràng
- Viết lời thoại tự nhiên
- Tạo tình huống hấp dẫn

### Lập trình hiệu quả
- Sử dụng broadcast để đồng bộ
- Tạo code rõ ràng và có comment
- Test từng cảnh một

### Tương tác thú vị
- Tạo lựa chọn có ý nghĩa
- Thêm bất ngờ cho người đọc
- Cân bằng giữa các lựa chọn

## 📚 Tài liệu tham khảo

- [Scratch Story Projects](https://scratch.mit.edu/explore/projects/stories)
- [Scratch Broadcast Tutorial](https://scratch.mit.edu/tutorials)
- [Storytelling Techniques](https://scratch.mit.edu/studios/104)

---

**Tác giả**: AI & Trần Việt Trung (BKHN)  
**Ngày tạo**: 04/10/2025  
**Phiên bản**: 1.0
