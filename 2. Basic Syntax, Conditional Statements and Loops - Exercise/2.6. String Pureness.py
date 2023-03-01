number = int(input())

special_characters = ",._"

for i in range(number):
    new_word = input()
    if any(c in special_characters for c in new_word):
        print(f"{new_word} is not pure!")
    else:
        print(f"{new_word} is pure.")

#    if "," in new_word or \
#        "." in new_word or \
#        "_" in new_word:
#        print(f"{new_word} is not pure!")
#    else:
#        print(f"{new_word} is pure.")