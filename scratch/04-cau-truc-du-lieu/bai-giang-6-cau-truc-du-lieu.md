# Bài giảng 6: Cấu trúc dữ liệu cơ bản

## 📋 Thông tin bài học
- **Thời gian**: 90 phút (2 tiết)
- **Độ tuổi**: Lớp 4-5 (9-11 tuổi)
- **Mức độ**: Trung bình đến nâng cao
- **Mục tiêu**: Hiểu các cấu trúc dữ liệu cơ bản để chuẩn bị cho Python

## 🎯 Mục tiêu học tập

### Kiến thức
- Hiểu khái niệm cấu trúc dữ liệu
- Biết cách sử dụng danh sách (List) hiệu quả
- Hiểu cách tổ chức và quản lý dữ liệu

### Kỹ năng
- Thao tác với danh sách
- Tìm kiếm và sắp xếp dữ liệu
- Quản lý bộ nhớ và hiệu suất

### Thái độ
- Phát triển tư duy tổ chức
- Rèn luyện tính cẩn thận
- Khuyến khích tư duy hệ thống


## 📊 Nội dung bài học

### Phần 1: Giới thiệu cấu trúc dữ liệu (15 phút)

#### Hoạt động khởi động - "Trò chơi tổ chức đồ vật"
- **Hoạt động**: Yêu cầu học sinh sắp xếp đồ vật trên bàn
- **Mục tiêu**: Hiểu cách tổ chức thông tin
- **Ví dụ**: Sắp xếp bút theo màu, sách theo kích thước

#### Ví dụ thực tế từ cuộc sống
- **Danh sách mua sắm**: Táo, Chuối, Cam (có thứ tự)
- **Hộp đồ chơi**: LEGO xanh, LEGO đỏ, LEGO vàng (phân loại)
- **Gia đình**: Ông bà → Bố mẹ → Con cái (cây gia đình)
- **Lớp học**: Danh sách học sinh theo thứ tự ABC

#### Khái niệm cơ bản qua ví dụ
- **Dữ liệu**: Những thông tin cần nhớ (tên, số, màu sắc)
- **Cấu trúc**: Cách sắp xếp để dễ tìm (theo thứ tự, theo nhóm)
- **Truy cập**: Cách lấy thông tin ra khi cần (tìm trong danh sách)

### Phần 2: Danh sách (List) cơ bản (25 phút)

#### Khái niệm danh sách qua trò chơi
- **Trò chơi**: "Danh sách đồ chơi yêu thích"
- **Hoạt động**: Mỗi học sinh viết 5 đồ chơi yêu thích
- **Mục tiêu**: Hiểu danh sách có thứ tự và có thể thay đổi

#### Ví dụ thực tế
- **Danh sách bài hát**: [Bài 1, Bài 2, Bài 3, Bài 4, Bài 5]
- **Danh sách Pokemon**: ["Pikachu", "Charizard", "Blastoise"]
- **Danh sách điểm số**: [8, 9, 7, 10, 6]

#### Tạo danh sách trong Scratch - "Trò chơi thu thập Pokemon"
```scratch
Khi cờ xanh được nhấn
xóa tất cả trong [Pokemon v]
nói [Bắt đầu thu thập Pokemon!] trong (2) giây
thêm [Pikachu] vào [Pokemon v]
thêm [Charmander] vào [Pokemon v]
thêm [Squirtle] vào [Pokemon v]
thêm [Bulbasaur] vào [Pokemon v]
```

#### Thao tác với danh sách - "Thêm Pokemon mới"
```scratch
Khi nhấn phím [a v]
thêm [Eevee] vào [Pokemon v]
nói [Đã bắt được Eevee!] trong (2) giây
phát âm thanh [pop v]

Khi nhấn phím [d v]
xóa (mục cuối) khỏi [Pokemon v]
nói [Pokemon cuối đã chạy mất!] trong (2) giây
phát âm thanh [pop v]
```

#### Truy cập phần tử - "Xem Pokemon nào mạnh nhất"
```scratch
Khi nhấn phím [s v]
nói [Pokemon đầu tiên: ] + (mục (1) của [Pokemon v]) trong (2) giây
nói [Pokemon cuối: ] + (mục cuối của [Pokemon v]) trong (2) giây
```

### Phần 3: Danh sách 2 chiều - "Bảng điểm Pokemon" (20 phút)

#### Khái niệm qua ví dụ thực tế
- **Trò chơi**: "Bảng điểm Pokemon"
- **Hoạt động**: Mỗi Pokemon có điểm tấn công, phòng thủ, tốc độ
- **Mục tiêu**: Hiểu cách lưu trữ nhiều thông tin về một đối tượng

#### Ví dụ thực tế
- **Bảng điểm học sinh**: Tên + Toán + Văn + Anh
- **Menu nhà hàng**: Tên món + Giá + Độ cay
- **Thư viện**: Tên sách + Tác giả + Năm xuất bản

