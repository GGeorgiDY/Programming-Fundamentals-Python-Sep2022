import re

command = input()
new_command = ""
for i in command:
    if i != " ":
        new_command += i

pattern = re.compile(r"(\@|\#)+(?P<color>[a-z]{3,})(\@|\#)+([^a-z0-9]+)(?P<amount>[0-9]+)\/")
result = re.finditer(pattern, new_command)

for my_item in result:
    print(f"You found {my_item['amount']} {my_item['color']} eggs!")