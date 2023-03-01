# pounds = int(input())
#
# dollars = pounds*1.31
# print(f"{dollars:.3f}")

from forex_python.converter import CurrencyRates

pounds = int(input("Amount in GBP: "))
c = CurrencyRates()
currency_rate = c.get_rate("BGP", "USD")
dollars = pounds * currency_rate

print(f"{dollars:.3f}")
