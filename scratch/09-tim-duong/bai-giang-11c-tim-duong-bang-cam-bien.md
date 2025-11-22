# Bài giảng 11C: Tìm đường bằng cảm biến

## 📋 Thông tin bài học
- **Thời gian**: 90 phút
- **Độ tuổi**: 10-11 tuổi
- **Trình độ**: Nâng cao
- **Mục tiêu**: Học thuật toán tìm đường bằng cảm biến

## 🎯 Mục tiêu học tập

### Kiến thức
- Hiểu cách tìm đường bằng cảm biến
- Nắm vững thuật toán thử sai (heuristic)
- Hiểu cách xử lý khi kẹt
- Biết cách kết hợp nhiều cảm biến

### Kỹ năng
- Lập trình tìm đường bằng cảm biến
- Xử lý các trường hợp đặc biệt
- Debug thuật toán tìm đường
- Tạo robot tự động tìm đường

## 🧠 Nội dung bài học

## 📚 PHẦN LÝ THUYẾT (45 phút)

### Phần 1: Khái niệm tìm đường bằng cảm biến (20 phút)

#### Hoạt động không máy tính - "Tìm đường mù"
- **Hoạt động**: Học sinh bịt mắt, tìm đường bằng tay
- **Quy tắc**: 
  1. Đi thẳng
  2. Nếu chạm tường, rẽ trái
  3. Nếu vẫn kẹt, rẽ phải
- **Kết quả**: Tìm được đường
- **Mục tiêu**: Hiểu thuật toán thử sai

#### Khái niệm heuristic
- **Định nghĩa**: Thuật toán thử sai, học từ kinh nghiệm
- **Quy tắc**:
  1. Đi thẳng
  2. Nếu chạm tường → rẽ trái
  3. Nếu vẫn kẹt → rẽ phải
  4. Lặp lại
- **Ứng dụng**: Robot thật, game AI

## 💻 PHẦN THỰC HÀNH (45 phút)

### Phần 1: Lập trình tìm đường cơ bản (20 phút)

```scratch
Khi cờ xanh được nhấn
lặp mãi mãi
  di chuyển (3) bước
  nếu <chạm cạnh?> thì
    quay về hướng ((hướng) - (90))  # Rẽ trái
    di chuyển (3) bước
    nếu <chạm cạnh?> thì
      quay về hướng ((hướng) + (180))  # Quay lại
      quay về hướng ((hướng) + (90))  # Rẽ phải
```

### Phần 2: Cải thiện thuật toán (25 phút)

```scratch
Khi cờ xanh được nhấn
đặt [buocDem v] thành [0]
lặp mãi mãi
  di chuyển (3) bước
  thay đổi [buocDem v] bởi (1)
  nếu <chạm cạnh?> thì
    quay về hướng ((hướng) - (90))  # Rẽ trái
    nếu <[buocDem v] > [100]> thì
      # Kẹt quá lâu, thử hướng khác
      quay về hướng ((hướng) + (180))
      đặt [buocDem v] thành [0]
```

## 📝 Tổng kết

- **Tìm đường bằng cảm biến**: Sử dụng cảm biến để tìm đường
- **Thuật toán thử sai**: Thử các hướng khác nhau
- **Xử lý kẹt**: Thay đổi chiến lược khi kẹt

## 🔗 Liên kết

- **Bài trước**: [Bài 11B: Line Following Robot](bai-giang-11b-line-following.md)
- **Bài tiếp theo**: [Bài 12A: Hệ thống vật phẩm](../10-game-nang-cao/bai-giang-12a-he-thong-vat-pham.md)
- **Về topic**: [README.md](README.md)

---

**🌟 Chúc các em học tốt!**

