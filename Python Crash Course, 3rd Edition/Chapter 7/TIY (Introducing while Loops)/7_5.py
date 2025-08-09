while True:
    age = int(input("Nhập số tuổi: "))
    if age < 3:
        print("Free")
    elif age <= 12:
        print("10$")
    else:
        print("15$")