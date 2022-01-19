cars = {}
cars["corolla"] = "red"
cars["fit"] = "green"
cars["A320"] = "black"

print(cars.keys())
print(cars.values())
print(cars["corolla"])

people = dict(Diego="Father", Flavia="Mother", Malu="Daughter")

print(people)

if ("Diego" in people):
    print(people["Diego"])

product = {
    "Computer": "Azus",
    "TV": "Samsung"
}

print(product)