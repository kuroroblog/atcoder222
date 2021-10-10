# 標準入力を受け付ける。
N, P = map(int, input().split())

A = list(map(int, input().split()))

ans = 0
# 学生1人1人の点数が、P点未満であるかどうか確認する。
for i in range(len(A)):
    # ある学生の点数がP点未満だった場合に、不可の人数を+1カウントする。
    if P > A[i]:
        ans += 1

print(ans)
