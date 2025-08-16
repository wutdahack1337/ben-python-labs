def make_car(manufacturer, model, **features):
    print(f"Xe thuộc hãng {manufacturer} | Sản phẩm tên: {model}")
    
    print("\n--- Các tính năng nổi bật: ---")

    for k, v in features.items():
        print(f"- {k}: {v}.")

make_car("Porsche", "911 Carrera", engine= "3.0L Twin-Turbo H6", transmission= "8-speed PDK")