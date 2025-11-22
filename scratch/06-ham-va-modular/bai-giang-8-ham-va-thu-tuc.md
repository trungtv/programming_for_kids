# Bài Giảng 8: Hàm Và Thủ Tục

## 📋 Thông tin bài học
- **Thời gian**: 90 phút (2 tiết)
- **Độ tuổi**: Lớp 4-5 (9-11 tuổi)
- **Mức độ**: Trung bình đến nâng cao
- **Mục tiêu**: Hiểu khái niệm hàm và thủ tục để chuẩn bị cho Python

## 🎯 Mục tiêu học tập

### Kiến thức
- Hiểu khái niệm hàm và thủ tục
- Biết cách tạo và sử dụng hàm
- Hiểu cách truyền tham số và trả về giá trị

### Kỹ năng
- Thiết kế hàm đơn giản
- Tái sử dụng code hiệu quả
- Tổ chức code có cấu trúc

### Thái độ
- Phát triển tư duy modular
- Rèn luyện tính cẩn thận
- Khuyến khích tư duy hệ thống


## 🔧 Nội dung bài học

### Phần 1: Ôn tập Custom Blocks và giới thiệu hàm nâng cao (15 phút)

#### Hoạt động khởi động - "Nhớ lại Custom Blocks từ Bài 3.5"
- **Hoạt động**: Nhắc lại Bài 3.5 về Custom Blocks
- **Câu hỏi**: "Chúng ta đã học cách tạo custom blocks như thế nào?"
- **Kết nối**: "Hôm nay chúng ta sẽ học nâng cao về custom blocks - tạo hàm phức tạp hơn"
- **Mục tiêu**: Củng cố kiến thức về custom blocks và chuẩn bị cho bài nâng cao

#### Ôn tập nhanh về Custom Blocks
- **Custom Blocks là gì?**: Khối lệnh do chúng ta tự tạo, có thể tái sử dụng
- **Lợi ích**: Tái sử dụng code, dễ quản lý, code ngắn gọn
- **Tham số**: Giúp custom blocks linh hoạt hơn

#### Giới thiệu bài mới - "Hàm và thủ tục nâng cao"
- **Hàm tính toán**: Tính diện tích, chu vi, giai thừa
- **Hàm kiểm tra**: Kiểm tra số chẵn/lẻ, số nguyên tố
- **Hàm phức tạp**: Hàm có nhiều tham số, hàm lồng nhau

#### Ví dụ thực tế
- **Hàm tính toán**: Tính diện tích, chu vi
- **Hàm hiển thị**: In ra màn hình, phát âm thanh
- **Hàm kiểm tra**: Kiểm tra số chẵn/lẻ

#### Khái niệm cơ bản
- **Hàm**: Nhận input, xử lý, trả về output
- **Thủ tục**: Thực hiện một tác vụ cụ thể
- **Tái sử dụng**: Sử dụng lại code nhiều lần

### Phần 2: Tạo hàm đơn giản (25 phút)

#### Hàm tính diện tích hình chữ nhật
- **Input**: Chiều dài, chiều rộng
- **Output**: Diện tích
- **Công thức**: Diện tích = dài × rộng

#### Tạo hàm trong Scratch

**Bước 1: Tạo hàm mới**
1. Chọn "My Blocks" (Khối của tôi)
2. Nhấn "Make a Block" (Tạo khối)
3. Đặt tên hàm: "TinhDienTich"
4. Nhấn "OK"

**Bước 2: Định nghĩa hàm**
```scratch
define TinhDienTich
đặt [ChieuDai v] thành (5)
đặt [ChieuRong v] thành (3)
đặt [DienTich v] thành ([ChieuDai v] * [ChieuRong v])
nói [Diện tích hình chữ nhật: ] + [DienTich v] trong (3) giây
```

**Bước 3: Sử dụng hàm**
```scratch
Khi nhấn phím [f v]
TinhDienTich
```

