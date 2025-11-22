# Bài giảng 3.5: Custom Blocks (Khối lệnh tùy chỉnh)

## 📋 Thông tin bài học
- **Thời gian**: 60 phút
- **Độ tuổi**: 9-10 tuổi
- **Trình độ**: Trung bình
- **Mục tiêu**: Hiểu và tạo custom blocks (khối lệnh tùy chỉnh) để tái sử dụng code

## 🎯 Mục tiêu học tập

### Kiến thức
- Hiểu khái niệm custom blocks (khối lệnh tùy chỉnh)
- Biết tại sao cần tạo custom blocks
- Nắm vững cách tạo custom blocks đơn giản
- Hiểu cách tạo custom blocks với tham số

### Kỹ năng
- Tạo custom blocks trong Scratch
- Sử dụng custom blocks để tái sử dụng code
- Thiết kế custom blocks hiệu quả
- Tổ chức code có cấu trúc với custom blocks

### Thái độ
- Phát triển tư duy modular
- Rèn luyện tính cẩn thận
- Khuyến khích tư duy tái sử dụng

## 🧠 Nội dung bài học

## 📚 PHẦN LÝ THUYẾT (30 phút)

### Phần 1: Khái niệm Custom Blocks qua hoạt động không máy tính (20 phút)

#### Hoạt động khởi động - "Tạo công thức nấu ăn riêng"
- **Hoạt động**: Học sinh viết công thức nấu ăn đơn giản
- **Câu hỏi**: "Nếu chúng ta muốn nấu món này nhiều lần, làm sao để không phải viết lại công thức?"
- **Kết nối**: "Trong Scratch, chúng ta có thể tạo 'công thức' riêng - đó là custom blocks"
- **Mục tiêu**: Hiểu custom blocks như công thức có thể tái sử dụng

#### Khái niệm Custom Blocks qua ví dụ thực tế
- **Định nghĩa**: Custom blocks là các khối lệnh do chúng ta tự tạo, có thể tái sử dụng nhiều lần
- **Ví dụ thực tế**: 
  - Công thức nấu ăn: Viết một lần, dùng nhiều lần
  - Hướng dẫn làm bánh: Tạo một lần, làm nhiều lần
  - Quy trình đánh răng: Tạo một lần, làm mỗi ngày
- **So sánh**: 
  - Blocks có sẵn: Giống như từ điển có sẵn
  - Custom blocks: Giống như tạo từ mới của riêng mình

#### Hoạt động thực hành - "Tạo hướng dẫn riêng"
- **Hoạt động**: Học sinh viết hướng dẫn "Cách chào hỏi" (3 bước)
- **Bước 1**: Mỉm cười
- **Bước 2**: Nói "Xin chào"
- **Bước 3**: Vẫy tay
- **Mục tiêu**: Hiểu cách tạo một "chương trình" có thể tái sử dụng
- **Kết quả**: Nhận ra có thể tạo "hướng dẫn" riêng và dùng nhiều lần

### Phần 2: Tại sao cần Custom Blocks? (10 phút)

#### Vấn đề: Code lặp lại
- **Ví dụ**: Nhân vật cần "Nhảy" 5 lần trong chương trình
- **Cách 1**: Viết lại code nhảy 5 lần (dài, khó quản lý)
- **Cách 2**: Tạo custom block "Nhảy", gọi 5 lần (ngắn gọn, dễ quản lý)
- **Kết luận**: Custom blocks giúp code ngắn gọn và dễ quản lý hơn

#### Lợi ích của Custom Blocks
- **Tái sử dụng**: Viết một lần, dùng nhiều lần
- **Dễ quản lý**: Thay đổi một nơi, áp dụng mọi nơi
- **Dễ đọc**: Code ngắn gọn, dễ hiểu hơn
- **Tổ chức**: Code có cấu trúc, dễ bảo trì

## 💻 PHẦN THỰC HÀNH SCRATCH (30 phút)

### Phần 3: Tạo Custom Block đầu tiên (15 phút)

#### Bài toán: Nhân vật cần "Nhảy" nhiều lần
- **Vấn đề**: Code nhảy lặp lại nhiều lần
- **Giải pháp**: Tạo custom block "Nhảy"

