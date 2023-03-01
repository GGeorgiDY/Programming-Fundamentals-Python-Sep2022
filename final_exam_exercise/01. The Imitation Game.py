first_command = input()
while True:
    command = input()
    if command == "Decode":
        break
    command = command.split('|')
    if command[0] == "Move":
        number_of_moves = int(command[1])
        first_command = first_command[number_of_moves:] + first_command[:number_of_moves]# махаме определен брой стрингове отначало и ги слагаме в края
        # долния вариант не винаги работи - дава ми 83% решение на задачата
        # for i in range(1, number_of_moves +1):
        #     letter_to_be_removed = first_command[0]
        #     first_command = first_command[1:]# изтриваме 1вата буква от стрингга
        #     first_command += letter_to_be_removed# добавяме я като последна
        #     first_command = first_command.lstrip()# махаме интервалите отляво
    elif command[0] == "Insert":# инсъртваме няколко стринга
        value_to_insert = command[2]
        index_to_insert = int(command[1])
        first_command = first_command[:index_to_insert] + value_to_insert + first_command[index_to_insert:]
    elif command[0] == "ChangeAll":
        value_to_insert = command[2]
        value_to_be_replaced = command[1]
        first_command = first_command.replace(value_to_be_replaced, value_to_insert)# реплейсвам даден знак с друг

print(f"The decrypted message is: {first_command}")

# zzHe
# ChangeAll|z|l
# Insert|2|o
# Move|3
# Decode

# owyouh
# Move|2
# Move|3
# Insert|3|are
# Insert|9|?
# Decode

