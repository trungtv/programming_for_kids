# Bài giảng 12C: Hệ thống điểm & khó dần

## 📋 Thông tin bài học
- **Thời gian**: 90 phút
- **Độ tuổi**: 10-11 tuổi
- **Trình độ**: Nâng cao
- **Mục tiêu**: Tạo hệ thống game loop phức tạp

## 🎯 Mục tiêu học tập

### Kiến thức
- Hiểu cách tăng tốc độ theo thời gian
- Nắm vững sinh vật xuất hiện nhiều dần
- Hiểu game loop phức tạp
- Biết cách cân bằng độ khó

### Kỹ năng
- Tạo hệ thống độ khó động
- Quản lý game loop
- Cân bằng game
- Tạo game hoàn chỉnh

## 🧠 Nội dung bài học

## 📚 PHẦN LÝ THUYẾT (45 phút)

### Phần 1: Tăng tốc độ theo thời gian (15 phút)

#### Khái niệm độ khó động
- **Quy tắc**: Tốc độ tăng dần theo thời gian
- **Công thức**: Tốc độ = Tốc độ cơ bản + (Thời gian × Hệ số)
- **Ứng dụng**: Game arcade, game survival

### Phần 2: Sinh vật xuất hiện nhiều dần (15 phút)

#### Khái niệm spawn rate
- **Quy tắc**: Sinh vật xuất hiện nhanh hơn theo thời gian
- **Công thức**: Thời gian spawn = Thời gian cơ bản - (Thời gian × Hệ số)
- **Ứng dụng**: Game wave, game survival

### Phần 3: Game loop phức tạp (15 phút)

#### Khái niệm game loop
- **Quy tắc**: Lặp lại các bước: Update → Render → Input
- **Công thức**: Kết hợp nhiều hệ thống
- **Ứng dụng**: Mọi game

## 💻 PHẦN THỰC HÀNH (45 phút)

### Phần 1: Tăng tốc độ (15 phút)

```scratch
Khi cờ xanh được nhấn
đặt [thoiGian v] thành [0]
đặt [tocDo v] thành [3]
lặp mãi mãi
  thay đổi [thoiGian v] bởi (1)
  đặt [tocDo v] thành ((3) + ((thoiGian) / (10)))
  di chuyển (tocDo) bước
```

### Phần 2: Sinh vật xuất hiện (15 phút)

```scratch
Khi cờ xanh được nhấn
đặt [thoiGianSpawn v] thành [3]
lặp mãi mãi
  đợi (thoiGianSpawn) giây
  tạo bản sao của [KeThu v]
  thay đổi [thoiGianSpawn v] bởi (-0.1)
  nếu <[thoiGianSpawn v] < [0.5]> thì
    đặt [thoiGianSpawn v] thành [0.5]
```

### Phần 3: Game loop (15 phút)

```scratch
Khi cờ xanh được nhấn
lặp mãi mãi
  # Update
  thay đổi [diem v] bởi (1)
  # Render
  nói [Điểm: ] + [diem v] trong (0.1) giây
  # Input (xử lý trong sprite khác)
```

## 📝 Tổng kết

- **Độ khó động**: Tăng dần theo thời gian
- **Spawn rate**: Sinh vật xuất hiện nhanh hơn
- **Game loop**: Update → Render → Input

## 🔗 Liên kết

- **Bài trước**: [Bài 12B: AI đơn giản cho kẻ thù](bai-giang-12b-ai-ke-thu.md)
- **Bài tiếp theo**: [Bài 13A: Hàm có tham số nâng cao](../11-tu-duy-may-tinh/bai-giang-13a-ham-tham-so-nang-cao.md)
- **Về topic**: [README.md](README.md)

---

**🌟 Chúc các em học tốt!**

