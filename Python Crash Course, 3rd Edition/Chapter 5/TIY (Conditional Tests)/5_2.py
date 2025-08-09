#conditional_tests.py

name = "khangtan"

print(name == "Khangtan")
print(name == "khangtan") 
print()
print(name != "quantminh")
print(name != "khangtan") 

fruit = "Apple"
print()
print(fruit == "apple")
print(fruit == "apple".title())

age = 18
print()
print(age == 18)
print(age != 18)
print(age != 25)
print(age >= 18)
print(age < 18)

temperature = 25
print()
print(temperature < 30 and temperature > 20)
print(temperature < 30 or temperature < 35)
print(temperature > 30 and temperature < 35)

foods = ['pizza', 'Pho', 'bread']
print()
print('bread' not in foods)
print('Pho' in foods)