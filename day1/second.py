f = open("day1/input")

nums = []
total_increase = 0

for line in f:
    nums.append(int(line))

first_start, first_end = 0, 2
second_start, second_end = 1, 3

while second_end <= len(nums) - 1:
    first_sum = nums[first_start] + nums[first_end] + nums[second_start]
    second_sum = nums[second_start] + nums[second_end] + nums[first_end]
    if first_sum < second_sum:
        total_increase += 1
    
    first_start, first_end = second_start, second_end
    second_start, second_end = second_start + 1, second_end + 1

print(total_increase)
