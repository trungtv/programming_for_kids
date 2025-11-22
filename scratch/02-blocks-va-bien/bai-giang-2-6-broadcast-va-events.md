# Bài giảng 2.6: Broadcast và Events (Sự kiện)

## 📋 Thông tin bài học
- **Thời gian**: 60 phút
- **Độ tuổi**: 9-10 tuổi
- **Trình độ**: Trung bình
- **Mục tiêu**: Hiểu khái niệm broadcast và events, cách các thành phần giao tiếp với nhau

## 🎯 Mục tiêu học tập

### Kiến thức
- Hiểu khái niệm event (sự kiện) và broadcast (phát sóng)
- Biết cách sử dụng broadcast để giao tiếp giữa các nhân vật
- Hiểu cách events hoạt động trong lập trình
- Biết cách áp dụng broadcast vào các dự án thực tế

### Kỹ năng
- Tạo và sử dụng broadcast message
- Thiết kế hệ thống giao tiếp giữa các thành phần
- Xử lý events trong Scratch
- Áp dụng vào game và ứng dụng

### Thái độ
- Phát triển tư duy hệ thống
- Rèn luyện kỹ năng thiết kế
- Khuyến khích tư duy modular

## 🧠 Nội dung bài học

## 📚 PHẦN LÝ THUYẾT (30 phút)

### Phần 1: Khái niệm Events qua hoạt động không máy tính (20 phút)

#### Hoạt động khởi động - "Trò chơi truyền tin"
- **Hoạt động**: Học sinh chơi trò "Truyền tin" trong lớp
- **Quy tắc**: Một bạn nói "Bắt đầu", các bạn khác phải làm theo
- **Mục tiêu**: Hiểu khái niệm broadcast qua trải nghiệm thực tế
- **Kết quả**: Nhận ra cần một cách để nhiều người cùng nhận thông điệp

#### Khái niệm Events qua ví dụ thực tế
- **Định nghĩa**: Event (sự kiện) là một hành động hoặc sự kiện xảy ra trong chương trình
- **Ví dụ thực tế**: 
  - Nhấn nút chuông cửa → chuông kêu (event: nhấn nút)
  - Bật công tắc đèn → đèn sáng (event: bật công tắc)
  - Nhấn nút thang máy → thang máy di chuyển (event: nhấn nút)
  - Giáo viên nói "Bắt đầu" → học sinh bắt đầu làm bài (event: lệnh)
- **Đặc điểm**: Một sự kiện có thể kích hoạt nhiều hành động

#### Hoạt động thực hành - "Mô phỏng hệ thống báo động"
- **Hoạt động**: Học sinh mô phỏng hệ thống báo động
- **Bước 1**: Một bạn hô "Báo động!" (broadcast message)
- **Bước 2**: Các bạn khác (đèn, còi, cửa) phản ứng (nhận message)
- **Mục tiêu**: Hiểu cách một message có thể kích hoạt nhiều hành động
- **Kết quả**: Nhận ra broadcast giúp đồng bộ nhiều thành phần

### Phần 2: Khái niệm Broadcast qua hoạt động không máy tính (10 phút)

#### Hoạt động không máy tính - "Đồng bộ hoạt động"
- **Hoạt động**: Học sinh đóng vai nhân vật trong một vở kịch
- **Mục tiêu**: Hiểu khái niệm đồng bộ và broadcast
- **Quy tắc**: 
  - Khi đạo diễn nói "Bắt đầu", tất cả nhân vật bắt đầu diễn
  - Khi đạo diễn nói "Dừng", tất cả nhân vật dừng lại
- **Kết quả**: Nhận ra cần đồng bộ hoạt động giữa các nhân vật

#### Bài toán: Thiết kế hệ thống giao tiếp
- **Vấn đề**: Làm sao để nhiều nhân vật biết khi nào cần hoạt động?
- **Giải pháp 1**: Nhân vật A nói trực tiếp với B, C, D... (phức tạp, khó quản lý)
- **Giải pháp 2**: Nhân vật A gửi broadcast message, B, C, D tự lắng nghe (đơn giản, dễ quản lý)
- **Kết luận**: Broadcast giúp giao tiếp dễ dàng và linh hoạt hơn

