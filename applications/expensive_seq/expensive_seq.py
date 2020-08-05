cache = {}

def exps(x, y, z):
    if x <= 0:
        return y + z
    if (x, y, z) not in cache:
        cache[(x, y, z)] = exps(x-1,y+1,z) + exps(x-2,y+2,z*2) + exps(x-3,y+3,x*3)
    return cache[(x, y, z)]

if __name__ == "__main__":
    for i in range(10):
        x = exps(i*2, i*3, i*4)
        print(f"{i*2} {i*3} {i*4} = {x}")

    print(exps(150, 400, 800))
