# Bài giảng 3: Thuật toán tìm kiếm - Tìm kiếm tuyến tính và nhị phân

## 📋 Thông tin bài học
- **Thời gian**: 90 phút
- **Độ tuổi**: 11-12 tuổi
- **Trình độ**: Trung bình
- **Mục tiêu**: Hiểu và áp dụng thuật toán tìm kiếm trong Python

## 🎯 Mục tiêu học tập

### Kiến thức
- Hiểu khái niệm tìm kiếm và tầm quan trọng
- Nắm vững thuật toán tìm kiếm tuyến tính (Linear Search)
- Hiểu thuật toán tìm kiếm nhị phân (Binary Search)
- Biết cách so sánh hiệu suất các thuật toán

### Kỹ năng
- Phân tích và thiết kế thuật toán tìm kiếm
- Áp dụng thuật toán tìm kiếm vào lập trình Python
- Sử dụng vòng lặp và điều kiện hiệu quả
- Debug và tối ưu hóa code tìm kiếm

### Thái độ
- Phát triển tư duy logic phức tạp
- Rèn luyện tính kiên trì với thuật toán khó
- Khuyến khích tư duy phản biện và so sánh

## 🧠 Nội dung bài học

## 📚 PHẦN LÝ THUYẾT (45 phút)

### Phần 1: Khái niệm tìm kiếm qua hoạt động không máy tính (25 phút)

#### Hoạt động khởi động - "Kết nối với Scratch"
- **Hoạt động**: Nhắc lại bài 7A về thuật toán tìm max và đếm
- **Câu hỏi**: "Chúng ta đã học cách tìm số lớn nhất như thế nào trong Scratch?"
- **Kết nối**: "Hôm nay chúng ta sẽ học cách tìm một số cụ thể trong danh sách"
- **Mục tiêu**: Kết nối thuật toán cơ bản với tìm kiếm

#### Khái niệm tìm kiếm qua ví dụ thực tế
- **Định nghĩa**: Tìm kiếm là quá trình tìm một phần tử cụ thể trong tập hợp dữ liệu
- **Ví dụ**: Tìm tên học sinh trong danh sách lớp, tìm sản phẩm trong cửa hàng
- **Input**: Danh sách [8, 3, 1, 9, 5] và giá trị cần tìm (9)
- **Output**: Vị trí của giá trị (4) hoặc "không tìm thấy"
- **Ứng dụng**: Tìm kiếm trong cơ sở dữ liệu, tìm kiếm web, tìm kiếm file

#### Hoạt động thực hành - "Tìm thẻ số trong bộ bài"
- **Hoạt động**: Học sinh tìm thẻ số 7 trong bộ bài 52 lá
- **Mục tiêu**: Hiểu khái niệm tìm kiếm qua trải nghiệm thực tế
- **Quy tắc**: Lật từng lá một cách tuần tự
- **Kết quả**: Nhận ra tìm kiếm cần thời gian và có thể không tìm thấy

### Phần 2: Thuật toán tìm kiếm tuyến tính qua hoạt động không máy tính (20 phút)

#### Hoạt động không máy tính - "Tìm số trong danh sách"
- **Hoạt động**: Học sinh tìm số 9 trong danh sách [8, 3, 1, 9, 5]
- **Mục tiêu**: Hiểu cách thuật toán tìm kiếm tuyến tính hoạt động
- **Quy tắc**: Kiểm tra từng số một cách tuần tự từ đầu đến cuối
- **Kết quả**: Nhận ra tìm kiếm tuyến tính đơn giản nhưng chậm

#### Bài toán: Tìm điểm số của học sinh
- **Input**: Danh sách điểm [8, 9, 7, 10, 6] và điểm cần tìm (9)
- **Output**: Vị trí của điểm (2) hoặc "không tìm thấy"
- **Ví dụ**: Tìm điểm của học sinh có tên "An"

#### Thuật toán tìm kiếm tuyến tính qua ví dụ thực tế
```
Bước 1: Bắt đầu từ vị trí đầu tiên (0)
Bước 2: Kiểm tra số tại vị trí 0 (8)
Bước 3: Vì 8 ≠ 9, chuyển sang vị trí tiếp theo (1)
Bước 4: Kiểm tra số tại vị trí 1 (9)
Bước 5: Vì 9 = 9, tìm thấy! Trả về vị trí 1
```

#### Hoạt động không máy tính - "Đếm số lần kiểm tra"
- **Hoạt động**: Học sinh đếm số lần phải kiểm tra để tìm số
- **Mục tiêu**: Hiểu độ phức tạp của thuật toán tìm kiếm
- **Kết quả**: Nhận ra tìm kiếm tuyến tính cần nhiều bước

## 💻 PHẦN THỰC HÀNH PYTHON (45 phút)

### Phần 3: Tạo chương trình "Tìm kiếm tuyến tính" trên Python (25 phút)

