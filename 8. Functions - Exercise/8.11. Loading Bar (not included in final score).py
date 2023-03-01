def loading_bar(number):
    if number == 100:
        return "100% Complete!\n[%%%%%%%%%%]"
    else:
        number_percent = number // 10
        return f"{number}% [{'%' * number_percent}{(10-number_percent) * '.'}]\nStill loading..."


given_number = int(input())
result = loading_bar(given_number)
print(result)
