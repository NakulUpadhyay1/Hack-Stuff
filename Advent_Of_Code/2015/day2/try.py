sum_area = 0
total_sum = 0

f = open('input.txt', 'r')
lines = f.readlines()

for line in lines:
    present = 0
    bow = 0
    l = []
    b = ""
    s = "1x1x10"
    inting = line.strip() + "x"
    
    for i in inting:
        if i == 'x':
            l.append(b)
            b = ""
        else:
            b = b + i

    length = int(l[0])
    width = int(l[1])
    height = int(l[2])

    surface_area = 2 * (length * width + width * height + height * length)
    smallest1 = min(length, width, height)
    temp = max(length, width, height)
    smallest2 = min(length + width + height - temp - smallest1, temp)

    surface_area += smallest1 * smallest2
    sum_area += surface_area

    present = smallest1 + smallest1 + smallest2 + smallest2
    bow = length * width * height
    total_sum += present + bow  # Fix: Move this line outside the loop

print("Total ribbon needed for wrapping:", sum_area)
print("Total ribbon needed for bows:", total_sum)

