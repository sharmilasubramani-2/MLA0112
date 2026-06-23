from itertools import permutations
def solve():
    print("Solving: TWO + TWO = FOUR")
    print("=" * 40)
    for perm in permutations(range(10), 6):
        T, W, O, F, U, R = perm
        if T == 0 or F == 0:
            continue
        TWO = T*100 + W*10 + O
        FOUR = F*1000 + O*100 + U*10 + R
        if TWO + TWO == FOUR:
            print(f"T={T}, W={W}, O={O}, F={F}, U={U}, R={R}")
            print(f"{TWO} + {TWO} = {FOUR}")
solve()