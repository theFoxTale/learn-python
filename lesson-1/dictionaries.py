product = {
    "name": "iPhone Xs",
    "stock": 24,
    "price": 65432.1
}
print(product)
print(f"dictionary length: {len(product)}")

print("")
product["memory"] = 4
product["stock"] = 5
print(product)
print(f"dictionary length: {len(product)}")

print(f"discount in dictionary: {product.get('discount', 0)}")
print(f"name in dictionary: {product.get('name')}")

print("")
del product["memory"]
print(f"dictionary without memory: {product}")

print("")
phones = ["iPhone Xs", "Samsung Galaxy S10", "Xiaomi Mi8"]
product["recomendations"] = phones
print(f'dictionary with list: {product}')
print(f"recomendation №1: {product['recomendations'][1]}")
