# Bài giảng 7E: Thuật toán tìm kiếm trong danh sách

## 📋 Thông tin bài học
- **Thời gian**: 90 phút
- **Độ tuổi**: 10-11 tuổi
- **Trình độ**: Trung bình
- **Mục tiêu**: Hiểu và áp dụng thuật toán tìm kiếm để tìm phần tử trong danh sách

## 🎯 Mục tiêu học tập

### Kiến thức
- Hiểu khái niệm tìm kiếm trong danh sách
- Nắm vững thuật toán tìm kiếm tuyến tính (Linear Search)
- Hiểu cách tìm vị trí của phần tử trong danh sách
- Biết cách xử lý trường hợp không tìm thấy

### Kỹ năng
- Thiết kế thuật toán tìm kiếm
- Áp dụng tìm kiếm vào lập trình Scratch
- Sử dụng biến và vòng lặp hiệu quả
- Xử lý các trường hợp đặc biệt

### Thái độ
- Phát triển tư duy logic
- Rèn luyện tính kiên trì
- Khuyến khích tư duy phản biện

## 🧠 Nội dung bài học

## 📚 PHẦN LÝ THUYẾT (45 phút)

### Phần 1: Khái niệm tìm kiếm qua hoạt động không máy tính (25 phút)

#### Hoạt động khởi động - "Tìm bạn trong lớp"
- **Hoạt động**: Giáo viên yêu cầu học sinh tìm một bạn trong lớp
- **Câu hỏi**: "Làm sao để tìm bạn An trong lớp?"
- **Kết nối**: "Hôm nay chúng ta sẽ học cách tìm phần tử trong danh sách bằng máy tính"
- **Mục tiêu**: Hiểu khái niệm tìm kiếm qua trải nghiệm thực tế

#### Khái niệm tìm kiếm qua ví dụ thực tế
- **Định nghĩa**: Tìm kiếm là quá trình tìm một phần tử cụ thể trong danh sách
- **Ví dụ thực tế**: 
  - Tìm tên học sinh trong danh sách lớp
  - Tìm số điện thoại trong danh bạ
  - Tìm sách trong thư viện
  - Tìm Pokemon trong danh sách Pokemon đã bắt
- **Hai câu hỏi quan trọng**:
  1. Phần tử có trong danh sách không? (Có/Không)
  2. Nếu có, nó ở vị trí nào? (Vị trí số mấy)

#### Hoạt động thực hành - "Tìm số trong dãy số"
- **Hoạt động**: Học sinh được phát một dãy số [8, 9, 7, 10, 6] và tìm số 7
- **Bước 1**: Xem số đầu tiên (8) - có phải số 7 không? → Không
- **Bước 2**: Xem số tiếp theo (9) - có phải số 7 không? → Không
- **Bước 3**: Xem số tiếp theo (7) - có phải số 7 không? → Có! Ở vị trí 3
- **Kết quả**: Tìm thấy số 7 ở vị trí 3
- **Mục tiêu**: Hiểu rõ các bước của thuật toán tìm kiếm

#### Bài toán: Tìm Pokemon trong danh sách
- **Input**: Danh sách Pokemon ["Pikachu", "Charmander", "Squirtle", "Bulbasaur"]
- **Tìm**: "Squirtle"
- **Output**: 
  - Có trong danh sách: Có
  - Vị trí: 3
- **Ví dụ**: Tìm Pokemon đã bắt trong danh sách Pokemon của mình

### Phần 2: Thuật toán tìm kiếm tuyến tính (20 phút)

#### Hoạt động không máy tính - "Tìm thẻ số"
- **Hoạt động**: Học sinh sử dụng thẻ số để mô phỏng thuật toán tìm kiếm
- **Mục tiêu**: Hiểu cách thuật toán tìm kiếm tuyến tính hoạt động
- **Quy tắc**: Xem từng thẻ một, từ trái sang phải, dừng khi tìm thấy
- **Kết quả**: Nhận ra cần duyệt qua từng phần tử một

