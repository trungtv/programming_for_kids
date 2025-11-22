# Bài giảng 9B: Sắp xếp nâng cao - Insertion Sort

## 📋 Thông tin bài học
- **Thời gian**: 90 phút
- **Độ tuổi**: 10-11 tuổi
- **Trình độ**: Nâng cao
- **Mục tiêu**: Học thuật toán sắp xếp Insertion Sort và so sánh với các thuật toán đã học

## 🎯 Mục tiêu học tập

### Kiến thức
- Hiểu thuật toán sắp xếp Insertion Sort (chèn)
- So sánh hiệu suất: Bubble Sort, Selection Sort (đã học) vs Insertion Sort
- Hiểu cách Insertion Sort hoạt động trực quan (giống như sắp xếp bài)
- Biết khi nào nên sử dụng Insertion Sort

### Kỹ năng
- Thiết kế và lập trình Insertion Sort
- So sánh và đánh giá hiệu suất các thuật toán sắp xếp
- Sử dụng vòng lặp lồng nhau hiệu quả
- Debug và tối ưu hóa code

### Thái độ
- Phát triển tư duy logic phức tạp
- Rèn luyện tính kiên trì
- Khuyến khích tư duy so sánh và phân tích

## 🧠 Nội dung bài học

## 📚 PHẦN LÝ THUYẾT (45 phút)

### Phần 1: Ôn tập và kết nối với Bài 7F (10 phút)

#### Hoạt động khởi động - "Nhớ lại các thuật toán sắp xếp đã học"
- **Hoạt động**: Nhắc lại Bài 7F về Bubble Sort và Selection Sort
- **Câu hỏi**: "Chúng ta đã học những thuật toán sắp xếp nào?"
- **Kết nối**: "Hôm nay chúng ta sẽ học một thuật toán sắp xếp mới - Insertion Sort"
- **Mục tiêu**: Củng cố kiến thức và chuẩn bị cho bài mới

#### Ôn tập nhanh về Bubble Sort và Selection Sort
- **Bubble Sort**: So sánh từng cặp số cạnh nhau, đổi chỗ nếu sai thứ tự
- **Selection Sort**: Tìm số nhỏ nhất, đặt vào đầu, lặp lại
- **Điểm chung**: Đều sử dụng swap (đã học ở Bài 7D) để đổi chỗ

### Phần 2: Khái niệm Insertion Sort qua hoạt động không máy tính (20 phút)

#### Hoạt động không máy tính - "Sắp xếp bài chơi"
- **Hoạt động**: Học sinh được phát 5 lá bài [8, 9, 7, 10, 6]
- **Mục tiêu**: Sắp xếp bài từ nhỏ đến lớn, giống như khi chơi bài
- **Quy tắc**: 
  1. Giữ lá bài đầu tiên (8) trong tay
  2. Lấy lá bài tiếp theo (9), so sánh với lá trong tay
  3. Nếu lớn hơn, đặt bên phải; nếu nhỏ hơn, đặt bên trái
  4. Lặp lại với các lá bài còn lại
- **Kết quả**: [6, 7, 8, 9, 10]
- **Mục tiêu**: Hiểu Insertion Sort qua trải nghiệm thực tế

#### Khái niệm Insertion Sort qua ví dụ thực tế
- **Định nghĩa**: Insertion Sort là sắp xếp bằng cách "chèn" từng phần tử vào đúng vị trí
- **Ví dụ thực tế**: 
  - Sắp xếp bài chơi trong tay
  - Sắp xếp sách vào kệ
  - Sắp xếp đồ vật vào hộp
- **Đặc điểm**: Rất trực quan, dễ hiểu, giống như cách con người sắp xếp

