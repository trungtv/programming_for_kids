# 🎮 Dự Án 1: Game Platformer Đơn Giản

## 📋 Mô tả dự án
Tạo một game platformer 2D đơn giản bằng Python và pygame, nơi người chơi điều khiển nhân vật nhảy qua các chướng ngại vật.

## 🎯 Mục tiêu học tập
- Sử dụng thư viện pygame
- Tạo giao diện game 2D
- Xử lý sự kiện bàn phím
- Quản lý va chạm và vật lý đơn giản
- Tạo hệ thống điểm số

## 🛠️ Yêu cầu kỹ thuật
- Python 3.7+
- Thư viện pygame
- Kiến thức cơ bản về Python

## 📚 Kiến thức cần có
- Biến số và kiểu dữ liệu
- Vòng lặp và điều kiện
- Hàm và thủ tục
- Xử lý sự kiện

## 🎮 Tính năng game

### Tính năng cơ bản
- Nhân vật có thể di chuyển trái/phải
- Nhân vật có thể nhảy
- Có chướng ngại vật di chuyển
- Hệ thống điểm số
- Game over khi va chạm

### Tính năng nâng cao
- Nhiều level khác nhau
- Power-up và item đặc biệt
- Âm thanh và hiệu ứng
- High score system
- Menu chính

## 💻 Code mẫu

### Cài đặt pygame
```bash
pip install pygame
```

### Code cơ bản
```python
# game-platformer.py
import pygame
import random

# Khởi tạo pygame
pygame.init()

# Cài đặt màn hình
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game Platformer")

# Màu sắc
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Nhân vật
class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 50
        self.height = 50
        self.vel_x = 0
        self.vel_y = 0
        self.jump_power = 15
        self.on_ground = False
        
    def update(self):
        # Cập nhật vị trí
        self.x += self.vel_x
        self.y += self.vel_y
        
        # Trọng lực
        if not self.on_ground:
            self.vel_y += 0.8
        
        # Giới hạn màn hình
        if self.x < 0:
            self.x = 0
        if self.x + self.width > WIDTH:
            self.x = WIDTH - self.width
        if self.y + self.height > HEIGHT - 50:
            self.y = HEIGHT - 50 - self.height
            self.on_ground = True
            self.vel_y = 0
        
    def jump(self):
        if self.on_ground:
            self.vel_y = -self.jump_power
            self.on_ground = False
    
    def draw(self):
        pygame.draw.rect(screen, BLUE, (self.x, self.y, self.width, self.height))

# Chướng ngại vật
class Obstacle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 30
        self.height = 30
        self.speed = 3
        
    def update(self):
        self.x -= self.speed
        if self.x < -self.width:
            self.x = WIDTH
            self.y = random.randint(HEIGHT - 200, HEIGHT - 50)
    
    def draw(self):
        pygame.draw.rect(screen, RED, (self.x, self.y, self.width, self.height))

# Game chính
def main():
    clock = pygame.time.Clock()
    player = Player(100, HEIGHT - 100)
    obstacles = [Obstacle(WIDTH, HEIGHT - 50) for _ in range(3)]
    score = 0
    font = pygame.font.Font(None, 36)
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    player.jump()
        
        # Xử lý phím
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player.vel_x = -5
        elif keys[pygame.K_RIGHT]:
            player.vel_x = 5
        else:
            player.vel_x = 0
        
        # Cập nhật game
        player.update()
        for obstacle in obstacles:
            obstacle.update()
            
            # Kiểm tra va chạm
            if (player.x < obstacle.x + obstacle.width and
                player.x + player.width > obstacle.x and
                player.y < obstacle.y + obstacle.height and
                player.y + player.height > obstacle.y):
                print(f"Game Over! Score: {score}")
                running = False
        
        # Tăng điểm
        score += 1
        
        # Vẽ game
        screen.fill(WHITE)
        player.draw()
        for obstacle in obstacles:
            obstacle.draw()
        
        # Vẽ điểm số
        score_text = font.render(f"Score: {score}", True, BLACK)
        screen.blit(score_text, (10, 10))
        
        pygame.display.flip()
        clock.tick(60)
    
    pygame.quit()

if __name__ == "__main__":
    main()
```

## 🎨 Hướng dẫn phát triển

### Bước 1: Thiết lập cơ bản
1. Cài đặt pygame
2. Tạo cửa sổ game
3. Tạo nhân vật đơn giản

### Bước 2: Thêm chuyển động
1. Xử lý phím điều khiển
2. Thêm trọng lực và nhảy
3. Giới hạn màn hình

### Bước 3: Thêm chướng ngại vật
1. Tạo class Obstacle
2. Thêm va chạm
3. Tạo hệ thống điểm số

### Bước 4: Cải thiện game
1. Thêm âm thanh
2. Tạo menu chính
3. Thêm nhiều level

## 📊 Đánh giá dự án

### Tiêu chí đánh giá
| Tiêu chí | Điểm | Mô tả |
|----------|------|-------|
| Game chạy được | 3 | Không có lỗi, game hoạt động |
| Tính năng cơ bản | 3 | Di chuyển, nhảy, va chạm |
| Tính năng nâng cao | 2 | Điểm số, âm thanh, menu |
| Code sạch | 2 | Dễ đọc, có comment |

### Cách chấm điểm
- **Hoàn thành cơ bản**: 6-7 điểm
- **Hoàn thành tốt**: 8-9 điểm
- **Xuất sắc**: 10 điểm

## 🚀 Mở rộng dự án

### Ý tưởng nâng cao
- Thêm nhiều loại chướng ngại vật
- Tạo power-up và item đặc biệt
- Thêm boss fight
- Tạo hệ thống save/load

### Tích hợp với Scratch
- So sánh cách tạo game trong Scratch vs Python
- Chuyển đổi logic từ Scratch sang Python
- Tạo phiên bản Scratch của game

## 💡 Lời khuyên

### Bắt đầu đơn giản
- Tạo nhân vật di chuyển trước
- Thêm từng tính năng một
- Test thường xuyên

### Debug hiệu quả
- Sử dụng print() để debug
- Kiểm tra từng phần một
- Đọc kỹ thông báo lỗi

### Sáng tạo
- Thêm tính năng riêng
- Tạo nhân vật độc đáo
- Thiết kế level thú vị

---

**🎮 Chúc bạn tạo ra game tuyệt vời!**
