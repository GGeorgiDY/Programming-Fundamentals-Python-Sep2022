import re

patern = r'\b([A-Z][a-z]+)\s([A-Z][a-z]+)\b'
data = input()
matches = re.findall(patern, data)
for i in matches:
    print(" ".join(i), end=" ")

# Peter Smith, peter smith, Peter smith, peter Smith, PEter Smith, Peter SmIth, Lily Everett