#### Thuật toán Insertion Sort qua ví dụ
```
Danh sách: [8, 9, 7, 10, 6]

Bước 1: Phần tử đầu tiên (8) đã "sắp xếp"
[8] | [9, 7, 10, 6]

Bước 2: Lấy phần tử tiếp theo (9), chèn vào đúng vị trí
So sánh: 9 > 8, đặt bên phải
[8, 9] | [7, 10, 6]

Bước 3: Lấy phần tử tiếp theo (7), chèn vào đúng vị trí
So sánh: 7 < 9, di chuyển
So sánh: 7 < 8, di chuyển
[7, 8, 9] | [10, 6]

Bước 4: Lấy phần tử tiếp theo (10), chèn vào đúng vị trí
So sánh: 10 > 9, đặt bên phải
[7, 8, 9, 10] | [6]

Bước 5: Lấy phần tử cuối cùng (6), chèn vào đúng vị trí
So sánh: 6 < 10, di chuyển
So sánh: 6 < 9, di chuyển
So sánh: 6 < 8, di chuyển
So sánh: 6 < 7, di chuyển
[6, 7, 8, 9, 10] | []

Kết quả: [6, 7, 8, 9, 10]
```

### Phần 3: So sánh các thuật toán sắp xếp (15 phút)

#### Hoạt động không máy tính - "Đếm số lần so sánh"
- **Hoạt động**: So sánh số lần so sánh của 3 thuật toán với danh sách [8, 9, 7, 10, 6]
- **Bubble Sort**: ~20 lần so sánh
- **Selection Sort**: ~10 lần so sánh
- **Insertion Sort**: ~10 lần so sánh (trong trường hợp tốt nhất)
- **Mục tiêu**: Hiểu sự khác biệt về hiệu suất

#### So sánh hiệu suất các thuật toán
| Thuật toán | Số lần so sánh (trung bình) | Đặc điểm |
|------------|------------------------------|----------|
| Bubble Sort | Nhiều nhất | Dễ hiểu, chậm nhất |
| Selection Sort | Trung bình | Ổn định, luôn cần N² lần |
| Insertion Sort | Ít nhất (nếu danh sách gần sắp xếp) | Nhanh với danh sách nhỏ, trực quan |

#### Khi nào nên dùng Insertion Sort?
- **Danh sách nhỏ**: < 10 phần tử
- **Danh sách gần sắp xếp**: Chỉ cần sửa một vài phần tử
- **Cần thuật toán trực quan**: Dễ hiểu, dễ debug

## 💻 PHẦN THỰC HÀNH (45 phút)

### Phần 1: Tạo game "Sắp xếp chèn" trên Scratch (25 phút)

#### Bước 1: Tạo các biến cần thiết
```scratch
# Tạo các biến sau:
1. Biến "i" - chỉ số phần tử đang xét
2. Biến "j" - chỉ số để so sánh và di chuyển
3. Biến "key" - giá trị phần tử đang chèn
4. List "DanhSach" - danh sách cần sắp xếp
```

#### Bước 2: Lập trình thuật toán Insertion Sort
```scratch
Khi cờ xanh được nhấn
xóa tất cả trong [DanhSach v]
thêm [8] vào [DanhSach v]
thêm [9] vào [DanhSach v]
thêm [7] vào [DanhSach v]
thêm [10] vào [DanhSach v]
thêm [6] vào [DanhSach v]
nói [Trước khi sắp xếp: ] + [DanhSach v] trong (3) giây

# Insertion Sort
đặt [i v] thành [2]
lặp lại ((chiều dài của [DanhSach v]) - (1)) lần
  đặt [key v] thành (mục (i) của [DanhSach v])
  đặt [j v] thành ((i) - (1))
  
  # Di chuyển các phần tử lớn hơn key sang phải
  lặp lại cho đến khi <[j v] < [1]> hoặc <(mục (j) của [DanhSach v]) <= [key v]>
    thay thế mục ((j) + (1)) của [DanhSach v] bằng (mục (j) của [DanhSach v])
    thay đổi [j v] bởi (-1)
  
  # Chèn key vào đúng vị trí
  thay thế mục ((j) + (1)) của [DanhSach v] bằng [key v]
  nói [Sau khi chèn phần tử ] + [i v] + [: ] + [DanhSach v] trong (2) giây
  thay đổi [i v] bởi (1)

nói [Kết quả cuối cùng: ] + [DanhSach v] trong (5) giây
```

