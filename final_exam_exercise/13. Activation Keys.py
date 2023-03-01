raw_activation_key = input()

command = input()
while command != "Generate":

    action, *data = command.split(">>>")

# проверяваме дали дадена комбинация от букви я има в стринга
    if "Contains" in action:
        substring = data[0]
        if substring in raw_activation_key:
            print(f"{raw_activation_key} contains {substring}")
        else:
            print("Substring not found!")

# от даден до даден индекс трябва да направим буквите в стринга главни или малки (в зависимост от условието)
    if "Flip" in action:
        upper_or_lower = data[0]
        start_index = int(data[1])
        end_index = int(data[2])
        if upper_or_lower == "Upper":
            raw_activation_key = raw_activation_key[:start_index] + raw_activation_key[start_index:end_index].upper() + raw_activation_key[end_index:]
            print(raw_activation_key)
        elif upper_or_lower == "Lower":
            raw_activation_key = raw_activation_key[:start_index] + raw_activation_key[start_index:end_index].lower() + raw_activation_key[end_index:]
            print(raw_activation_key)

# изтриваме буквите между двата подадени индекса в стринга
    if "Slice" in action:
        start_index = int(data[0])
        end_index = int(data[1])
        raw_activation_key = raw_activation_key[:start_index] + raw_activation_key[end_index:]
        print(raw_activation_key)

    command = input()

print(f"Your activation key is: {raw_activation_key}")


# abcdefghijklmnopqrstuvwxyz
# Slice>>>2>>>6
# Flip>>>Upper>>>3>>>14
# Flip>>>Lower>>>5>>>7
# Contains>>>def
# Contains>>>deF
# Generate