#### Bước 1: Tạo file Python mới
```python
# Tạo file: tim_kiem_tuyen_tinh.py
# Mục tiêu: Tìm kiếm tuyến tính trong danh sách
```

#### Bước 2: Lập trình thuật toán tìm kiếm tuyến tính
```python
def tim_kiem_tuyen_tinh(danh_sach, gia_tri_can_tim):
    """
    Tìm kiếm tuyến tính trong danh sách
    Trả về vị trí nếu tìm thấy, -1 nếu không tìm thấy
    """
    print(f"Đang tìm kiếm {gia_tri_can_tim} trong danh sách: {danh_sach}")
    
    # Duyệt qua từng phần tử
    for i in range(len(danh_sach)):
        print(f"Kiểm tra vị trí {i}: {danh_sach[i]}")
        
        # Nếu tìm thấy
        if danh_sach[i] == gia_tri_can_tim:
            print(f"Tìm thấy {gia_tri_can_tim} tại vị trí {i}!")
            return i
    
    # Không tìm thấy
    print(f"Không tìm thấy {gia_tri_can_tim} trong danh sách")
    return -1

# Chương trình chính
if __name__ == "__main__":
    # Danh sách điểm số
    danh_sach_diem = [8, 9, 7, 10, 6]
    
    # Tìm kiếm điểm 9
    vi_tri = tim_kiem_tuyen_tinh(danh_sach_diem, 9)
    
    if vi_tri != -1:
        print(f"Điểm 9 được tìm thấy tại vị trí {vi_tri}")
    else:
        print("Không tìm thấy điểm 9")
    
    # Tìm kiếm điểm 5
    vi_tri = tim_kiem_tuyen_tinh(danh_sach_diem, 5)
    
    if vi_tri != -1:
        print(f"Điểm 5 được tìm thấy tại vị trí {vi_tri}")
    else:
        print("Không tìm thấy điểm 5")
```

#### Hoạt động mở rộng - "Tìm kiếm với điều kiện"
- **Hoạt động**: Tìm kiếm điểm đầu tiên >= 8
- **Mục tiêu**: Hiểu cách điều chỉnh thuật toán tìm kiếm
- **Thử thách**: Tìm kiếm điểm cuối cùng < 7

#### Giải thích các khái niệm Python quan trọng:
```python
# Vòng lặp for:
for i in range(len(danh_sach)):
    # Duyệt qua từng phần tử với chỉ số i

# Điều kiện if:
if danh_sach[i] == gia_tri_can_tim:
    # So sánh giá trị tại vị trí i

# Hàm return:
return i  # Trả về giá trị và kết thúc hàm

# Hàm len():
len(danh_sach)  # Lấy số phần tử trong danh sách
```

### Phần 4: Tạo chương trình "Tìm kiếm nhị phân" trên Python (20 phút)

#### Bước 1: Tạo file Python mới
```python
# Tạo file: tim_kiem_nhi_phan.py
# Mục tiêu: Tìm kiếm nhị phân trong danh sách đã sắp xếp
```

#### Bước 2: Lập trình thuật toán tìm kiếm nhị phân
```python
def tim_kiem_nhi_phan(danh_sach, gia_tri_can_tim):
    """
    Tìm kiếm nhị phân trong danh sách đã sắp xếp
    Trả về vị trí nếu tìm thấy, -1 nếu không tìm thấy
    """
    print(f"Đang tìm kiếm {gia_tri_can_tim} trong danh sách đã sắp xếp: {danh_sach}")
    
    # Khởi tạo biến
    trai = 0
    phai = len(danh_sach) - 1
    
    # Vòng lặp tìm kiếm
    while trai <= phai:
        # Tính vị trí giữa
        giua = (trai + phai) // 2
        print(f"Kiểm tra vị trí {giua}: {danh_sach[giua]}")
        
        # Nếu tìm thấy
        if danh_sach[giua] == gia_tri_can_tim:
            print(f"Tìm thấy {gia_tri_can_tim} tại vị trí {giua}!")
            return giua
        
        # Nếu giá trị cần tìm nhỏ hơn
        elif danh_sach[giua] > gia_tri_can_tim:
            print(f"{gia_tri_can_tim} nhỏ hơn {danh_sach[giua]}, tìm kiếm bên trái")
            phai = giua - 1
        
        # Nếu giá trị cần tìm lớn hơn
        else:
            print(f"{gia_tri_can_tim} lớn hơn {danh_sach[giua]}, tìm kiếm bên phải")
            trai = giua + 1
    
    # Không tìm thấy
    print(f"Không tìm thấy {gia_tri_can_tim} trong danh sách")
    return -1

# Chương trình chính
if __name__ == "__main__":
    # Danh sách điểm số đã sắp xếp
    danh_sach_diem = [6, 7, 8, 9, 10]
    
    # Tìm kiếm điểm 9
    vi_tri = tim_kiem_nhi_phan(danh_sach_diem, 9)
    
    if vi_tri != -1:
        print(f"Điểm 9 được tìm thấy tại vị trí {vi_tri}")
    else:
        print("Không tìm thấy điểm 9")
    
    # Tìm kiếm điểm 5
    vi_tri = tim_kiem_nhi_phan(danh_sach_diem, 5)
    
    if vi_tri != -1:
        print(f"Điểm 5 được tìm thấy tại vị trí {vi_tri}")
    else:
        print("Không tìm thấy điểm 5")
```

