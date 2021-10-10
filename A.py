# 標準入力を受け付ける。
N = input()

# 入力されるNの文字の長さを調べる。
nLen = len(N)
# Nの文字の長さに応じて、先頭へ0を付与する。
if nLen == 1:
    print('000' + N)
elif nLen == 2:
    print('00' + N)
elif nLen == 3:
    print('0' + N)
else:
    print(N)