#### Thuật toán tìm kiếm tuyến tính qua ví dụ thực tế
```
Danh sách: [8, 9, 7, 10, 6]
Tìm: 7

Bước 1: Xem vị trí 1 (8) - có phải 7 không? → Không, tiếp tục
Bước 2: Xem vị trí 2 (9) - có phải 7 không? → Không, tiếp tục
Bước 3: Xem vị trí 3 (7) - có phải 7 không? → Có! Tìm thấy ở vị trí 3
Kết quả: Tìm thấy số 7 ở vị trí 3
```

#### Trường hợp không tìm thấy
```
Danh sách: [8, 9, 7, 10, 6]
Tìm: 5

Bước 1: Xem vị trí 1 (8) - có phải 5 không? → Không, tiếp tục
Bước 2: Xem vị trí 2 (9) - có phải 5 không? → Không, tiếp tục
Bước 3: Xem vị trí 3 (7) - có phải 5 không? → Không, tiếp tục
Bước 4: Xem vị trí 4 (10) - có phải 5 không? → Không, tiếp tục
Bước 5: Xem vị trí 5 (6) - có phải 5 không? → Không, tiếp tục
Bước 6: Đã xem hết danh sách, không tìm thấy
Kết quả: Không tìm thấy số 5
```

#### Hoạt động không máy tính - "Đếm số lần so sánh"
- **Hoạt động**: Học sinh đếm số lần phải so sánh để tìm phần tử
- **Mục tiêu**: Hiểu độ phức tạp của thuật toán tìm kiếm
- **Kết quả**: Nhận ra tìm kiếm có thể mất nhiều bước

## 💻 PHẦN THỰC HÀNH SCRATCH (45 phút)

### Phần 3: Tạo game "Tìm số trong danh sách" trên Scratch (25 phút)

#### Bước 1: Tạo các biến và list cần thiết
```scratch
# Tạo các biến sau:
1. List "DanhSach" - danh sách các số cần tìm
2. Biến "SoCanTim" - số cần tìm
3. Biến "ViTri" - chỉ số vị trí hiện tại
4. Biến "TimThay" - biến boolean để đánh dấu đã tìm thấy chưa
5. Biến "ViTriTimThay" - vị trí tìm thấy (nếu có)
```

#### Bước 2: Lập trình thuật toán tìm kiếm cơ bản
```scratch
Khi cờ xanh được nhấn
# Khởi tạo danh sách
xóa tất cả trong [DanhSach v]
thêm [8] vào [DanhSach v]
thêm [9] vào [DanhSach v]
thêm [7] vào [DanhSach v]
thêm [10] vào [DanhSach v]
thêm [6] vào [DanhSach v]

# Số cần tìm
đặt [SoCanTim v] thành (7)

# Hiển thị thông tin
nói [Danh sách: ] + [DanhSach v] trong (3) giây
chờ (1) giây
nói [Tìm số: ] + [SoCanTim v] trong (2) giây
chờ (1) giây

# Khởi tạo biến tìm kiếm
đặt [ViTri v] thành (1)
đặt [TimThay v] thành [false]
nói [Bắt đầu tìm kiếm...] trong (2) giây

# Duyệt qua danh sách
lặp lại (chiều dài của [DanhSach v]) lần
  nói [Đang kiểm tra vị trí ] + [ViTri v] + [: ] + (mục (ViTri) của [DanhSach v]) trong (2) giây
  chờ (0.5) giây
  
  # Kiểm tra xem có phải số cần tìm không
  nếu <(mục (ViTri) của [DanhSach v]) = [SoCanTim v]> thì
    đặt [TimThay v] thành [true]
    đặt [ViTriTimThay v] thành [ViTri v]
    phát âm thanh [pop v]
    nói [Tìm thấy! Số ] + [SoCanTim v] + [ ở vị trí ] + [ViTriTimThay v] trong (3) giây
    dừng [vòng lặp này v]
  
  thay đổi [ViTri v] bởi (1)

# Kiểm tra kết quả
nếu <[TimThay v] = [true]> thì
  nói [=== KẾT QUẢ ===] trong (2) giây
  nói [Tìm thấy số ] + [SoCanTim v] + [ ở vị trí ] + [ViTriTimThay v] trong (3) giây
nếu không
  nói [=== KẾT QUẢ ===] trong (2) giây
  nói [Không tìm thấy số ] + [SoCanTim v] + [ trong danh sách] trong (3) giây
  phát âm thanh [pop v]
```

