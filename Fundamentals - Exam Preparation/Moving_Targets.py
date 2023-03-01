def shoot(index, power, sequence_of_targets_func):
    if 0 <= index < len(sequence_of_targets_func):
        sequence_of_targets_func[index] -= power
        if sequence_of_targets_func[index] <= 0:
            sequence_of_targets_func.remove(index)
    return sequence_of_targets_func


def add(index, power, sequence_of_targets_func):
    if 0 <= index < len(sequence_of_targets_func):
        sequence_of_targets_func.insert(index, power)
    else:
        print("Invalid placement!")
    return sequence_of_targets_func


def strike(index, power, sequence_of_targets_func):
    if index - power >=  0 or index + power <= len(sequence_of_targets_func):
        start_target_index = index - power
        final_target_index = index + power
        sequence_of_targets_func = [sequence_of_targets_func[i] for i in sequence_of_targets_func if i < start_target_index and i < final_target_index]

    else:
        print("Strike missed!")
    return sequence_of_targets_func


def manipulating_targets(sequence_of_targets_func):

    while True:
        data = input()
        if data == "End":
            break
        data = data.split(" ")
        command = data[0]
        index = data[1]
        power = data[2]

        if command == "Shoot":
            sequence_of_targets_func = shoot(int(index), int(power), sequence_of_targets_func)
        elif command == "Add":
            sequence_of_targets_func = add(int(index), int(power), sequence_of_targets_func)
        elif command == "Strike":
            sequence_of_targets_func = strike(int(index), int(power), sequence_of_targets_func)

    result = sequence_of_targets_func
    print('|'.join(sequence_of_targets_func))


sequence_of_targets = list(map(int, input().split(" ")))
manipulating_targets(sequence_of_targets)