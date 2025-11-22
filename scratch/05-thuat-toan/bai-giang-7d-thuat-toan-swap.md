# Bài giảng 7D: Thuật toán Swap (Thay thế/Đổi chỗ)

## 📋 Thông tin bài học
- **Thời gian**: 60 phút
- **Độ tuổi**: 10-11 tuổi
- **Trình độ**: Trung bình
- **Mục tiêu**: Hiểu và áp dụng thuật toán swap để đổi chỗ hai giá trị

## 🎯 Mục tiêu học tập

### Kiến thức
- Hiểu khái niệm swap (thay thế/đổi chỗ)
- Nắm vững cách đổi chỗ hai giá trị bằng biến tạm
- Hiểu tầm quan trọng của swap trong các thuật toán
- Biết cách áp dụng swap vào thực tế

### Kỹ năng
- Thực hiện swap hai giá trị đúng cách
- Sử dụng biến tạm (temp) hiệu quả
- Áp dụng swap vào các thuật toán khác
- Debug và kiểm tra kết quả swap

### Thái độ
- Phát triển tư duy logic
- Rèn luyện tính cẩn thận
- Khuyến khích tư duy phản biện

## 🧠 Nội dung bài học

## 📚 PHẦN LÝ THUYẾT (30 phút)

### Phần 1: Khái niệm swap qua hoạt động không máy tính (20 phút)

#### Hoạt động khởi động - "Đổi chỗ hai bạn"
- **Hoạt động**: Học sinh đứng thành hai hàng, đổi chỗ hai bạn
- **Quy tắc**: Bạn A đứng vị trí 1, bạn B đứng vị trí 2. Làm sao để đổi chỗ?
- **Mục tiêu**: Hiểu khái niệm đổi chỗ qua trải nghiệm thực tế
- **Kết quả**: Nhận ra cần một vị trí tạm thời để đổi chỗ

#### Khái niệm swap qua ví dụ thực tế
- **Định nghĩa**: Swap là thao tác đổi chỗ hai giá trị cho nhau
- **Ví dụ thực tế**: 
  - Đổi chỗ hai cốc nước (cần cốc thứ 3 tạm thời)
  - Đổi chỗ hai quyển sách trên kệ
  - Đổi chỗ hai bạn ngồi trong lớp
- **Vấn đề**: Không thể đổi trực tiếp, cần biến tạm
- **Giải pháp**: Sử dụng biến tạm (temp) để lưu giá trị

#### Hoạt động thực hành - "Đổi chỗ hai cốc nước"
- **Hoạt động**: Học sinh thực hành đổi chỗ hai cốc nước (màu đỏ và màu xanh)
- **Bước 1**: Đổ nước từ cốc đỏ sang cốc tạm (trống)
- **Bước 2**: Đổ nước từ cốc xanh sang cốc đỏ (đã trống)
- **Bước 3**: Đổ nước từ cốc tạm sang cốc xanh (đã trống)
- **Kết quả**: Cốc đỏ có nước xanh, cốc xanh có nước đỏ
- **Mục tiêu**: Hiểu rõ các bước của thuật toán swap

#### Bài toán: Đổi chỗ hai số
- **Input**: Số A = 5, Số B = 10
- **Output**: Số A = 10, Số B = 5
- **Vấn đề**: Nếu gán trực tiếp A = B, thì A = 10 nhưng B cũng = 10 (mất giá trị 5)
- **Giải pháp**: Cần biến tạm để lưu giá trị A trước khi gán

### Phần 2: Thuật toán swap qua ví dụ (10 phút)

#### Thuật toán swap cơ bản
```
Bước 1: Lưu giá trị A vào biến tạm (temp = A)
Bước 2: Gán giá trị B cho A (A = B)
Bước 3: Gán giá trị temp cho B (B = temp)
Kết quả: A và B đã đổi chỗ cho nhau
```

