def solution(R, V):
    n = len(R)
    balance_A = balance_B = 0
    min_balance_A = min_balance_B = 0

    for i in range(n):
        recipient = R[i]
        value = V[i]

        if recipient == 'A':
            balance_A += value
        else:
            balance_B += value

        min_balance_A = min(min_balance_A, balance_A - balance_B)
        min_balance_B = min(min_balance_B, balance_B - balance_A)

    initial_balance_A = max(0, -min_balance_A)
    initial_balance_B = max(0, -min_balance_B)

    return [initial_balance_A, initial_balance_B]

# Test cases
print(solution('BAABA', [2, 4, 1, 1, 2]))  # Expected: [2, 4]
print(solution('ABAB', [10, 5, 10, 15]))   # Expected: [0, 15]
print(solution('B', [100]))                 # Expected: [100, 0]
