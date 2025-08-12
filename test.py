def family():
    number_members = int(input("How many members are there in your family?: "))

    i = 1

    while i <= number_members:
        member_name = input(f"mem{i}: Name: ")
        member_by = input(f"mem{i}: Born_year: ")

        print("="*45)

        oldest_person = min(member_by)
        youngest_person = max(member_by)
        i += 1
    print(oldest_person)
        
family()


