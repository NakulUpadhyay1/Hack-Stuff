def is_nice_string(s):
    # Condition 1: It contains at least three vowels
    vowels = "aeiou"
    vowel_count = sum(1 for char in s if char in vowels)
    if vowel_count < 3:
        return False

    # Condition 2: It contains at least one letter that appears twice in a row
    has_double_letter = any(s[i] == s[i + 1] for i in range(len(s) - 1))
    if not has_double_letter:
        return False

    # Condition 3: It does not contain the forbidden strings
    forbidden_strings = ["ab", "cd", "pq", "xy"]
    if any(substring in s for substring in forbidden_strings):
        return False

    # If all conditions are met, the string is nice
    return True

def count_nice_strings(filename):
    nice_count = 0
    with open(filename, 'r') as file:
        for line in file:
            if is_nice_string(line.strip()):
                nice_count += 1
    return nice_count

result = count_nice_strings('input.txt')
print("Number of nice strings:", result)

