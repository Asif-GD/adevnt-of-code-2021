# --- Day 1: Sonar Sweep ---
# Given the number of measurements, how many measurements are larger than the previous measurement?

input_file = open("puzzle_01.txt", "rt")
# input_file = open("sample_input.txt", "rt")
measurements_list = input_file.readlines()
# c = int(measurements_list[0]) + int(measurements_list[1])
# print(c)

current_index_in_list = 0
next_index_in_list = 1
size_of_list = len(measurements_list)
number_of_increments = 0

# for x in range(size_of_list):
#     # print(measurements_list[current_index_in_list], " ", measurements_list[next_index_in_list])
#     if int(measurements_list[next_index_in_list]) > int(
#             measurements_list[current_index_in_list]):
#         number_of_increments += 1
#         # print(number_of_increments)
#     current_index_in_list += 1
#     next_index_in_list += 1
#     if next_index_in_list == size_of_list:
#         break

while next_index_in_list < size_of_list:
    if int(measurements_list[next_index_in_list]) > int(
            measurements_list[current_index_in_list]):
        number_of_increments += 1
        # print(number_of_increments)
    current_index_in_list += 1
    next_index_in_list += 1

print(number_of_increments)
input_file.close()