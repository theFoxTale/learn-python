phones = ["iPhone Xs", "Samsung Galaxy S10", "Xiaomi Mi8"]
print( phones )
print( len(phones) )

print("")
phones.append("Asus Zen")
print( phones )
print( len(phones) )

print("")
iphCount = phones.count("iPhone Xs")
print(f"iPhone Xs count in list: {iphCount}.")
iphCount = phones.count("iPhone 9")
print(f"iPhone 9 count in list: {iphCount}.")

print(f"list slice 1:3: {phones[1:3]}")
print(f"list last element: {phones[-1]}")
print(f"fist two items: {phones[:2]}")

print("")
print(f"index of Xiaomi in list: { phones.index('Xiaomi Mi8') }")

phones.sort()
print(f"Sorted list: {phones}")

sgIn = "Samsung Galaxy S10" in phones
print(f"Samsung Galaxy S10 in list: {sgIn}")
sgIn = "Samsung 9" in phones
print(f"Samsung 9 in list: {sgIn}")

print("")
phones = ["iPhone Xs", "Samsung Galaxy S10", "iPhone Xs", "Xiaomi Mi8"]
print(phones)
del phones[2]
print(f"List without element id = 2: {phones}")

phones = ["iPhone Xs", "Samsung Galaxy S10", "iPhone Xs", "Xiaomi Mi8"]
phones.remove("iPhone Xs")
print(f"list after remove iPhone Xs: {phones}")