cars = {}
cars["corolla"] = "red"
cars["fit"] = "green"
cars["A320"] = "black"

for car in cars:
    print(car + " = " + cars[car]) # funciona mas é meio "gambiarra"

for key, value in cars.items():
    print(key + " = " + value)