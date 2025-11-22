# Bài giảng 10A: Mô phỏng nhiều đối tượng tương tác

## 📋 Thông tin bài học
- **Thời gian**: 90 phút
- **Độ tuổi**: 10-11 tuổi
- **Trình độ**: Nâng cao
- **Mục tiêu**: Hiểu cách mô phỏng nhiều đối tượng tương tác với nhau

## 🎯 Mục tiêu học tập

### Kiến thức
- Hiểu khái niệm mô phỏng bầy đàn (Boids - phiên bản đơn giản)
- Nắm vững mô phỏng va chạm giữa nhiều vật
- Hiểu cách mô phỏng lan truyền (virus / lửa / nước)
- Biết cách từ quy luật đơn giản tạo ra hành vi phức tạp

### Kỹ năng
- Tạo nhiều clone tương tác với nhau
- Thiết kế quy luật hành vi cho đối tượng
- Sử dụng broadcast để đồng bộ
- Tạo mô phỏng phức tạp

### Thái độ
- Phát triển tư duy mô phỏng
- Rèn luyện tính kiên trì
- Khuyến khích tư duy hệ thống

## 🧠 Nội dung bài học

## 📚 PHẦN LÝ THUYẾT (45 phút)

### Phần 1: Khái niệm mô phỏng bầy đàn (20 phút)

#### Hoạt động khởi động - "Quan sát đàn chim"
- **Hoạt động**: Học sinh quan sát video đàn chim bay
- **Câu hỏi**: "Tại sao đàn chim bay cùng nhau mà không va chạm?"
- **Kết nối**: "Chúng ta sẽ tạo mô phỏng đàn chim bằng Scratch"
- **Mục tiêu**: Hiểu khái niệm mô phỏng bầy đàn

#### Khái niệm Boids (Birds + Doids) qua ví dụ thực tế
- **Định nghĩa**: Boids là mô phỏng hành vi của bầy đàn dựa trên 3 quy tắc đơn giản
- **3 quy tắc cơ bản**:
  1. **Separation** (Tách biệt): Tránh va chạm với đối tượng gần
  2. **Alignment** (Căn chỉnh): Di chuyển theo hướng của đối tượng gần
  3. **Cohesion** (Gắn kết): Di chuyển về phía trung tâm của nhóm
- **Ví dụ thực tế**: Đàn chim, bầy cá, đàn ong

#### Hoạt động không máy tính - "Mô phỏng đàn chim bằng người"
- **Hoạt động**: Học sinh đóng vai đàn chim, di chuyển theo 3 quy tắc
- **Quy tắc 1**: Không được quá gần bạn bên cạnh (Separation)
- **Quy tắc 2**: Di chuyển theo hướng của bạn gần nhất (Alignment)
- **Quy tắc 3**: Di chuyển về phía trung tâm nhóm (Cohesion)
- **Kết quả**: Nhận ra từ quy tắc đơn giản tạo ra hành vi phức tạp

### Phần 2: Mô phỏng va chạm (15 phút)

#### Hoạt động không máy tính - "Bóng va chạm"
- **Hoạt động**: Học sinh quan sát bóng va chạm
- **Câu hỏi**: "Điều gì xảy ra khi 2 bóng va chạm?"
- **Kết nối**: "Chúng ta sẽ mô phỏng va chạm bằng Scratch"
- **Mục tiêu**: Hiểu khái niệm va chạm

#### Khái niệm va chạm qua ví dụ thực tế
- **Định nghĩa**: Va chạm là khi 2 đối tượng chạm vào nhau
- **Ví dụ thực tế**: 
  - Bóng va chạm
  - Xe va chạm
  - Người va chạm
- **Ứng dụng**: Game, mô phỏng vật lý

### Phần 3: Mô phỏng lan truyền (10 phút)

#### Hoạt động không máy tính - "Lan truyền lửa"
- **Hoạt động**: Học sinh quan sát lửa lan truyền
- **Câu hỏi**: "Lửa lan truyền như thế nào?"
- **Kết nối**: "Chúng ta sẽ mô phỏng lan truyền bằng Scratch"
- **Mục tiêu**: Hiểu khái niệm lan truyền

#### Khái niệm lan truyền qua ví dụ thực tế
- **Định nghĩa**: Lan truyền là quá trình một trạng thái lan từ đối tượng này sang đối tượng khác
- **Ví dụ thực tế**: 
  - Lửa lan truyền
  - Virus lan truyền
  - Nước lan truyền
