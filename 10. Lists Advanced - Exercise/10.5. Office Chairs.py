# number_of_rooms = int(input())
# total_number_of_chairs = 0
# total_number_of_people = 0
# more_chairs = 0
# enought_chairs = True
# for x in range(1, number_of_rooms + 1):
#     room = input().split(" ")
#     if int(len(room[0])) < int(room[1]):
#         needed_chairs = -(int(len(room[0])) - int(room[1]))
#         print(f"{needed_chairs} more chairs needed in room {x}")
#         total_number_of_chairs += int(len(room[0]))
#         total_number_of_people += int(room[1])
#         enought_chairs = False
#     if int(len(room[0])) >= int(room[1]):
#         total_number_of_chairs += int(len(room[0]))
#         total_number_of_people += int(room[1])
#
# if enought_chairs:
#     if total_number_of_chairs > total_number_of_people:
#         more_chairs = total_number_of_chairs - total_number_of_people
#         print(f"Game On, {more_chairs} free chairs left")

#написах го на 80%

# def check_the_rooms(numbers_of_rooms):
#     total_free_chairs = 0
#     total_needed_chairs = 0
#     for room in range(1, numbers_of_rooms + 1):
#         free_chair, visitors = input().split()
#         difference = len(free_chair) - int(visitors)
#         if difference >= 0:
#             total_free_chairs += difference
#         else:
#             total_needed_chairs += abs(difference)
#             print(f"{abs(total_needed_chairs)} more chairs needed in room {room}")
#     return total_free_chairs, total_needed_chairs
#
#
# number_of_rooms = int(input())
# free_chairs, needed_chairs = check_the_rooms(number_of_rooms)
# if free_chairs >= needed_chairs:
#     print(f"Game On, {free_chairs} free chairs left")

room_count = int(input())
chairs_total = 0
people_total = 0
for each_room in range(1, room_count + 1):
    room_data = input().split()
    chairs_count = len(room_data[0])
    people_count = int(room_data[1])
    chairs_total += chairs_count
    people_total += people_count
    if chairs_count < people_count:
        print(f"{(people_count-chairs_count)} more chairs needed in room {each_room}")
if chairs_total >= people_total:
    print(f"Game On, {chairs_total-people_total} free chairs left")





