def solve(s):
    result = ""
    i = 0

    while i < len(s):
        count =1 
        while i +1 <len(s) and s[i] == s[i+1]:
            i +=1
            count +=1

        result +=str(count) +s[i]
        i+=1
    return result


def iterate(n,puzzle_input):
    for _  in range(n):
        puzzle_input=solve(puzzle_input)
        
    return puzzle_input

#result = iterate(40,"3113322113") #part1
result2 = iterate(50,"3113322113") #part2
#print(len(result))
print(len(result2))


    
