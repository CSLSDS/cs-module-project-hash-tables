"""
find all a, b, c, d in q such that
f(a) + f(b) = f(c) - f(d)
"""

#q = set(range(1, 10))
#q = set(range(1, 200))
q = (1, 3, 4, 7, 12)


def f(x):
    return x * 4 + 6

def sumdiff(q):
    summed = {}
    diffed = {}
    for x in q:
        for y in q:
            comb = f(x) + f(y)
            diff = f(x) - f(y)
            if comb not in summed:
                summed[comb] = {(x,y)}
            else:
                summed[comb].add((x,y))
            if diff not in diffed:
                diffed[diff] = {(x,y)}
            else:
                diffed[diff].add((x,y))
    for val in summed:
        if val in diffed:
            for sumpair in summed[val]:
                for diffpair in diffed[val]:
                    print(f'Sum of f(n) of {sumpair} == diff of f(n) of {diffpair}.')

print(sumdiff(q))