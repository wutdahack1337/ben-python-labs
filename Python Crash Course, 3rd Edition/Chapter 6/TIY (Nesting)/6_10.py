fav_nums =  {
                'Bon' : [9, 12],
                'Ben' : [5, 2],
                'Ba'  : [7, 8],
                'Mẹ'  : [7, 8, 9],
                'Đại' : [12]
            }

for name, numbers in fav_nums.items():
    print(f'{name}:')
    for number in numbers:
        print(number)
    print('-' * 20)