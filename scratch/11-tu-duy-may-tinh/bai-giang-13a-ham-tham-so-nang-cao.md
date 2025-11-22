# Bài giảng 13A: Hàm có tham số nâng cao

## 📋 Thông tin bài học
- **Thời gian**: 90 phút
- **Độ tuổi**: 10-11 tuổi
- **Trình độ**: Nâng cao
- **Mục tiêu**: Học cách tạo hàm phức tạp với nhiều tham số

## 🎯 Mục tiêu học tập

### Kiến thức
- Hiểu My Blocks với nhiều tham số
- Nắm vững hàm trả về giá trị
- Hiểu hàm đệ quy đơn giản
- Biết cách tổ chức code modular

### Kỹ năng
- Tạo hàm với nhiều tham số
- Sử dụng hàm trả về giá trị
- Tạo hàm đệ quy đơn giản
- Tổ chức code có cấu trúc

## 🧠 Nội dung bài học

## 📚 PHẦN LÝ THUYẾT (45 phút)

### Phần 1: Ôn tập Custom Blocks (10 phút)

#### Hoạt động khởi động - "Nhớ lại Custom Blocks"
- **Hoạt động**: Nhắc lại Bài 3.5 và Bài 8
- **Câu hỏi**: "Chúng ta đã học Custom Blocks như thế nào?"
- **Kết nối**: "Hôm nay học nâng cao hơn"
- **Mục tiêu**: Củng cố kiến thức

### Phần 2: Hàm với nhiều tham số (15 phút)

#### Khái niệm nhiều tham số
- **Định nghĩa**: Hàm có thể nhận nhiều tham số
- **Ví dụ**: Tính diện tích hình chữ nhật (chiều dài, chiều rộng)
- **Ứng dụng**: Hàm linh hoạt hơn

### Phần 3: Hàm trả về giá trị (10 phút)

#### Khái niệm hàm trả về
- **Định nghĩa**: Hàm tính toán và trả về kết quả
- **Ví dụ**: Hàm tính tổng trả về tổng
- **Ứng dụng**: Tái sử dụng kết quả

### Phần 4: Hàm đệ quy đơn giản (10 phút)

#### Khái niệm đệ quy
- **Định nghĩa**: Hàm gọi chính nó
- **Ví dụ**: Tính giai thừa
- **Lưu ý**: Cần điều kiện dừng

## 💻 PHẦN THỰC HÀNH (45 phút)

### Phần 1: Hàm với nhiều tham số (15 phút)

```scratch
# Tạo custom block "Tính diện tích" với 2 tham số
định nghĩa Tính diện tích (chieuDai) (chieuRong)
đặt [dienTich v] thành ((chieuDai) * (chieuRong))
nói [Diện tích: ] + [dienTich v] trong (2) giây

# Sử dụng
Khi cờ xanh được nhấn
Tính diện tích (5) (3)
```

### Phần 2: Hàm trả về giá trị (15 phút)

```scratch
# Tạo custom block "Tính tổng" trả về giá trị
định nghĩa Tính tổng (so1) (so2)
đặt [ketQua v] thành ((so1) + (so2))
nói [Tổng: ] + [ketQua v] trong (2) giây

# Sử dụng
Khi cờ xanh được nhấn
Tính tổng (5) (3)
```

### Phần 3: Hàm đệ quy đơn giản (15 phút)

```scratch
# Tạo custom block "Giai thừa" (đơn giản hóa)
định nghĩa Giai thừa (n)
nếu <(n) = [1]> thì
  nói [1] trong (1) giây
không thì
  nói [Đang tính...] trong (1) giây
  Giai thừa ((n) - (1))
```

## 📝 Tổng kết

- **Nhiều tham số**: Hàm linh hoạt hơn
- **Trả về giá trị**: Tái sử dụng kết quả
- **Đệ quy**: Hàm gọi chính nó

## 🔗 Liên kết

- **Bài trước**: [Bài 12C: Hệ thống điểm & khó dần](../10-game-nang-cao/bai-giang-12c-he-thong-diem-va-kho-dan.md)
- **Bài tiếp theo**: [Bài 13B: Debug — Tìm lỗi](bai-giang-13b-debug-tim-loi.md)
- **Bài liên quan**: 
  - [Bài 3.5: Custom Blocks](../03-game-va-ung-dung/bai-giang-3-5-custom-blocks.md)
  - [Bài 8: Hàm và thủ tục](../06-ham-va-modular/bai-giang-8-ham-va-thu-tuc.md)
- **Về topic**: [README.md](README.md)

---

**🌟 Chúc các em học tốt!**

