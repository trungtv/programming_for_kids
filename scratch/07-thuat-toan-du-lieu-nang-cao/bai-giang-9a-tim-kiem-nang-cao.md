# Bài giảng 9A: Tìm kiếm nâng cao

## 📋 Thông tin bài học
- **Thời gian**: 90 phút
- **Độ tuổi**: 10-11 tuổi
- **Trình độ**: Nâng cao
- **Mục tiêu**: Mở rộng thuật toán tìm kiếm với các biến thể thực tế (mở rộng từ Bài 7E)

## 🎯 Mục tiêu học tập

### Kiến thức
- Hiểu khái niệm tìm số xuất hiện nhiều nhất (mode)
- Nắm vững cách tìm vị trí đầu tiên và cuối cùng
- Hiểu cách lọc phần tử thỏa điều kiện (filter)
- Biết cách áp dụng các kỹ thuật tìm kiếm nâng cao vào thực tế

### Kỹ năng
- Thiết kế thuật toán tìm mode
- Tìm vị trí đầu tiên/cuối cùng của phần tử
- Lọc dữ liệu theo điều kiện
- Kết hợp nhiều kỹ thuật tìm kiếm

### Thái độ
- Phát triển tư duy logic nâng cao
- Rèn luyện tính kiên trì
- Khuyến khích tư duy sáng tạo và ứng dụng

## 🧠 Nội dung bài học

## 📚 PHẦN LÝ THUYẾT (45 phút)

### Phần 1: Ôn tập và kết nối với Bài 7F (10 phút)

#### Hoạt động khởi động - "Nhớ lại tìm kiếm cơ bản"
- **Hoạt động**: Nhắc lại Bài 7E về tìm kiếm tuyến tính
- **Câu hỏi**: "Chúng ta đã học cách tìm phần tử trong danh sách như thế nào?"
- **Kết nối**: "Hôm nay chúng ta sẽ học các kỹ thuật tìm kiếm nâng cao hơn"
- **Mục tiêu**: Củng cố kiến thức và chuẩn bị cho bài mới

#### Ôn tập nhanh về tìm kiếm cơ bản
- **Tìm kiếm tuyến tính**: Duyệt qua từng phần tử, so sánh với giá trị cần tìm
- **Tìm vị trí**: Tìm vị trí bất kỳ của phần tử trong danh sách
- **Xử lý không tìm thấy**: Kiểm tra xem phần tử có tồn tại hay không

### Phần 2: Tìm số xuất hiện nhiều nhất (Mode) (20 phút)

#### Hoạt động không máy tính - "Tìm số điểm xuất hiện nhiều nhất"
- **Hoạt động**: Học sinh được phát danh sách điểm [8, 9, 8, 7, 8, 9, 8]
- **Câu hỏi**: "Số điểm nào xuất hiện nhiều nhất?"
- **Bước 1**: Đếm số lần xuất hiện của từng số
  - Số 8: xuất hiện 4 lần
  - Số 9: xuất hiện 2 lần
  - Số 7: xuất hiện 1 lần
- **Bước 2**: So sánh số lần xuất hiện
- **Kết quả**: Số 8 xuất hiện nhiều nhất (4 lần)
- **Mục tiêu**: Hiểu khái niệm mode qua trải nghiệm thực tế

#### Khái niệm Mode qua ví dụ thực tế
- **Định nghĩa**: Mode là giá trị xuất hiện nhiều nhất trong danh sách
- **Ví dụ thực tế**: 
  - Điểm số xuất hiện nhiều nhất trong lớp
  - Màu sắc được yêu thích nhất
  - Số tuổi phổ biến nhất trong nhóm
- **Ứng dụng**: Phân tích dữ liệu, tìm xu hướng