#### Tạo bảng điểm Pokemon
```scratch
Khi cờ xanh được nhấn
xóa tất cả trong [BangDiemPokemon v]
thêm [Pikachu,85,60,90] vào [BangDiemPokemon v]
thêm [Charizard,84,78,100] vào [BangDiemPokemon v]
thêm [Blastoise,83,100,78] vào [BangDiemPokemon v]
nói [Đã tạo bảng điểm Pokemon!] trong (2) giây
```

#### Truy cập dữ liệu trong bảng
```scratch
Khi nhấn phím [t v]
nói [Thông tin Pikachu: ] + (mục (1) của [BangDiemPokemon v]) trong (3) giây
nói [Thông tin Charizard: ] + (mục (2) của [BangDiemPokemon v]) trong (3) giây
```

#### Tính điểm tổng của Pokemon
```scratch
Khi nhấn phím [tb v]
đặt [TongDiem v] thành (0)
đặt [SoChiSo v] thành (3)
đặt [i v] thành (1)
lặp lại (SoChiSo) lần
thay đổi [TongDiem v] bởi (mục (i) của [BangDiemPokemon v])
thay đổi [i v] bởi (1)
đặt [DiemTB v] thành ([TongDiem v] / [SoChiSo v])
nói [Điểm tổng Pokemon: ] + [DiemTB v] trong (2) giây
```

### Phần 4: Tìm kiếm trong danh sách - "Tìm Pokemon mạnh nhất" (15 phút)

#### Trò chơi tìm kiếm
- **Hoạt động**: "Tìm Pokemon có điểm cao nhất"
- **Mục đích**: Hiểu cách tìm kiếm trong danh sách
- **Ví dụ**: Tìm Pokemon nào mạnh nhất trong đội

#### Lập trình tìm kiếm Pokemon mạnh nhất
```scratch
Khi nhấn phím [f v]
đặt [DiemCaoNhat v] thành (0)
đặt [PokemonManhNhat v] thành []
đặt [ViTri v] thành (1)
lặp lại (độ dài của [Pokemon v]) lần
nếu <(mục (ViTri) của [Pokemon v]) > [DiemCaoNhat v]> thì
đặt [DiemCaoNhat v] thành (mục (ViTri) của [Pokemon v])
đặt [PokemonManhNhat v] thành (mục (ViTri) của [Pokemon v])
thay đổi [ViTri v] bởi (1)
nói [Pokemon mạnh nhất: ] + [PokemonManhNhat v] + [ với điểm: ] + [DiemCaoNhat v] trong (3) giây
```

#### Tìm kiếm Pokemon cụ thể
```scratch
Khi nhấn phím [search v]
đặt [PokemonCanTim v] thành [Pikachu]
đặt [ViTri v] thành (1)
đặt [TimThay v] thành [false]
lặp lại (độ dài của [Pokemon v]) lần
nếu <(mục (ViTri) của [Pokemon v]) = [PokemonCanTim v]> thì
đặt [TimThay v] thành [true]
dừng [vòng lặp này v]
thay đổi [ViTri v] bởi (1)
nếu <[TimThay v] = [true]> thì
nói [Tìm thấy ] + [PokemonCanTim v] + [ tại vị trí: ] + [ViTri v] trong (2) giây
nếu không
nói [Không tìm thấy ] + [PokemonCanTim v] trong (2) giây
```

### Phần 5: Sắp xếp danh sách - "Xếp hạng Pokemon" (15 phút)

#### Trò chơi sắp xếp
- **Hoạt động**: "Xếp hạng Pokemon theo độ mạnh"
- **Mục đích**: Hiểu cách sắp xếp dữ liệu
- **Ví dụ**: Xếp Pokemon từ mạnh nhất đến yếu nhất

#### Sắp xếp Pokemon theo điểm (Bubble Sort)
```scratch
Khi nhấn phím [sort v]
nói [Bắt đầu xếp hạng Pokemon...] trong (2) giây
đặt [i v] thành (1)
lặp lại (độ dài của [Pokemon v]) lần
đặt [j v] thành (1)
lặp lại ((độ dài của [Pokemon v]) - [i v]) lần
nếu <(mục (j) của [Pokemon v]) > (mục ((j) + (1)) của [Pokemon v])> thì
đặt [Temp v] thành (mục (j) của [Pokemon v])
thay thế mục (j) của [Pokemon v] bằng (mục ((j) + (1)) của [Pokemon v])
thay thế mục ((j) + (1)) của [Pokemon v] bằng [Temp v]
phát âm thanh [pop v]
thay đổi [j v] bởi (1)
thay đổi [i v] bởi (1)
nói [Đã xếp hạng xong! Pokemon mạnh nhất: ] + (mục (1) của [Pokemon v]) trong (3) giây
```

#### Hiển thị bảng xếp hạng
```scratch
Khi nhấn phím [rank v]
đặt [ViTri v] thành (1)
lặp lại (độ dài của [Pokemon v]) lần
nói [Hạng ] + [ViTri v] + [: ] + (mục (ViTri) của [Pokemon v]) trong (2) giây
thay đổi [ViTri v] bởi (1)
```

