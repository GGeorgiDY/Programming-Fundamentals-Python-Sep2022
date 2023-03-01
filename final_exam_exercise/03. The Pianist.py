number_of_pieces = int(input())
my_dictionary = {}

for i in range(number_of_pieces):
    pieces_themselves = input()
    pieces_themselves = pieces_themselves.split("|")
    piece = pieces_themselves[0]
    composer = pieces_themselves[1]
    key = pieces_themselves[2]
    if piece in my_dictionary.keys():
        pass
    else:
        my_dictionary[piece] = []
        my_dictionary[piece].append(composer)
        my_dictionary[piece].append(key)
# {'Fur Elise': ['Beethoven', 'A Minor'], 'Moonlight Sonata': ['Beethoven', 'C# Minor'], 'Clair de Lune': ['Debussy', 'C# Minor']}
# горната част изпълнява първите няколко инпута
# долната изпълнява целия останал инпут до командата Stop
while True:
    pieces_themselves = input()
    if pieces_themselves == "Stop":
        break

    pieces_themselves = pieces_themselves.split("|")
    action = pieces_themselves[0]

    if action == "Add":# добавяме в речника нов key с value някакъв лист. Ако вече имаме key не правим нищо.
        piece = pieces_themselves[1]
        composer = pieces_themselves[2]
        key = pieces_themselves[3]
        if piece in my_dictionary.keys():
            print(f"{piece} is already in the collection!")
        else:
            my_dictionary[piece] = []
            my_dictionary[piece].append(composer)
            my_dictionary[piece].append(key)
            print(f"{piece} by {composer} in {key} added to the collection!")

    if action == "Remove":# махаме даден key от речника, ако го има
        piece = pieces_themselves[1]
        if piece in my_dictionary.keys():
            del my_dictionary[piece]
            print(f"Successfully removed {piece}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")

    if action == "ChangeKey":# променяме value-то на даден key в речника, ако го има
        piece = pieces_themselves[1]
        new_key = pieces_themselves[2]
        if piece in my_dictionary:
            my_dictionary[piece][1] = new_key
            print(f"Changed the key of {piece} to {new_key}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")

for key, value in my_dictionary.items():
    print(f"{key} -> Composer: {value[0]}, Key: {value[1]}")


# 3
# Fur Elise|Beethoven|A Minor
# Moonlight Sonata|Beethoven|C# Minor
# Clair de Lune|Debussy|C# Minor
# Add|Sonata No.2|Chopin|B Minor
# Add|Hungarian Rhapsody No.2|Liszt|C# Minor
# Add|Fur Elise|Beethoven|C# Minor
# Remove|Clair de Lune
# ChangeKey|Moonlight Sonata|C# Major
# Stop
