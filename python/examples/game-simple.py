# Game đoán số đơn giản
import random

print("=== GAME ĐOÁN SỐ ===")
print("Tôi đã chọn một số từ 1 đến 100")
print("Hãy đoán xem đó là số gì!")

# Máy tính chọn số ngẫu nhiên
so_bi_mat = random.randint(1, 100)
so_lan_doan = 0

print("Bắt đầu đoán!")

while True:
    # Người chơi nhập số đoán
    try:
        so_doan = int(input("Nhập số bạn đoán (1-100): "))
        so_lan_doan += 1
        
        # Kiểm tra kết quả
        if so_doan == so_bi_mat:
            print(f"🎉 Chúc mừng! Bạn đã đoán đúng!")
            print(f"Số bí mật là: {so_bi_mat}")
            print(f"Bạn đã đoán sau {so_lan_doan} lần!")
            break
        elif so_doan < so_bi_mat:
            print("📈 Số của bạn nhỏ hơn số bí mật!")
        else:
            print("📉 Số của bạn lớn hơn số bí mật!")
            
        # Gợi ý thêm
        if so_lan_doan >= 5:
            print("💡 Gợi ý: Hãy thử số ở giữa!")
            
    except ValueError:
        print("❌ Vui lòng nhập một số hợp lệ!")

print(f"\n🎮 Cảm ơn bạn đã chơi game!")
print(f"📊 Thống kê: {so_lan_doan} lần đoán")