#### Sử dụng hàm nhiều lần
```scratch
Khi nhấn phím [1 v]
TinhDienTich

Khi nhấn phím [2 v]
TinhDienTich
```

### Phần 3: Hàm với tham số (20 phút)

#### Khái niệm tham số
- **Tham số**: Giá trị đầu vào của hàm
- **Ví dụ**: Hàm tính tổng nhận 2 số
- **Lợi ích**: Linh hoạt và tái sử dụng

#### Tạo hàm với tham số

**Bước 1: Tạo hàm có tham số**
1. Chọn "My Blocks" → "Make a Block"
2. Đặt tên: "TinhTong"
3. Thêm tham số: Nhấn "+" và chọn "number input"
4. Đặt tên tham số: "So1", "So2"
5. Nhấn "OK"

**Bước 2: Định nghĩa hàm với tham số**
```scratch
define TinhTong (So1) (So2)
đặt [Tong v] thành ([So1 v] + [So2 v])
nói [Tổng của ] + [So1 v] + [ và ] + [So2 v] + [ là: ] + [Tong v] trong (3) giây
```

**Bước 3: Sử dụng hàm với giá trị khác nhau**
```scratch
Khi nhấn phím [t v]
TinhTong (10) (20)

Khi nhấn phím [a v]
TinhTong (15) (25)

Khi nhấn phím [b v]
TinhTong (100) (200)
```

### Phần 4: Hàm kiểm tra điều kiện (15 phút)

#### Hàm kiểm tra số chẵn/lẻ
- **Input**: Một số
- **Output**: "Chẵn" hoặc "Lẻ"
- **Logic**: Số chia hết cho 2 là chẵn

#### Tạo hàm kiểm tra số chẵn/lẻ

**Bước 1: Tạo hàm có tham số**
1. Chọn "My Blocks" → "Make a Block"
2. Đặt tên: "KiemTraChanLe"
3. Thêm tham số: "So"
4. Nhấn "OK"

**Bước 2: Định nghĩa hàm**
```scratch
define KiemTraChanLe (So)
nếu <([So v] mod (2)) = [0]> thì
nói [Số ] + [So v] + [ là số chẵn] trong (2) giây
nếu không
nói [Số ] + [So v] + [ là số lẻ] trong (2) giây
```

**Bước 3: Sử dụng hàm**
```scratch
Khi nhấn phím [c v]
KiemTraChanLe (8)

Khi nhấn phím [d v]
KiemTraChanLe (7)

Khi nhấn phím [e v]
KiemTraChanLe (12)
```

### Phần 5: Hàm phức tạp hơn (15 phút)

#### Hàm tính giai thừa
- **Input**: Số n
- **Output**: n! = n × (n-1) × ... × 1
- **Ví dụ**: 5! = 5 × 4 × 3 × 2 × 1 = 120

#### Tạo hàm tính giai thừa

**Bước 1: Tạo hàm có tham số**
1. Chọn "My Blocks" → "Make a Block"
2. Đặt tên: "TinhGiaiThua"
3. Thêm tham số: "n"
4. Nhấn "OK"

**Bước 2: Định nghĩa hàm**
```scratch
define TinhGiaiThua (n)
đặt [KetQua v] thành (1)
đặt [i v] thành (1)
lặp lại ([n v]) lần
đặt [KetQua v] thành ([KetQua v] * [i v])
thay đổi [i v] bởi (1)
nói [Giai thừa của ] + [n v] + [ là: ] + [KetQua v] trong (3) giây
```

**Bước 3: Sử dụng hàm**
```scratch
Khi nhấn phím [g v]
TinhGiaiThua (5)

Khi nhấn phím [h v]
TinhGiaiThua (3)

Khi nhấn phím [i v]
TinhGiaiThua (4)
```

## 🎨 Hoạt động mở rộng

