distance = 0
depth = 0 
with open("data/day2") as f:
    for line in f:
        command, value = line.split()
        if command == "forward":
            distance += int(value)
        elif command == "up":
            depth -= int(value)
        elif command == "down":
            depth += int(value)
print(depth * distance)