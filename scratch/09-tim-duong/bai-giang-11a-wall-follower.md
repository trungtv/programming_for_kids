# Bài giảng 11A: Wall Follower (Đi theo tường)

## 📋 Thông tin bài học
- **Thời gian**: 90 phút
- **Độ tuổi**: 10-11 tuổi
- **Trình độ**: Nâng cao
- **Mục tiêu**: Học thuật toán tìm đường bằng cách đi theo tường

## 🎯 Mục tiêu học tập

### Kiến thức
- Hiểu thuật toán đi theo tường (Wall Follower)
- Nắm vững cách nhân vật tự tìm đường ra mê cung
- Hiểu cách xử lý các trường hợp đặc biệt
- Biết ứng dụng vào robot thật

### Kỹ năng
- Lập trình thuật toán đi theo tường
- Xử lý cảm biến và điều hướng
- Tạo mê cung và giải mê cung
- Debug thuật toán tìm đường

## 🧠 Nội dung bài học

## 📚 PHẦN LÝ THUYẾT (45 phút)

### Phần 1: Khái niệm đi theo tường (20 phút)

#### Hoạt động không máy tính - "Đi theo tường bằng tay"
- **Hoạt động**: Học sinh đặt tay lên tường, đi theo tường
- **Quy tắc**: Luôn giữ tay trên tường, đi theo hướng tường
- **Kết quả**: Tìm được lối ra
- **Mục tiêu**: Hiểu thuật toán đi theo tường

#### Khái niệm Wall Follower
- **Định nghĩa**: Đi theo tường bên phải hoặc bên trái
- **Quy tắc đơn giản**:
  1. Đi thẳng
  2. Nếu có tường bên phải, tiếp tục đi thẳng
  3. Nếu không có tường bên phải, rẽ phải
  4. Nếu chạm tường phía trước, rẽ trái
- **Ứng dụng**: Robot thật, game mê cung

### Phần 2: Thuật toán đi theo tường (25 phút)

#### Hoạt động không máy tính - "Mô phỏng bằng giấy"
- **Hoạt động**: Học sinh vẽ mê cung, mô phỏng đi theo tường
- **Bước 1**: Đặt tay phải lên tường
- **Bước 2**: Đi theo hướng tường
- **Bước 3**: Nếu gặp ngã rẽ, rẽ phải
- **Kết quả**: Tìm được lối ra
- **Mục tiêu**: Hiểu rõ các bước thuật toán

## 💻 PHẦN THỰC HÀNH (45 phút)

### Phần 1: Tạo mê cung (15 phút)

```scratch
# Tạo backdrop mê cung
# Vẽ mê cung với tường màu đen, đường đi màu trắng
```

### Phần 2: Lập trình đi theo tường (30 phút)

```scratch
Khi cờ xanh được nhấn
lặp mãi mãi
  # Kiểm tra tường bên phải
  quay về hướng ((hướng) + (90))
  di chuyển (1) bước
  nếu <chạm màu [#000000]?> thì
    quay về hướng ((hướng) - (90))  # Quay lại
    # Có tường bên phải, đi thẳng
    quay về hướng ((hướng) - (90))
    di chuyển (1) bước
    quay về hướng ((hướng) + (90))
  không thì
    # Không có tường bên phải, rẽ phải
    quay về hướng ((hướng) - (90))
  
  # Kiểm tra tường phía trước
  di chuyển (1) bước
  nếu <chạm màu [#000000]?> thì
    quay về hướng ((hướng) - (90))  # Quay lại
    quay về hướng ((hướng) - (90))  # Rẽ trái
  không thì
    quay về hướng ((hướng) - (90))  # Quay lại
    di chuyển (1) bước  # Đi thẳng
```

## 📝 Tổng kết

- **Wall Follower**: Đi theo tường để tìm đường
- **Quy tắc**: Luôn giữ tường bên phải/trái
- **Ứng dụng**: Robot, game mê cung

## 🔗 Liên kết

- **Bài trước**: [Bài 10C: Mô phỏng hệ thống](../08-mo-phong-nang-cao/bai-giang-10c-mo-phong-he-thong.md)
- **Bài tiếp theo**: [Bài 11B: Line Following Robot](bai-giang-11b-line-following.md)
- **Về topic**: [README.md](README.md)

---

**🌟 Chúc các em học tốt!**

