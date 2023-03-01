def lenght_is_valid(username):
    if 3 <= len(username) <= 16:
        return True
    return False


def characters_are_valid(username):
    for i in username:
        if not (i.isalnum() or i == '-' or i == '_'):
            return False
    return True


def no_redundant_symbols(username):
    if not (' ' in username):
        return True
    return False


def username_is_valid(username):
    if lenght_is_valid(username) and characters_are_valid(username) and no_redundant_symbols(username):
        return True
    return False


usernames = input().split(", ")
for username in usernames:
    if username_is_valid(username):
        print(username)

# sh, too_long_username, !lleg@l ch@rs, jeffbutt          -> jeffbutt
# Jeff, john45, ab, cd, peter-ivanov, @smith              -> Jeff John45 peter-ivanov
