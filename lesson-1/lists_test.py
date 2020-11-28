dataList = [3, 5, 7, 9, 10.5]
print(f"my list: {dataList}")

dataList.append("Python")
print(f"upd my list: {dataList}")
print(f"my list length: {len(dataList)}")

print("")
print(f"first element: {dataList[0]}")
print(f"last element: {dataList[-1]}")
print(f"elements 2-4: {dataList[1:5]}")

print("")
dataList.remove("Python")
print(f"list without last element: {dataList}")