### Cấp độ 1: Thêm tính năng cơ bản
- Tạo hàm tính chu vi hình chữ nhật
- Tạo hàm kiểm tra số nguyên tố
- Thêm giao diện để nhập dữ liệu

### Cấp độ 2: Tính năng nâng cao
- Tạo hàm tính toán phức tạp
- Kết hợp nhiều hàm với nhau
- Tạo thư viện hàm cá nhân

### Cấp độ 3: Sáng tạo
- Thiết kế hàm riêng cho bài toán cụ thể
- Tạo game sử dụng nhiều hàm
- Áp dụng vào dự án thực tế

## 📝 Bài tập về nhà

### Bài tập bắt buộc
1. Tạo hàm tính diện tích hình tròn
2. Tạo hàm kiểm tra số chia hết cho 3
3. Tạo hàm tính tổng các số từ 1 đến n

### Bài tập nâng cao
1. Tạo hàm tìm số lớn nhất trong danh sách
2. Tạo hàm sắp xếp danh sách
3. Tạo hàm tính toán với nhiều tham số

## 🔍 Đánh giá

### Tiêu chí đánh giá
| Tiêu chí | Điểm | Mô tả |
|----------|------|-------|
| Hiểu khái niệm hàm | 3 | Giải thích được khái niệm |
| Tạo hàm đúng | 3 | Code hoạt động chính xác |
| Tái sử dụng | 2 | Sử dụng hàm nhiều lần |
| Sáng tạo | 1 | Có yếu tố độc đáo |
| Trình bày | 1 | Giải thích rõ ràng |
| Tổng cộng | 10 | |

### Cách đánh giá
- **Quan sát**: Giáo viên quan sát quá trình tạo hàm
- **Sản phẩm**: Kiểm tra hàm hoạt động đúng
- **Trình bày**: Học sinh demo và giải thích
- **Phản hồi**: Nhận xét từ bạn cùng lớp

## 🚀 Lưu ý quan trọng

### Cho giáo viên
- Giải thích kỹ khái niệm hàm và thủ tục
- Sử dụng ví dụ thực tế để minh họa
- Khuyến khích học sinh tạo hàm riêng
- Chuẩn bị nhiều bài tập thực hành

### Cho học sinh
- Hiểu rõ input và output của hàm
- Test kỹ từng hàm trước khi sử dụng
- Không ngại thử nghiệm với giá trị khác
- Lưu dự án thường xuyên

## 💡 Mẹo hay

### Thiết kế hàm hiệu quả
- Xác định rõ input và output
- Đặt tên hàm dễ hiểu
- Viết comment giải thích

### Tái sử dụng code
- Tạo hàm cho các tác vụ lặp lại
- Sử dụng tham số để linh hoạt
- Tổ chức code có cấu trúc

### Debug hiệu quả
- Test từng hàm riêng biệt
- Sử dụng "say" để theo dõi giá trị
- Kiểm tra với các trường hợp khác nhau

## 🔗 Kết nối với Python

### Khái niệm tương đồng
- **Hàm**: Scratch functions ↔ Python functions
- **Tham số**: Scratch parameters ↔ Python parameters
- **Trả về**: Scratch return ↔ Python return
- **Gọi hàm**: Scratch call ↔ Python call

### Chuẩn bị cho Python
- Hiểu cú pháp định nghĩa hàm
- Làm quen với tham số và return
- Thực hành với các bài toán thực tế

## 📚 Tài liệu tham khảo

- [Scratch Functions Tutorial](https://lam-programming.weebly.com/scratch-function.html)
- [Scratch Functions](https://scratch.mit.edu/explore/projects/functions)
- [Introduction to Functions](https://scratch.mit.edu/tutorials)
- [Python Functions Tutorial](https://python.org)

---

**Tác giả**: AI & Trần Việt Trung (BKHN)  
**Ngày tạo**: 04/10/2025  
**Phiên bản**: 1.0
