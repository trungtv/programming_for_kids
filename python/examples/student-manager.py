# Quản lý học sinh đơn giản
print("=== QUẢN LÝ HỌC SINH ===")

# Danh sách học sinh
danh_sach_hoc_sinh = []

def them_hoc_sinh():
    """Thêm học sinh mới vào danh sách"""
    ten = input("Nhập tên học sinh: ")
    tuoi = int(input("Nhập tuổi: "))
    lop = input("Nhập lớp: ")
    
    hoc_sinh = {
        "ten": ten,
        "tuoi": tuoi,
        "lop": lop
    }
    
    danh_sach_hoc_sinh.append(hoc_sinh)
    print(f"✅ Đã thêm học sinh {ten} vào danh sách!")

def hien_thi_danh_sach():
    """Hiển thị danh sách học sinh"""
    if not danh_sach_hoc_sinh:
        print("📝 Danh sách trống!")
        return
        
    print("\n📋 === DANH SÁCH HỌC SINH ===")
    for i, hs in enumerate(danh_sach_hoc_sinh, 1):
        print(f"{i}. {hs['ten']} - {hs['tuoi']} tuổi - Lớp {hs['lop']}")

def tim_kiem_hoc_sinh():
    """Tìm kiếm học sinh theo tên"""
    if not danh_sach_hoc_sinh:
        print("📝 Danh sách trống!")
        return
        
    ten_tim = input("Nhập tên học sinh cần tìm: ")
    tim_thay = False
    
    print(f"\n🔍 Kết quả tìm kiếm cho '{ten_tim}':")
    for hs in danh_sach_hoc_sinh:
        if ten_tim.lower() in hs['ten'].lower():
            print(f"✅ {hs['ten']} - {hs['tuoi']} tuổi - Lớp {hs['lop']}")
            tim_thay = True
    
    if not tim_thay:
        print("❌ Không tìm thấy học sinh!")

def thong_ke():
    """Thống kê số lượng học sinh"""
    print(f"\n📊 === THỐNG KÊ ===")
    print(f"Tổng số học sinh: {len(danh_sach_hoc_sinh)}")
    
    if danh_sach_hoc_sinh:
        # Thống kê theo lớp
        lop_count = {}
        for hs in danh_sach_hoc_sinh:
            lop = hs['lop']
            lop_count[lop] = lop_count.get(lop, 0) + 1
        
        print("Số học sinh theo lớp:")
        for lop, so_luong in lop_count.items():
            print(f"  - Lớp {lop}: {so_luong} học sinh")

# Menu chính
while True:
    print("\n" + "="*30)
    print("🏫 QUẢN LÝ HỌC SINH")
    print("="*30)
    print("1. ➕ Thêm học sinh")
    print("2. 📋 Hiển thị danh sách")
    print("3. 🔍 Tìm kiếm học sinh")
    print("4. 📊 Thống kê")
    print("5. 🚪 Thoát")
    
    lua_chon = input("\nChọn chức năng (1-5): ")
    
    if lua_chon == "1":
        them_hoc_sinh()
    elif lua_chon == "2":
        hien_thi_danh_sach()
    elif lua_chon == "3":
        tim_kiem_hoc_sinh()
    elif lua_chon == "4":
        thong_ke()
    elif lua_chon == "5":
        print("👋 Cảm ơn bạn đã sử dụng chương trình!")
        break
    else:
        print("❌ Lựa chọn không hợp lệ! Vui lòng chọn từ 1-5.")
