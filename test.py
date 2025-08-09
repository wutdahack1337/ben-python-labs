prompt = "Bạn nhập, tôi nói lại : "
prompt += "\nNhập 'quit' nếu muốn dừng. Nhập : "

mess = ""

while mess != 'quit':
    mess = input(prompt)
    if mess != 'quit':
        print(mess)