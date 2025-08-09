sandwich_orders = ["Bánh mì", 'pastrami', "Grilled cheese", "Chicken", 'pastrami', "Ham", "Cheesesteak", 'pastrami']
finished_sandwiches = []

print('We has run out of pastrami')

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
        sandwich = sandwich_orders.pop()
        print(f"I made your {sandwich} sandwich.")
        finished_sandwiches.append(sandwich)

print()

for fnsh_sandwich in finished_sandwiches:
    print(f"{fnsh_sandwich} was made.")