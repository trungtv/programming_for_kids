# Bài Giảng 1: Trò Chơi "Mèo Đuổi Chuột"

## 📋 Thông tin bài học
- **Thời gian**: 60 phút
- **Độ tuổi**: Lớp 3-4 (8-9 tuổi)
- **Mức độ**: Cơ bản
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


## 🎮 Nội dung bài học

### Phần 1: Giới thiệu (10 phút)

#### Hoạt động khởi động
- Cho học sinh xem video trò chơi "Mèo đuổi chuột" hoàn chỉnh
- Hỏi học sinh: "Các em có muốn tạo trò chơi này không?"
- Giải thích mục tiêu bài học

#### Giới thiệu trò chơi
- **Luật chơi**: Mèo sẽ đuổi theo chuột, chuột chạy trốn
- **Cách chơi**: Sử dụng phím mũi tên để điều khiển chuột
- **Mục tiêu**: Tránh để mèo bắt được chuột

### Phần 2: Tạo nhân vật và hình nền (15 phút)

#### Bước 1: Tạo nhân vật Mèo
1. Xóa nhân vật mặc định (Sprite1)
2. Chọn "Choose a Sprite" → "Animals" → chọn mèo
3. Đặt tên: "Meo"
4. Điều chỉnh kích thước phù hợp

#### Bước 2: Tạo nhân vật Chuột
1. Chọn "Choose a Sprite" → "Animals" → chọn chuột
2. Đặt tên: "Chuot"
3. Điều chỉnh kích thước nhỏ hơn mèo

#### Bước 3: Tạo hình nền
1. Chọn "Choose a Backdrop" → "Nature" → chọn sân cỏ
2. Hoặc vẽ hình nền đơn giản

### Phần 3: Lập trình cho Chuột (20 phút)

#### Bước 1: Chuyển động cơ bản
```scratch
Khi nhấn phím [mũi tên phải v]
di chuyển (10) bước
```

#### Bước 2: Thêm các hướng di chuyển
```scratch
Khi nhấn phím [mũi tên trái v]
di chuyển (-10) bước

Khi nhấn phím [mũi tên lên v]
thay đổi y bởi (10)

Khi nhấn phím [mũi tên xuống v]
thay đổi y bởi (-10)
```

#### Bước 3: Thêm hiệu ứng xoay
```scratch
Khi nhấn phím [mũi tên phải v]
di chuyển (10) bước
hướng về phía (90 vòng độ)

Khi nhấn phím [mũi tên trái v]
di chuyển (-10) bước
hướng về phía (-90 vòng độ)
```

### Phần 4: Lập trình cho Mèo (10 phút)

#### Bước 1: Mèo luôn hướng về chuột
```scratch
Mãi mãi
hướng về phía [Chuot v]
di chuyển (5) bước
```

#### Bước 2: Thêm âm thanh khi mèo di chuyển
```scratch
Mãi mãi
hướng về phía [Chuot v]
di chuyển (5) bước
phát âm thanh [meow v]
```

### Phần 5: Thêm điều kiện thắng/thua (5 phút)

#### Bước 1: Kiểm tra khi mèo bắt được chuột
```scratch
Mãi mãi
nếu <chạm [Chuot v]?> thì
nói [Mèo đã bắt được chuột!] trong (2) giây
dừng [tất cả v]
```

## 🎨 Hoạt động mở rộng

### Cấp độ 1: Thêm tính năng cơ bản
- Thêm điểm số
- Thêm âm thanh nền
- Thay đổi tốc độ di chuyển

### Cấp độ 2: Tính năng nâng cao
- Thêm nhiều chuột
- Thêm chướng ngại vật
- Tạo hệ thống level

### Cấp độ 3: Sáng tạo
- Thay đổi nhân vật
- Tạo câu chuyện cho trò chơi
- Thêm hiệu ứng đặc biệt

## 📝 Bài tập về nhà

### Bài tập bắt buộc
1. Hoàn thành trò chơi cơ bản
2. Thêm ít nhất 2 âm thanh khác nhau
3. Thay đổi màu sắc của nhân vật

### Bài tập nâng cao
1. Tạo thêm 1 nhân vật phụ
2. Thêm hệ thống điểm số
3. Tạo màn hình bắt đầu và kết thúc

## 🔍 Đánh giá

### Tiêu chí đánh giá
| Tiêu chí | Điểm | Mô tả |
|----------|------|-------|
| Hoàn thành cơ bản | 3 | Trò chơi chạy được, có chuyển động |
| Tính năng bổ sung | 2 | Thêm âm thanh, hiệu ứng |
| Sáng tạo | 2 | Thay đổi nhân vật, hình nền |
| Chia sẻ | 1 | Trình bày sản phẩm trước lớp |
| Hỗ trợ bạn | 1 | Giúp đỡ bạn cùng lớp |
| Tổng cộng | 9 | |

### Cách đánh giá
- **Quan sát**: Giáo viên quan sát quá trình làm việc
- **Sản phẩm**: Kiểm tra trò chơi hoàn chỉnh
- **Trình bày**: Học sinh demo trò chơi
- **Phản hồi**: Nhận xét từ bạn cùng lớp

## 🚀 Lưu ý quan trọng

### Cho giáo viên
- Kiên nhẫn với học sinh chậm hiểu
- Khuyến khích học sinh thử nghiệm
- Tạo không khí học tập vui vẻ
- Chuẩn bị sẵn file mẫu để hỗ trợ

### Cho học sinh
- Không sợ mắc lỗi, hãy thử nghiệm
- Hỏi giáo viên khi không hiểu
- Giúp đỡ bạn cùng lớp
- Lưu dự án thường xuyên

## 📚 Tài liệu tham khảo

- [Scratch Official Website](https://scratch.mit.edu)
- [Scratch Tutorials](https://scratch.mit.edu/tutorials)
- [Scratch Community](https://scratch.mit.edu/explore/projects/games)

---

**Tác giả**: AI & Trần Việt Trung (BKHN)  
**Ngày tạo**: 04/10/2025  
**Phiên bản**: 1.0
