import re

lst = []
pattern = re.compile(r"(\@\#+)(?P<word>[A-Z][A-Za-z0-9]{4,}[A-Z])(\@\#+)")
number_of_barcodes = int(input())
for i in range(number_of_barcodes):
    new_barcode = input()
    result = list(re.finditer(pattern, new_barcode))# [<re.Match object; span=(0, 13), match='@#ValidIteM@#'>] или []
    if len(result) == 0:
        lst.append("!")
    else:
        for text_in_barcode in result:
            lst.append(text_in_barcode['word'])# ['Val1d1teM', 'ValidIteM', '!', '!', '!', 'ValiditeM']

for text_in_barcode in lst:
    product_group = []
    for chr in text_in_barcode:
        if chr.isdigit():
            product_group.append(chr)
        if chr == "!":
            product_group.append(chr)# ['1', '1'][]['!']['!']['!'][] на отделни редове

    if len(product_group) == 0:
        print(f"Product group: 00")
    else:
        if ''.join(product_group) == "!":
            print("Invalid barcode")
        else:
            print(f"Product group: {''.join(product_group)}")

#крайния резултат е
# Product group: 11
# Product group: 00
# Invalid barcode
# Invalid barcode
# Invalid barcode
# Product group: 00

#инпута е
# 3
# @#FreshFisH@#
# @###Brea0D@###
# @##Che4s6E@##

#или
# 6
# @###Val1d1teM@###
# @#ValidIteM@#
# ##InvaliDiteM##
# @InvalidIteM@
# @#Invalid_IteM@#
# @#ValiditeM@#

