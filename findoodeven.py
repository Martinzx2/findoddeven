print('โปรแกรมตรวจสอบเลขคู่ เลขคี่')

while True:
    number = int(input("กรุณากรอกตัวเลข (กรอก 0 เพื่อออกจากโปรแกรม): "))
    
    # ถ้้ใช้กรอก 0 ให้หยุดโปรแกรม
    if number == 0:
        print("โปรแกรมจบการทำงาน")
        break
    
    # ตัวเลขหาร 2 ลงตัว แสดงว่าเป็นเลขคู่
    if number % 2 == 0:
        print(f"{number} is even.")
    else:
        print(f"{number} is odd.")