# 🎮 Giáo Trình Scratch Cho Học Sinh Tiểu Học

## 📋 Giới thiệu

Phần này chứa **30 bài giảng Scratch** dành cho học sinh tiểu học (lớp 3-5), giúp các em phát triển tư duy lập trình từ cơ bản đến nâng cao.

**Cấu trúc:**
- **Giai đoạn 1 (Nền tảng)**: 17 bài học - Từ làm quen đến hàm và modular
- **Giai đoạn 2 (Nâng cao)**: 13 bài học - Thuật toán nâng cao, mô phỏng, tìm đường, game nâng cao

📖 **Xem lộ trình nâng cao chi tiết**: [LO-TRINH-NAP-CAO.md](LO-TRINH-NAP-CAO.md) 

**Lưu ý về đánh số bài:**
- Bài 1.5 là bài bổ sung về Blocks, nên dạy sau Bài 1 để hiểu nền tảng
- Bài 2.5 là bài bổ sung về biến số, nên dạy sau Bài 2 hoặc trước Bài 3
- Bài 2.6 là bài bổ sung về Broadcast/Events, nên dạy trước Bài 5 (Câu chuyện tương tác)
- Bài 3.5 là bài bổ sung về Custom Blocks, nên dạy sau Bài 3, trước Bài 8
- Bài 7A, 7B, 7C, 7D, 7E, 7F là các phần của chủ đề Thuật toán
  - Bài 7D (Swap) phải dạy trước Bài 7F (Sắp xếp) vì swap là kỹ thuật cốt lõi
  - Bài 7E (Tìm kiếm) có thể dạy sau Bài 7A, không nhất thiết phải sau Bài 7F

## 🎯 Mục tiêu

- **Phát triển tư duy logic** thông qua lập trình trực quan
- **Rèn luyện kỹ năng giải quyết vấn đề** bằng cách chia nhỏ vấn đề phức tạp
- **Khuyến khích sáng tạo** và tạo ra sản phẩm cá nhân
- **Chuẩn bị nền tảng** cho việc chuyển sang Python

## 📚 Cấu trúc bài học

**Tổng cộng: 30 bài học** (17 bài nền tảng + 13 bài nâng cao)

Giáo trình được tổ chức thành **11 topic chính**, chia thành 2 giai đoạn:

### 📁 **Cấu trúc thư mục theo Topic**

#### **Giai đoạn 1: Nền tảng** (17 bài)
```
scratch/
├── 01-lam-quen/              # Làm quen với Scratch (2 bài)
├── 02-blocks-va-bien/        # Blocks và Biến số (3 bài)
├── 03-game-va-ung-dung/      # Game và Ứng dụng (4 bài)
├── 04-cau-truc-du-lieu/      # Cấu trúc dữ liệu (1 bài)
├── 05-thuat-toan/            # Thuật toán cơ bản (6 bài)
└── 06-ham-va-modular/        # Hàm và Modular (1 bài)
```

#### **Giai đoạn 2: Nâng cao** (13 bài) - *Xem [LO-TRINH-NAP-CAO.md](LO-TRINH-NAP-CAO.md)*
```
scratch/
├── 07-thuat-toan-du-lieu-nang-cao/  # Thuật toán dữ liệu nâng cao (3 bài)
├── 08-mo-phong-nang-cao/            # Mô phỏng nâng cao (3 bài)
├── 09-tim-duong/                     # Tìm đường (3 bài)
├── 10-game-nang-cao/                 # Game nâng cao (3 bài)
└── 11-tu-duy-may-tinh/               # Tư duy máy tính nâng cao (3 bài)
```

---

### 🎮 **Topic 1: Làm quen với Scratch** (`01-lam-quen/`)

#### **Bài 1: Trò chơi "Mèo đuổi chuột"** (`01-lam-quen/bai-giang-1-meo-duoi-chuot.md`)
- **Mục tiêu**: Làm quen với chuyển động và tương tác
- **Kiến thức**: Khối lệnh chuyển động, cảm biến phím, điều kiện
- **Kỹ năng**: Tạo nhân vật, lập trình chuyển động, thêm âm thanh
- **Thời gian**: 60 phút

