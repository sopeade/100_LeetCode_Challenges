def rotate(a):
    u = 0
    for i in range(len(a)):
        for j, _ in enumerate(a[u::], start = u):
            a[i][j], a[j][i] = a[j][i], a[i][j]
        u += 1
    for row in a:
        row.reverse()
    return a

a = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
    ]
print(rotate(a))