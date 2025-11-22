# Bài giảng 13B: Debug — Tìm lỗi

## 📋 Thông tin bài học
- **Thời gian**: 90 phút
- **Độ tuổi**: 10-11 tuổi
- **Trình độ**: Nâng cao
- **Mục tiêu**: Học kỹ năng debug quan trọng

## 🎯 Mục tiêu học tập

### Kiến thức
- Hiểu cách chạy theo từng bước
- Nắm vững kiểm tra biến
- Hiểu cách tìm giá trị sai
- Biết cách tìm điều kiện sai

### Kỹ năng
- Debug code hiệu quả
- Kiểm tra biến và giá trị
- Tìm và sửa lỗi
- Sử dụng các kỹ thuật debug

## 🧠 Nội dung bài học

## 📚 PHẦN LÝ THUYẾT (45 phút)

### Phần 1: Khái niệm debug (15 phút)

#### Hoạt động khởi động - "Tìm lỗi trong câu"
- **Hoạt động**: Học sinh tìm lỗi chính tả trong câu
- **Câu hỏi**: "Làm sao để tìm lỗi?"
- **Kết nối**: "Debug code cũng giống như vậy"
- **Mục tiêu**: Hiểu khái niệm debug

#### Khái niệm Debug
- **Định nghĩa**: Tìm và sửa lỗi trong code
- **Các bước**:
  1. Chạy từng bước
  2. Kiểm tra biến
  3. Tìm giá trị sai
  4. Sửa lỗi
- **Ứng dụng**: Mọi lập trình viên cần biết

### Phần 2: Chạy theo từng bước (15 phút)

#### Kỹ thuật step-by-step
- **Quy tắc**: Chạy code từng bước một
- **Công thức**: Thêm "nói" để xem từng bước
- **Ứng dụng**: Tìm lỗi logic

### Phần 3: Kiểm tra biến (15 phút)

#### Kỹ thuật kiểm tra biến
- **Quy tắc**: Hiển thị giá trị biến
- **Công thức**: Nói giá trị biến
- **Ứng dụng**: Tìm giá trị sai

## 💻 PHẦN THỰC HÀNH (45 phút)

### Phần 1: Debug code đơn giản (15 phút)

```scratch
# Code có lỗi
Khi cờ xanh được nhấn
đặt [tong v] thành [0]
đặt [i v] thành [1]
lặp lại (5) lần
  thay đổi [tong v] bởi (i)  # Lỗi: nên là mục (i) của list
  nói [Bước ] + [i v] + [. Tổng: ] + [tong v] trong (1) giây
  thay đổi [i v] bởi (1)

# Debug: Thêm "nói" để xem từng bước
```

### Phần 2: Kiểm tra biến (15 phút)

```scratch
# Thêm kiểm tra biến
Khi cờ xanh được nhấn
đặt [tong v] thành [0]
đặt [i v] thành [1]
lặp lại (5) lần
  nói [i = ] + [i v] trong (1) giây  # Debug
  nói [tong = ] + [tong v] trong (1) giây  # Debug
  thay đổi [tong v] bởi (i)
  thay đổi [i v] bởi (1)
```

### Phần 3: Tìm điều kiện sai (15 phút)

```scratch
# Debug điều kiện
Khi cờ xanh được nhấn
đặt [i v] thành [1]
lặp lại (5) lần
  nói [i = ] + [i v] trong (1) giây  # Debug
  nếu <(i) > [3]> thì  # Điều kiện cần kiểm tra
    nói [i > 3] trong (1) giây  # Debug
  thay đổi [i v] bởi (1)
```

## 📝 Tổng kết

- **Debug**: Tìm và sửa lỗi
- **Step-by-step**: Chạy từng bước
- **Kiểm tra biến**: Xem giá trị biến
- **Tìm điều kiện**: Kiểm tra điều kiện

## 🔗 Liên kết

- **Bài trước**: [Bài 13A: Hàm có tham số nâng cao](bai-giang-13a-ham-tham-so-nang-cao.md)
- **Bài tiếp theo**: [Bài 13C: Thiết kế thuật toán](bai-giang-13c-thiet-ke-thuat-toan.md)
- **Về topic**: [README.md](README.md)

---

**🌟 Chúc các em học tốt!**