#### **Bài 1.5: Giới thiệu về Blocks (Khối lệnh)** (`01-lam-quen/bai-giang-1-5-gioi-thieu-blocks.md`) *(Bài bổ sung - Nền tảng cho Scratch)*
- **Mục tiêu**: Hiểu khái niệm blocks và cách sử dụng các loại blocks trong Scratch
- **Kiến thức**: Các loại blocks (Motion, Looks, Sound, Events, Control, Sensing, Operators, Variables)
- **Kỹ năng**: Nhận biết và phân loại blocks, kết hợp blocks, đọc code Scratch
- **Thời gian**: 45 phút (1 tiết)
- **Lưu ý**: Nên dạy sau Bài 1 để học sinh hiểu blocks trước khi dùng nhiều hơn

---

### 🔧 **Topic 2: Blocks và Biến số** (`02-blocks-va-bien/`)

#### **Bài 2: Thiệp sinh nhật động** (`02-blocks-va-bien/bai-giang-2-thiep-sinh-nhat-dong.md`)
- **Mục tiêu**: Học về giao diện và hiệu ứng
- **Kiến thức**: Khối lệnh Looks, Sound, Events
- **Kỹ năng**: Tạo hoạt hình, thêm hiệu ứng, thiết kế giao diện
- **Thời gian**: 60 phút

#### **Bài 2.5: Biến số cơ bản** (`02-blocks-va-bien/bai-giang-2-5-bien-so-co-ban.md`) *(Bài bổ sung - có thể dạy sau Bài 2 hoặc trước Bài 3)*
- **Mục tiêu**: Làm quen với biến số và cách sử dụng
- **Kiến thức**: Khái niệm biến số, tạo và sử dụng biến số
- **Kỹ năng**: Tạo biến số, đếm và tính toán, hiển thị giá trị
- **Thời gian**: 45 phút
- **Lưu ý**: Bài này nên dạy trước Bài 3 để học sinh hiểu biến số trước khi làm game phức tạp

#### **Bài 2.6: Broadcast và Events (Sự kiện)** (`02-blocks-va-bien/bai-giang-2-6-broadcast-va-events.md`) *(Bài bổ sung - Nền tảng cho giao tiếp)*
- **Mục tiêu**: Hiểu khái niệm broadcast và events, cách các thành phần giao tiếp với nhau
- **Kiến thức**: Events, broadcast message, message passing, observer pattern
- **Kỹ năng**: Tạo và sử dụng broadcast, thiết kế hệ thống giao tiếp
- **Thời gian**: 60 phút (1 tiết)
- **Lưu ý**: Nên dạy trước Bài 5 (Câu chuyện tương tác) để học sinh hiểu broadcast trước khi dùng

---

### 🎮 **Topic 3: Game và Ứng dụng** (`03-game-va-ung-dung/`)

#### **Bài 3: Trò chơi "Bảo vệ đảo"** (`03-game-va-ung-dung/bai-giang-3-bao-ve-dao.md`)
- **Mục tiêu**: Giới thiệu clone và hệ thống điểm số
- **Kiến thức**: Clone, biến số, hệ thống điểm
- **Kỹ năng**: Tạo nhiều đối tượng, quản lý điểm số, tạo game hoàn chỉnh
- **Thời gian**: 120 phút (2 tiết)

#### **Bài 3.5: Custom Blocks (Khối lệnh tùy chỉnh)** (`03-game-va-ung-dung/bai-giang-3-5-custom-blocks.md`) *(Bài bổ sung - Tái sử dụng code)*
- **Mục tiêu**: Hiểu và tạo custom blocks để tái sử dụng code
- **Kiến thức**: Custom blocks, tham số, tái sử dụng code
- **Kỹ năng**: Tạo custom blocks, sử dụng tham số, tổ chức code
- **Thời gian**: 60 phút (1 tiết)
- **Lưu ý**: Nên dạy sau Bài 3, trước Bài 8 (Hàm và thủ tục) để học sinh hiểu custom blocks cơ bản

