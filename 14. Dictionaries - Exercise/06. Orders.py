my_dictionary = {}
while True:
    data = input()
    if data == "buy":
        break

    data = data.split(" ") #правя го тук, защото иначе на 9ти ред ми дава грешка index out of range...
    name = data[0]
    price = float(data[1])
    quantity = int(data[2])

    if name not in my_dictionary:
        my_dictionary[name] = [] #създавам си лист в речника
        my_dictionary[name].append(price) #добавям си цената в листа
        my_dictionary[name].append(quantity) #добавям си и количеството в листа
    else:
        my_dictionary[name][0] = price #променям цената да е равна на новоподадената
        my_dictionary[name][1] += quantity #добавям новото количество към предишното

for i in my_dictionary.keys():
    total_price = my_dictionary[i][0] * my_dictionary[i][1]
    print(f"{i} -> {total_price:.2f}")

# Beer 2.40 350
# Water 1.25 200
# IceTea 5.20 100
# Beer 1.20 200
# IceTea 0.50 120
# buy