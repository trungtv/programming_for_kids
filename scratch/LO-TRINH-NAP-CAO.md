# 🎯 Lộ Trình Nâng Cao: Thuật Toán & Tư Duy Lập Trình Thực Sự

## 📋 Giới thiệu

Sau khi học sinh đã hoàn thành **17 bài nền tảng** (biến → list → if → loop → toán tử → broadcast → my blocks → max/min → swap → mô phỏng đơn giản), đây là lộ trình tiếp theo để phát triển tư duy lập trình thực sự.

## 🎯 Mục tiêu giai đoạn nâng cao

- **Áp dụng thuật toán vào bài toán thực tế**
- **Phát triển tư duy mô phỏng và mô hình hóa**
- **Hiểu nguyên lý hoạt động của các hệ thống phức tạp**
- **Chuẩn bị cho lập trình văn bản (Python)**

---

## 📚 Cấu trúc 4 nhóm chủ đề nâng cao

### 🧠 **Nhóm 1: Thuật toán dữ liệu nâng cao** (`07-thuat-toan-du-lieu-nang-cao/`)

Sau khi đã học các thuật toán cơ bản (tìm kiếm, sắp xếp, đếm), học sinh sẽ học các biến thể và ứng dụng thực tế.

#### **Bài 9A: Tìm kiếm nâng cao** (mở rộng từ Bài 7E)
- Tìm số xuất hiện nhiều nhất (mode) - **MỚI**
- Tìm vị trí đầu tiên / cuối cùng - **MỞ RỘNG** từ tìm vị trí bất kỳ (Bài 7E)
- Tìm phần tử thỏa điều kiện (filter) - **MỚI**
- Ứng dụng: tìm bạn có điểm cao nhất, tìm số chẵn, lọc dữ liệu

#### **Bài 9B: Sắp xếp nâng cao - Insertion Sort**
- Insertion Sort (dễ mô phỏng bằng kéo thẻ, rất trực quan) - **MỚI**
- So sánh hiệu suất: Bubble Sort và Selection Sort (đã học ở Bài 7F) vs Insertion Sort
- Ứng dụng: sắp xếp danh sách điểm, sắp xếp theo nhiều tiêu chí
- **Lưu ý**: Bài này tập trung vào Insertion Sort - thuật toán mới, không trùng với Bài 7F

#### **Bài 9C: Thuật toán thống kê nâng cao**
- Tính trung bình **theo nhóm** (mở rộng từ tính trung bình cơ bản ở Bài 7C)
- Đếm theo điều kiện phức tạp (mở rộng từ Bài 7B)
- Tính tổng **có điều kiện** (ví dụ: chỉ tính tổng điểm của học sinh giỏi) - **MỚI**
- Tìm khoảng cách giữa 2 số - **MỚI**
- Thống kê nâng cao: độ lệch, phân phối - **MỚI**
- Ứng dụng: phân tích điểm số, thống kê dữ liệu

---

### 🤖 **Nhóm 2: Thuật toán mô phỏng nâng cao** (`08-mo-phong-nang-cao/`)

Đây là chủ đề trẻ cực kỳ thích và học rất nhanh vì trực quan và thú vị.

#### **Bài 10A: Mô phỏng nhiều đối tượng tương tác**
- Đàn chim/bầy cá (Boids - phiên bản đơn giản)
- Mô phỏng va chạm giữa nhiều vật
- Mô phỏng lan truyền (virus / lửa / nước)
- Tư duy: từ quy luật → hành vi phức tạp

#### **Bài 10B: Mô phỏng vật lý nâng cao**
- Trọng lực nâng cao
- Bật nảy với ma sát
- Quán tính & vận tốc
- Ứng dụng: game vật lý, mô phỏng chuyển động

#### **Bài 10C: Mô phỏng hệ thống**
- Mô phỏng giao thông (xe tránh nhau)
- Mô phỏng robot hút bụi
- Mô phỏng cửa tự động
- Kết hợp nhiều khái niệm cùng lúc

---

### 🧭 **Nhóm 3: Thuật toán tìm đường (Pathfinding)** (`09-tim-duong/`)

Ở tuổi nhỏ, không dạy BFS/A* lý thuyết, mà dạy **phiên bản "dễ hiểu – trực quan"**.

#### **Bài 11A: Wall Follower (Đi theo tường)**
- Dễ làm, cực trực quan
- Nhân vật tự tìm đường ra mê cung
- Ứng dụng: robot thật, game mê cung

#### **Bài 11B: Line Following Robot**
- Sprite đi theo đường vẽ sẵn
- Nếu lệch → điều chỉnh
- Ứng dụng: robot công nghiệp, xe tự lái (phiên bản đơn giản)

#### **Bài 11C: Tìm đường bằng cảm biến**
- Đi thẳng
- Nếu chạm tường → rẽ trái
- Nếu vẫn kẹt → rẽ phải
- Thuật toán thử sai (heuristic)

---