#### Ví dụ minh họa chi tiết
```
Ban đầu: A = 5, B = 10, temp = ?

Bước 1: temp = A
        → A = 5, B = 10, temp = 5

Bước 2: A = B
        → A = 10, B = 10, temp = 5

Bước 3: B = temp
        → A = 10, B = 5, temp = 5

Kết quả: A = 10, B = 5 (đã đổi chỗ thành công!)
```

#### Hoạt động không máy tính - "Mô phỏng swap bằng thẻ số"
- **Hoạt động**: Học sinh sử dụng 3 thẻ số để mô phỏng swap
- **Thẻ 1**: Số A (ví dụ: 5)
- **Thẻ 2**: Số B (ví dụ: 10)
- **Thẻ 3**: Biến tạm (trống)
- **Mục tiêu**: Thực hành các bước swap bằng tay
- **Kết quả**: Hiểu rõ từng bước của thuật toán

## 💻 PHẦN THỰC HÀNH SCRATCH (30 phút)

### Phần 3: Tạo game "Đổi chỗ hai số" trên Scratch (20 phút)

#### Bước 1: Tạo các biến cần thiết
```scratch
# Tạo các biến sau:
1. Biến "SoA" - số thứ nhất
2. Biến "SoB" - số thứ hai
3. Biến "Temp" - biến tạm để lưu giá trị
```

#### Bước 2: Khởi tạo giá trị
```scratch
Khi cờ xanh được nhấn
đặt [SoA v] thành (5)
đặt [SoB v] thành (10)
đặt [Temp v] thành (0)
nói [Ban đầu: Số A = ] + [SoA v] + [, Số B = ] + [SoB v] trong (3) giây
chờ (1) giây
```

#### Bước 3: Lập trình thuật toán swap
```scratch
Khi nhấn phím [s v]
nói [=== BẮT ĐẦU SWAP ===] trong (2) giây
chờ (1) giây

# Bước 1: Lưu giá trị A vào biến tạm
nói [Bước 1: Lưu giá trị A vào biến tạm] trong (2) giây
đặt [Temp v] thành [SoA v]
nói [Temp = ] + [Temp v] + [ (đã lưu giá trị A)] trong (2) giây
chờ (1) giây

# Bước 2: Gán giá trị B cho A
nói [Bước 2: Gán giá trị B cho A] trong (2) giây
đặt [SoA v] thành [SoB v]
nói [A = ] + [SoA v] + [ (đã nhận giá trị B)] trong (2) giây
chờ (1) giây

# Bước 3: Gán giá trị temp cho B
nói [Bước 3: Gán giá trị temp cho B] trong (2) giây
đặt [SoB v] thành [Temp v]
nói [B = ] + [SoB v] + [ (đã nhận giá trị từ temp)] trong (2) giây
chờ (1) giây

# Kết quả
nói [=== KẾT QUẢ ===] trong (2) giây
nói [Sau khi swap: Số A = ] + [SoA v] + [, Số B = ] + [SoB v] trong (3) giây
phát âm thanh [pop v]
```

#### Hoạt động mở rộng - "Swap với nhiều giá trị"
- **Hoạt động**: Thử swap với các giá trị khác nhau (số âm, số lớn, số bằng nhau)
- **Mục tiêu**: Hiểu swap hoạt động với mọi loại giá trị
- **Thử thách**: Swap ba số (A, B, C) theo vòng tròn (A→B, B→C, C→A)

### Phần 4: Swap trong danh sách (10 phút)

#### Bài toán: Đổi chỗ hai phần tử trong danh sách
- **Input**: Danh sách [8, 9, 7, 10, 6], đổi chỗ vị trí 2 và 4
- **Output**: Danh sách [8, 10, 7, 9, 6]
- **Ví dụ**: Đổi chỗ điểm của hai học sinh trong bảng điểm

