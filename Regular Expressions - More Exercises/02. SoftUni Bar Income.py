import re

total_income = 0
while True:
    command = input()
    if command == "end of shift":
        break

    pattern = re.compile(r"%(?P<customer>[A-Z][a-z]+)%([^\|\$\%\.])*<(?P<product>[\w]+)>([^\|\$\%\.])*\|(?P<count>[0-9]+)\|([^\|\$\%\.])*(?P<price>[1-9]+[.0-9]+)\$")
    result = re.finditer(pattern, command)
    for i in result:
        count = int(i['count'])
        price = float(i['price'])
        total_price = count * price
        total_income += total_price
        print(f"{i['customer']}: {i['product']} - {total_price:.2f}")

print(f"Total income: {total_income:.2f}")

# %InvalidName%<Croissant>|2|10.3$
# %Peter%<Gum>1.3$
# %Maria%<Cola>|1|2.4
# %Valid%<Valid>valid|10|valid20$
# end of shift
#
# result
# Valid: Valid - 200.00
# Total income: 200.00
#
# %George%<Croissant>|2|10.3$
# %Peter%<Gum>|1|1.3$
# %Maria%<Cola>|1|2.4$
# end of shift
#
# result
# George: Croissant - 20.60
# Peter: Gum - 1.30
# Maria: Cola - 2.40
# Total income: 24.30
