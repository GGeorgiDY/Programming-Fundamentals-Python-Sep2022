# def deck_of_cards(initial_lst, actions_ctr):
#     if initial_lst == "":
#         initial_lst = []
#     else:
#         initial_lst = initial_lst.split(", ")
#
#     for i in range(0, actions_ctr):
#         command = str(input())
#
#         action = command.split(", ")[0]
#         card = command.split(", ")[1]
#
#         if action == "Add":
#             if card in initial_lst:
#                 print("Card is already in the deck")
#
#             else:
#                 initial_lst.append(card)
#                 print("Card successfully added")
#
#         elif action == "Remove":
#             if card in initial_lst:
#                 initial_lst.remove(card)
#                 print("Card successfully removed")
#
#             else:
#                 print("Card not found")
#
#         elif action == "Remove At":
#             index = int(command.split(", ")[1])
#             card = ""
#             if (int(len(initial_lst)) > index) & (index >= 0):
#                 del initial_lst[index]
#                 print("Card successfully removed")
#
#             else:
#                 print("Index out of range")
#
#         elif action == "Insert":
#             index = int(command.split(", ")[1])
#             card = command.split(", ")[2]
#             if index >= 0:
#                 if card in initial_lst:
#                     print("Card already added")
#                 else:
#                     initial_lst.insert(index, card)
#                     print("Card successfully added")
#
#             else:
#                 print("Index out of range")
#
#     return print(', '.join(initial_lst))
#
#
# initial_set = str(input())
# commands_ctr = int(input())
# deck_of_cards(initial_set, commands_ctr)

deck_cards = input().split(", ")
commands = int(input())

for command in range(commands):
    received_command = input().split(", ")
    action = received_command[0]
    element = received_command[1]

    if action == "Add":
        if element in deck_cards:
            print("Card is already in the deck")
        else:
            print("Card successfully added")
            deck_cards.append(element)

    elif action == "Remove":
        if element in deck_cards:
            print("Card successfully removed")
            deck_cards.remove(element)
        else:
            print("Card not found")

    elif action == "Remove At":
        if int(element) not in range(len(deck_cards)):
            print("Index out of range")
        else:
            deck_cards.pop(int(element))
            print("Card successfully removed")

    elif action == "Insert":
        card_name = received_command[2]
        if int(element) not in range(len(deck_cards)):
            print("Index out of range")
        else:
            if card_name not in deck_cards:
                deck_cards.insert(int(element), card_name)
                print("Card successfully added")
            else:
                print("Card is already added")

print(", ".join(deck_cards))