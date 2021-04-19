
customer = {"name":"Naufal", "age":25, "city":"jakarta"}

customer["job"] = "telkom"

del customer["age"]

for key in customer:
    print(customer[key])

print(customer.items())