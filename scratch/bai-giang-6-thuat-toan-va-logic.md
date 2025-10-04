# Bài Giảng 6: Thuật Toán Và Logic Lập Trình

## 📋 Thông tin bài học
- **Thời gian**: 90 phút (2 tiết)
- **Độ tuổi**: Lớp 4-5 (9-11 tuổi)
- **Mức độ**: Trung bình đến nâng cao
- **Mục tiêu**: Phát triển tư duy thuật toán và logic để chuẩn bị cho Python

## 🎯 Mục tiêu học tập

### Kiến thức
- Hiểu khái niệm thuật toán và cách hoạt động
- Biết cách chia nhỏ vấn đề thành các bước
- Hiểu các cấu trúc điều khiển cơ bản

### Kỹ năng
- Phân tích và giải quyết vấn đề
- Thiết kế thuật toán đơn giản
- Debug và tối ưu hóa code

### Thái độ
- Phát triển tư duy logic
- Rèn luyện tính kiên trì
- Khuyến khích tư duy phản biện


## 🧠 Nội dung bài học

### Phần 1: Giới thiệu thuật toán qua hoạt động không máy tính (15 phút)

#### Hoạt động khởi động - "Hướng dẫn bạn làm bánh sandwich"
- **Hoạt động**: Học sinh A hướng dẫn học sinh B làm bánh sandwich mà không được nhìn
- **Mục tiêu**: Hiểu tầm quan trọng của hướng dẫn chính xác và logic
- **Kết quả**: Nhận ra cần hướng dẫn từng bước cụ thể

#### Ví dụ thuật toán từ cuộc sống
```
Thuật toán làm bánh sandwich:
Bước 1: Lấy 2 lát bánh mì
Bước 2: Phết bơ lên lát bánh thứ nhất
Bước 3: Đặt thịt lên lát bánh có bơ
Bước 4: Đặt rau lên thịt
Bước 5: Đặt lát bánh thứ hai lên trên
Bước 6: Cắt đôi bánh sandwich
```

#### Khái niệm cơ bản qua ví dụ
- **Input**: Nguyên liệu (bánh mì, bơ, thịt, rau)
- **Process**: Các bước chế biến (phết bơ, đặt thịt...)
- **Output**: Bánh sandwich hoàn chỉnh
- **Đặc điểm**: Các bước phải rõ ràng, có thứ tự, có thể lặp lại

### Phần 2: Thuật toán sắp xếp qua trò chơi thực tế (25 phút)

#### Hoạt động không máy tính - "Sắp xếp học sinh theo chiều cao"
- **Hoạt động**: Yêu cầu học sinh đứng thành hàng theo chiều cao từ thấp đến cao
- **Mục tiêu**: Hiểu thuật toán sắp xếp bằng cách so sánh và đổi chỗ
- **Quy tắc**: Chỉ được so sánh 2 người cạnh nhau, nếu sai thứ tự thì đổi chỗ

#### Bài toán: Sắp xếp 3 số từ nhỏ đến lớn
- **Input**: 3 số bất kỳ (ví dụ: 5, 2, 8)
- **Output**: 3 số đã sắp xếp (2, 5, 8)
- **Ví dụ**: Sắp xếp điểm số của 3 bạn trong lớp

#### Thuật toán Bubble Sort qua ví dụ thực tế
```
Bước 1: So sánh bạn A và bạn B
Bước 2: Nếu bạn A cao hơn bạn B, đổi chỗ
Bước 3: So sánh bạn B và bạn C
Bước 4: Nếu bạn B cao hơn bạn C, đổi chỗ
Bước 5: Lặp lại cho đến khi không còn đổi chỗ nào
```

#### Vẽ sơ đồ thuật toán trước khi lập trình
```
[Start] → [So sánh số 1 và số 2] → [Số 1 > Số 2?] → [Có: Đổi chỗ] → [Không: Giữ nguyên]
    ↓
[So sánh số 2 và số 3] → [Số 2 > Số 3?] → [Có: Đổi chỗ] → [Không: Giữ nguyên]
    ↓
[Còn đổi chỗ?] → [Có: Lặp lại] → [Không: Kết thúc]
```

#### Lập trình trong Scratch với hiệu ứng trực quan
```scratch
Khi cờ xanh được nhấn
đặt [So1 v] thành (5)
đặt [So2 v] thành (2)
đặt [So3 v] thành (8)
nói [Trước khi sắp xếp: ] + [So1 v] + [, ] + [So2 v] + [, ] + [So3 v] trong (3) giây
chờ (2) giây
```