### 🎮 **Nhóm 4: Lập trình game nâng cao** (`10-game-nang-cao/`)

Đây là cách tốt nhất để trẻ học tư duy phức tạp mà vẫn vui.

#### **Bài 12A: Hệ thống vật phẩm / Inventory**
- Thêm/xóa item vào list
- Kiểm tra có item hay không
- Dùng item
- Ứng dụng: game RPG đơn giản, quản lý đồ vật

#### **Bài 12B: AI đơn giản cho kẻ thù**
- Đuổi theo người chơi
- Tránh vật cản
- Patrol (đi tuần tra)
- Ứng dụng: game hành động, game chiến lược

#### **Bài 12C: Hệ thống điểm & khó dần**
- Tốc độ tăng theo thời gian
- Sinh vật xuất hiện nhiều dần
- Game loop phức tạp
- Ứng dụng: game arcade, game survival

---

### 🏛 **Nhóm 5: Tư duy máy tính nâng cao** (`11-tu-duy-may-tinh/`)

Khi trẻ đã đủ vững, có thể dạy các khái niệm nâng cao.

#### **Bài 13A: Hàm có tham số nâng cao**
- My Blocks với nhiều tham số
- Hàm trả về giá trị
- Hàm đệ quy đơn giản
- Rất quan trọng cho tư duy lập trình "đúng bản chất"

#### **Bài 13B: Debug — Tìm lỗi**
- Chạy theo từng bước
- Kiểm tra biến
- Kiểm tra giá trị sai
- Tìm điều kiện sai
- Ứng dụng: kỹ năng quan trọng cho mọi lập trình viên

#### **Bài 13C: Thiết kế thuật toán**
- Chia nhỏ vấn đề
- Dự đoán kết quả
- Mô phỏng bằng giấy trước
- Vẽ sơ đồ thuật toán
- Ứng dụng: chuẩn bị cho lập trình văn bản

---

## 📊 Tổng quan lộ trình

### **Giai đoạn 1: Nền tảng** (17 bài - Đã hoàn thành)
- Topic 1-6: Từ làm quen đến hàm và modular

### **Giai đoạn 2: Nâng cao** (13 bài mới)
- **Topic 7**: Thuật toán dữ liệu nâng cao (3 bài)
- **Topic 8**: Mô phỏng nâng cao (3 bài)
- **Topic 9**: Tìm đường (3 bài)
- **Topic 10**: Game nâng cao (3 bài)
- **Topic 11**: Tư duy máy tính nâng cao (3 bài)

**Tổng cộng: 30 bài học** (17 nền tảng + 13 nâng cao)

---

## 🎯 Thứ tự dạy đề xuất

### **Sau khi hoàn thành 17 bài nền tảng:**

1. **Bắt đầu với Topic 7** (Thuật toán dữ liệu nâng cao)
   - Bài 9A → 9B → 9C
   - Nền tảng vững chắc từ Topic 5

2. **Tiếp theo Topic 8** (Mô phỏng nâng cao)
   - Bài 10A → 10B → 10C
   - Trẻ rất thích, tạo động lực

3. **Topic 9** (Tìm đường)
   - Bài 11A → 11B → 11C
   - Trực quan, dễ hiểu

4. **Topic 10** (Game nâng cao)
   - Bài 12A → 12B → 12C
   - Áp dụng tất cả kiến thức đã học

5. **Topic 11** (Tư duy máy tính nâng cao)
   - Bài 13A → 13B → 13C
   - Chuẩn bị cho Python

---

## ⏱️ Thời gian ước tính

- **Mỗi bài**: 90-120 phút (1-2 tiết)
- **Mỗi topic**: 3-4 tuần (tùy tốc độ lớp)
- **Toàn bộ giai đoạn nâng cao**: 15-20 tuần (1 học kỳ)

---

## 🎓 Độ tuổi phù hợp

- **8-9 tuổi**: Có thể bắt đầu sau khi hoàn thành nền tảng, tập trung vào Topic 7, 8, 10
- **9-10 tuổi**: Có thể học tất cả các topic
- **10-11 tuổi**: Có thể học nhanh hơn, tập trung vào Topic 11 để chuẩn bị Python

---

## 📝 Lưu ý quan trọng

1. **Không nên nhảy ngay vào thuật toán "khó"** sau nền tảng
2. **Ưu tiên trực quan và thú vị** để giữ động lực
3. **Áp dụng vào dự án thực tế** để trẻ hiểu rõ hơn
4. **Điều chỉnh tốc độ** theo trình độ lớp
5. **Khuyến khích sáng tạo** và thử nghiệm

---

## 🔗 Liên kết

- **Về giáo trình nền tảng**: [README.md](README.md)
- **Cấu trúc topic nền tảng**: Xem các topic 01-06 trong `scratch/`

---

**🌟 Mục tiêu cuối cùng: Trẻ không chỉ biết code, mà hiểu được tư duy lập trình thực sự!**

