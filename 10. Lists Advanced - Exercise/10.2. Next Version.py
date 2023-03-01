# version = input().split(".")
# version = list(map(int, version))  може и по този начин
version =[int(x) for x in input().split(".")]

version[-1] += 1
for x in range(len(version) -1, -1, -1):     #прави го да върви от зад напред
    if version[x] > 9:
        version[x] = 0
        if x - 1 >= 0:
            version[x -1] += 1

result = ".".join(str(x) for x in version)    #join работи само със str
print(result)

#може цялто това нещо да се реши и на 2 реда:
#get_new_version = str(int("".join(input().split(".")))+1)  #при input 3.9.9 дава резултат 400 като str
#print(f"{get_new_version[0]}.{get_new_version[1]}.{get_new_version[2]}")
