# Bài giảng 12A: Hệ thống vật phẩm / Inventory

## 📋 Thông tin bài học
- **Thời gian**: 90 phút
- **Độ tuổi**: 10-11 tuổi
- **Trình độ**: Nâng cao
- **Mục tiêu**: Tạo hệ thống quản lý vật phẩm trong game

## 🎯 Mục tiêu học tập

### Kiến thức
- Hiểu cách tạo hệ thống inventory
- Nắm vững thêm/xóa item vào list
- Hiểu cách kiểm tra có item hay không
- Biết cách sử dụng item

### Kỹ năng
- Tạo hệ thống inventory hoàn chỉnh
- Quản lý danh sách vật phẩm
- Xử lý thêm/xóa item
- Tạo giao diện inventory

## 🧠 Nội dung bài học

## 📚 PHẦN LÝ THUYẾT (45 phút)

### Phần 1: Khái niệm inventory (20 phút)

#### Hoạt động không máy tính - "Quản lý đồ vật"
- **Hoạt động**: Học sinh liệt kê đồ vật trong túi
- **Câu hỏi**: "Làm sao để biết có đồ vật gì?"
- **Kết nối**: "Chúng ta sẽ tạo hệ thống inventory"
- **Mục tiêu**: Hiểu khái niệm inventory

#### Khái niệm Inventory
- **Định nghĩa**: Danh sách vật phẩm người chơi có
- **Chức năng**:
  1. Thêm item
  2. Xóa item
  3. Kiểm tra có item
  4. Sử dụng item
- **Ứng dụng**: Game RPG, game phiêu lưu

## 💻 PHẦN THỰC HÀNH (45 phút)

### Phần 1: Tạo danh sách inventory (15 phút)

```scratch
# Tạo list "Inventory"
# Ban đầu rỗng
```

### Phần 2: Thêm/xóa item (15 phút)

```scratch
# Thêm item
Khi nhận được [themItem v]
thêm [item] vào [Inventory v]

# Xóa item
Khi nhận được [xoaItem v]
xóa (mục (1) của [Inventory v]) khỏi [Inventory v]
```

### Phần 3: Kiểm tra và sử dụng item (15 phút)

```scratch
# Kiểm tra có item
đặt [i v] thành [1]
đặt [coItem v] thành [0]
lặp lại (chiều dài của [Inventory v]) lần
  nếu <(mục (i) của [Inventory v]) = [item]> thì
    đặt [coItem v] thành [1]
  thay đổi [i v] bởi (1)

# Sử dụng item
nếu <[coItem v] = [1]> thì
  xóa [item] khỏi [Inventory v]
  nói [Đã sử dụng item!] trong (2) giây
```

## 📝 Tổng kết

- **Inventory**: Danh sách vật phẩm
- **Thêm/xóa**: Quản lý item
- **Kiểm tra**: Xem có item không
- **Sử dụng**: Dùng item

## 🔗 Liên kết

- **Bài trước**: [Bài 11C: Tìm đường bằng cảm biến](../09-tim-duong/bai-giang-11c-tim-duong-bang-cam-bien.md)
- **Bài tiếp theo**: [Bài 12B: AI đơn giản cho kẻ thù](bai-giang-12b-ai-ke-thu.md)
- **Về topic**: [README.md](README.md)

---

**🌟 Chúc các em học tốt!**