#### **Bài 4: Máy tính đơn giản** (`03-game-va-ung-dung/bai-giang-4-may-tinh-don-gian.md`)
- **Mục tiêu**: Học về biến số và logic tính toán
- **Kiến thức**: Biến số, phép toán, điều kiện phức tạp
- **Kỹ năng**: Tạo ứng dụng tính toán, xử lý input, hiển thị kết quả
- **Thời gian**: 90 phút

#### **Bài 5: Câu chuyện tương tác** (`03-game-va-ung-dung/bai-giang-5-cau-chuyen-tuong-tac.md`)
- **Mục tiêu**: Phát triển kỹ năng storytelling và broadcast
- **Kiến thức**: Broadcast, Events, điều khiển luồng chương trình
- **Kỹ năng**: Tạo câu chuyện tương tác, quản lý scene, thiết kế UX
- **Thời gian**: 90 phút

---

### 📊 **Topic 4: Cấu trúc dữ liệu** (`04-cau-truc-du-lieu/`)

#### **Bài 6: Cấu trúc dữ liệu cơ bản** (`04-cau-truc-du-lieu/bai-giang-6-cau-truc-du-lieu.md`)
- **Mục tiêu**: Học về danh sách và tổ chức thông tin
- **Kiến thức**: List, array, tổ chức dữ liệu
- **Kỹ năng**: Quản lý danh sách, tìm kiếm, sắp xếp
- **Thời gian**: 90 phút (1 tiết)
- **Lưu ý**: Bài này là nền tảng cho các bài thuật toán (7A, 7B, 7C, 7D, 7E, 7F)

---

### 🧠 **Topic 5: Thuật toán** (`05-thuat-toan/`)

#### **Bài 7A: Thuật toán tìm số lớn nhất và nhỏ nhất** (`05-thuat-toan/bai-giang-7a-tim-so-lon-nhat-nho-nhat.md`) *(Phần 1/6 của chủ đề Thuật toán)*
- **Mục tiêu**: Hiểu và áp dụng thuật toán tìm số lớn nhất, nhỏ nhất trong danh sách
- **Kiến thức**: Thuật toán tìm max, min, tối ưu hóa tìm cả hai
- **Kỹ năng**: Phân tích vấn đề, thiết kế thuật toán tìm kiếm, debug code
- **Thời gian**: 90 phút (1 tiết)
- **Lưu ý**: Nên dạy liên tiếp với 7B, 7C, 7D để học sinh hiểu đầy đủ về thuật toán

#### **Bài 7B: Thuật toán đếm** (`05-thuat-toan/bai-giang-7b-thuat-toan-dem.md`) *(Phần 2/6 của chủ đề Thuật toán)*
- **Mục tiêu**: Hiểu và áp dụng thuật toán đếm số phần tử theo điều kiện
- **Kiến thức**: Thuật toán đếm, đếm với điều kiện, đếm nhiều loại
- **Kỹ năng**: Thiết kế thuật toán đếm, sử dụng biến đếm hiệu quả
- **Thời gian**: 90 phút (1 tiết)
- **Lưu ý**: Yêu cầu đã hoàn thành Bài 7A

#### **Bài 7C: Thuật toán tính toán** (`05-thuat-toan/bai-giang-7c-thuat-toan-tinh-toan.md`) *(Phần 3/6 của chủ đề Thuật toán)*
- **Mục tiêu**: Học thuật toán tính tổng và trung bình, tích hợp nhiều thuật toán
- **Kiến thức**: Tính tổng, tính trung bình, tích hợp nhiều thuật toán
- **Kỹ năng**: Thiết kế thuật toán tính toán, tích hợp hệ thống
- **Thời gian**: 90 phút (1 tiết)
- **Lưu ý**: Yêu cầu đã hoàn thành Bài 7A và 7B

