def fileToMap():
    numbers = {}
    with open('data/day3') as f:
        for line in f:
            num = int(line, 2)
            numbers[num] = True
    return numbers

def part1():
    ones = [0] * 12
    zeroes = [0] * 12
    frequent = ''
    infrequent = ''
    numbers = fileToMap()
    for num in numbers:
        for i in reversed(range(12)):
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

def part2():
    numbers = fileToMap()
    oxygenGeneratorRating = calcOxygenGenRating(numbers)
    resetNumbers(numbers)
    scrubberRating = calcScrubberRating(numbers)
    print(oxygenGeneratorRating * scrubberRating)

def calcOxygenGenRating(numbers):
    for i in reversed(range(12)):
        ones, zeroes = determineNumberFrequency(numbers, i)
        if ones + zeroes == 1:
            break
        cullOxyNumbers(numbers, ones, zeroes, i)
    return next((num for num, val in numbers.items() if val == True), None)

def calcScrubberRating(numbers):
    for i in reversed(range(12)):
        ones, zeroes = determineNumberFrequency(numbers, i)
        if ones + zeroes == 1:
            break
        cullCO2Numbers(numbers, ones, zeroes, i)
    return next((num for num, val in numbers.items() if val == True), None)

def determineNumberFrequency(numbers, bitPos):
    ones = 0
    zeroes = 0
    for num in numbers:
        if numbers[num] == True:
            digit = (num >> bitPos) & 1
            if digit == 1:
                ones += 1
            else:
                zeroes += 1
    return ones, zeroes

def cullOxyNumbers(numbers, ones, zeroes, bitPos):
    for num in numbers:
        digit = (num >> bitPos) & 1
        if ones >= zeroes and digit == 0:
            numbers[num] = False
        elif ones < zeroes and digit == 1:
            numbers[num] = False

def cullCO2Numbers(numbers, ones, zeroes, bitPos):
    for num in numbers:
        digit = (num >> bitPos) & 1
        if ones < zeroes and digit == 0:
            numbers[num] = False
        elif ones >= zeroes and digit == 1:
            numbers[num] = False

def resetNumbers(numbers):
    for n in numbers:
        numbers[n] = True

part1()
part2()