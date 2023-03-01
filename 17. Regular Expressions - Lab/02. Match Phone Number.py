import re

lst = []
pattern = r'(\+359)(\s|\-)(2)(\2)(\d{3})(\2)(\d{4})\b'
data = input()
result = re.findall(pattern, data)
for i in result:
    lst.append(''.join(i))
print(", ".join(lst))

# +359 2 222 2222,359-2-222-2222, +359/2/222/2222, +359-2 222 2222 +359 2-222-2222, +359-2-222-222, +359-2-222-22222 +359-2-222-2222