#### Thuật toán tìm Mode qua ví dụ
```
Danh sách: [8, 9, 8, 7, 8, 9, 8]

Bước 1: Đếm số lần xuất hiện của từng số
- Số 8: đếm được 4 lần
- Số 9: đếm được 2 lần
- Số 7: đếm được 1 lần

Bước 2: Tìm số có số lần xuất hiện lớn nhất
- So sánh: 4 > 2 và 4 > 1
- Kết quả: Mode = 8 (xuất hiện 4 lần)
```

### Phần 3: Tìm vị trí đầu tiên và cuối cùng (15 phút)

#### Hoạt động không máy tính - "Tìm vị trí đầu tiên và cuối cùng"
- **Hoạt động**: Học sinh được phát danh sách [8, 9, 7, 9, 8, 9]
- **Câu hỏi**: "Số 9 xuất hiện ở vị trí nào đầu tiên? Vị trí nào cuối cùng?"
- **Tìm vị trí đầu tiên**: Duyệt từ đầu, dừng khi gặp số 9 lần đầu → Vị trí 2
- **Tìm vị trí cuối cùng**: Duyệt từ cuối, dừng khi gặp số 9 lần đầu → Vị trí 6
- **Mục tiêu**: Hiểu sự khác biệt giữa tìm vị trí đầu tiên và cuối cùng

#### Thuật toán tìm vị trí đầu tiên
```
Danh sách: [8, 9, 7, 9, 8, 9]
Tìm: 9

Duyệt từ đầu:
- Vị trí 1: 8 ≠ 9, tiếp tục
- Vị trí 2: 9 = 9, tìm thấy!
Kết quả: Vị trí đầu tiên = 2
```

#### Thuật toán tìm vị trí cuối cùng
```
Danh sách: [8, 9, 7, 9, 8, 9]
Tìm: 9

Duyệt từ cuối:
- Vị trí 6: 9 = 9, tìm thấy!
Kết quả: Vị trí cuối cùng = 6
```

### Phần 4: Lọc phần tử thỏa điều kiện (Filter) (15 phút)

#### Hoạt động không máy tính - "Lọc số chẵn"
- **Hoạt động**: Học sinh được phát danh sách [8, 9, 7, 10, 6, 11]
- **Câu hỏi**: "Hãy tìm tất cả số chẵn trong danh sách"
- **Bước 1**: Duyệt qua từng số
- **Bước 2**: Kiểm tra điều kiện (số chẵn = chia hết cho 2)
- **Bước 3**: Nếu thỏa điều kiện, thêm vào danh sách kết quả
- **Kết quả**: [8, 10, 6]
- **Mục tiêu**: Hiểu khái niệm filter qua trải nghiệm thực tế

#### Khái niệm Filter qua ví dụ thực tế
- **Định nghĩa**: Filter là lọc ra các phần tử thỏa một điều kiện nào đó
- **Ví dụ thực tế**: 
  - Lọc học sinh có điểm >= 8
  - Lọc số chẵn trong danh sách
  - Lọc Pokemon loại nước
- **Ứng dụng**: Phân loại dữ liệu, tìm kiếm có điều kiện

#### Thuật toán Filter qua ví dụ
```
Danh sách: [8, 9, 7, 10, 6, 11]
Điều kiện: Số chẵn (chia hết cho 2)

Duyệt qua từng phần tử:
- 8: 8 % 2 = 0 → Chẵn, thêm vào kết quả
- 9: 9 % 2 = 1 → Lẻ, bỏ qua
- 7: 7 % 2 = 1 → Lẻ, bỏ qua
- 10: 10 % 2 = 0 → Chẵn, thêm vào kết quả
- 6: 6 % 2 = 0 → Chẵn, thêm vào kết quả
- 11: 11 % 2 = 1 → Lẻ, bỏ qua

Kết quả: [8, 10, 6]
```

## 💻 PHẦN THỰC HÀNH (45 phút)

### Phần 1: Tạo game "Tìm Mode" trên Scratch (15 phút)