#### Khái niệm Broadcast qua ví dụ thực tế
- **Định nghĩa**: Broadcast là cách gửi một thông điệp cho tất cả các thành phần đang lắng nghe
- **Ví dụ thực tế**: 
  - Radio/TV: Phát sóng cho tất cả người nghe
  - Hệ thống báo động: Một nút báo động → tất cả đèn và còi hoạt động
  - Hệ thống trường học: Chuông báo → tất cả lớp học biết giờ ra chơi
- **Lợi ích**: 
  - Tách rời các thành phần (decoupling)
  - Dễ mở rộng (thêm thành phần mới chỉ cần lắng nghe)
  - Dễ quản lý (một nơi gửi, nhiều nơi nhận)

## 💻 PHẦN THỰC HÀNH SCRATCH (30 phút)

### Phần 3: Tạo broadcast message đầu tiên (15 phút)

#### Bước 1: Tạo nhân vật và broadcast
```scratch
# Tạo 3 nhân vật:
1. Nhân vật "NguoiGui" - người gửi message
2. Nhân vật "NguoiNhan1" - người nhận message
3. Nhân vật "NguoiNhan2" - người nhận message

# Nhân vật gửi message
Khi cờ xanh được nhấn
nói [Tôi sẽ gửi broadcast message!] trong (2) giây
chờ (1) giây
gửi tin nhắn [chao_hoi] cho tất cả
nói [Đã gửi message "chao_hoi"] trong (2) giây

# Nhân vật nhận message 1
Khi nhận tin nhắn [chao_hoi]
nói [Tôi là người nhận 1, đã nhận được message!] trong (2) giây
phát âm thanh [pop v]

# Nhân vật nhận message 2
Khi nhận tin nhắn [chao_hoi]
nói [Tôi là người nhận 2, đã nhận được message!] trong (2) giây
phát âm thanh [pop v]
```

#### Hoạt động mở rộng - "Thêm nhiều người nhận"
- **Hoạt động**: Tạo thêm nhân vật thứ 3, 4 để nhận message
- **Mục tiêu**: Hiểu broadcast có thể gửi cho nhiều người nhận
- **Thử thách**: Tạo hệ thống với 5 nhân vật cùng nhận một message

### Phần 4: Ứng dụng Broadcast trong Game (15 phút)

#### Bài toán: Tạo game "Bắt đầu và Dừng"
- **Mục tiêu**: Khi nhấn phím Space, tất cả nhân vật bắt đầu di chuyển
- **Khi nhấn phím S**, tất cả nhân vật dừng lại

#### Lập trình game với broadcast
```scratch
# Nhân vật điều khiển (có thể là Stage hoặc một sprite đặc biệt)
Khi nhấn phím [space v]
gửi tin nhắn [bat_dau] cho tất cả
nói [Bắt đầu!] trong (1) giây

Khi nhấn phím [s v]
gửi tin nhắn [dung] cho tất cả
nói [Dừng!] trong (1) giây

# Nhân vật 1 - Di chuyển
Khi nhận tin nhắn [bat_dau]
mãi mãi
  di chuyển (5) bước
  nếu <chạm cạnh?> thì
    quay bên phải (180) độ

Khi nhận tin nhắn [dung]
dừng [tất cả v]

# Nhân vật 2 - Xoay tròn
Khi nhận tin nhắn [bat_dau]
mãi mãi
  quay bên phải (15) độ
  chờ (0.1) giây

Khi nhận tin nhắn [dung]
dừng [tất cả v]

# Nhân vật 3 - Nhảy
Khi nhận tin nhắn [bat_dau]
lặp lại (10) lần
  thay đổi y bởi (10)
  chờ (0.1) giây
  thay đổi y bởi (-10)
  chờ (0.1) giây

Khi nhận tin nhắn [dung]
dừng [tất cả v]
```

#### Hoạt động mở rộng - "Thêm nhiều events"
- **Hoạt động**: Tạo thêm events: "Nhanh lên", "Chậm lại", "Đổi màu"
- **Mục tiêu**: Hiểu cách sử dụng nhiều broadcast messages
- **Thử thách**: Tạo hệ thống điều khiển phức tạp với 5 events khác nhau

