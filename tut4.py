# Dictionary and its Function
d1 = {}
print(type(d1))
d2 = {"Harry": "Burger", "Rohan": "Fish", "Sumit": {"B": "maggie", "L": "Roti", "D": "Chicken"}}
print(d2["Harry"])
print(d2["Sumit"])
print(d2["Sumit"]["L"])
d2["Mohit"] = "Junk food"
d2[420] = {"Name": "JK", 43: 4, "Class": 1}
print(d2)
del d2["Mohit"]
print(d2)
d3 = d2.copy()
del d3["Harry"]
print(d2.get("Harry"))
d2.update({"Leena": "Toffee"})
print(d2)
print(d2.keys())
print(d2.items())