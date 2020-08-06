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
    # first we'll need a database of possible answers to compare
    sumcache = {}
    diffcache = {}
    for x in q: # both seem necessary
        for y in q: # to compare all possible combinations
            added = f(x) + f(y)
            subbed = f(x) - f(y)
            # if new answer:
            if added not in sumcache:
                # initialize w possible key to list of keys per answer
                sumcache[added] = {(x,y)}
            else:
                sumcache[added].add((x,y))
            if subbed not in diffcache:
                diffcache[subbed] = {(x,y)}
            else:
                diffcache[subbed].add((x,y))
    ''' now, for assembly! '''
    # check each answer in cache of sums
    for result in sumcache:
        # and if it's matched in diff
        if result in diffcache:
            for sumpair in sumcache[result]:
                for diffpair in diffcache[result]:
                    print(f'f({sumpair[0]}) + f({sumpair[1]}) = \
f({diffpair[0]} - f({diffpair[1]})    {f(sumpair[0])} + \
{f(sumpair[1])} = {f(diffpair[0])} - {f(diffpair[1])}')

print(sumdiff(q))

''' but i can't tell why it's printing None at the end XD '''