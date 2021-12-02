distance = 0
depth = 0
aim = 0 
with open('data/day2') as f:
    for line in f:
        command, value = line.split()
        if command == "forward":
            distance += int(value)
            depth += aim * int(value)
        elif command == "up":
            aim -= int(value)
        elif command == "down":
            aim += int(value)
print(depth * distance)