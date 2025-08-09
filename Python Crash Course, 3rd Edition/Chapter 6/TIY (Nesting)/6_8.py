pet1 =  {
            'name' : 'Layla',
            'age' : 2,
            'owner' : 'Jessica'
        }

pet2 =  {
            'name' : 'Coconut',
            'age' : 1,
            'owner' : 'Olivia'
        }

pet3 =  {
            'name' : 'Bella',
            'age' : 0.5,
            'owner' : 'Isla'
        }

pets = [pet1, pet2, pet3]

for pet in pets:
    for k,v in pet.items():
        print(k, ':', v)
    print("-" * 20)