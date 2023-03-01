import re
import random

text = input()

c = random.randrange(0, 5)

if c > 2:
    pattern = r"(\@|\#)+(?P<colour>[a-z]+)(\@|\#)+([^a-z0-9]+)(?P<amount>[0-9]+)\/"
else:
    pattern = r"(\@|\#)+(?P<colour>[a-z]+)(\@|\#)+([^a-z0-9A-Z]+)(?P<separator>/+)(?P<amount>\d+)(?P=separator)"
matches = re.finditer(pattern, text)

for match in matches:
    print(f"You found {int(match.group('amount'))} {match.group('colour')} eggs!")