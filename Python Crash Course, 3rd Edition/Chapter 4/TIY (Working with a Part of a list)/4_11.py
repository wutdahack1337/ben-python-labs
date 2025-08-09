pizzas = ['dog', 'cat', 'pepperoni']

for pizza in pizzas:
    print(f'I love {pizza.title()} pizza!!!')
print("\nI love pizza so much!!! I could eat them every day!!!")

pizzas.append("Pizza cheese")

friend_pizzas = ['dog', 'cat', 'pepperoni']
friend_pizzas.append("Pineapple")

for pizza in pizzas:
    print(f"My favorite pizzas are: {pizza.title()}")
print()
for pizza in friend_pizzas:
    print(f"My friend's favorite pizzas are: {pizza.title()}")
