input_char = input("Input character: ")
n = int(input("Height of the tree: "))

for i in range(n):
    for j in range(n - i - 1):
        print(" ", end="")
    for j in range(i + 1):
        if j is not i:
            print(input_char, end=" "),
        else:
            print(input_char)
