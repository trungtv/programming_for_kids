# Bài giảng 12B: AI đơn giản cho kẻ thù

## 📋 Thông tin bài học
- **Thời gian**: 90 phút
- **Độ tuổi**: 10-11 tuổi
- **Trình độ**: Nâng cao
- **Mục tiêu**: Tạo AI đơn giản cho kẻ thù trong game

## 🎯 Mục tiêu học tập

### Kiến thức
- Hiểu cách tạo AI đuổi theo người chơi
- Nắm vững AI tránh vật cản
- Hiểu cách tạo AI patrol (đi tuần tra)
- Biết cách kết hợp nhiều hành vi

### Kỹ năng
- Lập trình AI đơn giản
- Kết hợp nhiều hành vi AI
- Tạo kẻ thù thông minh
- Debug AI

## 🧠 Nội dung bài học

## 📚 PHẦN LÝ THUYẾT (45 phút)

### Phần 1: AI đuổi theo (15 phút)

#### Khái niệm AI đuổi
- **Quy tắc**: Luôn di chuyển về phía người chơi
- **Công thức**: Quay về hướng người chơi, di chuyển
- **Ứng dụng**: Kẻ thù đuổi theo

### Phần 2: AI tránh vật cản (15 phút)

#### Khái niệm tránh vật cản
- **Quy tắc**: Nếu chạm vật cản, đổi hướng
- **Công thức**: Kiểm tra chạm, rẽ nếu cần
- **Ứng dụng**: Kẻ thù thông minh

### Phần 3: AI patrol (15 phút)

#### Khái niệm patrol
- **Quy tắc**: Đi theo đường định sẵn
- **Công thức**: Di chuyển giữa 2 điểm
- **Ứng dụng**: Kẻ thù tuần tra

## 💻 PHẦN THỰC HÀNH (45 phút)

### Phần 1: AI đuổi theo (15 phút)

```scratch
Khi cờ xanh được nhấn
lặp mãi mãi
  quay về hướng (hướng đến [NguoiChoi v])
  di chuyển (3) bước
```

### Phần 2: AI tránh vật cản (15 phút)

```scratch
Khi cờ xanh được nhấn
lặp mãi mãi
  quay về hướng (hướng đến [NguoiChoi v])
  di chuyển (3) bước
  nếu <chạm [VatCan v]?> thì
    quay về hướng ((hướng) + (90))
```

### Phần 3: AI patrol (15 phút)

```scratch
Khi cờ xanh được nhấn
đặt [diemDen v] thành [1]
lặp mãi mãi
  quay về hướng (hướng đến [DiemPatrol v])
  di chuyển (2) bước
  nếu <khoảng cách đến [DiemPatrol v] < [10]> thì
    đặt [diemDen v] thành ((diemDen) + (1))
    nếu <[diemDen v] > [2]> thì
      đặt [diemDen v] thành [1]
```

## 📝 Tổng kết

- **AI đuổi**: Đuổi theo người chơi
- **AI tránh**: Tránh vật cản
- **AI patrol**: Đi tuần tra

## 🔗 Liên kết

- **Bài trước**: [Bài 12A: Hệ thống vật phẩm](bai-giang-12a-he-thong-vat-pham.md)
- **Bài tiếp theo**: [Bài 12C: Hệ thống điểm & khó dần](bai-giang-12c-he-thong-diem-va-kho-dan.md)
- **Về topic**: [README.md](README.md)

---

**🌟 Chúc các em học tốt!**

