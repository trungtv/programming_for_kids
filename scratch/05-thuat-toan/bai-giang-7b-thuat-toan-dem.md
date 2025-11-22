# Bài giảng 7B: Thuật toán đếm

## 📋 Thông tin bài học
- **Thời gian**: 90 phút
- **Độ tuổi**: 10-11 tuổi
- **Trình độ**: Trung bình
- **Mục tiêu**: Hiểu và áp dụng thuật toán đếm số phần tử theo điều kiện

## 🎯 Mục tiêu học tập

### Kiến thức
- Hiểu khái niệm thuật toán đếm
- Nắm vững thuật toán đếm số phần tử
- Hiểu cách đếm với điều kiện
- Biết cách áp dụng thuật toán đếm vào thực tế

### Kỹ năng
- Phân tích và giải quyết vấn đề có hệ thống
- Áp dụng thuật toán vào lập trình Scratch
- Sử dụng biến và vòng lặp hiệu quả
- Debug và tối ưu hóa code

### Thái độ
- Phát triển tư duy logic
- Rèn luyện tính kiên trì
- Khuyến khích tư duy phản biện

## 🧠 Nội dung bài học

## 📚 PHẦN LÝ THUYẾT (45 phút)

### Phần 1: Khái niệm thuật toán qua hoạt động không máy tính (20 phút)

#### Hoạt động khởi động - "Kết nối với cấu trúc dữ liệu"
- **Hoạt động**: Nhắc lại bài 6 về cấu trúc dữ liệu (danh sách Pokemon)
- **Câu hỏi**: "Chúng ta đã học cách tổ chức dữ liệu như thế nào?"
- **Kết nối**: "Hôm nay chúng ta sẽ học cách xử lý dữ liệu đã tổ chức"
- **Mục tiêu**: Kết nối cấu trúc dữ liệu với thuật toán

#### Khái niệm thuật toán qua ví dụ thực tế
- **Định nghĩa**: Thuật toán là tập hợp các bước rõ ràng để giải quyết một vấn đề
- **Ví dụ**: Công thức làm bánh sandwich
- **Input**: Nguyên liệu (bánh mì, bơ, thịt, rau)
- **Process**: Các bước chế biến (phết bơ, đặt thịt...)
- **Output**: Bánh sandwich hoàn chỉnh
- **Đặc điểm**: Các bước phải rõ ràng, có thứ tự, có thể lặp lại

#### Hoạt động thực hành - "Hướng dẫn bạn đi từ lớp đến thư viện"
- **Hoạt động**: Học sinh viết hướng dẫn chi tiết từ lớp đến thư viện
- **Mục tiêu**: Thực hành chia nhỏ vấn đề thành các bước
- **Kết quả**: Hiểu tầm quan trọng của thuật toán trong cuộc sống

### Phần 2: Thuật toán đếm (25 phút)

#### Hoạt động không máy tính - "Đếm số bạn trong lớp"
- **Hoạt động**: Học sinh đếm số bạn nam và nữ trong lớp
- **Mục tiêu**: Hiểu thuật toán đếm đơn giản
- **Quy tắc**: Đi từ đầu đến cuối lớp, đếm từng người một
- **Kết quả**: Nhận ra thuật toán đếm có thể áp dụng cho nhiều tình huống

#### Bài toán: Đếm số học sinh giỏi
- **Input**: Danh sách điểm [8, 9, 7, 10, 6]
- **Output**: Số học sinh có điểm >= 8 (3 học sinh)
- **Ví dụ**: Đếm số bạn đạt loại giỏi trong lớp

#### Thuật toán đếm qua ví dụ thực tế
```
Bước 1: Khởi tạo biến đếm = 0
Bước 2: Xem điểm của bạn đầu tiên (8)
Bước 3: Vì 8 >= 8, tăng biến đếm lên 1
Bước 4: Xem điểm của bạn tiếp theo (9)
Bước 5: Vì 9 >= 8, tăng biến đếm lên 2
Bước 6: Tiếp tục cho đến hết danh sách
```

## 💻 PHẦN THỰC HÀNH SCRATCH (45 phút)

### Phần 3: Tạo game "Đếm số học sinh giỏi" trên Scratch (30 phút)

#### Bước 1: Tạo các biến cần thiết
```scratch
# Tạo các biến sau:
1. Biến "DanhSachDiem" - danh sách điểm số (List)
2. Biến "SoHocSinhGioi" - đếm số học sinh giỏi
3. Biến "ViTri" - chỉ số vị trí hiện tại
```

#### Bước 2: Lập trình thuật toán đếm
```scratch
Khi cờ xanh được nhấn
# Khởi tạo danh sách điểm
xóa tất cả trong [DanhSachDiem v]
thêm [8] vào [DanhSachDiem v]
thêm [9] vào [DanhSachDiem v]
thêm [7] vào [DanhSachDiem v]
thêm [10] vào [DanhSachDiem v]
thêm [6] vào [DanhSachDiem v]

# Hiển thị danh sách
nói [Danh sách điểm: ] + [DanhSachDiem v] trong (3) giây
chờ (1) giây

# Khởi tạo biến đếm
đặt [SoHocSinhGioi v] thành (0)
đặt [ViTri v] thành (1)
nói [Bắt đầu đếm học sinh giỏi (điểm >= 8)...] trong (2) giây

# Duyệt qua danh sách và đếm
lặp lại (chiều dài của [DanhSachDiem v]) lần
  nếu <(mục (ViTri) của [DanhSachDiem v]) >= [8]> thì
    thay đổi [SoHocSinhGioi v] bởi (1)
    phát âm thanh [pop v]
    nói [Tìm thấy học sinh giỏi! Điểm: ] + (mục (ViTri) của [DanhSachDiem v]) + [. Tổng: ] + [SoHocSinhGioi v] trong (2) giây
  nếu không
    nói [Điểm ] + (mục (ViTri) của [DanhSachDiem v]) + [ không đạt loại giỏi] trong (1) giây
  thay đổi [ViTri v] bởi (1)
  chờ (0.5) giây

# Kết quả
nói [=== KẾT QUẢ ===] trong (2) giây
nói [Số học sinh giỏi (điểm >= 8): ] + [SoHocSinhGioi v] trong (3) giây
```