#### Thuật toán sắp xếp với hiệu ứng âm thanh
```scratch
lặp lại (3) lần
nếu <[So1 v] > [So2 v]> thì
phát âm thanh [pop v]
đặt [Temp v] thành [So1 v]
đặt [So1 v] thành [So2 v]
đặt [So2 v] thành [Temp v]
nói [Đã đổi chỗ số 1 và số 2] trong (2) giây
nếu <[So2 v] > [So3 v]> thì
phát âm thanh [pop v]
đặt [Temp v] thành [So2 v]
đặt [So2 v] thành [So3 v]
đặt [So3 v] thành [Temp v]
nói [Đã đổi chỗ số 2 và số 3] trong (2) giây
nói [Sau khi sắp xếp: ] + [So1 v] + [, ] + [So2 v] + [, ] + [So3 v] trong (3) giây
```

### Phần 3: Thuật toán tìm kiếm qua trò chơi "Tìm kho báu" (20 phút)

#### Hoạt động không máy tính - "Tìm bạn cao nhất trong lớp"
- **Hoạt động**: Học sinh đứng thành vòng tròn, tìm bạn cao nhất
- **Quy tắc**: Chỉ được so sánh với người bên cạnh, đi theo chiều kim đồng hồ
- **Mục tiêu**: Hiểu thuật toán tìm kiếm tuyến tính

#### Bài toán: Tìm số lớn nhất trong danh sách điểm số
- **Input**: Danh sách điểm của lớp [8, 9, 7, 10, 6]
- **Output**: Điểm cao nhất (10)
- **Ví dụ**: Tìm học sinh có điểm cao nhất trong lớp

#### Thuật toán tìm kiếm tuyến tính qua ví dụ thực tế
```
Bước 1: Giả sử điểm đầu tiên là cao nhất (8)
Bước 2: So sánh với điểm tiếp theo (9)
Bước 3: Vì 9 > 8, cập nhật điểm cao nhất = 9
Bước 4: So sánh với điểm tiếp theo (7)
Bước 5: Vì 7 < 9, giữ nguyên điểm cao nhất = 9
Bước 6: Tiếp tục cho đến hết danh sách
```

#### Vẽ sơ đồ thuật toán
```
[Start] → [Đặt điểm cao nhất = điểm đầu tiên] → [So sánh với điểm tiếp theo]
    ↓
[Điểm tiếp theo > điểm cao nhất?] → [Có: Cập nhật điểm cao nhất] → [Không: Giữ nguyên]
    ↓
[Còn điểm nào?] → [Có: Tiếp tục] → [Không: Kết thúc]
```

#### Lập trình trong Scratch với hiệu ứng trực quan
```scratch
Khi cờ xanh được nhấn
đặt [DanhSachDiem v] thành [8,9,7,10,6]
nói [Danh sách điểm: ] + [DanhSachDiem v] trong (3) giây
chờ (2) giây
đặt [DiemCaoNhat v] thành (8)
đặt [ViTri v] thành (1)
nói [Giả sử điểm cao nhất là: ] + [DiemCaoNhat v] trong (2) giây
```

#### Thuật toán tìm kiếm với hiệu ứng âm thanh
```scratch
lặp lại (5) lần
nếu <(mục (ViTri) của [DanhSachDiem v]) > [DiemCaoNhat v]> thì
phát âm thanh [pop v]
đặt [DiemCaoNhat v] thành (mục (ViTri) của [DanhSachDiem v])
nói [Tìm thấy điểm cao hơn: ] + [DiemCaoNhat v] trong (2) giây
nếu không
nói [Điểm ] + (mục (ViTri) của [DanhSachDiem v]) + [ không cao hơn] trong (1) giây
thay đổi [ViTri v] bởi (1)
chờ (1) giây
nói [Điểm cao nhất trong lớp là: ] + [DiemCaoNhat v] trong (3) giây
```

### Phần 4: Thuật toán đếm và thống kê qua trò chơi "Đếm đồ vật" (20 phút)

#### Hoạt động không máy tính - "Đếm số bạn nam và nữ trong lớp"
- **Hoạt động**: Học sinh đứng thành hàng, đếm số bạn nam và nữ
- **Quy tắc**: Đi từ đầu đến cuối hàng, đếm từng người một
- **Mục tiêu**: Hiểu thuật toán đếm và phân loại

#### Bài toán: Đếm số học sinh giỏi trong lớp
- **Input**: Danh sách điểm [8, 9, 7, 10, 6, 9, 8, 7]
- **Output**: Số học sinh có điểm >= 8 (4 học sinh)
- **Ví dụ**: Thống kê số học sinh đạt loại giỏi

#### Thuật toán đếm qua ví dụ thực tế
```
Bước 1: Khởi tạo biến đếm = 0
Bước 2: Xem điểm của bạn đầu tiên (8)
Bước 3: Vì 8 >= 8, tăng biến đếm lên 1
Bước 4: Xem điểm của bạn tiếp theo (9)
Bước 5: Vì 9 >= 8, tăng biến đếm lên 2
Bước 6: Tiếp tục cho đến hết danh sách
```

