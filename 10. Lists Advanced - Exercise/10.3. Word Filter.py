words = input().split(" ")
only_even_words =[x for x in words if int(len(x)) % 2 == 0]
only_even_words = "\n".join(only_even_words)

print(only_even_words)