#### **Bài 7D: Thuật toán Swap (Thay thế/Đổi chỗ)** (`05-thuat-toan/bai-giang-7d-thuat-toan-swap.md`) *(Phần 4/6 của chủ đề Thuật toán - Nền tảng cho sắp xếp)*
- **Mục tiêu**: Hiểu và áp dụng thuật toán swap để đổi chỗ hai giá trị
- **Kiến thức**: Khái niệm swap, biến tạm, đổi chỗ trong danh sách
- **Kỹ năng**: Thực hiện swap đúng cách, sử dụng biến tạm hiệu quả
- **Thời gian**: 60 phút (1 tiết)
- **Yêu cầu**: Đã hoàn thành Bài 7A
- **Lưu ý**: Phải dạy trước Bài 7F (Sắp xếp) vì swap là kỹ thuật cốt lõi

#### **Bài 7E: Thuật toán tìm kiếm** (`05-thuat-toan/bai-giang-7e-thuat-toan-tim-kiem.md`) *(Phần 5/6 của chủ đề Thuật toán)*
- **Mục tiêu**: Hiểu và áp dụng thuật toán tìm kiếm để tìm phần tử trong danh sách
- **Kiến thức**: Tìm kiếm tuyến tính, tìm vị trí, xử lý không tìm thấy
- **Kỹ năng**: Thiết kế thuật toán tìm kiếm, xử lý các trường hợp đặc biệt
- **Thời gian**: 90 phút (1 tiết)
- **Yêu cầu**: Đã hoàn thành Bài 7A
- **Lưu ý**: Có thể dạy sau Bài 7A, không nhất thiết phải sau Bài 7F

#### **Bài 7F: Thuật toán sắp xếp** (`05-thuat-toan/bai-giang-7f-thuat-toan-sap-xep.md`) *(Phần 6/6 của chủ đề Thuật toán)*
- **Mục tiêu**: Học thuật toán sắp xếp cơ bản
- **Kiến thức**: Sắp xếp nổi bọt, sắp xếp chọn, so sánh hiệu suất
- **Kỹ năng**: Thiết kế thuật toán sắp xếp, phân tích hiệu suất
- **Thời gian**: 90 phút (1 tiết)
- **Yêu cầu**: Đã hoàn thành Bài 7A, 7B, 7C và 7D (swap)

---

### 🔨 **Topic 6: Hàm và Modular** (`06-ham-va-modular/`)

#### **Bài 8: Hàm và thủ tục** (`06-ham-va-modular/bai-giang-8-ham-va-thu-tuc.md`) *(Nâng cao về Custom Blocks)*
- **Mục tiêu**: Chuẩn bị cho lập trình modular
- **Kiến thức**: Custom blocks nâng cao, functions phức tạp, code reuse
- **Kỹ năng**: Tạo hàm tùy chỉnh phức tạp, tổ chức code, modular programming
- **Thời gian**: 120 phút (2 tiết)
- **Lưu ý**: Yêu cầu đã hoàn thành Bài 3.5 (Custom Blocks cơ bản)

---

## 🚀 **Giai đoạn 2: Nâng cao** (Sau khi hoàn thành 17 bài nền tảng)

Sau khi học sinh đã nắm vững các kiến thức nền tảng, có thể tiếp tục với các topic nâng cao:

### 🧠 **Topic 7: Thuật toán dữ liệu nâng cao** (`07-thuat-toan-du-lieu-nang-cao/`)
- **Bài 9A**: Tìm kiếm nâng cao (mode, filter, vị trí đầu/cuối) - *Mở rộng từ Bài 7E*
- **Bài 9B**: Sắp xếp nâng cao - Insertion Sort - *Mới, so sánh với Bubble/Selection Sort đã học ở Bài 7F*
- **Bài 9C**: Thuật toán thống kê nâng cao (tính tổng có điều kiện, thống kê phức tạp) - *Mở rộng từ Bài 7C*

📖 **Chi tiết**: [Topic 7 README](07-thuat-toan-du-lieu-nang-cao/README.md)

### 🤖 **Topic 8: Mô phỏng nâng cao** (`08-mo-phong-nang-cao/`)
- **Bài 10A**: Mô phỏng nhiều đối tượng tương tác (Boids, va chạm, lan truyền)
- **Bài 10B**: Mô phỏng vật lý nâng cao (trọng lực, ma sát, quán tính)
- **Bài 10C**: Mô phỏng hệ thống (giao thông, robot, cửa tự động)

