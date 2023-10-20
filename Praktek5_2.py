total = 0

while True:
    umur = input("input umur: ")
    if umur == "":
        uang = int(input("input uang: "))
        while uang < total:
            print("uang anda kurang")
            uang = int(input("input uang: "))
        kembalian = uang - total
        
        print(f"""
              _______Pembayaran_______
              Total: {total}$
              Uang : {uang}$
              Kembalian: {kembalian}$
              """)
        break
    
    umur = int(umur)
    
    if umur <= 2:
        print("Gratis")
        print(f"total: {total}$")
    elif umur >= 3 and umur <=12:
        print("harga: 14$")
        total += 14
        print(f"total: {total}$")
    elif umur > 65:
        print("harga: 18$")
        total += 18
        print(f"total: {total}$")
    else:
        print("harga: 23$")
        total += 23
        print(f"total: {total}$")