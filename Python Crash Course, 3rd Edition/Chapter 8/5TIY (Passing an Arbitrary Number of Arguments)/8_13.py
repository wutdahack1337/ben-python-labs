def build_profile(first, last, **info_user):
    print("--- 📋 Hồ sơ người dùng: ---")
    print(f"   Tên của bạn là: {first}.")
    print(f"   Họ của bạn là: {last}.")

    for k, v in info_user.items():
        print(f"   {k.title()}: {v}.")

build_profile('Khang', 'Trần',
              Địa_chỉ= "Cantho",
              Thú_cưng= "Cat",
              Sở_thích= "Gaming")