# --- Day 2: Dive! ---
# What do you get if you multiply your final horizontal position by your final depth?

input_dictionary = {'forward': 0, 'down': 0, 'up': 0}
# input_file = open("sample_input_02.txt","rt")
input_file = open("puzzle_02.txt","rt")

for line in input_file:
  key, value = line.split()
  input_dictionary[key] += int(value)

# print(input_dictionary)

horizontal_position = input_dictionary['forward']
print(horizontal_position)

depth = input_dictionary['down'] - input_dictionary['up']
print(depth)

final_position = horizontal_position * depth
print(final_position)

input_file.close()