#### Hoạt động mở rộng - "Đếm với điều kiện khác"
- **Hoạt động**: Thay đổi điều kiện đếm (ví dụ: điểm >= 9)
- **Mục tiêu**: Hiểu cách điều chỉnh điều kiện trong thuật toán
- **Thử thách**: Đếm nhiều loại học sinh cùng lúc (giỏi, khá, trung bình)

## 🎯 Tổng kết và đánh giá (10 phút)

### Tổng kết kiến thức
- **Thuật toán đếm**: Duyệt qua danh sách và đếm theo điều kiện
- **Khởi tạo biến đếm**: Bắt đầu từ 0
- **Điều kiện đếm**: Kiểm tra điều kiện trước khi tăng biến đếm
- **Ứng dụng**: Đếm có mặt khắp nơi trong cuộc sống (đếm học sinh giỏi, đếm số chẵn, v.v.)

### Đánh giá học sinh
- **Hiểu thuật toán**: Có thể giải thích các bước của thuật toán đếm
- **Áp dụng thực tế**: Tìm được ví dụ đếm trong cuộc sống
- **Lập trình Scratch**: Tạo được chương trình đếm với điều kiện
- **Tư duy logic**: Phân tích và giải quyết vấn đề có hệ thống

## 🎨 Hoạt động mở rộng

### Cấp độ 1: Thêm tính năng cơ bản
- **Giao diện tương tác**: Tạo nút để nhập dữ liệu mới
- **Hiệu ứng trực quan**: Thêm màu sắc và animation khi thực hiện thuật toán
- **Âm thanh**: Tạo âm thanh khác nhau cho từng loại thuật toán

### Cấp độ 2: Tính năng nâng cao
- **Tìm kiếm thông minh**: Tìm kiếm với nhiều điều kiện
- **Đếm phức tạp**: Đếm nhiều loại cùng lúc
- **So sánh hiệu suất**: So sánh tốc độ của các thuật toán khác nhau

### Cấp độ 3: Sáng tạo
- **Game thuật toán**: Tạo trò chơi đếm với nhiều điều kiện
- **Thuật toán riêng**: Thiết kế thuật toán đếm giải quyết vấn đề thực tế
- **Dự án tích hợp**: Kết hợp đếm với các thuật toán khác

## 📝 Bài tập về nhà

### Bài tập bắt buộc
1. **Đếm học sinh giỏi**: Viết thuật toán đếm số học sinh có điểm >= 8 trong 7 điểm số
2. **Đếm học sinh khá**: Tạo chương trình đếm số học sinh có điểm >= 7
3. **Đếm số chẵn**: Tạo chương trình đếm số chẵn trong danh sách

### Bài tập nâng cao
1. **Đếm nhiều loại**: Đếm đồng thời số học sinh giỏi, khá, trung bình
2. **Đếm với nhiều điều kiện**: Đếm số học sinh có điểm từ 7 đến 9
3. **Thống kê cơ bản**: Kết hợp đếm với tính tổng và trung bình

### Bài tập sáng tạo
1. **Game điểm số**: Tạo game cho phép nhập điểm và đếm theo nhiều tiêu chí
2. **Thuật toán riêng**: Thiết kế thuật toán đếm giải quyết vấn đề trong lớp học
3. **Dự án tích hợp**: Kết hợp đếm với các thuật toán khác (tìm max, tính tổng)

## 🔧 Tài nguyên hỗ trợ

### Tài liệu tham khảo
- **Scratch Programming**: Hướng dẫn lập trình Scratch cơ bản
- **Algorithm Visualization**: Công cụ minh họa thuật toán
- **Unplugged Activities**: Hoạt động không máy tính cho thuật toán

### Công cụ hỗ trợ
- **Scratch Editor**: Môi trường lập trình trực quan
- **Algorithm Simulator**: Mô phỏng thuật toán
- **Debugging Tools**: Công cụ gỡ lỗi và tối ưu hóa

### Đánh giá và phản hồi
- **Rubric đánh giá**: Tiêu chí đánh giá kỹ năng thuật toán
- **Peer Review**: Đánh giá lẫn nhau giữa học sinh
- **Portfolio**: Tập hợp các dự án và bài tập của học sinh

## 🔗 Kết nối với bài học khác

### Kiến thức liên quan
- **Bài 6**: Cấu trúc dữ liệu - Sử dụng danh sách (List)
- **Bài 7A**: Thuật toán tìm số lớn nhất và nhỏ nhất - Tìm kiếm trong danh sách
- **Bài 7C**: Thuật toán tính toán - Tính tổng và trung bình

### Chuẩn bị cho bài tiếp theo
- Hiểu cách duyệt qua danh sách
- Nắm vững điều kiện và biến đếm
- Sẵn sàng học thuật toán tính toán (Bài 7C)

---

**Tác giả**: AI & Trần Việt Trung (BKHN)  
**Ngày tạo**: 04/10/2025  
**Phiên bản**: 1.0