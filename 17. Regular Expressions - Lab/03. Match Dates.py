# import re

# pattern = r"\b(\d{2})([\.\-/])([A-Z][a-z]{2})\2(\d{4})\b"
# data = input().split(", ")
# for i in data:
#     result = re.search(pattern, i)
#     if result:
#         print(f"Day: {result.group(1)}, Month: {result.group(3)}, Year: {result.group(4)}")
# горният вариант работи в pycharm, но не и в Judge
import re

pattern = r"\b(\d{2})([\.\-/])([A-Z][a-z]{2})\2(\d{4})\b"
data = input()
result = re.findall(pattern, data)
for i in result:
    print(f"Day: {i[0]}, Month: {i[2]}, Year: {i[3]}")

# 13/Jul/1928, 10-Nov-1934, , 01/Jan-1951,f 25.Dec.1937 23/09/1973, 1/Feb/2016