phone1 = {'name': 'iPhone Xs Plus', 'stock': 24, 'price': 65432.1, 'discount': 15}
phone2 = {'name': 'Samsung Galaxy S10', 'stock': 8, 'price': 50000.0, 'discount': 10}

def discounted(price, discount, max_discount=20, name=''):
    price = abs(float(price))
    discount = abs(float(discount))
    max_discount = abs(float(max_discount))
    if max_discount > 99:
        raise ValueError('Слишком большая максимальная скидка')
    if discount >= max_discount or 'iphone' in name.lower() or not name:
        return price
    else:
        return price - (price * discount / 100)

discounted_phone1 = discounted(phone1['price'], phone1['discount'], name=phone1['name'])
print(f"Phone: {phone1['name']}, discounted: {discounted_phone1}")

discounted_phone2 = discounted(phone2['price'], phone2['discount'])
print(f"Phone: {phone2['name']}, discounted: {discounted_phone2}")