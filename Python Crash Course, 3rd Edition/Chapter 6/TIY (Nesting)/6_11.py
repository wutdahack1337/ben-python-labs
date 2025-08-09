cities =    {
                'Los Angeles' :   {
                                'country'    : 'USA',
                                'population' :  3.879,
                                'fact'      : 'Los Angeles is the Birthplace of the Internet'
                            },

                'New York City' :   {
                                'country'    : 'USA',
                                'population' : 8.475,
                                'fact'       : 'More than 800 languages are spoken throughout the city'
                            },

                'London' :   {
                                'country'    : 'UK',
                                'population' : 8.951,
                                'fact'       : 'The City of London is the smallest city in the UK'
                            }
            }

for city_key, city_value in cities.items():
    print(f'{city_key} : ')
    for info_types, info in city_value.items():
        print(f'{info_types} : {info}')
    print('-' * 30)
