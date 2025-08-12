info =  {
            "khang" : 12,
            "minh"  : 20
        }
info_sort_age = []
for age in info.values():
    info_sort_age.append(age)

info_sort_age.sort()

print(info_sort_age[0])