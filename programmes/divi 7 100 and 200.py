start = 100
end = 200
divisor = 7

total_sum = 0

for num in range(start + 1, end):
    if num % divisor == 0:
        total_sum += num

print("Sum:", total_sum)