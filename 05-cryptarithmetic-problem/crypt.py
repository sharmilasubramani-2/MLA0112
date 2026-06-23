from itertools import permutations

def solve_cryptarithmetic():
    letters = set('SENDMORY')
    for perm in permutations(range(10), len(letters)):
        m = dict(zip(letters, perm))
        if m['S'] == 0 or m['M'] == 0:
            continue
        send = m['S']*1000 + m['E']*100 + m['N']*10 + m['D']
        more = m['M']*1000 + m['O']*100 + m['R']*10 + m['E']
        money = m['M']*10000 + m['O']*1000 + m['N']*100 + m['E']*10 + m['Y']
        if send + more == money:
            print(f"S={m['S']} E={m['E']} N={m['N']} D={m['D']} M={m['M']} O={m['O']} R={m['R']} Y={m['Y']}")
            print(f"{send} + {more} = {money}")
            return

solve_cryptarithmetic()