#### Hoạt động mở rộng - "So sánh hiệu suất"
- **Hoạt động**: So sánh thời gian thực thi giữa tìm kiếm tuyến tính và nhị phân
- **Mục tiêu**: Hiểu cách đánh giá hiệu suất thuật toán
- **Thử thách**: Tạo thuật toán tìm kiếm riêng

## 🎯 Tổng kết và đánh giá (10 phút)

### Tổng kết kiến thức
- **Tìm kiếm**: Quá trình tìm một phần tử cụ thể trong tập hợp dữ liệu
- **Tìm kiếm tuyến tính**: Kiểm tra từng phần tử một cách tuần tự
- **Tìm kiếm nhị phân**: Chia đôi danh sách và tìm kiếm hiệu quả
- **Hiệu suất**: Tìm kiếm nhị phân nhanh hơn tìm kiếm tuyến tính
- **Ứng dụng**: Tìm kiếm có mặt khắp nơi trong cuộc sống

### Đánh giá học sinh
- **Hiểu thuật toán**: Có thể giải thích các bước của thuật toán tìm kiếm
- **Áp dụng thực tế**: Tìm được ví dụ tìm kiếm trong cuộc sống
- **Lập trình Python**: Tạo được chương trình tìm kiếm hoạt động
- **Tư duy logic**: Phân tích và so sánh hiệu suất thuật toán

## 🎨 Hoạt động mở rộng

### Cấp độ 1: Thêm tính năng cơ bản
- **Giao diện tương tác**: Tạo menu để chọn loại tìm kiếm
- **Hiệu ứng trực quan**: Thêm màu sắc và animation khi tìm kiếm
- **Âm thanh**: Tạo âm thanh khác nhau cho từng loại tìm kiếm

### Cấp độ 2: Tính năng nâng cao
- **Tìm kiếm nhiều phần tử**: Tìm tất cả vị trí của một giá trị
- **Tìm kiếm thông minh**: Tìm kiếm theo nhiều tiêu chí
- **So sánh hiệu suất**: Đo thời gian thực thi của các thuật toán

### Cấp độ 3: Sáng tạo
- **Game tìm kiếm**: Tạo trò chơi tìm kiếm thẻ bài
- **Thuật toán riêng**: Thiết kế thuật toán tìm kiếm mới
- **Dự án tích hợp**: Kết hợp tìm kiếm với các thuật toán đã học

## 📝 Bài tập về nhà

### Bài tập bắt buộc
1. **Tìm kiếm điểm số**: Viết thuật toán tìm kiếm điểm trong danh sách
2. **Tìm kiếm tên**: Tạo chương trình tìm kiếm tên học sinh theo ABC
3. **So sánh thuật toán**: So sánh số lần kiểm tra giữa 2 thuật toán

### Bài tập nâng cao
1. **Tìm kiếm phức tạp**: Tìm kiếm trong danh sách có 100 phần tử
2. **Tìm kiếm thông minh**: Tìm kiếm theo nhiều tiêu chí
3. **Tối ưu hóa**: Tìm cách giảm số lần kiểm tra

### Bài tập sáng tạo
1. **Game tìm kiếm**: Tạo game tìm kiếm với giao diện đẹp
2. **Thuật toán riêng**: Thiết kế thuật toán tìm kiếm độc đáo
3. **Dự án tích hợp**: Kết hợp tìm kiếm với sắp xếp và đếm

## 🔧 Tài nguyên hỗ trợ

### Tài liệu tham khảo
- **Python Programming**: Hướng dẫn lập trình Python cơ bản
- **Algorithm Visualization**: Công cụ minh họa thuật toán tìm kiếm
- **Search Algorithms**: Các thuật toán tìm kiếm phổ biến

### Công cụ hỗ trợ
- **Python Editor**: Môi trường lập trình Python
- **Algorithm Simulator**: Mô phỏng thuật toán tìm kiếm
- **Debugging Tools**: Công cụ gỡ lỗi và tối ưu hóa

### Đánh giá và phản hồi
- **Rubric đánh giá**: Tiêu chí đánh giá kỹ năng tìm kiếm
- **Peer Review**: Đánh giá lẫn nhau giữa học sinh
- **Portfolio**: Tập hợp các dự án và bài tập của học sinh
