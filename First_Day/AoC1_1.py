with open('first_puzzle.txt', 'r') as file:
    answer = 0
    linenumber = 1
    for line in file.readlines():
        first_digit = '-1'
        last_digit = '-1'
        for c in line:
            if ((first_digit == '-1') & c.isdigit()):
                first_digit = c
            if (c.isdigit()):
                last_digit = c
        last_digit_normalized = 0
        if (int(last_digit) >= 0):
            last_digit_normalized = int(last_digit)
        answer += (int(first_digit) * 10 + last_digit_normalized)
        print(first_digit, last_digit, linenumber)
        linenumber += 1
print(answer)

