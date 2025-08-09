info_minh =  {
                'First name' : 'Minh',
                'Last name' : 'Trần',
                'Age' : 20,
                'City' : 'Can Tho City'
             }

info_khang = {
                'First name' : 'Minh',
                'Last name' : 'Trần',
                'Age' : 13,
                'City' : 'Can Tho City'
             }

info_hai =   {
                'First name' : 'Hải',
                'Last name' : 'Lý',
                'Age' : 46,
                'City' : 'Can Tho City'
             }

people = [info_khang, info_hai, info_minh]

for person in people:
    for k, v in person.items():
        print(k,':',v)
    print("-" * 20)
