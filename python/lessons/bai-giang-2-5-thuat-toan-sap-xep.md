# Bài giảng 2.5: Thuật toán sắp xếp Python - Bubble Sort và Selection Sort

## 📋 Thông tin bài học
- **Thời gian**: 90 phút
- **Độ tuổi**: 11-12 tuổi
- **Trình độ**: Trung bình đến nâng cao
- **Mục tiêu**: Hiểu và áp dụng thuật toán sắp xếp trong Python

## 🎯 Mục tiêu học tập

### Kiến thức
- Hiểu khái niệm sắp xếp và tầm quan trọng
- Nắm vững thuật toán sắp xếp nổi bọt (Bubble Sort)
- Hiểu thuật toán sắp xếp chọn (Selection Sort)
- Biết cách so sánh hiệu suất các thuật toán

### Kỹ năng
- Phân tích và thiết kế thuật toán sắp xếp
- Áp dụng thuật toán sắp xếp vào lập trình Python
- Sử dụng vòng lặp lồng nhau hiệu quả
- Debug và tối ưu hóa code sắp xếp

### Thái độ
- Phát triển tư duy logic phức tạp
- Rèn luyện tính kiên trì với thuật toán khó
- Khuyến khích tư duy phản biện và so sánh

## 🧠 Nội dung bài học

## 📚 PHẦN LÝ THUYẾT (45 phút)

### Phần 1: Khái niệm sắp xếp qua hoạt động không máy tính (25 phút)

#### Hoạt động khởi động - "Kết nối với Scratch"
- **Hoạt động**: Nhắc lại bài 7C về thuật toán sắp xếp trong Scratch
- **Câu hỏi**: "Chúng ta đã học cách sắp xếp như thế nào trong Scratch?"
- **Kết nối**: "Hôm nay chúng ta sẽ học cách sắp xếp hiệu quả hơn trong Python"
- **Mục tiêu**: Kết nối kiến thức Scratch với Python

#### Khái niệm sắp xếp qua ví dụ thực tế
- **Định nghĩa**: Sắp xếp là sắp đặt các phần tử theo một thứ tự nhất định
- **Ví dụ**: Sắp xếp sách theo thứ tự ABC, sắp xếp điểm từ cao đến thấp
- **Input**: Danh sách không có thứ tự [8, 3, 1, 9, 5]
- **Output**: Danh sách có thứ tự [1, 3, 5, 8, 9]
- **Ứng dụng**: Tìm kiếm nhanh, hiển thị dữ liệu đẹp mắt, phân tích dữ liệu

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

## 💻 PHẦN THỰC HÀNH PYTHON (45 phút)

### Phần 3: Tạo chương trình "Sắp xếp nổi bọt" trên Python (25 phút)

#### Bước 1: Tạo file Python mới
```python
# Tạo file: sap_xep_noi_bot.py
# Mục tiêu: Sắp xếp nổi bọt trong Python
```

#### Bước 2: Lập trình thuật toán sắp xếp nổi bọt
```python
def sap_xep_noi_bot(danh_sach):
    """
    Sắp xếp nổi bọt - sắp xếp danh sách theo thứ tự tăng dần
    """
    print(f"Danh sách ban đầu: {danh_sach}")
    
    # Tạo bản sao để không thay đổi danh sách gốc
    danh_sach_sap_xep = danh_sach.copy()
    n = len(danh_sach_sap_xep)
    
    # Vòng lặp ngoài - số lần duyệt
    for i in range(n):
        print(f"\n--- Lần duyệt {i + 1} ---")
        da_doi_cho = False
        
        # Vòng lặp trong - so sánh từng cặp
        for j in range(n - 1 - i):
            print(f"So sánh {danh_sach_sap_xep[j]} và {danh_sach_sap_xep[j + 1]}")
            
            # Nếu phần tử trước lớn hơn phần tử sau
            if danh_sach_sap_xep[j] > danh_sach_sap_xep[j + 1]:
                # Đổi chỗ
                danh_sach_sap_xep[j], danh_sach_sap_xep[j + 1] = danh_sach_sap_xep[j + 1], danh_sach_sap_xep[j]
                da_doi_cho = True
                print(f"Đổi chỗ! Kết quả: {danh_sach_sap_xep}")
            else:
                print("Giữ nguyên")
        
        # Nếu không có đổi chỗ nào, danh sách đã được sắp xếp
        if not da_doi_cho:
            print("Không có đổi chỗ nào - danh sách đã được sắp xếp!")
            break
    
    print(f"\nDanh sách sau khi sắp xếp: {danh_sach_sap_xep}")
    return danh_sach_sap_xep

# Chương trình chính
if __name__ == "__main__":
    # Danh sách điểm số
    danh_sach_diem = [8, 9, 7, 10, 6]
    
    # Sắp xếp nổi bọt
    danh_sach_da_sap_xep = sap_xep_noi_bot(danh_sach_diem)
    
    print(f"\nKết quả cuối cùng: {danh_sach_da_sap_xep}")
```

#### Hoạt động mở rộng - "Sắp xếp ngược"
- **Hoạt động**: Thay đổi thuật toán để sắp xếp từ thấp đến cao
- **Mục tiêu**: Hiểu cách điều chỉnh điều kiện so sánh
- **Thử thách**: Tạo thuật toán sắp xếp theo nhiều tiêu chí khác nhau

