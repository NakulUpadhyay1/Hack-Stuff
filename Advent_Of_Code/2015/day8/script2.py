def encode_string_length_difference(input_strings):
    total_difference = 0

    for string_literal in input_strings:
        original_length = len(string_literal)
        encoded_length = len(encode_string(string_literal))
        difference = encoded_length - original_length
        total_difference += difference

    return total_difference

def encode_string(s):
    s = s.replace('\\', '\\\\')
    s = s.replace('"', '\\"')
    s = '"' + s + '"'
    return s

def read_input_from_file(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file]

file_path = 'input.txt'  
input_strings = read_input_from_file(file_path)
result = encode_string_length_difference(input_strings)
print(result)

