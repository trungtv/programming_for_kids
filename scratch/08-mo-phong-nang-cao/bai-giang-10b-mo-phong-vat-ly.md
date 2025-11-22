# Bài giảng 10B: Mô phỏng vật lý nâng cao

## 📋 Thông tin bài học
- **Thời gian**: 90 phút
- **Độ tuổi**: 10-11 tuổi
- **Trình độ**: Nâng cao
- **Mục tiêu**: Mô phỏng các hiện tượng vật lý phức tạp

## 🎯 Mục tiêu học tập

### Kiến thức
- Hiểu khái niệm trọng lực nâng cao
- Nắm vững bật nảy với ma sát
- Hiểu quán tính và vận tốc
- Biết cách mô phỏng chuyển động thực tế

### Kỹ năng
- Lập trình trọng lực nâng cao
- Xử lý ma sát và bật nảy
- Tính toán vận tốc và quán tính
- Tạo mô phỏng vật lý chân thực

## 🧠 Nội dung bài học

## 📚 PHẦN LÝ THUYẾT (45 phút)

### Phần 1: Trọng lực nâng cao (15 phút)

#### Hoạt động khởi động - "Quan sát vật rơi"
- **Hoạt động**: Học sinh quan sát vật rơi
- **Câu hỏi**: "Vật rơi nhanh dần hay chậm dần?"
- **Kết nối**: "Chúng ta sẽ mô phỏng trọng lực nâng cao"
- **Mục tiêu**: Hiểu trọng lực làm vật rơi nhanh dần

#### Khái niệm trọng lực nâng cao
- **Trọng lực cơ bản**: Vật rơi với tốc độ không đổi
- **Trọng lực nâng cao**: Vật rơi nhanh dần (tăng tốc)
- **Công thức đơn giản**: Vận tốc = Vận tốc cũ + Trọng lực

### Phần 2: Bật nảy với ma sát (15 phút)

#### Hoạt động không máy tính - "Quan sát bóng bật"
- **Hoạt động**: Học sinh quan sát bóng bật
- **Câu hỏi**: "Tại sao bóng bật thấp dần?"
- **Kết nối**: "Ma sát làm bóng mất năng lượng"
- **Mục tiêu**: Hiểu ma sát ảnh hưởng đến bật nảy

#### Khái niệm ma sát và bật nảy
- **Bật nảy cơ bản**: Bóng bật với cùng vận tốc
- **Bật nảy với ma sát**: Bóng bật thấp dần (mất năng lượng)
- **Công thức**: Vận tốc mới = Vận tốc cũ × Hệ số ma sát

### Phần 3: Quán tính và vận tốc (15 phút)

#### Khái niệm quán tính
- **Định nghĩa**: Quán tính là xu hướng vật tiếp tục chuyển động
- **Vận tốc**: Tốc độ và hướng chuyển động
- **Ứng dụng**: Mô phỏng chuyển động tự nhiên

## 💻 PHẦN THỰC HÀNH (45 phút)

### Phần 1: Tạo mô phỏng trọng lực nâng cao (15 phút)

```scratch
Khi cờ xanh được nhấn
đặt [vanTocY v] thành [0]
lặp mãi mãi
  thay đổi [vanTocY v] bởi [0.5]  # Trọng lực
  thay đổi y bởi (vanTocY)
  nếu <y < [-180]> thì
    đặt y thành [-180]
    đặt [vanTocY v] thành ((vanTocY) * (-0.8))  # Bật nảy
```

### Phần 2: Tạo mô phỏng bật nảy với ma sát (15 phút)

```scratch
Khi cờ xanh được nhấn
đặt [vanTocY v] thành [10]
lặp mãi mãi
  thay đổi [vanTocY v] bởi [0.5]  # Trọng lực
  thay đổi y bởi (vanTocY)
  nếu <y < [-180]> thì
    đặt y thành [-180]
    đặt [vanTocY v] thành ((vanTocY) * (-0.7))  # Ma sát
    nếu <[vanTocY v] < [1]> thì
      dừng tất cả
```

### Phần 3: Tạo mô phỏng quán tính (15 phút)

```scratch
Khi cờ xanh được nhấn
đặt [vanTocX v] thành [5]
đặt [vanTocY v] thành [0]
lặp mãi mãi
  thay đổi x bởi (vanTocX)
  thay đổi [vanTocX v] bởi [-0.1]  # Ma sát ngang
  thay đổi [vanTocY v] bởi [0.5]  # Trọng lực
  thay đổi y bởi (vanTocY)
  nếu <chạm cạnh?> thì
    quay lại (180) độ
```

## 🎨 Hoạt động mở rộng

- **Game vật lý**: Tạo game dựa trên vật lý
- **Mô phỏng phức tạp**: Kết hợp nhiều hiện tượng vật lý
- **Dự án tích hợp**: Kết hợp với các bài học khác

## 📝 Tổng kết

- **Trọng lực nâng cao**: Vật rơi nhanh dần
- **Bật nảy với ma sát**: Mất năng lượng khi bật
- **Quán tính**: Vật tiếp tục chuyển động

## 🔗 Liên kết

- **Bài trước**: [Bài 10A: Mô phỏng nhiều đối tượng](bai-giang-10a-mo-phong-nhieu-doi-tuong.md)
- **Bài tiếp theo**: [Bài 10C: Mô phỏng hệ thống](bai-giang-10c-mo-phong-he-thong.md)
- **Về topic**: [README.md](README.md)

---

**🌟 Chúc các em học tốt!**

