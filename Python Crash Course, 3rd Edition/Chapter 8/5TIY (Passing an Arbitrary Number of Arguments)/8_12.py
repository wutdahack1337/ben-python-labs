def make_sandwiches(*toppings):
    print("\n|-| Toppings đã yêu cầu: |-|")
    for topping in toppings:
        print(f"- {topping}.")

make_sandwiches("Peperoni")
make_sandwiches("Cheese", "Sausage")
make_sandwiches("Meat", "Vegetable", "Neapolitan")
