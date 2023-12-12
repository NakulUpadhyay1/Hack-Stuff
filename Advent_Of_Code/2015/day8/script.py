def calculate_difference(line):
    code_length = len(line)
    memory_length = len(eval(line))
    return code_length - memory_length

def main():
    with open("input.txt", "r") as file:
        lines = file.readlines()

    total_difference = sum(calculate_difference(line.strip()) for line in lines)

    print("Total difference:", total_difference)

if __name__ == "__main__":
    main()

