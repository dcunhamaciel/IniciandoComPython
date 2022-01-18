number = 5

while number < 10:
    print(number)
    number += 1
    if number == 8:
        print("Break!!")
        break
else: # terminou no 8, não executa o else
    print("not true anymore!!")

while number < 10:
    print(number)
    number += 1
else: # terminou no 10, executa o else
    print("not true anymore!!")