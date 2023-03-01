import re

cool_threshold = 1

valid_emoji_pattern = re.compile(r"((\:\:)|(\*\*))(?P<valid_emoji>[A-Z][a-z]{2,})\1")
text_string = input()

valid_emoji_result = list(re.finditer(valid_emoji_pattern, text_string))
full_valid_emojis_names = [x.group(0) for x in valid_emoji_result]
# ['::Smiley::', '**Tigers**', '::Mooning::', '**Shy**']

valid_emojis = [x['valid_emoji'] for x in valid_emoji_result]
# ['Smiley', 'Tigers', 'Mooning', 'Shy']

cool_emoji_pattern = re.compile(r"(?P<cool_emoji>\d)")
cool_emoji_result = list(re.finditer(cool_emoji_pattern, text_string))
cool_emojis = [x['cool_emoji'] for x in cool_emoji_result]
# ['3', '1', '1', '3', '1', '1', '2', '3', '5', '2', '1']

for i in cool_emojis:
    cool_threshold *= int(i)
print(f"Cool threshold: {cool_threshold}")
print(f"{len(valid_emojis)} emojis found in the text.", end=" ")
print("The cool ones are:")

counter = 0
for word in valid_emojis:
    word_rating = 0
    for chr in word:
        word_rating += ord(chr)
    if word_rating >= cool_threshold:
        print(f"{full_valid_emojis_names[counter]}")
    counter += 1


# In the Sofia Zoo there are 311 animals in total! ::Smiley:: This includes 3 **Tigers**, 1 ::Elephant:, 12 **Monk3ys**, a **Gorilla::, 5 ::fox:es: and 21 different types of :Snak::Es::. ::Mooning:: **Shy**