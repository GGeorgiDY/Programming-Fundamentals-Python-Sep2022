import re

data = input()
searced_word = input()

pattern = fr"\b{searced_word}\b" #така гледаме дали думата я има като самостоятелна дума, а не като част от друга дума
matches = re.findall(pattern, data, flags=re.I) #добавяме флаг re.I за да игнорира главни и малки букви
print(len(matches))

# There was one. Therefore I bought it. I wouldn't buy it otherwise.
# there

