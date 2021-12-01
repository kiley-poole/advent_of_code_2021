f = open("input")
prev = int(f.readline())
total_increase = 0

for line in f:
    if int(line) > prev:
        total_increase += 1
    prev = int(line)

f.close()
print(total_increase)