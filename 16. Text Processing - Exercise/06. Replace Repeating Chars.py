data = input()
sequence = [" "]
for i in data:
    if i != sequence[-1]:
        sequence.append(i)
sequence.remove(" ")
print(''.join(sequence))

# aaaaabbbbbcdddeeeedssaa
# ->
# abcdedsa