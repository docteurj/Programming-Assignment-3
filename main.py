import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    K = int(input_data[0])

    index = 1
    val_map = {}
    for _ in range(K):
        char = input_data[index]
        val = int(input_data[index+1])
        val_map[char] = val
        index += 2

    if index < len(input_data):
        A = input_data[index]
    else:
        A = ""

    if index + 1 < len(input_data):
        B = input_data[index+1]
    else:
        B = ""

    m, n = len(A), len(B)

    dp = []
    for _ in range(m + 1):
        row = []
        for _ in range(n + 1):
            row.append(0)
        dp.append(row)

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if A[i-1] == B[j-1]:
                char_val = val_map.get(A[i-1], 0)
                dp[i][j] = dp[i-1][j-1] + char_val
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    max_value = dp[m][n]

    subseq = []
    i, j = m, n
    while i > 0 and j > 0:
        if A[i-1] == B[j-1]:
            subseq.append(A[i-1])
            i -= 1
            j -= 1
        elif dp[i-1][j] > dp[i][j-1]:
            i -= 1
        else:
            j -= 1

    subseq.reverse()
    optimal_subsequence = "".join(subseq)

    print(max_value)
    print(optimal_subsequence)

if __name__ == '__main__':
    solve()