## 🎯 Tổng kết và đánh giá (10 phút)

### Tổng kết kiến thức
- **Event (Sự kiện)**: Một hành động hoặc sự kiện xảy ra trong chương trình
- **Broadcast (Phát sóng)**: Cách gửi thông điệp cho tất cả các thành phần đang lắng nghe
- **Lợi ích**: Tách rời các thành phần, dễ mở rộng, dễ quản lý
- **Ứng dụng**: Game, ứng dụng, hệ thống điều khiển

### Đánh giá học sinh
- **Hiểu broadcast**: Có thể giải thích cách broadcast hoạt động
- **Áp dụng thực tế**: Tìm được ví dụ broadcast trong cuộc sống
- **Lập trình Scratch**: Tạo được chương trình sử dụng broadcast
- **Tư duy hệ thống**: Thiết kế được hệ thống với nhiều thành phần giao tiếp

## 🎨 Hoạt động mở rộng

### Cấp độ 1: Thêm tính năng cơ bản
- **Nhiều events**: Tạo nhiều broadcast messages khác nhau
- **Hiệu ứng trực quan**: Thêm màu sắc và animation khi nhận message
- **Âm thanh**: Tạo âm thanh khác nhau cho từng loại message

### Cấp độ 2: Tính năng nâng cao
- **Điều kiện broadcast**: Chỉ gửi message khi thỏa mãn điều kiện
- **Chuỗi events**: Tạo chuỗi events (event 1 → event 2 → event 3)
- **Broadcast có tham số**: Sử dụng biến số trong broadcast (nâng cao)

### Cấp độ 3: Sáng tạo
- **Game điều khiển**: Tạo game với hệ thống điều khiển phức tạp
- **Hệ thống thông báo**: Tạo hệ thống thông báo cho game
- **Dự án tích hợp**: Kết hợp broadcast với các bài học khác

## 📝 Bài tập về nhà

### Bài tập bắt buộc
1. **Broadcast đơn giản**: Tạo chương trình có 1 người gửi và 2 người nhận message
2. **Game điều khiển**: Tạo game với nút "Bắt đầu" và "Dừng" sử dụng broadcast
3. **Hệ thống báo động**: Tạo hệ thống báo động với đèn và còi phản ứng với broadcast

### Bài tập nâng cao
1. **Chuỗi events**: Tạo chuỗi 3 events nối tiếp nhau
2. **Điều kiện broadcast**: Chỉ gửi message khi điểm số > 10
3. **Hệ thống phức tạp**: Tạo hệ thống với 5 nhân vật và 3 loại messages

### Bài tập sáng tạo
1. **Game điều khiển**: Tạo game với nhiều nút điều khiển khác nhau
2. **Hệ thống thông báo**: Tạo hệ thống thông báo cho game
3. **Dự án tích hợp**: Kết hợp broadcast với các bài học khác (biến số, clone, v.v.)

## 🔧 Tài nguyên hỗ trợ

### Tài liệu tham khảo
- **Scratch Programming**: Hướng dẫn lập trình Scratch cơ bản
- **Event-Driven Programming**: Lập trình hướng sự kiện
- **Message Passing**: Truyền thông điệp trong lập trình

### Công cụ hỗ trợ
- **Scratch Editor**: Môi trường lập trình trực quan
- **Events Blocks**: Khối lệnh Events trong Scratch
- **Broadcast Blocks**: Khối lệnh Broadcast trong Scratch

### Đánh giá và phản hồi
- **Rubric đánh giá**: Tiêu chí đánh giá kỹ năng sử dụng broadcast
- **Peer Review**: Đánh giá lẫn nhau giữa học sinh
- **Portfolio**: Tập hợp các dự án và bài tập của học sinh

## 🔗 Kết nối với lập trình thực tế

### Khái niệm tương đồng

#### 1. Event-Driven Programming (Lập trình hướng sự kiện)
- **Scratch**: Broadcast message → Nhận message
- **JavaScript**: `addEventListener('click', function)` → Xử lý sự kiện
- **Python**: Signal handlers → Xử lý tín hiệu
- **Ứng dụng**: Web development, GUI applications, game development

