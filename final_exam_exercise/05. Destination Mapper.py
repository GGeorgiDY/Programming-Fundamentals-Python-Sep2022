import re

lst = []
travel_points = 0
data = input()
pattern = re.compile(r"(\=|\/)(?P<item>[A-Z][A-Za-z]{2,})\1")
result = re.finditer(pattern, data)# използва се когато искаш да работиш с някакви групи
for x in result:
    # current_destination = re.split("\=\/", x.group())[1]
    # може като горе да се реши. Реално маха = или / и оставя текста вътре
    # аз го избягвам това чрез ?P<item> в регекса
    travel_points += len(x["item"])
    lst.append(x["item"])

print(f"Destinations: {', '.join(lst)}")
print(f"Travel Points: {travel_points}")


# =Hawai=/Cyprus/=Invalid/invalid==i5valid=/I5valid/=i=