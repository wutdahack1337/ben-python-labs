def family():
    number_members = int(input("How many members are there in your family?: "))
    info = {}
    i = 1
    info_sort = []

    while i <= number_members:
        member_name = input(f"(Mem{i}) Name: ")
        member_by = int(input(f"(Mem{i}) Born_year: "))
        info[member_name] = member_by
        i += 1
        print("---" * 15)

    for age in info.values():
        info_sort.append(age)
        info_sort.sort()
    print(info_sort[0])
        





    

family()


