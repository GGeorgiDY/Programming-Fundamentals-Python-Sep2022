countries = input().split(", ")
capitals = input().split(", ")

# my_dict = dict(zip(countries, capitals))
# for k, v in my_dict.items():
#     print(f"{k} -> {v}")

result = {countries[i] : capitals[i] for i in range(len(countries))}
for key, value in result.items():
    print(f"{key} -> {value}")