#### 2. Observer Pattern (Mẫu quan sát)
- **Scratch**: Nhiều nhân vật lắng nghe cùng một message
- **Lập trình**: Nhiều observers lắng nghe một subject
- **Ứng dụng**: Model-View-Controller (MVC), Event systems

#### 3. Message Passing (Truyền thông điệp)
- **Scratch**: Gửi message giữa các nhân vật
- **Lập trình**: Giao tiếp giữa các processes, threads, services
- **Ứng dụng**: Microservices, Distributed systems, IPC

#### 4. Decoupling (Tách rời)
- **Scratch**: Nhân vật không cần biết trực tiếp về nhau
- **Lập trình**: Modules/components độc lập, giao tiếp qua interfaces
- **Lợi ích**: Dễ bảo trì, mở rộng, test

### Ví dụ trong lập trình thực tế

#### JavaScript (Web Development)
```javascript
// Tương tự broadcast trong Scratch
button.addEventListener('click', function() {
    // Xử lý sự kiện click
    console.log('Button clicked!');
});

// React Events
function MyComponent() {
    const handleClick = () => {
        // Xử lý sự kiện
    };
    return <button onClick={handleClick}>Click me</button>;
}
```

#### Python (Game Development)
```python
# Pygame Events (tương tự broadcast)
import pygame

for event in pygame.event.get():
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_SPACE:
            # Xử lý sự kiện nhấn phím Space
            print("Space pressed!")
```

#### Android Development
```java
// Broadcast Receiver (giống hệt broadcast trong Scratch!)
public class MyReceiver extends BroadcastReceiver {
    @Override
    public void onReceive(Context context, Intent intent) {
        // Xử lý broadcast message
        String message = intent.getStringExtra("message");
        Toast.makeText(context, message, Toast.LENGTH_SHORT).show();
    }
}
```

### Chuẩn bị cho bài tiếp theo
- Hiểu cách các thành phần giao tiếp với nhau
- Nắm vững broadcast và events
- **Sẵn sàng học Bài 5 (Câu chuyện tương tác)** - Sử dụng broadcast để đồng bộ nhân vật

## 💡 Lưu ý quan trọng

### Tại sao cần Broadcast?
- **Giao tiếp dễ dàng**: Không cần biết trực tiếp về nhau
- **Đồng bộ**: Nhiều thành phần cùng phản ứng với một sự kiện
- **Mở rộng**: Dễ thêm thành phần mới (chỉ cần lắng nghe message)
- **Quản lý**: Một nơi gửi, nhiều nơi nhận (dễ quản lý)

### Broadcast vs Gọi trực tiếp
- **Gọi trực tiếp**: Nhân vật A phải biết về B, C, D... (phức tạp)
- **Broadcast**: Nhân vật A gửi message, B, C, D tự lắng nghe (đơn giản)
- **Ví dụ**: Giống như radio - một đài phát, nhiều người nghe

### Mẹo hay
- **Đặt tên rõ ràng**: Đặt tên message dễ hiểu (ví dụ: "bat_dau", "dung")
- **Một message, nhiều mục đích**: Một message có thể kích hoạt nhiều hành động khác nhau
- **Kiểm tra kỹ**: Đảm bảo tất cả nhân vật cần thiết đều nhận được message

## 🎓 Kiến thức nâng cao (cho giáo viên)

### Observer Pattern trong lập trình
- **Subject**: Người gửi broadcast (trong Scratch: người gửi message)
- **Observer**: Người nhận broadcast (trong Scratch: người nhận message)
- **Lợi ích**: Tách rời subject và observer, dễ mở rộng

### Event-Driven Architecture
- **Events**: Sự kiện xảy ra trong hệ thống
- **Event Handlers**: Xử lý sự kiện
- **Event Bus**: Hệ thống phân phối events (trong Scratch: broadcast system)

### Message Queue
- **Producer**: Người gửi message
- **Consumer**: Người nhận message
- **Queue**: Hàng đợi message (trong Scratch: message được xử lý ngay lập tức)

---

**Tác giả**: AI & Trần Việt Trung (BKHN)  
**Ngày tạo**: 04/10/2025  
**Phiên bản**: 1.0

