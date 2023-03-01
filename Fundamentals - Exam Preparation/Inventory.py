def inventory(collecting_items_func):
    while True:
        command = input()
        if command == "Craft!":
            break

        command = command.split(" - ")
        action = command[0]
        item = command[1]

        if action == "Collect":
            if item not in collecting_items_func:
                collecting_items_func.append(item)
        if action == "Drop":
            if item in collecting_items_func:
                collecting_items_func.remove(item)
        if action == "Combine Items":
            item = item.split(":")
            old_item = item[0]
            new_item = item[1]
            if old_item in collecting_items_func:
                index = collecting_items_func.index(old_item)
                collecting_items_func.insert(index +1, new_item)
        if action == "Renew":
            if item in collecting_items_func:
                collecting_items_func.remove(item)
                collecting_items_func.append(item)

    result = ', '.join(collecting_items_func)
    return result


collecting_items = input().split(", ")
print(inventory(collecting_items))


