# def reverse_func(data):
#     for i in data:
#         print(f"{i} = {i[::-1]}")
#
#
# words_list = []
# while True:
#     word = input()
#     if word == "end":
#         break
#     words_list.append(word)
# reverse_func(words_list)

#или
# while True:
#     word = input()
#     if word == "end":
#         break
#     print(f'{word} = {word[::-1]}')

#или
while True:
    text = input()
    if text == "end":
        break
    text_reversed = ""
    for i in reversed(text):
        text_reversed += i
    print(f'{text} = {text_reversed}')

# helLo
# Softuni
# bottle
# end
