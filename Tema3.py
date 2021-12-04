cars = [{
    "Brand": "Tesla",
    "Model": "X3",
    "hp": 180,
    "Price": 15000
}, {
    "Brand": "Audi",
    "Model": "A5",
    "hp": 120,
    "Price": 4900
}, {
    "Brand": "BMW",
    "Model": "M8",
    "hp": 150,
    "Price": 980
}, {
    "Brand": "Dacia",
    "Model": "Duster",
    "hp": 70,
    "Price": 700
}, {
    "Brand": "Mercedes",
    "Model": "Benz",
    "hp": 220,
    "Price": 25000
}]
slow_cars = list(filter(lambda car: car["hp"] < 120, cars))
print(f"Slow cars : {slow_cars}")

fast_cars = list(filter(lambda car: 120 <= car["hp"] < 180, cars))
print(f"Fast cars : {fast_cars}")

sport_cars = list(filter(lambda car: car["hp"] >= 180, cars))
print(f"Sport cars : {sport_cars}")

cheap = list(filter(lambda car: car["Price"] < 1000, cars))
print(f"Cheap cars : {cheap}")

medium = list(filter(lambda car: 1000 <= car["Price"] < 5000, cars))
print(f"Medium cars : {medium}")

expencive = list(filter(lambda car: car["Price"] >= 5000, cars))
print(f"Expencive cars : {expencive}")