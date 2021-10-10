# 標準入力を受け付ける。
N, M = map(int, input().split())

A = []
users = []
for i in range(2 * N):
    A.append(list(input()))
    # [[じゃんけんに勝利した数, 番号1], [じゃんけんに勝利した数, 番号2], ...]で情報管理を行う。
    users.append([0, i + 1])

for i in range(M):
    for j in range(N):
        # 2 * j + 1に該当する番号と2 * jに該当する番号を取得する。
        numA = users[2 * j + 1][1]
        numB = users[2 * j][1]

        # 実際にじゃんけんを行い、じゃんけんに勝利した番号の、じゃんけんに勝利した数を+1カウントする。
        if A[numA - 1][i] == 'G' and A[numB - 1][i] == 'C':
            users[2 * j + 1][0] += 1

        if A[numA - 1][i] == 'C' and A[numB - 1][i] == 'P':
            users[2 * j + 1][0] += 1

        if A[numA - 1][i] == 'P' and A[numB - 1][i] == 'G':
            users[2 * j + 1][0] += 1

        if A[numB - 1][i] == 'G' and A[numA - 1][i] == 'C':
            users[2 * j][0] += 1

        if A[numB - 1][i] == 'C' and A[numA - 1][i] == 'P':
            users[2 * j][0] += 1

        if A[numB - 1][i] == 'P' and A[numA - 1][i] == 'G':
            users[2 * j][0] += 1

    # じゃんけんに勝利した数を降順でソートしつつ、番号を昇順でソートする。
    # 参考 : https://yshystsj.com/2019/05/28/post-182/
    users = sorted(users, key=lambda k: (-k[0], k[1]))

# 結果を出力する。
for user in users:
    print(user[1])
