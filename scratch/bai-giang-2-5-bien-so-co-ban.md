# Bài Giảng 2.5: Biến Số Cơ Bản

## 📋 Thông tin bài học
- **Thời gian**: 45 phút
- **Độ tuổi**: Lớp 3-4 (8-9 tuổi)
- **Mức độ**: Cơ bản đến trung bình
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

## 🧮 Nội dung bài học

### Phần 1: Giới thiệu biến số qua hoạt động không máy tính (10 phút)

#### Hoạt động khởi động - "Hộp đựng đồ"
- **Hoạt động**: Giáo viên cầm một hộp và hỏi: "Hộp này đựng gì?"
- **Mục tiêu**: Hiểu biến số như một "hộp" để chứa thông tin
- **Kết quả**: Nhận ra biến số có thể chứa nhiều loại thông tin khác nhau

#### Ví dụ biến số từ cuộc sống
```
Hộp điểm số: Có thể chứa 8, 9, 10...
Hộp tên: Có thể chứa "An", "Bình", "Châu"...
Hộp tuổi: Có thể chứa 8, 9, 10...
Hộp màu sắc: Có thể chứa "đỏ", "xanh", "vàng"...
```

#### Khái niệm cơ bản
- **Biến số**: Như một hộp để chứa thông tin
- **Tên biến**: Nhãn dán trên hộp (ví dụ: "điểm", "tuổi")
- **Giá trị**: Nội dung trong hộp (ví dụ: 8, "An")
- **Thay đổi**: Có thể thay đổi nội dung trong hộp

#### Hoạt động thực hành - "Đếm số bạn trong lớp"
- **Hoạt động**: Học sinh đếm số bạn nam và nữ
- **Mục tiêu**: Thực hành sử dụng biến số để đếm
- **Kết quả**: Hiểu cách biến số giúp theo dõi thông tin

### Phần 2: Tạo biến số trong Scratch (15 phút)

#### Bước 1: Tạo biến số đầu tiên
1. Mở Scratch và tạo dự án mới
2. Chọn "Variables" (Biến số) trong menu
3. Nhấn "Make a Variable" (Tạo biến số)
4. Đặt tên: "DiemSo"
5. Chọn "For all sprites" (Cho tất cả nhân vật)

#### Bước 2: Hiển thị biến số
1. Kéo khối "show variable [DiemSo]" vào Scripts
2. Nhấn cờ xanh để chạy
3. Quan sát: Biến số xuất hiện trên màn hình với giá trị 0

#### Bước 3: Thay đổi giá trị biến số
```scratch
Khi cờ xanh được nhấn
đặt [DiemSo v] thành (5)
nói [Điểm số của tôi là: ] + [DiemSo v] trong (3) giây
```

#### Hoạt động thực hành - "Thay đổi điểm số"
- **Hoạt động**: Học sinh thay đổi giá trị biến số và quan sát
- **Mục tiêu**: Hiểu cách thay đổi giá trị biến số
- **Thử thách**: Thử các giá trị khác nhau (1, 10, 100)

### Phần 3: Sử dụng biến số để đếm (20 phút)

#### Bài toán: Đếm số lần nhấn phím
- **Mục tiêu**: Mỗi lần nhấn phím cách, tăng điểm số lên 1
- **Ví dụ**: Nhấn 3 lần → điểm số = 3

#### Lập trình đếm cơ bản
```scratch
Khi cờ xanh được nhấn
đặt [DiemSo v] thành (0)
nói [Bắt đầu đếm! Nhấn phím cách để tăng điểm] trong (3) giây

Khi nhấn phím [cách v]
thay đổi [DiemSo v] bởi (1)
nói [Điểm số: ] + [DiemSo v] trong (1) giây
```

#### Hoạt động mở rộng - "Đếm với nhiều phím"
- **Hoạt động**: Tạo biến số cho từng phím (A, S, D)
- **Mục tiêu**: Hiểu cách sử dụng nhiều biến số
- **Thử thách**: Tạo game đếm điểm đơn giản

