list1 = [2, 4, 6, 8, 10]

for item in list1:
    print(item)

for item in list1[0:3]:
    print(item)

list2 = ["Diego", "Cunha", "Maciel"]

for item in list2:
    if not item == "Cunha":
        print(item)