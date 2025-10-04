# Bài giảng 7C: Thuật toán sắp xếp cơ bản

## 📋 Thông tin bài học
- **Thời gian**: 90 phút
- **Độ tuổi**: 10-11 tuổi
- **Trình độ**: Trung bình đến nâng cao
- **Mục tiêu**: Hiểu và áp dụng thuật toán sắp xếp cơ bản vào Scratch

## 🎯 Mục tiêu học tập

### Kiến thức
- Hiểu khái niệm sắp xếp và tầm quan trọng
- Nắm vững thuật toán sắp xếp nổi bọt (Bubble Sort)
- Hiểu thuật toán sắp xếp chọn (Selection Sort)
- Biết cách so sánh hiệu suất các thuật toán

### Kỹ năng
- Phân tích và thiết kế thuật toán sắp xếp
- Áp dụng thuật toán sắp xếp vào lập trình Scratch
- Sử dụng vòng lặp lồng nhau hiệu quả
- Debug và tối ưu hóa code sắp xếp

### Thái độ
- Phát triển tư duy logic phức tạp
- Rèn luyện tính kiên trì với thuật toán khó
- Khuyến khích tư duy phản biện và so sánh

## 🧠 Nội dung bài học

## 📚 PHẦN LÝ THUYẾT (45 phút)

### Phần 1: Khái niệm sắp xếp qua hoạt động không máy tính (25 phút)

#### Hoạt động khởi động - "Kết nối với bài trước"
- **Hoạt động**: Nhắc lại bài 7A về thuật toán tìm max và đếm
- **Câu hỏi**: "Chúng ta đã học cách tìm số lớn nhất như thế nào?"
- **Kết nối**: "Hôm nay chúng ta sẽ học cách sắp xếp tất cả số theo thứ tự"
- **Mục tiêu**: Kết nối thuật toán cơ bản với sắp xếp

#### Khái niệm sắp xếp qua ví dụ thực tế
- **Định nghĩa**: Sắp xếp là sắp đặt các phần tử theo một thứ tự nhất định
- **Ví dụ**: Sắp xếp sách theo thứ tự ABC, sắp xếp điểm từ cao đến thấp
- **Input**: Danh sách không có thứ tự [8, 3, 1, 9, 5]
- **Output**: Danh sách có thứ tự [1, 3, 5, 8, 9]
- **Ứng dụng**: Tìm kiếm nhanh, hiển thị dữ liệu đẹp mắt

#### Hoạt động thực hành - "Sắp xếp học sinh theo chiều cao"
- **Hoạt động**: Học sinh đứng thành hàng, sắp xếp theo chiều cao từ thấp đến cao
- **Mục tiêu**: Hiểu khái niệm sắp xếp qua trải nghiệm thực tế
- **Quy tắc**: Chỉ được so sánh 2 người cạnh nhau, nếu sai thứ tự thì đổi chỗ
- **Kết quả**: Nhận ra sắp xếp cần nhiều bước so sánh và đổi chỗ

### Phần 2: Thuật toán sắp xếp nổi bọt qua hoạt động không máy tính (20 phút)

#### Hoạt động không máy tính - "Sắp xếp thẻ số"
- **Hoạt động**: Học sinh sử dụng thẻ số để mô phỏng thuật toán sắp xếp nổi bọt
- **Mục tiêu**: Hiểu cách thuật toán sắp xếp nổi bọt hoạt động
- **Quy tắc**: So sánh từng cặp số cạnh nhau, đổi chỗ nếu sai thứ tự
- **Kết quả**: Nhận ra số lớn "nổi" lên trên như bong bóng

#### Bài toán: Sắp xếp điểm số từ cao đến thấp
- **Input**: Danh sách điểm [8, 9, 7, 10, 6]
- **Output**: Danh sách đã sắp xếp [10, 9, 8, 7, 6]
- **Ví dụ**: Sắp xếp điểm của lớp từ cao đến thấp

#### Thuật toán sắp xếp nổi bọt qua ví dụ thực tế
```
Lần 1: So sánh từng cặp
- 8 vs 9: 8 < 9, giữ nguyên → [8, 9, 7, 10, 6]
- 9 vs 7: 9 > 7, đổi chỗ → [8, 7, 9, 10, 6]
- 9 vs 10: 9 < 10, giữ nguyên → [8, 7, 9, 10, 6]
- 10 vs 6: 10 > 6, đổi chỗ → [8, 7, 9, 6, 10]

Lần 2: Lặp lại quá trình
- 8 vs 7: 8 > 7, đổi chỗ → [7, 8, 9, 6, 10]
- 8 vs 9: 8 < 9, giữ nguyên → [7, 8, 9, 6, 10]
- 9 vs 6: 9 > 6, đổi chỗ → [7, 8, 6, 9, 10]

Tiếp tục cho đến khi hoàn thành...
```

#### Hoạt động không máy tính - "Đếm số lần đổi chỗ"
- **Hoạt động**: Học sinh đếm số lần phải đổi chỗ để sắp xếp hoàn chỉnh
- **Mục tiêu**: Hiểu độ phức tạp của thuật toán sắp xếp
- **Kết quả**: Nhận ra sắp xếp cần nhiều bước và thời gian

