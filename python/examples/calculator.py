# Máy tính đơn giản
print("=== MÁY TÍNH ĐƠN GIẢN ===")

# Nhập hai số
so1 = float(input("Nhập số thứ nhất: "))
so2 = float(input("Nhập số thứ hai: "))

# Thực hiện các phép tính
tong = so1 + so2
hieu = so1 - so2
tich = so1 * so2
thuong = so1 / so2

# Hiển thị kết quả
print(f"\nKết quả:")
print(f"{so1} + {so2} = {tong}")
print(f"{so1} - {so2} = {hieu}")
print(f"{so1} × {so2} = {tich}")
print(f"{so1} ÷ {so2} = {thuong}")

# Tính chu vi và diện tích hình chữ nhật
chieu_dai = float(input("\nNhập chiều dài hình chữ nhật: "))
chieu_rong = float(input("Nhập chiều rộng hình chữ nhật: "))

chu_vi = 2 * (chieu_dai + chieu_rong)
dien_tich = chieu_dai * chieu_rong

print(f"\nChu vi hình chữ nhật: {chu_vi}")
print(f"Diện tích hình chữ nhật: {dien_tich}")