#### Bước 1: Tạo Custom Block "Nhảy"
```scratch
# Bước 1: Tạo custom block
1. Chọn "My Blocks" (Khối của tôi) trong menu
2. Nhấn "Make a Block" (Tạo khối)
3. Đặt tên: "Nhay"
4. Nhấn "OK"

# Bước 2: Định nghĩa custom block
define Nhay
thay đổi y bởi (20)
chờ (0.2) giây
thay đổi y bởi (-20)
phát âm thanh [pop v]

# Bước 3: Sử dụng custom block
Khi cờ xanh được nhấn
Nhay
chờ (1) giây
Nhay
chờ (1) giây
Nhay
```

#### Hoạt động mở rộng - "Tạo nhiều custom blocks"
- **Hoạt động**: Tạo thêm custom blocks: "Xoay", "Đổi màu", "Phát âm thanh"
- **Mục tiêu**: Hiểu cách tạo nhiều custom blocks
- **Thử thách**: Tạo 3 custom blocks khác nhau và sử dụng chúng

### Phần 4: Custom Blocks với tham số (15 phút)

#### Bài toán: Nhảy với độ cao khác nhau
- **Vấn đề**: Muốn nhảy cao/thấp khác nhau
- **Giải pháp**: Tạo custom block có tham số (độ cao)

#### Bước 1: Tạo Custom Block có tham số
```scratch
# Bước 1: Tạo custom block có tham số
1. Chọn "My Blocks" → "Make a Block"
2. Đặt tên: "NhayCao"
3. Nhấn "+" và chọn "number input"
4. Đặt tên tham số: "DoCao"
5. Nhấn "OK"

# Bước 2: Định nghĩa custom block với tham số
define NhayCao (DoCao)
thay đổi y bởi ([DoCao v])
chờ (0.2) giây
thay đổi y bởi ([DoCao v] * (-1))
phát âm thanh [pop v]

# Bước 3: Sử dụng với giá trị khác nhau
Khi cờ xanh được nhấn
NhayCao (10)  # Nhảy thấp
chờ (1) giây
NhayCao (30)  # Nhảy cao
chờ (1) giây
NhayCao (50)  # Nhảy rất cao
```

#### Hoạt động mở rộng - "Custom block với nhiều tham số"
- **Hoạt động**: Tạo custom block "DiChuyen" với tham số: số bước, hướng
- **Mục tiêu**: Hiểu cách sử dụng nhiều tham số
- **Thử thách**: Tạo custom block có 2-3 tham số

## 🎯 Tổng kết và đánh giá (10 phút)

### Tổng kết kiến thức
- **Custom Blocks**: Khối lệnh do chúng ta tự tạo, có thể tái sử dụng
- **Lợi ích**: Tái sử dụng code, dễ quản lý, code ngắn gọn
- **Tham số**: Giúp custom blocks linh hoạt hơn
- **Ứng dụng**: Sử dụng trong game, ứng dụng, dự án lớn

### Đánh giá học sinh
- **Hiểu custom blocks**: Có thể giải thích tại sao cần custom blocks
- **Tạo custom blocks**: Tạo được custom block đơn giản
- **Sử dụng tham số**: Tạo được custom block có tham số
- **Tư duy modular**: Tổ chức code có cấu trúc với custom blocks

## 🎨 Hoạt động mở rộng

### Cấp độ 1: Thêm tính năng cơ bản
- **Nhiều custom blocks**: Tạo 3-5 custom blocks khác nhau
- **Kết hợp**: Sử dụng custom blocks trong custom blocks khác
- **Tổ chức**: Tổ chức code với nhiều custom blocks

### Cấp độ 2: Tính năng nâng cao
- **Nhiều tham số**: Tạo custom blocks có 2-3 tham số
- **Custom blocks phức tạp**: Tạo custom blocks có điều kiện, vòng lặp
- **Thư viện**: Tạo thư viện custom blocks cho dự án

### Cấp độ 3: Sáng tạo
- **Game với custom blocks**: Tạo game sử dụng nhiều custom blocks
- **Dự án lớn**: Áp dụng custom blocks vào dự án lớn
- **Chia sẻ**: Chia sẻ custom blocks với bạn bè

## 📝 Bài tập về nhà

### Bài tập bắt buộc
1. **Custom block đơn giản**: Tạo custom block "ChaoHoi" (chào hỏi)
2. **Custom block với tham số**: Tạo custom block "DiChuyen" với tham số số bước
3. **Sử dụng nhiều lần**: Sử dụng custom block ít nhất 3 lần trong chương trình

### Bài tập nâng cao
1. **Nhiều custom blocks**: Tạo 3 custom blocks khác nhau
2. **Custom blocks phức tạp**: Tạo custom block có điều kiện hoặc vòng lặp
3. **Game với custom blocks**: Tạo game sử dụng custom blocks