#### Vẽ sơ đồ thuật toán
```
[Start] → [Đặt đếm = 0] → [Xem điểm tiếp theo]
    ↓
[Điểm >= 8?] → [Có: Tăng đếm lên 1] → [Không: Giữ nguyên đếm]
    ↓
[Còn điểm nào?] → [Có: Tiếp tục] → [Không: Hiển thị kết quả]
```

#### Lập trình trong Scratch với hiệu ứng trực quan
```scratch
Khi cờ xanh được nhấn
đặt [DanhSachDiem v] thành [8,9,7,10,6,9,8,7]
nói [Danh sách điểm lớp: ] + [DanhSachDiem v] trong (3) giây
chờ (2) giây
đặt [DemHocSinhGioi v] thành (0)
đặt [ViTri v] thành (1)
nói [Bắt đầu đếm học sinh giỏi (điểm >= 8)...] trong (2) giây
```

#### Thuật toán đếm với hiệu ứng âm thanh
```scratch
lặp lại (8) lần
nếu <(mục (ViTri) của [DanhSachDiem v]) >= [8]> thì
phát âm thanh [pop v]
thay đổi [DemHocSinhGioi v] bởi (1)
nói [Điểm ] + (mục (ViTri) của [DanhSachDiem v]) + [ - Đạt loại giỏi!] trong (2) giây
nếu không
nói [Điểm ] + (mục (ViTri) của [DanhSachDiem v]) + [ - Chưa đạt loại giỏi] trong (1) giây
thay đổi [ViTri v] bởi (1)
chờ (1) giây
nói [Tổng số học sinh giỏi: ] + [DemHocSinhGioi v] + [ học sinh] trong (3) giây
```

### Phần 5: Thuật toán tính toán qua trò chơi "Xây tháp" (10 phút)

#### Hoạt động không máy tính - "Xây tháp bằng khối LEGO"
- **Hoạt động**: Xây tháp 5 tầng bằng khối LEGO
- **Quy tắc**: Tầng 1 có 1 khối, tầng 2 có 2 khối, tầng 3 có 3 khối...
- **Mục tiêu**: Hiểu thuật toán tính tổng và giai thừa

#### Bài toán: Tính tổng điểm của lớp
- **Input**: Số học sinh n = 5
- **Output**: Tổng điểm từ 1 đến 5 = 1+2+3+4+5 = 15
- **Ví dụ**: Tính tổng điểm của 5 học sinh đầu tiên

#### Thuật toán tính tổng qua ví dụ thực tế
```
Bước 1: Khởi tạo tổng = 0
Bước 2: Thêm điểm học sinh 1 (1) vào tổng → tổng = 1
Bước 3: Thêm điểm học sinh 2 (2) vào tổng → tổng = 3
Bước 4: Thêm điểm học sinh 3 (3) vào tổng → tổng = 6
Bước 5: Tiếp tục cho đến học sinh thứ 5
```

#### Lập trình trong Scratch với hiệu ứng trực quan
```scratch
Khi cờ xanh được nhấn
đặt [SoHocSinh v] thành (5)
nói [Tính tổng điểm của ] + [SoHocSinh v] + [ học sinh đầu tiên] trong (3) giây
chờ (2) giây
đặt [TongDiem v] thành (0)
đặt [i v] thành (1)
nói [Bắt đầu tính tổng...] trong (2) giây
```

#### Thuật toán tính tổng với hiệu ứng âm thanh
```scratch
lặp lại ([SoHocSinh v]) lần
phát âm thanh [pop v]
thay đổi [TongDiem v] bởi ([i v])
nói [Học sinh ] + [i v] + [ có điểm ] + [i v] + [. Tổng hiện tại: ] + [TongDiem v] trong (2) giây
thay đổi [i v] bởi (1)
chờ (1) giây
nói [Tổng điểm của ] + [SoHocSinh v] + [ học sinh là: ] + [TongDiem v] trong (3) giây
```

## 🎨 Hoạt động mở rộng

### Cấp độ 1: Thêm tính năng cơ bản
- **Giao diện tương tác**: Tạo nút để nhập dữ liệu mới
- **Hiệu ứng trực quan**: Thêm màu sắc và animation khi sắp xếp
- **Âm thanh**: Tạo âm thanh khác nhau cho từng loại thuật toán

### Cấp độ 2: Tính năng nâng cao
- **Sắp xếp nhiều phần tử**: Mở rộng thuật toán cho 10 số
- **Tìm kiếm thông minh**: Tìm kiếm với nhiều điều kiện
- **Thống kê nâng cao**: Tính điểm trung bình, độ lệch chuẩn