#### Bước 1: Tạo các biến và danh sách cần thiết
```scratch
# Tạo các biến sau:
1. Biến "i" - chỉ số vị trí hiện tại
2. Biến "soLanXuatHien" - số lần xuất hiện tạm thời
3. Biến "soLanXuatHienMax" - số lần xuất hiện lớn nhất
4. Biến "mode" - giá trị xuất hiện nhiều nhất
5. List "DanhSach" - danh sách cần tìm mode
6. List "SoLanXuatHien" - danh sách lưu số lần xuất hiện
```

#### Bước 2: Lập trình thuật toán tìm Mode
```scratch
Khi cờ xanh được nhấn
xóa tất cả trong [DanhSach v]
thêm [8] vào [DanhSach v]
thêm [9] vào [DanhSach v]
thêm [8] vào [DanhSach v]
thêm [7] vào [DanhSach v]
thêm [8] vào [DanhSach v]
thêm [9] vào [DanhSach v]
thêm [8] vào [DanhSach v]
nói [Danh sách: ] + [DanhSach v] trong (3) giây

# Tìm mode
đặt [soLanXuatHienMax v] thành [0]
đặt [mode v] thành [0]
đặt [i v] thành [1]
lặp lại (chiều dài của [DanhSach v]) lần
  đặt [soLanXuatHien v] thành [0]
  đặt [j v] thành [1]
  lặp lại (chiều dài của [DanhSach v]) lần
    nếu <(mục (i) của [DanhSach v]) = (mục (j) của [DanhSach v])> thì
      thay đổi [soLanXuatHien v] bởi (1)
    thay đổi [j v] bởi (1)
  
  nếu <[soLanXuatHien v] > [soLanXuatHienMax v]> thì
    đặt [soLanXuatHienMax v] thành [soLanXuatHien v]
    đặt [mode v] thành (mục (i) của [DanhSach v])
  thay đổi [i v] bởi (1)

nói [Số xuất hiện nhiều nhất: ] + [mode v] + [ (xuất hiện ] + [soLanXuatHienMax v] + [ lần)] trong (5) giây
```

### Phần 2: Tạo game "Tìm vị trí đầu tiên và cuối cùng" (15 phút)

#### Bước 1: Tìm vị trí đầu tiên
```scratch
Khi cờ xanh được nhấn
xóa tất cả trong [DanhSach v]
thêm [8] vào [DanhSach v]
thêm [9] vào [DanhSach v]
thêm [7] vào [DanhSach v]
thêm [9] vào [DanhSach v]
thêm [8] vào [DanhSach v]
thêm [9] vào [DanhSach v]

# Tìm vị trí đầu tiên của số 9
đặt [i v] thành [1]
đặt [viTriDauTien v] thành [0]
lặp lại (chiều dài của [DanhSach v]) lần
  nếu <(mục (i) của [DanhSach v]) = [9]> thì
    đặt [viTriDauTien v] thành [i v]
    dừng tất cả
  thay đổi [i v] bởi (1)

nếu <[viTriDauTien v] > [0]> thì
  nói [Vị trí đầu tiên của số 9: ] + [viTriDauTien v] trong (3) giây
không thì
  nói [Không tìm thấy số 9] trong (3) giây
```

#### Bước 2: Tìm vị trí cuối cùng
```scratch
# Tìm vị trí cuối cùng của số 9
đặt [i v] thành (chiều dài của [DanhSach v])
đặt [viTriCuoiCung v] thành [0]
lặp lại (chiều dài của [DanhSach v]) lần
  nếu <(mục (i) của [DanhSach v]) = [9]> thì
    đặt [viTriCuoiCung v] thành [i v]
    dừng tất cả
  thay đổi [i v] bởi (-1)

nếu <[viTriCuoiCung v] > [0]> thì
  nói [Vị trí cuối cùng của số 9: ] + [viTriCuoiCung v] trong (3) giây
không thì
  nói [Không tìm thấy số 9] trong (3) giây
```

