toppings = "\nHãy yêu cầu toppings bạn muốn: "
toppings += "\nNhập 'quit' nếu không muốn thêm "

order = ""

while order != 'quit':
    order = input(toppings)
    if order != 'quit':
        print(f'\n --- Đã thêm {order} --- ')
