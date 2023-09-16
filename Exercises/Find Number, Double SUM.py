def solution(N):
    def digit_sum(num):
        return sum(map(int, str(num)))

    target_sum = 2 * digit_sum(N)
    next_number = N + 1

    while True:
        if digit_sum(next_number) == target_sum:
            return next_number
        next_number += 1

# Test cases
print(solution(14))  # Output: 19
print(solution(10))  # Output: 11
print(solution(99))  # Output: 9999
