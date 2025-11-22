# Bài giảng 10C: Mô phỏng hệ thống

## 📋 Thông tin bài học
- **Thời gian**: 90 phút
- **Độ tuổi**: 10-11 tuổi
- **Trình độ**: Nâng cao
- **Mục tiêu**: Mô phỏng các hệ thống thực tế

## 🎯 Mục tiêu học tập

### Kiến thức
- Hiểu cách mô phỏng giao thông (xe tránh nhau)
- Nắm vững mô phỏng robot hút bụi
- Hiểu cách mô phỏng cửa tự động
- Biết cách kết hợp nhiều khái niệm

### Kỹ năng
- Thiết kế hệ thống mô phỏng
- Kết hợp nhiều quy tắc
- Sử dụng broadcast và sensing
- Tạo mô phỏng thực tế

## 🧠 Nội dung bài học

## 📚 PHẦN LÝ THUYẾT (45 phút)

### Phần 1: Mô phỏng giao thông (15 phút)

#### Hoạt động không máy tính - "Quan sát giao thông"
- **Hoạt động**: Học sinh quan sát xe tránh nhau
- **Câu hỏi**: "Xe làm sao để tránh nhau?"
- **Kết nối**: "Chúng ta sẽ mô phỏng giao thông"
- **Mục tiêu**: Hiểu quy tắc tránh va chạm

### Phần 2: Mô phỏng robot hút bụi (15 phút)

#### Hoạt động không máy tính - "Quan sát robot"
- **Hoạt động**: Học sinh quan sát robot hút bụi
- **Câu hỏi**: "Robot làm sao để hút bụi?"
- **Kết nối**: "Chúng ta sẽ mô phỏng robot"
- **Mục tiêu**: Hiểu quy tắc di chuyển và làm sạch

### Phần 3: Mô phỏng cửa tự động (15 phút)

#### Hoạt động không máy tính - "Quan sát cửa tự động"
- **Hoạt động**: Học sinh quan sát cửa tự động
- **Câu hỏi**: "Cửa tự động hoạt động như thế nào?"
- **Kết nối**: "Chúng ta sẽ mô phỏng cửa tự động"
- **Mục tiêu**: Hiểu quy tắc cảm biến và phản ứng

## 💻 PHẦN THỰC HÀNH (45 phút)

### Phần 1: Mô phỏng giao thông (15 phút)

```scratch
Khi cờ xanh được nhấn
lặp mãi mãi
  di chuyển (3) bước
  nếu <khoảng cách đến [Xe v] < [50]> thì
    quay về hướng ((hướng) + (90))
  nếu <chạm cạnh?> thì
    quay lại (180) độ
```

### Phần 2: Mô phỏng robot hút bụi (15 phút)

```scratch
Khi cờ xanh được nhấn
lặp mãi mãi
  di chuyển (2) bước
  nếu <chạm [Bui v]?> thì
    xóa bản sao của [Bui v]
    thay đổi [Diem v] bởi (1)
  nếu <chạm cạnh?> thì
    quay lại (180) độ
```

### Phần 3: Mô phỏng cửa tự động (15 phút)

```scratch
Khi cờ xanh được nhấn
lặp mãi mãi
  nếu <khoảng cách đến [Nguoi v] < [100]> thì
    thay đổi y bởi (5)  # Mở cửa
  không thì
    thay đổi y bởi (-5)  # Đóng cửa
```

## 📝 Tổng kết

- **Mô phỏng giao thông**: Xe tránh nhau
- **Mô phỏng robot**: Robot hút bụi
- **Mô phỏng cửa tự động**: Cảm biến và phản ứng

## 🔗 Liên kết

- **Bài trước**: [Bài 10B: Mô phỏng vật lý](bai-giang-10b-mo-phong-vat-ly.md)
- **Bài tiếp theo**: [Bài 11A: Wall Follower](../09-tim-duong/bai-giang-11a-wall-follower.md)
- **Về topic**: [README.md](README.md)

---

**🌟 Chúc các em học tốt!**

