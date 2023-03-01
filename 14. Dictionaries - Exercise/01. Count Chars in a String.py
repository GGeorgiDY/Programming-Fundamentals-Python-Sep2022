# text text text
data = input().split(" ")
data = ''.join(data) #texttexttext
my_dict = {}

for i in data:
    if i not in my_dict:
        my_dict[i] = 1
    else:
        my_dict[i] += 1

for key, value in my_dict.items():
    print(f"{key} -> {value}")
