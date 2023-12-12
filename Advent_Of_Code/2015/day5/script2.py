#!/usr/bin/env python3
def is_nice_string(input_str):
    pair_twice = False
    for i in range(len(input_str) - 1):
        pair = input_str[i:i+2]
        if input_str.count(pair) >= 2:
            pair_twice = True
            break

    repeat_with_one_between = False
    for i in range(len(input_str) - 2):
        if input_str[i] == input_str[i+2]:
            repeat_with_one_between = True
            break

    return pair_twice and repeat_with_one_between

def count_nice_strings(filename):
    nice_count = 0
    with open(filename, 'r') as file:
        for line in file:
            if is_nice_string(line.strip()):
                nice_count += 1
    return nice_count

result = count_nice_strings('input.txt')
print("Number of nice strings:", result)