#### Giải thích các khái niệm Python quan trọng:
```python
# Vòng lặp lồng nhau:
for i in range(n):           # Vòng lặp ngoài
    for j in range(n-1-i):   # Vòng lặp trong

# Đổi chỗ phần tử:
a, b = b, a  # Đổi chỗ a và b

# Copy danh sách:
danh_sach_copy = danh_sach.copy()  # Tạo bản sao

# Điều kiện dừng sớm:
if not da_doi_cho:
    break  # Thoát khỏi vòng lặp
```

### Phần 4: Tạo chương trình "Sắp xếp chọn" trên Python (20 phút)

#### Bước 1: Tạo file Python mới
```python
# Tạo file: sap_xep_chon.py
# Mục tiêu: Sắp xếp chọn trong Python
```

#### Bước 2: Lập trình thuật toán sắp xếp chọn
```python
def sap_xep_chon(danh_sach):
    """
    Sắp xếp chọn - tìm phần tử nhỏ nhất và đặt vào vị trí đúng
    """
    print(f"Danh sách ban đầu: {danh_sach}")
    
    # Tạo bản sao để không thay đổi danh sách gốc
    danh_sach_sap_xep = danh_sach.copy()
    n = len(danh_sach_sap_xep)
    
    # Vòng lặp ngoài - duyệt qua từng vị trí
    for i in range(n - 1):
        print(f"\n--- Lần {i + 1}: Tìm phần tử nhỏ nhất từ vị trí {i} ---")
        
        # Tìm phần tử nhỏ nhất từ vị trí i đến cuối
        vi_tri_nho_nhat = i
        for j in range(i + 1, n):
            print(f"So sánh {danh_sach_sap_xep[vi_tri_nho_nhat]} và {danh_sach_sap_xep[j]}")
            if danh_sach_sap_xep[j] < danh_sach_sap_xep[vi_tri_nho_nhat]:
                vi_tri_nho_nhat = j
                print(f"Phần tử nhỏ nhất hiện tại: {danh_sach_sap_xep[vi_tri_nho_nhat]}")
        
        # Đổi chỗ nếu cần
        if vi_tri_nho_nhat != i:
            print(f"Đổi chỗ {danh_sach_sap_xep[i]} và {danh_sach_sap_xep[vi_tri_nho_nhat]}")
            danh_sach_sap_xep[i], danh_sach_sap_xep[vi_tri_nho_nhat] = danh_sach_sap_xep[vi_tri_nho_nhat], danh_sach_sap_xep[i]
            print(f"Kết quả: {danh_sach_sap_xep}")
        else:
            print("Không cần đổi chỗ")
    
    print(f"\nDanh sách sau khi sắp xếp: {danh_sach_sap_xep}")
    return danh_sach_sap_xep

# Chương trình chính
if __name__ == "__main__":
    # Danh sách điểm số
    danh_sach_diem = [8, 9, 7, 10, 6]
    
    # Sắp xếp chọn
    danh_sach_da_sap_xep = sap_xep_chon(danh_sach_diem)
    
    print(f"\nKết quả cuối cùng: {danh_sach_da_sap_xep}")
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
- **Lập trình Python**: Tạo được chương trình sắp xếp hoạt động
- **Tư duy logic**: Phân tích và so sánh hiệu suất thuật toán

## 🎨 Hoạt động mở rộng

### Cấp độ 1: Thêm tính năng cơ bản
- **Giao diện tương tác**: Tạo menu để chọn loại sắp xếp
- **Hiệu ứng trực quan**: Thêm màu sắc và animation khi sắp xếp
- **Âm thanh**: Tạo âm thanh khác nhau cho từng loại sắp xếp

### Cấp độ 2: Tính năng nâng cao
- **Sắp xếp nhiều phần tử**: Mở rộng thuật toán cho 100 số
- **Sắp xếp thông minh**: Sắp xếp theo nhiều tiêu chí
- **So sánh hiệu suất**: Đo thời gian thực thi của các thuật toán

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
1. **Sắp xếp phức tạp**: Sắp xếp danh sách có 50 phần tử
2. **Sắp xếp thông minh**: Sắp xếp theo nhiều tiêu chí
3. **Tối ưu hóa**: Tìm cách giảm số lần so sánh

### Bài tập sáng tạo
1. **Game sắp xếp**: Tạo game sắp xếp với giao diện đẹp
2. **Thuật toán riêng**: Thiết kế thuật toán sắp xếp độc đáo
3. **Dự án tích hợp**: Kết hợp sắp xếp với tìm kiếm và đếm

## 🔧 Tài nguyên hỗ trợ

### Tài liệu tham khảo
- **Python Programming**: Hướng dẫn lập trình Python cơ bản
- **Algorithm Visualization**: Công cụ minh họa thuật toán sắp xếp
- **Sorting Algorithms**: Các thuật toán sắp xếp phổ biến

### Công cụ hỗ trợ
- **Python Editor**: Môi trường lập trình Python
- **Algorithm Simulator**: Mô phỏng thuật toán sắp xếp
- **Debugging Tools**: Công cụ gỡ lỗi và tối ưu hóa

### Đánh giá và phản hồi
- **Rubric đánh giá**: Tiêu chí đánh giá kỹ năng sắp xếp
- **Peer Review**: Đánh giá lẫn nhau giữa học sinh
- **Portfolio**: Tập hợp các dự án và bài tập của học sinh
