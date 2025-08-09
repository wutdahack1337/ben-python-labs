current_users = ['Khang', 'Minh', 'Bông', 'Lư', 'Hải']
current_user = [user.lower() for user in current_users]
new_users = ['Khang', 'Minh', 'Đại', 'Ân', 'Lâm']

for new_name in new_users:
    if new_name.lower() in current_user:
        print(f"{new_name}: Enter a new username!")
    else:
        print(f"{new_name}: The username is available.")   
