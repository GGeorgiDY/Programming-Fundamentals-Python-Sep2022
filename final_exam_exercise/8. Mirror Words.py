import re

pattern = re.compile(r"([\#|\@])(?P<word>[A-Za-z]{3,})(\1{2})(?P<word2>[a-zA-Z]{3,})\1")
text_string = input()

result = list(re.finditer(pattern, text_string))
pairs = [x['word'] for x in result]# ['poOl', 'Part', 'leveL', 'pack', 'sAw']

if len(pairs) == 0:
    print("No word pairs found!")
elif len(pairs) > 0:
    print(f"{len(pairs)} word pairs found!")

mirror_words = []
for i in result:
    if len(i['word']) == len(i['word2']):
        if i['word'] == i['word2'][::-1]:
            mirror_words.append(f"{i['word']} <=> {i['word2']}")

# print(mirror_words)# ['Part <=> traP', 'leveL <=> Level', 'sAw <=> wAs']

if len(mirror_words) > 0:
    print("The mirror words are:")
    print(', '.join(mirror_words))
    # Part <=> traP, leveL <=> Level, sAw <=> wAs
else:
    print("No mirror words!")


# @mix#tix3dj#poOl##loOp#wl@@bong&song%4very$long@thong#Part##traP##@@leveL@@Level@##car#rac##tu@pack@@ckap@#rr#sAw##wAs#r#@w1r
# намери двойките думии и виж дали има огледални такива