📖 **Chi tiết**: [Topic 8 README](08-mo-phong-nang-cao/README.md)

### 🧭 **Topic 9: Tìm đường** (`09-tim-duong/`)
- **Bài 11A**: Wall Follower (Đi theo tường)
- **Bài 11B**: Line Following Robot
- **Bài 11C**: Tìm đường bằng cảm biến

📖 **Chi tiết**: [Topic 9 README](09-tim-duong/README.md)

### 🎮 **Topic 10: Game nâng cao** (`10-game-nang-cao/`)
- **Bài 12A**: Hệ thống vật phẩm / Inventory
- **Bài 12B**: AI đơn giản cho kẻ thù
- **Bài 12C**: Hệ thống điểm & khó dần

📖 **Chi tiết**: [Topic 10 README](10-game-nang-cao/README.md)

### 🏛 **Topic 11: Tư duy máy tính nâng cao** (`11-tu-duy-may-tinh/`)
- **Bài 13A**: Hàm có tham số nâng cao
- **Bài 13B**: Debug — Tìm lỗi
- **Bài 13C**: Thiết kế thuật toán

📖 **Chi tiết**: [Topic 11 README](11-tu-duy-may-tinh/README.md)

**📘 Xem lộ trình chi tiết**: [LO-TRINH-NAP-CAO.md](LO-TRINH-NAP-CAO.md)

---

## 🎯 Độ tuổi phù hợp

| Độ tuổi | Bài học | Mức độ | Thời gian |
|---------|---------|--------|-----------|
| **8-9 tuổi** | Bài 1-1.5, 2-2.5 | Cơ bản | 45-60 phút/bài |
| **9-10 tuổi** | Bài 3-5 | Trung bình | 90-120 phút/bài |
| **10-11 tuổi** | Bài 6-8 | Nâng cao | 90 phút/bài |

**Lưu ý về số lượng bài:**
- **Giai đoạn 1 (Nền tảng)**: 17 bài (bao gồm Bài 1.5, 2.5, 2.6, 3.5 và 6 bài thuật toán 7A-7F)
- **Giai đoạn 2 (Nâng cao)**: 13 bài (Topic 7-11)
- **Tổng cộng**: 30 bài học

**Lưu ý về thời gian:**
- Bài 2.5: 45 phút (bài ngắn, bổ sung)
- Bài 3: 120 phút (2 tiết, dự án lớn)
- Bài 6, 7A, 7B, 7C, 8: 90 phút (1 tiết)

## 🛠️ Công cụ cần thiết