### Phần 2: So sánh hiệu suất các thuật toán (20 phút)

#### Bước 1: Tạo game so sánh
```scratch
# Tạo biến đếm số lần so sánh
đặt [soLanSoSanh v] thành [0]

# Bubble Sort với đếm
# [Code Bubble Sort từ Bài 7F, thêm đếm so sánh]

# Selection Sort với đếm
# [Code Selection Sort từ Bài 7F, thêm đếm so sánh]

# Insertion Sort với đếm
# [Code Insertion Sort, thêm đếm so sánh]
```

#### Bước 2: Hiển thị kết quả so sánh
```scratch
nói [Bubble Sort: ] + [soLanSoSanhBubble v] + [ lần so sánh] trong (3) giây
nói [Selection Sort: ] + [soLanSoSanhSelection v] + [ lần so sánh] trong (3) giây
nói [Insertion Sort: ] + [soLanSoSanhInsertion v] + [ lần so sánh] trong (3) giây
```

## 🎨 Hoạt động mở rộng

### Cấp độ 1: Thêm tính năng cơ bản
- **Hiệu ứng trực quan**: Hiển thị từng bước sắp xếp
- **Đếm số lần swap**: So sánh số lần đổi chỗ
- **Sắp xếp giảm dần**: Sắp xếp từ lớn đến nhỏ

### Cấp độ 2: Tính năng nâng cao
- **So sánh với danh sách lớn**: Test với 20, 50 phần tử
- **Đo thời gian**: So sánh thời gian thực thi
- **Sắp xếp danh sách phức tạp**: Sắp xếp danh sách có tên và điểm

### Cấp độ 3: Sáng tạo
- **Game sắp xếp**: Tạo game để người chơi sắp xếp
- **Visualization**: Tạo animation minh họa các thuật toán
- **Dự án tích hợp**: Kết hợp với các bài học khác

## 📝 Tổng kết kiến thức

### Kiến thức đã học
- **Insertion Sort**: Sắp xếp bằng cách chèn từng phần tử vào đúng vị trí
- **So sánh thuật toán**: Bubble Sort, Selection Sort, Insertion Sort
- **Hiệu suất**: Insertion Sort nhanh với danh sách nhỏ hoặc gần sắp xếp
- **Ứng dụng**: Khi nào nên dùng Insertion Sort

### Kỹ năng đã rèn luyện
- Thiết kế và lập trình Insertion Sort
- So sánh và đánh giá hiệu suất
- Sử dụng vòng lặp lồng nhau
- Debug và tối ưu hóa code

## 🎯 Đánh giá học sinh

### Tiêu chí đánh giá
- **Hiểu thuật toán**: Có thể giải thích các bước Insertion Sort
- **Lập trình Scratch**: Tạo được game sắp xếp với Insertion Sort
- **Tư duy so sánh**: So sánh được hiệu suất các thuật toán
- **Sáng tạo**: Tạo được dự án tích hợp

## 🔗 Liên kết

- **Bài trước**: [Bài 9A: Tìm kiếm nâng cao](bai-giang-9a-tim-kiem-nang-cao.md)
- **Bài tiếp theo**: [Bài 9C: Thuật toán thống kê nâng cao](bai-giang-9c-thuat-toan-thong-ke.md)
- **Bài liên quan**: [Bài 7F: Thuật toán sắp xếp](../05-thuat-toan/bai-giang-7f-thuat-toan-sap-xep.md)
- **Về topic**: [README.md](README.md)

---

**🌟 Chúc các em học tốt và sáng tạo!**