#### Hoạt động mở rộng - "Tìm với nhiều số"
- **Hoạt động**: Tạo chương trình tìm nhiều số khác nhau
- **Mục tiêu**: Hiểu cách sử dụng lại thuật toán tìm kiếm
- **Thử thách**: Tìm tất cả các vị trí có giá trị bằng số cần tìm (nếu có nhiều số giống nhau)

### Phần 4: Tìm kiếm Pokemon trong danh sách (20 phút)

#### Bài toán: Tìm Pokemon trong danh sách Pokemon đã bắt
- **Input**: Danh sách Pokemon ["Pikachu", "Charmander", "Squirtle", "Bulbasaur"]
- **Tìm**: "Squirtle"
- **Output**: 
  - Có trong danh sách: Có
  - Vị trí: 3

#### Lập trình tìm kiếm Pokemon
```scratch
Khi nhấn phím [p v]
# Khởi tạo danh sách Pokemon
xóa tất cả trong [DanhSachPokemon v]
thêm [Pikachu] vào [DanhSachPokemon v]
thêm [Charmander] vào [DanhSachPokemon v]
thêm [Squirtle] vào [DanhSachPokemon v]
thêm [Bulbasaur] vào [DanhSachPokemon v]

# Pokemon cần tìm
đặt [PokemonCanTim v] thành [Squirtle]

# Hiển thị thông tin
nói [Danh sách Pokemon: ] + [DanhSachPokemon v] trong (3) giây
chờ (1) giây
nói [Tìm Pokemon: ] + [PokemonCanTim v] trong (2) giây
chờ (1) giây

# Khởi tạo biến tìm kiếm
đặt [ViTri v] thành (1)
đặt [TimThay v] thành [false]
nói [Bắt đầu tìm kiếm Pokemon...] trong (2) giây

# Duyệt qua danh sách
lặp lại (chiều dài của [DanhSachPokemon v]) lần
  nói [Đang kiểm tra vị trí ] + [ViTri v] + [: ] + (mục (ViTri) của [DanhSachPokemon v]) trong (2) giây
  chờ (0.5) giây
  
  # Kiểm tra xem có phải Pokemon cần tìm không
  nếu <(mục (ViTri) của [DanhSachPokemon v]) = [PokemonCanTim v]> thì
    đặt [TimThay v] thành [true]
    đặt [ViTriTimThay v] thành [ViTri v]
    phát âm thanh [pop v]
    nói [Tìm thấy! ] + [PokemonCanTim v] + [ ở vị trí ] + [ViTriTimThay v] trong (3) giây
    dừng [vòng lặp này v]
  
  thay đổi [ViTri v] bởi (1)

# Kiểm tra kết quả
nếu <[TimThay v] = [true]> thì
  nói [=== KẾT QUẢ ===] trong (2) giây
  nói [Tìm thấy ] + [PokemonCanTim v] + [ ở vị trí ] + [ViTriTimThay v] trong (3) giây
  nói [Bạn đã bắt được Pokemon này rồi!] trong (2) giây
nếu không
  nói [=== KẾT QUẢ ===] trong (2) giây
  nói [Không tìm thấy ] + [PokemonCanTim v] + [ trong danh sách] trong (3) giây
  nói [Bạn chưa bắt được Pokemon này] trong (2) giây
  phát âm thanh [pop v]
```

#### Hoạt động mở rộng - "Tìm tất cả vị trí"
- **Hoạt động**: Tìm tất cả các vị trí có giá trị bằng số cần tìm
- **Mục tiêu**: Hiểu cách tìm nhiều kết quả
- **Thử thách**: Tạo danh sách các vị trí tìm thấy

### Phần 5: Tìm kiếm với giao diện tương tác (10 phút)

