def max_square(given_list):

    n = len(given_list) + 1

    dp = [[0] * n for i in range(n)]
    cum_col = [0] * n

    result = 0
    for i in range(1, n):
        cum_row = 0
        for j in range(1, n):
            if given_list[i - 1][j - 1]:
                cum_col[j], cum_row = 0, 0
            else:
                cum_col[j] += 1
                cum_row += 1
                dp[i][j] = min(dp[i - 1][j - 1] + 1, min(cum_row, cum_col[j]))
                result = max(result, dp[i][j])

    return result * result


given_matrix1 = [
    [True, False, True, False, True, False, False, False, False, False], 
    [False, False, False, False, False, True, False, False, True, False],
    [False, False, False, False, False, False, False, False, False, False],
    [True, False, False, False, False, True, False, False, False, False], 
    [False, False, False, False, False, False, False, False, False, True],
    [False, True, False, False, False, False, False, False, True, False],
    [True, False, False, False, True, False, False, False, False, True],
    [True, False, False, False, False, False, False, False, False, False],
    [False, False, True, False, False, False, True, True, False, False],
    [False, False, False, False, False, True, False, False, False, False]
]
print(max_square(given_matrix1))

given_matrix2 = [
    [True, False, False, False, False],
    [False, False, False, False, False],
    [False, False, False, False, False],
    [False, False, False, True, False],
    [False, True, False, False, False]
]

print(max_square(given_matrix2))
