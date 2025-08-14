def family():
    num_of_members = int(input("Gia đình của bạn có bao nhiêu thành viên?: "))
    info = []
    tuoi = []
    i = 1

    while i <= num_of_members:
        name_of_each_member = input(f"(Mem{i}) Tên: ")
        born_year_of_each_member = int(input(f"(Mem{i}) Năm sinh: "))
        print("---"*15)
        info.append((name_of_each_member, 2025 - born_year_of_each_member))
        i += 1

    mx = 0
    mxName = ""

    mn = 999
    mnName = ""
    for name, age in info:
        if age >= mx:
            mx = age        #Người lớn tuổi nhất
            mxName = name
        if age <= mn:
            mn = age        #Người nhỏ tuổi nhất
            mnName = name
    print(f"Người lớn tuổi nhất: {mxName}")
    print(f"Người nhỏ tuổi nhất: {mnName}")
    mx_tuoi= 0
    mx_name= ""

    for name, age in info:
        if age == mx:
            continue
        else:    
            tui_tru = mx - age
            if tui_tru >= mx_tuoi:
                mx_tuoi = tui_tru
                mx_name = name

    print(mx_tuoi, mx_name)
                            

family()    