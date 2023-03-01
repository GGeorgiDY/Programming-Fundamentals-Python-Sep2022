import re

data = input()
patern = r"(?<=\s)(([a-z0-9]+[\-\.\_a-z0-9]*)@[a-z\-]+(\.[a-z]+)+\b)"
result = re.findall(patern, data)
for i in result:
    print(i[0])


# Many users @ SoftUni confuse email addresses. We @ Softuni.BG provide high-quality training @ home or @ class. –- steve.parker@softuni.de.
# Just send email to s.miller@mit.edu and j.hopking@york.ac.uk for more information.
# Please contact us at: support@github.com.