## 🎨 Hoạt động mở rộng

### Cấp độ 1: Thêm tính năng cơ bản
- **Thêm Pokemon mới**: Tạo giao diện để nhập Pokemon và điểm số
- **Xóa Pokemon**: Thêm chức năng xóa Pokemon khỏi danh sách
- **Hiển thị đẹp**: Tạo giao diện hiển thị danh sách Pokemon đẹp mắt

### Cấp độ 2: Tính năng nâng cao
- **Sắp xếp theo nhiều tiêu chí**: Theo điểm tấn công, phòng thủ, hoặc tốc độ
- **Tìm kiếm thông minh**: Tìm Pokemon theo loại hoặc điểm số
- **Thống kê**: Tính điểm trung bình, cao nhất, thấp nhất của đội

### Cấp độ 3: Sáng tạo
- **Hệ thống Pokemon hoàn chỉnh**: Tạo game Pokemon mini với đầy đủ tính năng
- **Thiết kế cấu trúc dữ liệu riêng**: Tạo hệ thống lưu trữ Pokemon theo ý tưởng riêng
- **Áp dụng vào bài toán thực tế**: Quản lý điểm số lớp học, thư viện sách

## 📝 Bài tập về nhà

### Bài tập bắt buộc
1. **Tạo đội Pokemon**: Tạo danh sách 5 Pokemon yêu thích và sắp xếp theo độ mạnh
2. **Tìm Pokemon mạnh nhất**: Viết chương trình tìm Pokemon có điểm cao nhất
3. **Tính điểm trung bình**: Tính điểm trung bình của đội Pokemon

### Bài tập nâng cao
1. **Bảng điểm Pokemon**: Tạo bảng điểm với Pokemon, điểm tấn công, phòng thủ, tốc độ
2. **Xếp hạng toàn diện**: Tính điểm tổng và xếp hạng Pokemon theo điểm tổng
3. **Tìm kiếm Pokemon**: Tạo chức năng tìm Pokemon theo tên hoặc điểm số

## 🔍 Đánh giá

### Tiêu chí đánh giá
| Tiêu chí | Điểm | Mô tả |
|----------|------|-------|
| Hiểu cấu trúc dữ liệu | 3 | Giải thích được khái niệm |
| Thao tác đúng | 3 | Code hoạt động chính xác |
| Tối ưu hóa | 2 | Sử dụng hiệu quả |
| Sáng tạo | 1 | Có yếu tố độc đáo |
| Trình bày | 1 | Giải thích rõ ràng |
| Tổng cộng | 10 | |

### Cách đánh giá
- **Quan sát**: Giáo viên quan sát quá trình làm việc
- **Sản phẩm**: Kiểm tra chương trình hoàn chỉnh
- **Trình bày**: Học sinh demo và giải thích
- **Phản hồi**: Nhận xét từ bạn cùng lớp

## 🚀 Lưu ý quan trọng

### Cho giáo viên
- Giải thích kỹ khái niệm cấu trúc dữ liệu
- Sử dụng ví dụ thực tế để minh họa
- Khuyến khích học sinh thử nghiệm
- Chuẩn bị nhiều bài tập thực hành

### Cho học sinh
- Hiểu rõ từng thao tác với danh sách
- Test kỹ từng chức năng
- Không ngại thử nghiệm với dữ liệu khác
- Lưu dự án thường xuyên

## 💡 Mẹo hay

### Quản lý danh sách
- Luôn kiểm tra độ dài danh sách
- Sử dụng biến tạm thời khi cần
- Tránh truy cập phần tử không tồn tại

### Tối ưu hiệu suất
- Sử dụng vòng lặp hiệu quả
- Tránh lặp lại không cần thiết
- Sắp xếp dữ liệu khi cần thiết

### Debug hiệu quả
- Sử dụng "say" để theo dõi giá trị
- Kiểm tra từng bước một
- Test với dữ liệu mẫu

## 🔗 Kết nối với Python

### Khái niệm tương đồng
- **Danh sách**: Scratch lists ↔ Python lists
- **Truy cập**: Scratch mục (i) ↔ Python list[i]
- **Thao tác**: Scratch thêm/xóa ↔ Python append/remove
- **Vòng lặp**: Scratch lặp lại ↔ Python for loop

### Chuẩn bị cho Python
- Hiểu cú pháp truy cập phần tử
- Làm quen với các phương thức
- Thực hành với các bài toán thực tế

## 📚 Tài liệu tham khảo

- [Data Structure for Kids - JetLearn](https://www.jetlearn.com/blog/data-structure-for-kids-a-complete-guide-to-teaching-logic-through-code)
- [Scratch Data Structures](https://scratch.mit.edu/explore/projects/data)
- [Introduction to Data Structures](https://scratch.mit.edu/tutorials)
- [Python Lists Tutorial](https://python.org)

---

**Tác giả**: AI & Trần Việt Trung (BKHN)  
**Ngày tạo**: 04/10/2025  
**Phiên bản**: 1.0
