def send_messages():
    messages = ["Xin chào!", "Chúc một ngày tốt lành!", "Học Python vui quá!"]
    send_messages = []

    while messages:
        current = messages.pop()
        print(f"Đang gửi: {current}")
        send_messages.append(current)

    print(f"Danh sách gốc: {messages}")
    for send_message in send_messages:
        print(f"Danh sách đã gửi: {send_message, end= " "}")

send_messages()