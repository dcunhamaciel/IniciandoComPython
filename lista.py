numbers1 = [0, 2, 4, 6]
numbers2 = [10, 12, 14, 16]

numbers3 = numbers1 + numbers2

print(numbers1)
print(numbers2)
print(numbers3)

print(numbers1[1])
print(numbers3[2:4])

mix = [1, 4, "5", 6.3, [1, 3, 4]]
print(mix)
print(mix[4])
print(mix[4][0:2])

numbers1.append(8)
print(numbers1)
numbers1.remove(8) # remove primeira ocorrência do 8
print(numbers1)

numbers1.append(8)
numbers1.append(8)
numbers1.remove(8)
print(numbers1)

del(numbers1[4]) # apaga item do índice 4
print(numbers1)