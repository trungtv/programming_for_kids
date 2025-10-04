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

#### Lập trình trong Scratch với hiệu ứng trực quan
```scratch
# Khởi tạo dữ liệu
Khi cờ xanh được nhấn
đặt [So1 v] thành [8]
đặt [So2 v] thành [9]
đặt [So3 v] thành [7]
đặt [So4 v] thành [10]
đặt [So5 v] thành [6]
nói [Trước khi sắp xếp: ] + [So1 v] + [, ] + [So2 v] + [, ] + [So3 v] + [, ] + [So4 v] + [, ] + [So5 v] trong (3) giây

# Thuật toán sắp xếp nổi bọt
lặp lại (4) lần
  nếu <[So1 v] < [So2 v]> thì
    phát âm thanh [pop v]
    đặt [Temp v] thành [So1 v]
    đặt [So1 v] thành [So2 v]
    đặt [So2 v] thành [Temp v]
    nói [Đã đổi chỗ số 1 và số 2] trong (1) giây
  
  nếu <[So2 v] < [So3 v]> thì
    phát âm thanh [pop v]
    đặt [Temp v] thành [So2 v]
    đặt [So2 v] thành [So3 v]
    đặt [So3 v] thành [Temp v]
    nói [Đã đổi chỗ số 2 và số 3] trong (1) giây
  
  nếu <[So3 v] < [So4 v]> thì
    phát âm thanh [pop v]
    đặt [Temp v] thành [So3 v]
    đặt [So3 v] thành [So4 v]
    đặt [So4 v] thành [Temp v]
    nói [Đã đổi chỗ số 3 và số 4] trong (1) giây
  
  nếu <[So4 v] < [So5 v]> thì
    phát âm thanh [pop v]
    đặt [Temp v] thành [So4 v]
    đặt [So4 v] thành [So5 v]
    đặt [So5 v] thành [Temp v]
    nói [Đã đổi chỗ số 4 và số 5] trong (1) giây
  
  nói [Kết quả sau lần này: ] + [So1 v] + [, ] + [So2 v] + [, ] + [So3 v] + [, ] + [So4 v] + [, ] + [So5 v] trong (2) giây

nói [Sau khi sắp xếp: ] + [So1 v] + [, ] + [So2 v] + [, ] + [So3 v] + [, ] + [So4 v] + [, ] + [So5 v] trong (3) giây
```

#### Hoạt động mở rộng - "Sắp xếp ngược"
- **Hoạt động**: Thay đổi thuật toán để sắp xếp từ thấp đến cao
- **Mục tiêu**: Hiểu cách điều chỉnh điều kiện so sánh
- **Thử thách**: Tạo thuật toán sắp xếp theo nhiều tiêu chí khác nhau

### Phần 4: Tạo game "Sắp xếp chọn" trên Scratch (20 phút)

#### Hoạt động không máy tính - "Tìm số nhỏ nhất"
- **Hoạt động**: Học sinh tìm số nhỏ nhất trong danh sách và đặt lên đầu
- **Mục tiêu**: Hiểu thuật toán sắp xếp chọn
- **Quy tắc**: Tìm số nhỏ nhất, đổi chỗ với vị trí đầu tiên
- **Kết quả**: Nhận ra cách sắp xếp chọn hiệu quả hơn

#### Lập trình trong Scratch với hiệu ứng trực quan
```scratch
# Thuật toán sắp xếp chọn
Khi cờ xanh được nhấn
đặt [So1 v] thành [8]
đặt [So2 v] thành [9]
đặt [So3 v] thành [7]
đặt [So4 v] thành [10]
đặt [So5 v] thành [6]
nói [Trước khi sắp xếp: ] + [So1 v] + [, ] + [So2 v] + [, ] + [So3 v] + [, ] + [So4 v] + [, ] + [So5 v] trong (3) giây

# Tìm số nhỏ nhất và đổi chỗ
đặt [ViTriNhoNhat v] thành [1]
đặt [SoNhoNhat v] thành [So1 v]

# Tìm số nhỏ nhất
nếu <[So2 v] < [SoNhoNhat v]> thì
  đặt [SoNhoNhat v] thành [So2 v]
  đặt [ViTriNhoNhat v] thành [2]

nếu <[So3 v] < [SoNhoNhat v]> thì
  đặt [SoNhoNhat v] thành [So3 v]
  đặt [ViTriNhoNhat v] thành [3]

nếu <[So4 v] < [SoNhoNhat v]> thì
  đặt [SoNhoNhat v] thành [So4 v]
  đặt [ViTriNhoNhat v] thành [4]

nếu <[So5 v] < [SoNhoNhat v]> thì
  đặt [SoNhoNhat v] thành [So5 v]
  đặt [ViTriNhoNhat v] thành [5]

# Đổi chỗ số nhỏ nhất với vị trí đầu tiên
nếu <[ViTriNhoNhat v] = [2]> thì
  đặt [Temp v] thành [So1 v]
  đặt [So1 v] thành [So2 v]
  đặt [So2 v] thành [Temp v]

nói [Số nhỏ nhất là: ] + [SoNhoNhat v] + [ ở vị trí ] + [ViTriNhoNhat v] trong (2) giây
nói [Kết quả: ] + [So1 v] + [, ] + [So2 v] + [, ] + [So3 v] + [, ] + [So4 v] + [, ] + [So5 v] trong (2) giây
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