- **Ứng dụng**: Mô phỏng dịch bệnh, mô phỏng cháy rừng

## 💻 PHẦN THỰC HÀNH (45 phút)

### Phần 1: Tạo mô phỏng đàn chim đơn giản (20 phút)

#### Bước 1: Tạo sprite chim và clone
```scratch
Khi cờ xanh được nhấn
tạo bản sao của [bản thân v]
tạo bản sao của [bản thân v]
tạo bản sao của [bản thân v]
tạo bản sao của [bản thân v]
```

#### Bước 2: Lập trình hành vi cho chim
```scratch
Khi tôi là bản sao
lặp mãi mãi
  # Quy tắc 1: Separation - Tránh va chạm
  nếu <khoảng cách đến [Chim v] < [30]> thì
    quay về hướng ((hướng) + (180))
  
  # Quy tắc 2: Alignment - Di chuyển theo hướng
  quay về hướng (hướng của [Chim v] gần nhất)
  
  # Quy tắc 3: Cohesion - Di chuyển về trung tâm
  quay về hướng (hướng đến [Chim v] gần nhất)
  
  di chuyển (2) bước
  nếu <chạm cạnh?> thì
    quay lại (180) độ
```

### Phần 2: Tạo mô phỏng va chạm (15 phút)

#### Bước 1: Tạo sprite bóng
```scratch
Khi cờ xanh được nhấn
tạo bản sao của [bản thân v]
tạo bản sao của [bản thân v]
```

#### Bước 2: Lập trình va chạm
```scratch
Khi tôi là bản sao
lặp mãi mãi
  di chuyển (5) bước
  nếu <chạm cạnh?> thì
    quay lại (180) độ
  
  nếu <chạm [Bóng v]?> thì
    quay lại (180) độ
    phát âm thanh [pop v]
```

### Phần 3: Tạo mô phỏng lan truyền (10 phút)

#### Bước 1: Tạo sprite và trạng thái
```scratch
# Tạo biến "trangThai" (0 = bình thường, 1 = bị lây)
```

#### Bước 2: Lập trình lan truyền
```scratch
Khi tôi là bản sao
đặt [trangThai v] thành [0]
lặp mãi mãi
  nếu <[trangThai v] = [0]> thì
    nếu <khoảng cách đến [Virus v] < [50]> thì
      đặt [trangThai v] thành [1]
      thay đổi màu hiệu ứng bởi (50)
```

## 🎨 Hoạt động mở rộng

### Cấp độ 1: Thêm tính năng cơ bản
- **Thêm nhiều đối tượng**: Tạo nhiều clone hơn
- **Thay đổi tốc độ**: Mỗi đối tượng có tốc độ khác nhau
- **Thêm màu sắc**: Mỗi đối tượng có màu khác nhau

### Cấp độ 2: Tính năng nâng cao
- **Mô phỏng phức tạp**: Kết hợp nhiều quy tắc
- **Thêm vật cản**: Đối tượng tránh vật cản
- **Mô phỏng thực tế**: Mô phỏng giao thông, đám đông

### Cấp độ 3: Sáng tạo
- **Game mô phỏng**: Tạo game dựa trên mô phỏng
- **Hệ thống mô phỏng**: Kết hợp nhiều loại mô phỏng
- **Dự án tích hợp**: Kết hợp với các bài học khác

## 📝 Tổng kết kiến thức

### Kiến thức đã học
- **Mô phỏng bầy đàn**: 3 quy tắc cơ bản (Separation, Alignment, Cohesion)
- **Mô phỏng va chạm**: Xử lý va chạm giữa nhiều đối tượng
- **Mô phỏng lan truyền**: Lan truyền trạng thái từ đối tượng này sang đối tượng khác
- **Tư duy hệ thống**: Từ quy luật đơn giản tạo ra hành vi phức tạp

## 🔗 Liên kết

- **Bài trước**: [Bài 9C: Thuật toán thống kê nâng cao](../07-thuat-toan-du-lieu-nang-cao/bai-giang-9c-thuat-toan-thong-ke.md)
- **Bài tiếp theo**: [Bài 10B: Mô phỏng vật lý nâng cao](bai-giang-10b-mo-phong-vat-ly.md)
- **Bài liên quan**: [Bài 3: Trò chơi "Bảo vệ đảo"](../03-game-va-ung-dung/bai-giang-3-bao-ve-dao.md)
- **Về topic**: [README.md](README.md)

---

**🌟 Chúc các em học tốt và sáng tạo!**

