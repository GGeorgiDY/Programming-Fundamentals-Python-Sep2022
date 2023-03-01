import re
data = input()
pattern = r"\b_([a-zA-Z0-9]+)\b" #използваме \b за да кажем да започва и да завършва с дадено нещо

result = re.findall(pattern, data)
print(','.join(result))

# The _id and _age variables are both integers.