#### Tạo chương trình tìm kiếm tương tác
```scratch
# Cho phép người dùng nhập số cần tìm
Khi nhấn phím [t v]
hỏi [Nhập số cần tìm: ] và chờ
đặt [SoCanTim v] thành (câu trả lời)

# Khởi tạo danh sách (nếu chưa có)
nếu <(chiều dài của [DanhSach v]) = [0]> thì
  xóa tất cả trong [DanhSach v]
  thêm [8] vào [DanhSach v]
  thêm [9] vào [DanhSach v]
  thêm [7] vào [DanhSach v]
  thêm [10] vào [DanhSach v]
  thêm [6] vào [DanhSach v]

# Hiển thị thông tin
nói [Danh sách: ] + [DanhSach v] trong (3) giây
chờ (1) giây
nói [Tìm số: ] + [SoCanTim v] trong (2) giây
chờ (1) giây

# Tìm kiếm
đặt [ViTri v] thành (1)
đặt [TimThay v] thành [false]

lặp lại (chiều dài của [DanhSach v]) lần
  nếu <(mục (ViTri) của [DanhSach v]) = [SoCanTim v]> thì
    đặt [TimThay v] thành [true]
    đặt [ViTriTimThay v] thành [ViTri v]
    dừng [vòng lặp này v]
  thay đổi [ViTri v] bởi (1)

# Hiển thị kết quả
nếu <[TimThay v] = [true]> thì
  nói [Tìm thấy số ] + [SoCanTim v] + [ ở vị trí ] + [ViTriTimThay v] trong (3) giây
nếu không
  nói [Không tìm thấy số ] + [SoCanTim v] trong (3) giây
```

#### Hoạt động mở rộng - "Tìm kiếm thông minh"
- **Hoạt động**: Tạo chương trình tìm kiếm với nhiều tính năng
- **Mục tiêu**: Hiểu cách mở rộng chức năng tìm kiếm
- **Thử thách**: Tìm kiếm không phân biệt chữ hoa/thường (cho chuỗi)

## 🎯 Tổng kết và đánh giá (10 phút)

### Tổng kết kiến thức
- **Tìm kiếm tuyến tính**: Duyệt qua từng phần tử một, từ đầu đến cuối
- **Hai câu hỏi**: Có trong danh sách không? Ở vị trí nào?
- **Xử lý không tìm thấy**: Kiểm tra sau khi duyệt hết danh sách
- **Ứng dụng**: Tìm kiếm có mặt khắp nơi trong cuộc sống

### Đánh giá học sinh
- **Hiểu thuật toán**: Có thể giải thích các bước của thuật toán tìm kiếm
- **Áp dụng thực tế**: Tìm được ví dụ tìm kiếm trong cuộc sống
- **Lập trình Scratch**: Tạo được chương trình tìm kiếm hoạt động đúng
- **Xử lý trường hợp đặc biệt**: Xử lý được trường hợp không tìm thấy

## 🎨 Hoạt động mở rộng

### Cấp độ 1: Thêm tính năng cơ bản
- **Giao diện tương tác**: Tạo nút để nhập số cần tìm
- **Hiệu ứng trực quan**: Thêm màu sắc và animation khi tìm kiếm
- **Âm thanh**: Tạo âm thanh khác nhau khi tìm thấy/không tìm thấy

### Cấp độ 2: Tính năng nâng cao
- **Tìm tất cả vị trí**: Tìm tất cả các vị trí có giá trị bằng số cần tìm
- **Tìm kiếm có điều kiện**: Tìm số lớn hơn hoặc nhỏ hơn một giá trị
- **Tìm kiếm trong nhiều danh sách**: Tìm trong nhiều danh sách cùng lúc

### Cấp độ 3: Sáng tạo
- **Game tìm kiếm**: Tạo trò chơi tìm kiếm Pokemon hoặc đồ vật
- **Thuật toán riêng**: Thiết kế thuật toán tìm kiếm độc đáo
- **Dự án tích hợp**: Kết hợp tìm kiếm với các thuật toán khác

## 📝 Bài tập về nhà

### Bài tập bắt buộc
1. **Tìm số trong danh sách**: Viết chương trình tìm số 10 trong danh sách [8, 9, 7, 10, 6]
2. **Tìm Pokemon**: Tạo chương trình tìm Pokemon "Pikachu" trong danh sách Pokemon
3. **Xử lý không tìm thấy**: Tạo chương trình tìm số 5 (không có trong danh sách) và hiển thị "Không tìm thấy"

