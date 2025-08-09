toppings = "\nHãy yêu cầu toppings bạn muốn: "
toppings += "\nNhập 'quit' nếu không muốn thêm "

order = ""

#1
"""
order = ""

while order != 'quit':
    order = input(toppings)
    if order != 'quit':
        print(f'\n --- Đã thêm {order} --- ')
"""

#2
"""
active = True

while active:
    order = input(toppings)

    if order == 'quit':
        active = False
    else:
        print(f'--- Đã thêm {order} ---')
""" 

#3
"""
while True:
    order = input(toppings)
    if order == 'quit':
        break
    else:
        print(f'--- Đã thêm {order} ---')
"""