### Phần 3: Tạo game "Lọc số chẵn" (15 phút)

#### Bước 1: Tạo danh sách kết quả
```scratch
# Tạo danh sách kết quả
xóa tất cả trong [KetQua v]
```

#### Bước 2: Lập trình thuật toán Filter
```scratch
Khi cờ xanh được nhấn
xóa tất cả trong [DanhSach v]
xóa tất cả trong [KetQua v]
thêm [8] vào [DanhSach v]
thêm [9] vào [DanhSach v]
thêm [7] vào [DanhSach v]
thêm [10] vào [DanhSach v]
thêm [6] vào [DanhSach v]
thêm [11] vào [DanhSach v]
nói [Danh sách gốc: ] + [DanhSach v] trong (3) giây

# Lọc số chẵn
đặt [i v] thành [1]
lặp lại (chiều dài của [DanhSach v]) lần
  nếu <((mục (i) của [DanhSach v]) mod (2)) = [0]> thì
    thêm (mục (i) của [DanhSach v]) vào [KetQua v]
  thay đổi [i v] bởi (1)

nói [Số chẵn trong danh sách: ] + [KetQua v] trong (5) giây
```

## 🎨 Hoạt động mở rộng

### Cấp độ 1: Thêm tính năng cơ bản
- **Tìm mode của danh sách điểm**: Tìm điểm số xuất hiện nhiều nhất
- **Tìm vị trí của nhiều phần tử**: Tìm tất cả vị trí của một số
- **Lọc với nhiều điều kiện**: Lọc số chẵn và lớn hơn 5

### Cấp độ 2: Tính năng nâng cao
- **Tìm mode của nhiều danh sách**: So sánh mode của các lớp khác nhau
- **Lọc phức tạp**: Lọc học sinh có điểm >= 8 và <= 10
- **Kết hợp nhiều kỹ thuật**: Tìm mode, sau đó tìm vị trí của mode

### Cấp độ 3: Sáng tạo
- **Game phân tích dữ liệu**: Tạo game phân tích điểm số của lớp
- **Hệ thống tìm kiếm thông minh**: Kết hợp tất cả kỹ thuật tìm kiếm
- **Dự án tích hợp**: Kết hợp với các bài học khác

## 📝 Tổng kết kiến thức

### Kiến thức đã học
- **Mode**: Số xuất hiện nhiều nhất trong danh sách
- **Vị trí đầu tiên/cuối cùng**: Tìm vị trí cụ thể của phần tử
- **Filter**: Lọc phần tử thỏa điều kiện
- **Kết hợp**: Sử dụng nhiều kỹ thuật tìm kiếm cùng lúc

### Kỹ năng đã rèn luyện
- Thiết kế thuật toán tìm mode
- Tìm vị trí đầu tiên và cuối cùng
- Lọc dữ liệu theo điều kiện
- Kết hợp nhiều kỹ thuật tìm kiếm

## 🎯 Đánh giá học sinh

### Tiêu chí đánh giá
- **Hiểu thuật toán**: Có thể giải thích các bước tìm mode, filter
- **Lập trình Scratch**: Tạo được game tìm kiếm nâng cao
- **Tư duy logic**: Kết hợp được nhiều kỹ thuật tìm kiếm
- **Sáng tạo**: Tạo được dự án tích hợp các kỹ thuật

## 🔗 Liên kết

- **Bài trước**: [Bài 7E: Thuật toán tìm kiếm](../05-thuat-toan/bai-giang-7e-thuat-toan-tim-kiem.md)
- **Bài tiếp theo**: [Bài 9B: Sắp xếp nâng cao - Insertion Sort](bai-giang-9b-sap-xep-nang-cao.md)
- **Về topic**: [README.md](README.md)

---

**🌟 Chúc các em học tốt và sáng tạo!**