### Cấp độ 3: Sáng tạo
- **Game thuật toán**: Tạo trò chơi sắp xếp thẻ bài
- **Thuật toán riêng**: Thiết kế thuật toán giải quyết vấn đề thực tế
- **Dự án tích hợp**: Kết hợp nhiều thuật toán trong một dự án lớn

## 📝 Bài tập về nhà

### Bài tập bắt buộc
1. **Sắp xếp điểm số**: Viết thuật toán sắp xếp 5 điểm số từ cao đến thấp
2. **Tìm học sinh giỏi nhất**: Tạo chương trình tìm học sinh có điểm cao nhất
3. **Tính điểm trung bình**: Tính điểm trung bình của lớp học

### Bài tập nâng cao
1. **Sắp xếp thông minh**: Sắp xếp danh sách học sinh theo điểm từ cao đến thấp
2. **Thống kê lớp học**: Tìm số học sinh đạt loại giỏi, khá, trung bình
3. **Thuật toán riêng**: Thiết kế thuật toán giải quyết vấn đề thực tế (ví dụ: sắp xếp lịch học)

## 🔍 Đánh giá

### Tiêu chí đánh giá
| Tiêu chí | Điểm | Mô tả |
|----------|------|-------|
| Hiểu thuật toán | 3 | Giải thích được các bước thuật toán |
| Lập trình đúng | 3 | Code hoạt động chính xác |
| Tối ưu hóa | 2 | Thuật toán hiệu quả |
| Sáng tạo | 1 | Có yếu tố độc đáo |
| Trình bày | 1 | Giải thích rõ ràng |
| Tổng cộng | 10 | |

### Cách đánh giá
- **Quan sát**: Giáo viên quan sát quá trình tư duy
- **Sản phẩm**: Kiểm tra thuật toán hoàn chỉnh
- **Trình bày**: Học sinh giải thích thuật toán
- **Phản hồi**: Nhận xét từ bạn cùng lớp

## 🚀 Lưu ý quan trọng

### Cho giáo viên
- Khuyến khích học sinh vẽ sơ đồ thuật toán
- Giải thích từng bước một cách chi tiết
- Tạo không khí học tập tích cực
- Chuẩn bị nhiều ví dụ thực tế

### Cho học sinh
- Vẽ sơ đồ trước khi lập trình
- Hiểu rõ từng bước thuật toán
- Không ngại thử nghiệm và sai lầm
- Lưu dự án thường xuyên

## 💡 Mẹo hay

### Thiết kế thuật toán
- **Chia nhỏ vấn đề**: Phân tích bài toán thành các bước nhỏ
- **Vẽ sơ đồ trước**: Sử dụng sơ đồ khối để hình dung thuật toán
- **Test với dữ liệu mẫu**: Kiểm tra thuật toán với các trường hợp khác nhau

### Debug hiệu quả
- **Sử dụng "say"**: Thêm lệnh nói để theo dõi giá trị biến
- **Kiểm tra từng bước**: Debug từng phần một thay vì toàn bộ
- **Test với các trường hợp**: Kiểm tra với dữ liệu khác nhau

### Tối ưu hóa
- **Giảm số bước**: Tìm cách làm thuật toán ngắn gọn hơn
- **Sử dụng biến tạm**: Dùng biến tạm để lưu giá trị trung gian
- **Tránh lặp lại**: Không lặp lại các phép tính không cần thiết

### Phương pháp học hiệu quả
- **Hoạt động không máy tính**: Thực hành thuật toán bằng tay trước
- **Ví dụ từ cuộc sống**: Liên hệ với các tình huống thực tế
- **Làm việc nhóm**: Thảo luận và chia sẻ ý tưởng với bạn bè

## 🔗 Kết nối với Python

### Khái niệm tương đồng
- **Biến**: Scratch variables ↔ Python variables
- **Vòng lặp**: Scratch loops ↔ Python for/while
- **Điều kiện**: Scratch if/else ↔ Python if/else
- **Danh sách**: Scratch lists ↔ Python lists

### Chuẩn bị cho Python
- Hiểu cú pháp cơ bản
- Làm quen với môi trường lập trình
- Thực hành với các bài toán đơn giản

## 📚 Tài liệu tham khảo

- [Unplugged Activities for Teaching Algorithms](https://missmorenakos.com/education/algorithm-activities/)
- [Teaching Algorithmic Thinking](https://codinginmathclass.wordpress.com/2014/09/10/how-to-teach-algorithmic-thinking/)
- [Computational Thinking in Scratch](https://www.lifeinthetechlab.com/teacher/compThinking/)
- [Scratch Algorithm Projects](https://scratch.mit.edu/explore/projects/algorithms)
- [Introduction to Algorithms](https://scratch.mit.edu/tutorials)
- [Python for Kids](https://python.org)

---

**Tác giả**: AI & Trần Việt Trung (BKHN)  
**Ngày tạo**: 04/10/2025  
**Phiên bản**: 1.0
