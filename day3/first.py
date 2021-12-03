ones = [0] * 12
zeroes = [0] * 12
frequent = ''
infrequent = ''

with open('data/day3') as f:
    for line in f:
        num = int(line, 2)
        for i in range(11, -1, -1):
            digit = num & 1
            if digit == 1:
                ones[i] += 1
            else:
                zeroes[i] += 1
            num = num >> 1

for i in range(12):
    if ones[i] > zeroes[i]:
        frequent += '1'
        infrequent += '0'
    else:
        frequent += '0'
        infrequent += '1'

print(int(frequent, 2) * int(infrequent, 2))