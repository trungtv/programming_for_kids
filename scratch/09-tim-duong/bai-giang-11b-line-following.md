# Bài giảng 11B: Line Following Robot

## 📋 Thông tin bài học
- **Thời gian**: 90 phút
- **Độ tuổi**: 10-11 tuổi
- **Trình độ**: Nâng cao
- **Mục tiêu**: Học cách robot đi theo đường vẽ

## 🎯 Mục tiêu học tập

### Kiến thức
- Hiểu cách robot đi theo đường vẽ
- Nắm vững điều chỉnh khi lệch đường
- Hiểu cách xử lý góc cua và đường cong
- Biết ứng dụng vào robot công nghiệp

### Kỹ năng
- Lập trình robot đi theo đường
- Xử lý cảm biến màu
- Điều chỉnh hướng khi lệch
- Tạo đường vẽ và robot

## 🧠 Nội dung bài học

## 📚 PHẦN LÝ THUYẾT (45 phút)

### Phần 1: Khái niệm đi theo đường (20 phút)

#### Hoạt động không máy tính - "Đi theo đường vẽ"
- **Hoạt động**: Học sinh vẽ đường, đi theo đường bằng tay
- **Quy tắc**: Luôn giữ chân trên đường
- **Kết quả**: Đi được theo đường
- **Mục tiêu**: Hiểu khái niệm đi theo đường

#### Khái niệm Line Following
- **Định nghĩa**: Robot đi theo đường vẽ sẵn
- **Quy tắc**:
  1. Kiểm tra màu dưới chân
  2. Nếu trên đường (màu đen), đi thẳng
  3. Nếu lệch trái, rẽ phải
  4. Nếu lệch phải, rẽ trái
- **Ứng dụng**: Robot công nghiệp, xe tự lái

### Phần 2: Thuật toán điều chỉnh (25 phút)

#### Hoạt động không máy tính - "Mô phỏng điều chỉnh"
- **Hoạt động**: Học sinh mô phỏng điều chỉnh khi lệch
- **Bước 1**: Kiểm tra vị trí
- **Bước 2**: Nếu lệch, điều chỉnh hướng
- **Bước 3**: Tiếp tục đi
- **Mục tiêu**: Hiểu cách điều chỉnh

## 💻 PHẦN THỰC HÀNH (45 phút)

### Phần 1: Tạo đường vẽ (15 phút)

```scratch
# Tạo backdrop với đường màu đen
# Vẽ đường cong, có góc cua
```

### Phần 2: Lập trình robot đi theo đường (30 phút)

```scratch
Khi cờ xanh được nhấn
lặp mãi mãi
  nếu <chạm màu [#000000]?> thì
    # Đang trên đường, đi thẳng
    di chuyển (2) bước
  không thì
    # Lệch đường, tìm đường
    quay về hướng ((hướng) + (5))  # Rẽ phải
    di chuyển (1) bước
    nếu <chạm màu [#000000]?> thì
      # Tìm thấy đường bên phải
      di chuyển (2) bước
    không thì
      # Không tìm thấy, rẽ trái
      quay về hướng ((hướng) - (10))
      di chuyển (1) bước
```

## 📝 Tổng kết

- **Line Following**: Robot đi theo đường vẽ
- **Điều chỉnh**: Rẽ khi lệch đường
- **Ứng dụng**: Robot công nghiệp, xe tự lái

## 🔗 Liên kết

- **Bài trước**: [Bài 11A: Wall Follower](bai-giang-11a-wall-follower.md)
- **Bài tiếp theo**: [Bài 11C: Tìm đường bằng cảm biến](bai-giang-11c-tim-duong-bang-cam-bien.md)
- **Về topic**: [README.md](README.md)

---

**🌟 Chúc các em học tốt!**

