# Bài Giảng 4: Máy Tính Đơn Giản

## 📋 Thông tin bài học
- **Thời gian**: 60 phút
- **Độ tuổi**: Lớp 4-5 (9-11 tuổi)
- **Mức độ**: Trung bình
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


## 🧮 Nội dung bài học

### Phần 1: Giới thiệu và thiết kế (10 phút)

#### Hoạt động khởi động
- Cho học sinh xem máy tính thật và hỏi: "Máy tính hoạt động như thế nào?"
- Giải thích mục tiêu: Tạo máy tính đơn giản bằng Scratch
- Thảo luận: "Các phép toán nào cần có trong máy tính?"

#### Thiết kế giao diện
- **Màn hình hiển thị**: Hiển thị số và kết quả
- **Nút số**: 0-9
- **Nút phép toán**: +, -, ×, ÷
- **Nút đặc biệt**: =, C (xóa)

### Phần 2: Tạo giao diện máy tính (15 phút)

#### Bước 1: Tạo hình nền
1. Chọn "Choose a Backdrop" → "Other" → chọn màu xám
2. Hoặc vẽ hình nền đơn giản

#### Bước 2: Tạo màn hình hiển thị
1. Chọn "Choose a Sprite" → "Things" → chọn hình chữ nhật
2. Đặt tên: "ManHinh"
3. Điều chỉnh kích thước và màu sắc
4. Thêm văn bản "0" làm giá trị mặc định

#### Bước 3: Tạo các nút số
1. Tạo sprite cho nút số 0-9
2. Đặt tên: "Nut0", "Nut1", ..., "Nut9"
3. Sắp xếp thành bàn phím số

#### Bước 4: Tạo các nút phép toán
1. Tạo sprite cho +, -, ×, ÷
2. Đặt tên: "Cong", "Tru", "Nhan", "Chia"
3. Đặt màu sắc khác biệt

### Phần 3: Lập trình logic tính toán (25 phút)

#### Bước 1: Tạo biến số
1. Chọn "Variables" → "Make a Variable"
2. Tạo các biến:
   - "SoHienTai": Số đang hiển thị
   - "SoThuNhat": Số đầu tiên
   - "PhepToan": Phép toán được chọn
   - "KetQua": Kết quả tính toán

#### Bước 2: Lập trình nút số
```scratch
Khi nhấn phím [0 v]
nếu <[SoHienTai v] = [0]> thì
đặt [SoHienTai v] thành (0)
nếu không
đặt [SoHienTai v] thành (join [SoHienTai v] [0])
```

#### Bước 3: Lập trình nút phép toán
```scratch
Khi nhấn phím [+] v
đặt [SoThuNhat v] thành [SoHienTai v]
đặt [PhepToan v] thành [+]
đặt [SoHienTai v] thành [0]
```

#### Bước 4: Lập trình nút bằng
```scratch
Khi nhấn phím [= v]
nếu <[PhepToan v] = [+]> thì
đặt [KetQua v] thành ([SoThuNhat v] + [SoHienTai v])
nếu <[PhepToan v] = [-]> thì
đặt [KetQua v] thành ([SoThuNhat v] - [SoHienTai v])
nếu <[PhepToan v] = [×]> thì
đặt [KetQua v] thành ([SoThuNhat v] * [SoHienTai v])
nếu <[PhepToan v] = [÷]> thì
đặt [KetQua v] thành ([SoThuNhat v] / [SoHienTai v])
đặt [SoHienTai v] thành [KetQua v]
```

#### Bước 5: Lập trình nút xóa
```scratch
Khi nhấn phím [C v]
đặt [SoHienTai v] thành [0]
đặt [SoThuNhat v] thành [0]
đặt [PhepToan v] thành []
```

### Phần 4: Cải thiện giao diện (5 phút)

#### Bước 1: Cập nhật màn hình
```scratch
Khi cờ xanh được nhấn
lặp lại mãi mãi
nói [SoHienTai v]
```

#### Bước 2: Thêm hiệu ứng nhấn nút
```scratch
Khi nhấn phím [0 v]
thay đổi kích thước bởi (-10)
chờ (0.1) giây
thay đổi kích thước bởi (10)
```