#### Lập trình swap trong danh sách
```scratch
Khi nhấn phím [d v]
# Khởi tạo danh sách
xóa tất cả trong [DanhSach v]
thêm [8] vào [DanhSach v]
thêm [9] vào [DanhSach v]
thêm [7] vào [DanhSach v]
thêm [10] vào [DanhSach v]
thêm [6] vào [DanhSach v]

nói [Danh sách ban đầu: ] + [DanhSach v] trong (3) giây
chờ (1) giây

# Đổi chỗ vị trí 2 và 4 (chỉ số 2 và 4 trong Scratch)
đặt [ViTri1 v] thành (2)
đặt [ViTri2 v] thành (4)
nói [Đổi chỗ vị trí ] + [ViTri1 v] + [ và ] + [ViTri2 v] trong (2) giây

# Bước 1: Lưu giá trị vị trí 1 vào temp
đặt [Temp v] thành (mục (ViTri1) của [DanhSach v])
nói [Bước 1: Lưu giá trị vị trí ] + [ViTri1 v] + [ vào temp: ] + [Temp v] trong (2) giây
chờ (1) giây

# Bước 2: Gán giá trị vị trí 2 cho vị trí 1
thay thế mục (ViTri1) của [DanhSach v] bằng (mục (ViTri2) của [DanhSach v])
nói [Bước 2: Gán giá trị vị trí ] + [ViTri2 v] + [ cho vị trí ] + [ViTri1 v] trong (2) giây
nói [Danh sách hiện tại: ] + [DanhSach v] trong (2) giây
chờ (1) giây

# Bước 3: Gán giá trị temp cho vị trí 2
thay thế mục (ViTri2) của [DanhSach v] bằng [Temp v]
nói [Bước 3: Gán giá trị temp cho vị trí ] + [ViTri2 v] trong (2) giây
chờ (1) giây

# Kết quả
nói [=== KẾT QUẢ ===] trong (2) giây
nói [Danh sách sau khi swap: ] + [DanhSach v] trong (3) giây
phát âm thanh [pop v]
```

#### Hoạt động mở rộng - "Swap nhiều lần"
- **Hoạt động**: Tạo chương trình swap nhiều cặp phần tử
- **Mục tiêu**: Hiểu cách sử dụng swap trong vòng lặp
- **Thử thách**: Swap tất cả các phần tử lẻ với phần tử chẵn kế tiếp

## 🎯 Tổng kết và đánh giá (10 phút)

### Tổng kết kiến thức
- **Swap**: Thao tác đổi chỗ hai giá trị cho nhau
- **Biến tạm**: Cần thiết để lưu giá trị trước khi đổi chỗ
- **Ba bước**: Lưu → Gán → Gán (temp = A, A = B, B = temp)
- **Ứng dụng**: Swap là nền tảng cho nhiều thuật toán (sắp xếp, tìm kiếm)

### Đánh giá học sinh
- **Hiểu swap**: Có thể giải thích các bước của thuật toán swap
- **Áp dụng thực tế**: Tìm được ví dụ swap trong cuộc sống
- **Lập trình Scratch**: Tạo được chương trình swap đúng
- **Tư duy logic**: Hiểu tại sao cần biến tạm

## 🎨 Hoạt động mở rộng

### Cấp độ 1: Thêm tính năng cơ bản
- **Giao diện tương tác**: Tạo nút để nhập giá trị A và B
- **Hiệu ứng trực quan**: Thêm màu sắc và animation khi swap
- **Âm thanh**: Tạo âm thanh khác nhau cho từng bước

### Cấp độ 2: Tính năng nâng cao
- **Swap nhiều giá trị**: Swap ba hoặc bốn giá trị
- **Swap trong vòng lặp**: Swap nhiều cặp phần tử trong danh sách
- **Swap có điều kiện**: Chỉ swap khi thỏa mãn điều kiện

### Cấp độ 3: Sáng tạo
- **Game swap**: Tạo trò chơi sắp xếp bằng cách swap
- **Thuật toán riêng**: Thiết kế thuật toán swap độc đáo
- **Dự án tích hợp**: Kết hợp swap với các thuật toán khác

