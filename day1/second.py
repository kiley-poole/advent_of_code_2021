f = open("day1/input")

nums = []
total_increase = 0

for line in f:
    nums.append(int(line))

first_start = 0
second_end =  3

while second_end <= len(nums) - 1:
    if nums[first_start]  < nums[second_end]:
        total_increase += 1
    
    first_start = first_start + 1
    second_end = second_end + 1

print(total_increase)