#### Bước 3: Thêm âm thanh
```scratch
Khi nhấn phím [0 v]
phát âm thanh [pop v]
```

### Phần 5: Thêm tính năng nâng cao (5 phút)

#### Bước 1: Xử lý lỗi chia cho 0
```scratch
Khi nhấn phím [= v]
nếu <[PhepToan v] = [÷]> và <[SoHienTai v] = [0]> thì
nói [Lỗi: Chia cho 0!] trong (2) giây
nếu không
[thực hiện phép chia bình thường]
```

#### Bước 2: Thêm phép toán phần trăm
```scratch
Khi nhấn phím [% v]
đặt [KetQua v] thành ([SoHienTai v] / [100])
đặt [SoHienTai v] thành [KetQua v]
```

## 🎨 Hoạt động mở rộng

### Cấp độ 1: Thêm tính năng cơ bản
- Thêm nút dấu chấm thập phân
- Thêm nút đổi dấu (+/-)
- Thêm lịch sử tính toán

### Cấp độ 2: Tính năng nâng cao
- Thêm phép toán lũy thừa
- Thêm phép toán căn bậc hai
- Thêm bộ nhớ (M+, M-, MR, MC)

### Cấp độ 3: Sáng tạo
- Tạo máy tính khoa học
- Thêm chế độ đổi đơn vị
- Tạo máy tính chuyên dụng

## 📝 Bài tập về nhà

### Bài tập bắt buộc
1. Hoàn thành máy tính cơ bản với 4 phép toán
2. Thêm xử lý lỗi chia cho 0
3. Test máy tính với các phép toán khác nhau

### Bài tập nâng cao
1. Thêm phép toán phần trăm
2. Tạo giao diện đẹp hơn
3. Thêm âm thanh và hiệu ứng

## 🔍 Đánh giá

### Tiêu chí đánh giá
| Tiêu chí | Điểm | Mô tả |
|----------|------|-------|
| Tính toán đúng | 4 | Tất cả phép toán hoạt động chính xác |
| Giao diện | 2 | Giao diện rõ ràng, dễ sử dụng |
| Xử lý lỗi | 2 | Xử lý được các trường hợp lỗi |
| Sáng tạo | 1 | Có tính năng độc đáo |
| Trình bày | 1 | Demo mượt mà, giải thích rõ ràng |
| Tổng cộng | 10 | |

### Cách đánh giá
- **Test tính toán**: Kiểm tra độ chính xác
- **Quan sát**: Giáo viên quan sát quá trình lập trình
- **Sản phẩm**: Kiểm tra máy tính hoàn chỉnh
- **Trình bày**: Học sinh demo và giải thích

## 🚀 Lưu ý quan trọng

### Cho giáo viên
- Giải thích kỹ logic tính toán
- Hướng dẫn cách test từng phép toán
- Khuyến khích học sinh thử nghiệm
- Chuẩn bị sẵn test cases

### Cho học sinh
- Hiểu rõ logic từng phép toán
- Test kỹ từng tính năng
- Không ngại thử nghiệm tính năng mới
- Lưu dự án thường xuyên

## 💡 Mẹo hay

### Logic tính toán
- Luôn kiểm tra điều kiện trước khi tính
- Sử dụng biến để lưu trữ trạng thái
- Xử lý tất cả các trường hợp có thể

### Giao diện thân thiện
- Sử dụng màu sắc rõ ràng
- Sắp xếp nút hợp lý
- Thêm hiệu ứng phản hồi

### Test hiệu quả
- Test với số nhỏ trước
- Test với số âm
- Test với số thập phân
- Test các trường hợp lỗi

## 📚 Tài liệu tham khảo

- [Scratch Math Projects](https://scratch.mit.edu/explore/projects/math)
- [Scratch Variables Tutorial](https://scratch.mit.edu/tutorials)
- [Calculator Design Principles](https://scratch.mit.edu/studios/104)

---

**Tác giả**: AI & Trần Việt Trung (BKHN)  
**Ngày tạo**: 04/10/2025  
**Phiên bản**: 1.0
