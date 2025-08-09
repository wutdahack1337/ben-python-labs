mess = "Bạn đi mấy người?"
mess += "\nNhập số người: "

qst = int(input(mess))

print("Bạn sẽ phải đợi bàn." if qst > 8 else "Bàn đã sẵn sàng, mời vào!")