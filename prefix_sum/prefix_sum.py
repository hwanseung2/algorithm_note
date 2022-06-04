# input example
# n : length of logs
# logs : logs[i] : [start, end, degreee]
logs = [
    [4815, 6314, 1], 
    [2431, 3600, 1],
    [1550, 2909, 1],
    [5459, 6809, 1],
    [5864, 7350, 1]
    ]
n = 10000

def prefix_sum_1d(n, logs):
    ary = [0] * (n+1)
    
    for log in logs:
        # 증가하는 경우 ex) kakao 광고삽입
        start, end, degree = log
        ary[start] += degree
        ary[end] += -degree
    
    for i in range(1, n):
        ary[i] = ary[i] + ary[i-1]
    
    """
    ex) kakao 광고 삽입의 경우, 여기서 
    for i in range(1, n):
        ary[i] = ary[i] + ary[i-1]
    을 한번 더 진행해서 누적 시청자를 계산.
    """
    return ary

# input example 
# board: n X m matrix
# logs[i]: [r1, c1, r2, c2, degree]

board = [
    [5,5,5,5,5],
    [5,5,5,5,5],
    [5,5,5,5,5],
    [5,5,5,5,5]
    ]
logs = [
    [0,0,3,4,4],
    [2,0,2,3,2],
    [1,0,3,1,2], 
    [0,1,3,3,1]
    ]

#output example 
# (n + 1) X (m + 1) matrix
"""
ex) kakao 파괴되지 않은 건물
"""
def prefix_sum_2d(board, logs):
    n = len(board)
    m = len(board[0])
    ary = [[0] * (m+1) for _ in range(n+1)]

    for log in logs:
        r1, c1, r2, c2, degree = log
        ary[r1][c1] += degree
        ary[r1][c2+1] += -degree
        ary[r2+1][c1] += -degree
        ary[r2+1][c2+1] += degree
    
    # 행을 기준으로 column들부터 prefix_sum
    for i in range(n):
        for j in range(m):
            ary[i][j+1] += ary[i][j]
    
    for j in range(m):
        for i in range(n):
            ary[i+1][j] += ary[i][j]
    
    return ary
    

# print(prefix_sum_1d(n, logs))
ary_2d = prefix_sum_2d(board, logs)
for row in ary_2d:
    print(row)
print()