### Phần mềm
- **Scratch Online**: [scratch.mit.edu](https://scratch.mit.edu) (miễn phí)
- **Scratch Desktop**: Tải về để sử dụng offline
- **Trình duyệt**: Chrome, Firefox, Safari

### Tài khoản
- Tạo tài khoản Scratch cho giáo viên
- Hướng dẫn học sinh tạo tài khoản riêng
- Lưu trữ dự án trên cloud

## 📖 Cách sử dụng

### Cho giáo viên
1. **Đọc kỹ bài giảng** trước khi dạy
2. **Thực hành trước** các dự án mẫu
3. **Chuẩn bị file mẫu** để hỗ trợ học sinh
4. **Điều chỉnh tốc độ** theo trình độ lớp

### Cho học sinh
1. **Làm theo hướng dẫn** từng bước
2. **Thực hành** các bài tập trong bài
3. **Thử nghiệm** và sáng tạo
4. **Chia sẻ** sản phẩm với bạn bè

## 🎨 Phương pháp giảng dạy

### Cấu trúc bài học chuẩn
1. **Khởi động** (5-10 phút): Hoạt động không máy tính
2. **Giới thiệu** (10-15 phút): Khái niệm mới và ví dụ
3. **Thực hành có hướng dẫn** (15-20 phút): Giáo viên làm mẫu
4. **Thực hành độc lập** (10-15 phút): Học sinh tự làm
5. **Tổng kết** (5-10 phút): Chia sẻ và nhận xét

### Phương pháp hiệu quả
- **Học qua trò chơi**: Biến bài học thành trò chơi
- **Học qua dự án**: Tạo ra sản phẩm cụ thể
- **Học hợp tác**: Làm việc nhóm 2-3 học sinh
- **Học qua khám phá**: Để học sinh tự thử nghiệm

## 📊 Đánh giá và theo dõi

### Tiêu chí đánh giá
| Tiêu chí | Điểm | Mô tả |
|----------|------|-------|
| Hoàn thành cơ bản | 3 | Dự án chạy được, có chức năng chính |
| Tính năng bổ sung | 2 | Thêm âm thanh, hiệu ứng, tính năng |
| Sáng tạo | 2 | Thay đổi nhân vật, câu chuyện độc đáo |
| Chia sẻ | 1 | Trình bày sản phẩm trước lớp |
| Hỗ trợ bạn | 1 | Giúp đỡ bạn cùng lớp |
| **Tổng cộng** | **9** | |

### Cách đánh giá
- **Quan sát**: Giáo viên quan sát quá trình làm việc
- **Sản phẩm**: Kiểm tra dự án hoàn chỉnh
- **Trình bày**: Học sinh demo và giải thích
- **Phản hồi**: Nhận xét từ bạn cùng lớp

## 🚀 Lưu ý quan trọng

### Cho giáo viên
- **Kiên nhẫn** với học sinh chậm hiểu
- **Khuyến khích** sáng tạo và thử nghiệm
- **Tạo không khí** học tập vui vẻ
- **Chuẩn bị sẵn** file mẫu để hỗ trợ

### Cho học sinh
- **Không sợ mắc lỗi**, hãy thử nghiệm
- **Hỏi giáo viên** khi không hiểu
- **Giúp đỡ bạn** cùng lớp
- **Lưu dự án** thường xuyên

## 💡 Mẹo hay

### Học Scratch hiệu quả
- Bắt đầu với các dự án đơn giản
- Thực hành thường xuyên
- Tham khảo dự án của người khác
- Tham gia cộng đồng Scratch

### Tránh lỗi thường gặp
- Kiểm tra kết nối internet
- Lưu dự án thường xuyên
- Không xóa nhân vật quan trọng
- Test dự án trước khi chia sẻ

### Sáng tạo
- Thay đổi nhân vật và hình nền
- Thêm âm thanh và hiệu ứng
- Tạo câu chuyện độc đáo
- Thêm tính năng mới

## 📚 Tài liệu tham khảo

### Trang web chính thức
- [Scratch.mit.edu](https://scratch.mit.edu) - Trang chủ Scratch
- [Scratch Tutorials](https://scratch.mit.edu/tutorials) - Hướng dẫn chính thức
- [Scratch Community](https://scratch.mit.edu/explore) - Cộng đồng Scratch

### Sách tham khảo
- "Tự học lập trình Scratch" - Bùi Việt Hà
- "Coding projects in Scratch" - Jon Woodcock
- "Scratch Programming for Kids" - DK Publishing

### Video hướng dẫn
- Scratch Official YouTube Channel
- Khan Academy Computer Science
- Code.org Scratch Courses

## 🤝 Đóng góp

Chúng tôi hoan nghênh mọi đóng góp để cải thiện giáo trình:
- **Báo lỗi**: Nếu phát hiện sai sót
- **Đề xuất**: Cải thiện nội dung và phương pháp
- **Chia sẻ**: Kinh nghiệm sử dụng giáo trình

## 📞 Liên hệ

- **Tác giả**: AI & Trần Việt Trung (BKHN)
- **Ngày tạo**: 04/10/2025
- **Phiên bản**: 1.0

## 📄 Giấy phép

Giáo trình này được phát hành dưới giấy phép Creative Commons, cho phép sử dụng và chia sẻ miễn phí cho mục đích giáo dục.

---

**🌟 Hãy bắt đầu hành trình lập trình thú vị cùng Scratch!**