### Bài tập nâng cao
1. **Tìm tất cả vị trí**: Tìm tất cả các vị trí có số 7 trong danh sách [7, 9, 7, 10, 7]
2. **Tìm kiếm có điều kiện**: Tìm số lớn hơn 8 trong danh sách
3. **Tìm kiếm trong nhiều danh sách**: Tìm Pokemon trong nhiều danh sách Pokemon khác nhau

### Bài tập sáng tạo
1. **Game tìm kiếm**: Tạo game tìm kiếm Pokemon với giao diện đẹp
2. **Thuật toán riêng**: Thiết kế thuật toán tìm kiếm nhanh hơn
3. **Dự án tích hợp**: Kết hợp tìm kiếm với sắp xếp (sắp xếp trước, sau đó tìm kiếm)

## 🔧 Tài nguyên hỗ trợ

### Tài liệu tham khảo
- **Scratch Programming**: Hướng dẫn lập trình Scratch cơ bản
- **Algorithm Visualization**: Công cụ minh họa thuật toán tìm kiếm
- **Unplugged Activities**: Hoạt động không máy tính cho tìm kiếm

### Công cụ hỗ trợ
- **Scratch Editor**: Môi trường lập trình trực quan
- **List Blocks**: Khối lệnh danh sách trong Scratch
- **Control Blocks**: Khối lệnh điều khiển (vòng lặp, điều kiện)

### Đánh giá và phản hồi
- **Rubric đánh giá**: Tiêu chí đánh giá kỹ năng tìm kiếm
- **Peer Review**: Đánh giá lẫn nhau giữa học sinh
- **Portfolio**: Tập hợp các dự án và bài tập của học sinh

## 🔗 Kết nối với bài học khác

### Kiến thức liên quan
- **Bài 6**: Cấu trúc dữ liệu - Sử dụng danh sách (List)
- **Bài 7A**: Thuật toán tìm số lớn nhất và nhỏ nhất - Tìm kiếm giá trị đặc biệt
- **Bài 7B**: Thuật toán đếm - Đếm số phần tử
- **Bài 7F**: Thuật toán sắp xếp - **Sắp xếp giúp tìm kiếm nhanh hơn!**

### Chuẩn bị cho bài tiếp theo
- Hiểu cách duyệt qua danh sách
- Nắm vững so sánh và điều kiện
- Sẵn sàng học hàm và thủ tục (Bài 8)

## 💡 Lưu ý quan trọng

### Tại sao cần tìm kiếm?
- **Kiểm tra tồn tại**: Xem phần tử có trong danh sách không
- **Tìm vị trí**: Biết phần tử ở đâu trong danh sách
- **Ứng dụng thực tế**: Tìm tên trong danh sách, tìm sách trong thư viện

### Thuật toán tìm kiếm tuyến tính
- **Cách hoạt động**: Duyệt qua từng phần tử một, từ đầu đến cuối
- **Độ phức tạp**: Có thể phải xem tất cả các phần tử (trường hợp xấu nhất)
- **Ưu điểm**: Đơn giản, dễ hiểu, hoạt động với mọi loại danh sách
- **Nhược điểm**: Chậm với danh sách lớn

### Xử lý trường hợp không tìm thấy
- **Biến đánh dấu**: Sử dụng biến boolean (TimThay) để đánh dấu
- **Kiểm tra sau vòng lặp**: Kiểm tra biến đánh dấu sau khi duyệt hết danh sách
- **Thông báo rõ ràng**: Hiển thị thông báo "Không tìm thấy" cho người dùng

### Mẹo hay
- **Dừng sớm**: Dừng vòng lặp ngay khi tìm thấy (sử dụng "dừng vòng lặp này")
- **Kiểm tra kỹ**: Luôn kiểm tra cả trường hợp tìm thấy và không tìm thấy
- **Hiển thị rõ ràng**: Hiển thị vị trí tìm thấy một cách rõ ràng

---

**Tác giả**: AI & Trần Việt Trung (BKHN)  
**Ngày tạo**: 04/10/2025  
**Phiên bản**: 1.0

