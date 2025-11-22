# Bài giảng 13C: Thiết kế thuật toán

## 📋 Thông tin bài học
- **Thời gian**: 90 phút
- **Độ tuổi**: 10-11 tuổi
- **Trình độ**: Nâng cao
- **Mục tiêu**: Học cách thiết kế thuật toán có hệ thống

## 🎯 Mục tiêu học tập

### Kiến thức
- Hiểu cách chia nhỏ vấn đề
- Nắm vững dự đoán kết quả
- Hiểu cách mô phỏng bằng giấy
- Biết cách vẽ sơ đồ thuật toán

### Kỹ năng
- Thiết kế thuật toán có hệ thống
- Chia nhỏ vấn đề phức tạp
- Mô phỏng và kiểm tra
- Vẽ sơ đồ thuật toán

## 🧠 Nội dung bài học

## 📚 PHẦN LÝ THUYẾT (45 phút)

### Phần 1: Chia nhỏ vấn đề (15 phút)

#### Hoạt động khởi động - "Chia nhỏ công việc"
- **Hoạt động**: Học sinh chia nhỏ công việc "nấu cơm"
- **Bước 1**: Vo gạo
- **Bước 2**: Nấu cơm
- **Bước 3**: Ăn cơm
- **Mục tiêu**: Hiểu cách chia nhỏ vấn đề

#### Khái niệm chia nhỏ
- **Định nghĩa**: Chia vấn đề lớn thành các bước nhỏ
- **Ví dụ**: Tính tổng điểm → Đếm số học sinh → Tính trung bình
- **Ứng dụng**: Mọi thuật toán

### Phần 2: Dự đoán kết quả (15 phút)

#### Khái niệm dự đoán
- **Định nghĩa**: Nghĩ trước kết quả sẽ như thế nào
- **Ví dụ**: Tính tổng [1,2,3] → Kết quả = 6
- **Ứng dụng**: Kiểm tra code đúng

### Phần 3: Mô phỏng bằng giấy (15 phút)

#### Khái niệm mô phỏng
- **Định nghĩa**: Chạy thuật toán bằng tay trên giấy
- **Ví dụ**: Tính tổng bằng cách viết từng bước
- **Ứng dụng**: Hiểu rõ thuật toán trước khi code

## 💻 PHẦN THỰC HÀNH (45 phút)

### Phần 1: Thiết kế thuật toán "Tìm số lớn nhất" (15 phút)

#### Bước 1: Chia nhỏ vấn đề
```
1. Duyệt qua từng số
2. So sánh với số lớn nhất hiện tại
3. Cập nhật nếu lớn hơn
4. Trả về số lớn nhất
```

#### Bước 2: Mô phỏng bằng giấy
```
Danh sách: [8, 9, 7, 10, 6]
Max = 8 (số đầu tiên)

Bước 1: So sánh 8 và 9 → Max = 9
Bước 2: So sánh 9 và 7 → Max = 9
Bước 3: So sánh 9 và 10 → Max = 10
Bước 4: So sánh 10 và 6 → Max = 10

Kết quả: 10
```

### Phần 2: Vẽ sơ đồ thuật toán (15 phút)

```
Bắt đầu
  ↓
Đặt max = số đầu tiên
  ↓
Duyệt qua từng số
  ↓
Số hiện tại > max?
  ├─ Có → Cập nhật max
  └─ Không → Tiếp tục
  ↓
Còn số nữa?
  ├─ Có → Quay lại duyệt
  └─ Không → Trả về max
  ↓
Kết thúc
```

### Phần 3: Lập trình từ thiết kế (15 phút)

```scratch
# Lập trình theo thiết kế
Khi cờ xanh được nhấn
đặt [max v] thành (mục (1) của [DanhSach v])
đặt [i v] thành [2]
lặp lại ((chiều dài của [DanhSach v]) - (1)) lần
  nếu <(mục (i) của [DanhSach v]) > [max v]> thì
    đặt [max v] thành (mục (i) của [DanhSach v])
  thay đổi [i v] bởi (1)
nói [Số lớn nhất: ] + [max v] trong (3) giây
```

## 📝 Tổng kết

- **Chia nhỏ**: Chia vấn đề lớn thành bước nhỏ
- **Dự đoán**: Nghĩ trước kết quả
- **Mô phỏng**: Chạy bằng tay trước
- **Sơ đồ**: Vẽ để hiểu rõ

## 🔗 Liên kết

- **Bài trước**: [Bài 13B: Debug — Tìm lỗi](bai-giang-13b-debug-tim-loi.md)
- **Chuyển sang Python**: [../../python/README.md](../../python/README.md)
- **Về topic**: [README.md](README.md)

---

**🌟 Chúc các em học tốt và sẵn sàng chuyển sang Python!**

