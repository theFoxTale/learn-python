def format_price(price):
    price = int(float(price))
    result = f"Цена: {price} руб."
    return result

result_price = format_price(56.24)
print(result_price)