## 💻 PHẦN THỰC HÀNH SCRATCH (45 phút)

### Phần 3: Tạo game "Sắp xếp nổi bọt" trên Scratch (25 phút)

#### Bước 1: Tạo các biến và list cần thiết
```scratch
# Tạo các biến sau:
1. Biến "isSorted" - để kiểm tra xem danh sách đã được sắp xếp chưa
2. Biến "i" - để làm chỉ số duyệt qua danh sách
3. Biến "temp" - để lưu tạm giá trị khi đổi chỗ
4. List "DanhSach" - để chứa các số cần sắp xếp
```

#### Bước 2: Lập trình thuật toán sắp xếp nổi bọt
```scratch
# Khởi tạo dữ liệu
Khi cờ xanh được nhấn
xóa tất cả trong [DanhSach v]
thêm [8] vào [DanhSach v]
thêm [9] vào [DanhSach v]
thêm [7] vào [DanhSach v]
thêm [10] vào [DanhSach v]
thêm [6] vào [DanhSach v]
nói [Trước khi sắp xếp: ] + [DanhSach v] trong (3) giây

# Thuật toán sắp xếp nổi bọt
đặt [isSorted v] thành [0]
lặp lại cho đến khi <[isSorted v] = [1]>
  đặt [isSorted v] thành [1]
  đặt [i v] thành [1]
  lặp lại ((chiều dài của [DanhSach v]) - (1)) lần
    nếu <(mục (i) của [DanhSach v]) > (mục ((i) + (1)) của [DanhSach v])> thì
      phát âm thanh [pop v]
      đặt [temp v] thành (mục (i) của [DanhSach v])
      thay thế mục (i) của [DanhSach v] bằng (mục ((i) + (1)) của [DanhSach v])
      thay thế mục ((i) + (1)) của [DanhSach v] bằng [temp v]
      đặt [isSorted v] thành [0]
      nói [Đã đổi chỗ mục ] + [i v] + [ và ] + ((i) + (1)) trong (1) giây
    thay đổi [i v] bởi (1)
  nói [Kết quả sau lần này: ] + [DanhSach v] trong (2) giây

nói [Sau khi sắp xếp: ] + [DanhSach v] trong (3) giây
```

#### Hoạt động mở rộng - "Sắp xếp ngược"
- **Hoạt động**: Thay đổi thuật toán để sắp xếp từ thấp đến cao
- **Mục tiêu**: Hiểu cách điều chỉnh điều kiện so sánh
- **Thử thách**: Tạo thuật toán sắp xếp theo nhiều tiêu chí khác nhau

#### Giải thích các Scratch blocks quan trọng:
```scratch
# List blocks:
- "xóa tất cả trong [DanhSach v]" - Xóa toàn bộ danh sách
- "thêm [8] vào [DanhSach v]" - Thêm phần tử vào cuối danh sách
- "(mục (i) của [DanhSach v])" - Lấy giá trị tại vị trí i
- "thay thế mục (i) của [DanhSach v] bằng [temp v]" - Thay đổi giá trị tại vị trí i
- "(chiều dài của [DanhSach v])" - Lấy số phần tử trong danh sách

# Control blocks:
- "lặp lại cho đến khi <[isSorted v] = [1]>" - Vòng lặp với điều kiện dừng
- "lặp lại ((chiều dài của [DanhSach v]) - (1)) lần" - Vòng lặp với số lần cố định
- "nếu <(mục (i) của [DanhSach v]) > (mục ((i) + (1)) của [DanhSach v])> thì" - Điều kiện so sánh

# Variable blocks:
- "đặt [i v] thành [1]" - Gán giá trị cho biến
- "thay đổi [i v] bởi (1)" - Tăng giá trị biến lên 1
```

### Phần 4: Tạo game "Sắp xếp chọn" trên Scratch (20 phút)

#### Bước 1: Tạo các biến cần thiết cho Selection Sort
```scratch
# Tạo các biến sau:
1. Biến "i" - chỉ số vị trí hiện tại
2. Biến "j" - chỉ số để duyệt qua các phần tử còn lại
3. Biến "minIndex" - vị trí của phần tử nhỏ nhất
4. Biến "temp" - để lưu tạm giá trị khi đổi chỗ
5. List "DanhSach" - danh sách cần sắp xếp
```

