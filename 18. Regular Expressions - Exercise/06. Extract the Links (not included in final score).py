import re

valid_url =[]
pattern = '((www)\.([a-zA-Z0-9])+([\-\.a-zA-Z0-9]+)*\.([a-z])+)'
data = input()
while data:
    matches = re.search(pattern,data)
    if matches:
        valid_url.append(matches.group(0))
    data = input()

for i in valid_url:
    print(i)

# Join WebStars now for free, at www.web-stars.com
# You can also support our partners:
# Internet - www.internet.com
# WebSpiders - www.webspiders101.com
# Sentinel - www.sentinel.-ko

# Need information about cheap hotels in London?
# You can check us at www.london-hotels.co.uk !
# We provide the best services in London.
# Here are some reviews in some blogs:
# London Hotels are awesome! - www.indigo.bloggers.com
# I am very satisfied with their services - ww.ivan.bg
# Best Hotel Services! - www.rebel21.sedecrem.moc

