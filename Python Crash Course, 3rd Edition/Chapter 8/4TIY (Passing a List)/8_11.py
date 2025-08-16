def send_messages(messages, sent_messages):
    while messages:
        current = messages.pop()
        print(f"Đang gửi: {current}")
        sent_messages.append(current)

messages = ["Xin chào!", "Chúc một ngày tốt lành!", "Học Python vui quá!"]
sent_messages = []

# gọi hàm với bản sao
send_messages(messages[:], sent_messages)

print(f"\nDanh sách gốc (không đổi): {messages}")
print("Danh sách đã gửi:")
for sent_message in sent_messages:
    print(f"- {sent_message}")