## 📝 Bài tập về nhà

### Bài tập bắt buộc
1. **Swap hai số**: Viết chương trình swap hai số A và B
2. **Swap trong danh sách**: Đổi chỗ vị trí 1 và 3 trong danh sách 5 phần tử
3. **Kiểm tra swap**: Tạo chương trình kiểm tra kết quả swap có đúng không

### Bài tập nâng cao
1. **Swap ba số**: Đổi chỗ ba số A, B, C theo vòng tròn (A→B, B→C, C→A)
2. **Swap có điều kiện**: Chỉ swap khi A > B
3. **Swap nhiều cặp**: Swap tất cả các cặp phần tử lẻ-chẵn trong danh sách

### Bài tập sáng tạo
1. **Game swap**: Tạo game sắp xếp số bằng cách swap
2. **Thuật toán riêng**: Thiết kế cách swap không dùng biến tạm (chỉ với phép toán)
3. **Dự án tích hợp**: Sử dụng swap trong thuật toán sắp xếp

## 🔧 Tài nguyên hỗ trợ

### Tài liệu tham khảo
- **Scratch Programming**: Hướng dẫn lập trình Scratch cơ bản
- **Algorithm Visualization**: Công cụ minh họa thuật toán swap
- **Unplugged Activities**: Hoạt động không máy tính cho swap

### Công cụ hỗ trợ
- **Scratch Editor**: Môi trường lập trình trực quan
- **Variable Blocks**: Khối lệnh biến số trong Scratch
- **List Blocks**: Khối lệnh danh sách trong Scratch

### Đánh giá và phản hồi
- **Rubric đánh giá**: Tiêu chí đánh giá kỹ năng swap
- **Peer Review**: Đánh giá lẫn nhau giữa học sinh
- **Portfolio**: Tập hợp các dự án và bài tập của học sinh

## 🔗 Kết nối với bài học khác

### Kiến thức liên quan
- **Bài 6**: Cấu trúc dữ liệu - Sử dụng danh sách (List)
- **Bài 7A**: Thuật toán tìm số lớn nhất và nhỏ nhất
- **Bài 7B**: Thuật toán đếm
- **Bài 7C**: Thuật toán tính toán
- **Bài 7F**: Thuật toán sắp xếp - **Swap là nền tảng của sắp xếp!**

### Chuẩn bị cho bài tiếp theo
- Hiểu cách đổi chỗ hai giá trị
- Nắm vững sử dụng biến tạm
- **Sẵn sàng học thuật toán sắp xếp (Bài 7F)** - Swap là kỹ thuật cốt lõi!

## 💡 Lưu ý quan trọng

### Tại sao cần biến tạm?
- **Không có temp**: Nếu gán trực tiếp A = B, thì A = B nhưng B vẫn = B (không đổi)
- **Có temp**: Lưu giá trị A trước, sau đó mới gán B cho A, cuối cùng gán temp cho B
- **Ví dụ**: Giống như đổi chỗ hai cốc nước, cần cốc thứ 3 tạm thời

### Ứng dụng của swap
- **Sắp xếp**: Đổi chỗ các phần tử để sắp xếp
- **Tìm kiếm**: Đổi chỗ để đưa phần tử về vị trí đúng
- **Xử lý dữ liệu**: Sắp xếp lại thứ tự trong danh sách

### Mẹo hay
- **Luôn kiểm tra**: Sau khi swap, kiểm tra xem giá trị có đổi đúng không
- **Sử dụng temp**: Không bao giờ quên tạo biến tạm
- **Thứ tự bước**: Phải làm đúng thứ tự (temp = A, A = B, B = temp)

---

**Tác giả**: AI & Trần Việt Trung (BKHN)  
**Ngày tạo**: 04/10/2025  
**Phiên bản**: 1.0

