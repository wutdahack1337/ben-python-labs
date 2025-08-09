favorite_languages = {
                     'jen': 'python',
                     'sarah': 'c',
                     'edward': 'rust',
                     'phil': 'python',
                     }

favorite_languages1 = {
                     'jen': 'python',
                     'sarah': 'c',
                     'jaden': 'c#',
                     'michael': 'rust',
                     }

for person in favorite_languages1.keys():
    if person in favorite_languages.keys():
        print(f"{person}, Thanks for taking the poll!")
    else:
        print(f"{person}, You should take the poll!")