#### Bài toán: Tính tổng điểm
```scratch
Khi cờ xanh được nhấn
đặt [DiemSo v] thành (0)
đặt [TongDiem v] thành (0)
nói [Nhấn phím cách để thêm điểm] trong (3) giây

Khi nhấn phím [cách v]
thay đổi [DiemSo v] bởi (1)
thay đổi [TongDiem v] bởi ([DiemSo v])
nói [Điểm hiện tại: ] + [DiemSo v] + [. Tổng: ] + [TongDiem v] trong (2) giây
```

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

## 🔍 Đánh giá

### Tiêu chí đánh giá
| Tiêu chí | Điểm | Mô tả |
|----------|------|-------|
| Hiểu biến số | 3 | Giải thích được khái niệm biến số |
| Sử dụng đúng | 3 | Tạo và sử dụng biến số chính xác |
| Ứng dụng | 2 | Áp dụng biến số vào bài toán |
| Sáng tạo | 1 | Có yếu tố độc đáo |
| Trình bày | 1 | Giải thích rõ ràng |
| **Tổng cộng** | **10** | |

### Cách đánh giá
- **Quan sát**: Giáo viên quan sát quá trình học
- **Sản phẩm**: Kiểm tra chương trình hoàn chỉnh
- **Trình bày**: Học sinh giải thích cách sử dụng biến số
- **Phản hồi**: Nhận xét từ bạn cùng lớp

## 🚀 Lưu ý quan trọng

### Cho giáo viên
- Sử dụng ví dụ cụ thể từ cuộc sống
- Khuyến khích học sinh thử nghiệm với các giá trị khác nhau
- Tạo không khí học tập vui vẻ
- Chuẩn bị nhiều ví dụ thực tế

### Cho học sinh
- Hiểu biến số như một "hộp" chứa thông tin
- Thử nghiệm với các giá trị khác nhau
- Không ngại thử nghiệm và sai lầm
- Lưu dự án thường xuyên

## 💡 Mẹo hay

### Sử dụng biến số hiệu quả
- **Đặt tên có ý nghĩa**: Sử dụng tên dễ hiểu (DiemSo, Tuoi, Ten)
- **Khởi tạo giá trị**: Luôn đặt giá trị ban đầu cho biến số
- **Hiển thị giá trị**: Sử dụng "say" để theo dõi giá trị biến số

### Debug hiệu quả
- **Sử dụng "say"**: Thêm lệnh nói để theo dõi giá trị biến số
- **Kiểm tra từng bước**: Debug từng phần một thay vì toàn bộ
- **Test với các giá trị**: Kiểm tra với các giá trị khác nhau

### Tối ưu hóa
- **Sử dụng biến số chung**: Tạo biến số cho tất cả nhân vật khi cần
- **Đặt tên ngắn gọn**: Sử dụng tên ngắn nhưng dễ hiểu
- **Tránh tạo quá nhiều**: Chỉ tạo biến số khi thực sự cần thiết

## 🔗 Chuẩn bị cho bài tiếp theo

### Bài 3: Trò chơi "Bảo vệ đảo"
- Sử dụng biến số để tạo hệ thống điểm
- Quản lý nhiều biến số cùng lúc
- Tạo game logic với biến số

### Kết nối với các bài trước
- **Bài 1**: Chuyển động cơ bản
- **Bài 2**: Giao diện và hiệu ứng
- **Bài 2.5**: Biến số cơ bản ← Bài này
- **Bài 3**: Game phức tạp với biến số

## 📚 Tài liệu tham khảo

- [Scratch Variables Tutorial](https://scratch.mit.edu/tutorials)
- [Teaching Variables to Kids](https://www.education.com/lesson-plan/variables/)
- [Scratch Programming for Kids](https://scratch.mit.edu/explore/projects/variables)

---

**Tác giả**: AI & Trần Việt Trung (BKHN)  
**Ngày tạo**: 04/10/2025  
**Phiên bản**: 1.0