#### Bước 2: Lập trình thuật toán sắp xếp chọn
```scratch
# Thuật toán sắp xếp chọn
Khi cờ xanh được nhấn
xóa tất cả trong [DanhSach v]
thêm [8] vào [DanhSach v]
thêm [9] vào [DanhSach v]
thêm [7] vào [DanhSach v]
thêm [10] vào [DanhSach v]
thêm [6] vào [DanhSach v]
nói [Trước khi sắp xếp: ] + [DanhSach v] trong (3) giây

# Sắp xếp chọn
đặt [i v] thành [1]
lặp lại ((chiều dài của [DanhSach v]) - (1)) lần
  đặt [minIndex v] thành [i v]
  đặt [j v] thành ((i) + (1))
  lặp lại ((chiều dài của [DanhSach v]) - (i)) lần
    nếu <(mục (j) của [DanhSach v]) < (mục (minIndex) của [DanhSach v])> thì
      đặt [minIndex v] thành [j v]
    thay đổi [j v] bởi (1)
  
  # Đổi chỗ nếu cần
  nếu <[minIndex v] ≠ [i v]> thì
    phát âm thanh [pop v]
    đặt [temp v] thành (mục (i) của [DanhSach v])
    thay thế mục (i) của [DanhSach v] bằng (mục (minIndex) của [DanhSach v])
    thay thế mục (minIndex) của [DanhSach v] bằng [temp v]
    nói [Đã đổi chỗ mục ] + [i v] + [ và ] + [minIndex v] trong (1) giây
  
  thay đổi [i v] bởi (1)
  nói [Kết quả sau lần này: ] + [DanhSach v] trong (2) giây

nói [Sau khi sắp xếp: ] + [DanhSach v] trong (3) giây
```

#### Hoạt động mở rộng - "So sánh hiệu suất"
- **Hoạt động**: So sánh số lần đổi chỗ giữa sắp xếp nổi bọt và sắp xếp chọn
- **Mục tiêu**: Hiểu cách đánh giá hiệu suất thuật toán
- **Thử thách**: Tạo thuật toán sắp xếp riêng

## 🎯 Tổng kết và đánh giá (10 phút)

### Tổng kết kiến thức
- **Sắp xếp**: Sắp đặt các phần tử theo thứ tự nhất định
- **Sắp xếp nổi bọt**: So sánh từng cặp và đổi chỗ nếu sai thứ tự
- **Sắp xếp chọn**: Tìm phần tử nhỏ nhất và đặt vào vị trí đúng
- **Hiệu suất**: Các thuật toán có hiệu suất khác nhau
- **Ứng dụng**: Sắp xếp có mặt khắp nơi trong cuộc sống

### Đánh giá học sinh
- **Hiểu thuật toán**: Có thể giải thích các bước của thuật toán sắp xếp
- **Áp dụng thực tế**: Tìm được ví dụ sắp xếp trong cuộc sống
- **Lập trình Scratch**: Tạo được chương trình sắp xếp hoạt động
- **Tư duy logic**: Phân tích và so sánh hiệu suất thuật toán

## 🎨 Hoạt động mở rộng

### Cấp độ 1: Thêm tính năng cơ bản
- **Giao diện tương tác**: Tạo nút để nhập dữ liệu mới
- **Hiệu ứng trực quan**: Thêm màu sắc và animation khi sắp xếp
- **Âm thanh**: Tạo âm thanh khác nhau cho từng loại sắp xếp

### Cấp độ 2: Tính năng nâng cao
- **Sắp xếp nhiều phần tử**: Mở rộng thuật toán cho 10 số
- **Sắp xếp thông minh**: Sắp xếp theo nhiều tiêu chí
- **So sánh hiệu suất**: So sánh tốc độ của các thuật toán khác nhau

### Cấp độ 3: Sáng tạo
- **Game sắp xếp**: Tạo trò chơi sắp xếp thẻ bài
- **Thuật toán riêng**: Thiết kế thuật toán sắp xếp mới
- **Dự án tích hợp**: Kết hợp sắp xếp với các thuật toán đã học

## 📝 Bài tập về nhà

### Bài tập bắt buộc
1. **Sắp xếp điểm số**: Viết thuật toán sắp xếp điểm từ cao đến thấp
2. **Sắp xếp tên**: Tạo chương trình sắp xếp tên học sinh theo ABC
3. **So sánh thuật toán**: So sánh số lần đổi chỗ giữa 2 thuật toán

### Bài tập nâng cao
1. **Sắp xếp phức tạp**: Sắp xếp danh sách có 10 phần tử
2. **Sắp xếp thông minh**: Sắp xếp theo nhiều tiêu chí
3. **Tối ưu hóa**: Tìm cách giảm số lần so sánh

### Bài tập sáng tạo
1. **Game sắp xếp**: Tạo game sắp xếp với giao diện đẹp
2. **Thuật toán riêng**: Thiết kế thuật toán sắp xếp độc đáo
3. **Dự án tích hợp**: Kết hợp sắp xếp với tìm kiếm và đếm

## 🔧 Tài nguyên hỗ trợ

### Tài liệu tham khảo
- **Scratch Programming**: Hướng dẫn lập trình Scratch cơ bản
- **Algorithm Visualization**: Công cụ minh họa thuật toán sắp xếp
- **Sorting Algorithms**: Các thuật toán sắp xếp phổ biến

### Công cụ hỗ trợ
- **Scratch Editor**: Môi trường lập trình trực quan
- **Algorithm Simulator**: Mô phỏng thuật toán sắp xếp
- **Debugging Tools**: Công cụ gỡ lỗi và tối ưu hóa

### Đánh giá và phản hồi
- **Rubric đánh giá**: Tiêu chí đánh giá kỹ năng sắp xếp
- **Peer Review**: Đánh giá lẫn nhau giữa học sinh
- **Portfolio**: Tập hợp các dự án và bài tập của học sinh
