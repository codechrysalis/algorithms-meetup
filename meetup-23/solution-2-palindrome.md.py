def max_palindrome(input_string):
    length = len(input_string)
    dp = [[0] * length for i in range(length)]

    result_st_index = 0
    max_result = 1
    for i in range(length - 1, -1, -1):
        if input_string[i] == ' ':
            continue
        dp[i][i] = 1
        if i + 1 < length and input_string[i] == input_string[i + 1]:
            dp[i][i + 1] = 1
        for j in range(i + 2, length):
            if input_string[i] == input_string[j] and dp[i + 1][j - 1]:
                dp[i][j] = 1
                if max_result <= (j - i + 1):
                    max_result = j - i + 1
                    result_st_index = i

    return input_string[result_st_index : result_st_index + max_result]


input_string = input("Input string: ")
print(max_palindrome(input_string))
