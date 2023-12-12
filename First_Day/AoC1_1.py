with open('First_Day\\first_puzzle.txt', 'r') as file:
    answer = 0
    linenumber = 1
    for line in file:
        digits = [c for c in line if c.isdigit()]
        if digits:
            first_digit = int(digits[0])
            last_digit = int(digits[-1])
            answer += (first_digit * 10 + last_digit)
        print(first_digit, last_digit, linenumber)
        linenumber += 1
print(answer)

