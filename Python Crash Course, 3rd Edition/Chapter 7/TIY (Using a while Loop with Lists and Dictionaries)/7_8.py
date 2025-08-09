sandwich_orders = ["Bánh mì", "Grilled cheese", "Chicken", "Ham", "Cheesesteak"]
finished_sandwiches = []

while sandwich_orders:
    for sandwich in sandwich_orders:
        print(f"I made your {sandwich} sandwich.")
        sandwich_orders.pop()
        finished_sandwiches.append(sandwich)

print()

for fnsh_sandwich in finished_sandwiches:
    print(f"{fnsh_sandwich} was made.")