### Bài tập sáng tạo
1. **Thư viện custom blocks**: Tạo thư viện 5 custom blocks cho game
2. **Dự án tích hợp**: Áp dụng custom blocks vào dự án lớn
3. **Chia sẻ**: Chia sẻ custom blocks với bạn bè

## 🔧 Tài nguyên hỗ trợ

### Tài liệu tham khảo
- **Bài 1.5**: Giới thiệu về Blocks - Nền tảng về blocks
- **Bài 8**: Hàm và thủ tục - Nâng cao về custom blocks
- **Scratch Custom Blocks**: Hướng dẫn tạo custom blocks

### Công cụ hỗ trợ
- **Scratch Editor**: Môi trường lập trình trực quan
- **My Blocks**: Menu tạo custom blocks trong Scratch
- **Block Editor**: Trình chỉnh sửa custom blocks

### Đánh giá và phản hồi
- **Rubric đánh giá**: Tiêu chí đánh giá kỹ năng tạo custom blocks
- **Peer Review**: Đánh giá lẫn nhau giữa học sinh
- **Portfolio**: Tập hợp các dự án và bài tập của học sinh

## 🔗 Kết nối với lập trình thực tế

### Khái niệm tương đồng

#### 1. Functions (Hàm)
- **Scratch**: Custom blocks
- **Python**: `def function_name():`
- **JavaScript**: `function functionName() {}`
- **Ứng dụng**: Tái sử dụng code trong mọi ngôn ngữ lập trình

#### 2. Methods (Phương thức)
- **Scratch**: Custom blocks cho nhân vật
- **Lập trình**: Methods của object/class
- **Ví dụ**: 
  - Scratch: Custom block "Nhay"
  - Python: `def jump(self):`
  - JavaScript: `jump() {}`

#### 3. Code Reusability (Tái sử dụng code)
- **Scratch**: Custom blocks giúp tái sử dụng
- **Lập trình**: Functions giúp tái sử dụng code
- **Lợi ích**: Giảm code trùng lặp, dễ bảo trì

### Ví dụ trong lập trình thực tế

#### Python
```python
# Tương tự custom block "Nhay" trong Scratch
def nhay(do_cao):
    y += do_cao
    time.sleep(0.2)
    y -= do_cao
    play_sound("pop")

# Sử dụng
nhay(10)  # Nhảy thấp
nhay(30)  # Nhảy cao
```

#### JavaScript
```javascript
// Tương tự custom block "Nhay" trong Scratch
function nhay(doCao) {
    y += doCao;
    setTimeout(() => {
        y -= doCao;
        playSound("pop");
    }, 200);
}

// Sử dụng
nhay(10);  // Nhảy thấp
nhay(30);  // Nhảy cao
```

### Chuẩn bị cho bài tiếp theo
- Hiểu cách tạo custom blocks đơn giản
- Nắm vững custom blocks với tham số
- **Sẵn sàng học Bài 8 (Hàm và thủ tục)** - Nâng cao về custom blocks

## 💡 Lưu ý quan trọng

### Tại sao cần Custom Blocks?
- **Code lặp lại**: Nếu code lặp lại nhiều lần → tạo custom block
- **Dễ quản lý**: Thay đổi một nơi → áp dụng mọi nơi
- **Code ngắn gọn**: Code dễ đọc và hiểu hơn
- **Tổ chức**: Code có cấu trúc, dễ bảo trì

### Khi nào nên tạo Custom Block?
- **Code lặp lại**: Khi code xuất hiện 2-3 lần trở lên
- **Chức năng rõ ràng**: Khi có một chức năng cụ thể (ví dụ: "Nhảy", "Đổi màu")
- **Cần tái sử dụng**: Khi cần dùng lại nhiều lần
- **Tổ chức code**: Khi muốn code có cấu trúc hơn

### Mẹo hay
- **Đặt tên rõ ràng**: Tên custom block nên mô tả chức năng (ví dụ: "Nhay", "ChaoHoi")
- **Bắt đầu đơn giản**: Tạo custom block đơn giản trước, sau đó thêm tham số
- **Test kỹ**: Test custom block trước khi sử dụng nhiều lần
- **Tổ chức**: Nhóm các custom blocks liên quan lại với nhau

---

**Tác giả**: AI & Trần Việt Trung (BKHN)  
**Ngày tạo**: 04/10/2025  
**Phiên bản**: 1.0

