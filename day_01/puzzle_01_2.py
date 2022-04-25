# --- Day 1: Sonar Sweep ---
# Consider sums of a three-measurement sliding window. How many sums are larger than the previous sum?

input_file = open("puzzle_01.txt", "rt")
# input_file = open("sample_input.txt", "rt")
measurements_list = input_file.readlines()
# c = int(measurements_list[0]) + int(measurements_list[1])
# print(c)

current_3_measurements_window = int(measurements_list[0]) + int(
    measurements_list[1]) + int(measurements_list[2])
next_3_measurements_window = 0
index_one = 1
index_two = 2
index_three = 3
size_of_list = len(measurements_list)
number_of_increments = 0

# for x in range(size_of_list):
#     # print(measurements_list[current_index_in_list], " ", measurements_list[next_index_in_list])
#     if int(measurements_list[next_index_in_list]) > int(
#             measurements_list[current_index_in_list]):
#         number_of_increments += 1
#       # print(number_of_increments)
#     current_index_in_list += 1
#     next_index_in_list += 1
#     if next_index_in_list == size_of_list:
#         break

while index_three < size_of_list:
    next_3_measurements_window = int(measurements_list[index_one]) + int(
        measurements_list[index_two]) + int(measurements_list[index_three])
    if next_3_measurements_window > current_3_measurements_window:
        number_of_increments += 1
    index_one += 1
    index_two += 1
    index_three += 1
    current_3_measurements_window = next_3_measurements_window

print(number_of_increments)
input_file.close()