cityDict = {
    "city": "Москва", 
    "temperature": "20"
}
print(f"city from dict: {cityDict['city']}")

cityDict["temperature"] = int(cityDict["temperature"]) - 5
print(f"dictionary: {cityDict}")

print("")
print(f"key 'country' in dict: {cityDict.get('country')}")
print(f"default country: {cityDict.get('country', 'Россия')}")

print("")
cityDict["date"] = "27.05.2019"
print(f"dictionary: {cityDict}")
print(f"dictionary length: {len(cityDict)}")