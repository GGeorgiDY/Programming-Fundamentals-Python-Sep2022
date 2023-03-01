centuries = int(input())
years = centuries * 100
days = int(years * 365.2422)
hours = days * 24
minutes = hours * 60
print(f"{centuries:.0F} centuries = {years:.0F} years = {days:.0F} days = {hours:.0F} hours = {minutes:.0F} minutes")