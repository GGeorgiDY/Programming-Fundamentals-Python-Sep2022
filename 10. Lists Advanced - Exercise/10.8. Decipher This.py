secret_message = input().split(" ")

for word in secret_message:
    code = "".join([i for i in word if i.isnumeric()])  #изважда числата от стринга
    code = chr(int(code)) #преобразувам чилото в буква от ASCII таблицата
    letters = [i for i in word if i.isalpha()]  #правя лист, съдържащ като елемент всяка отделна буква
    letters[0], letters[-1] = letters[-1], letters[0] #разменям буквите
    letters = "".join(letters)
    result = code + letters
    print(result, end=" ")