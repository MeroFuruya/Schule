geldgrößen = [50, 20, 10, 5, 2, 1]

def wechselautomat(geld: int) -> list:
    r = [0, 0, 0, 0, 0, 0]
    for i in range(0, len(geldgrößen)):
        r[i] = geld // geldgrößen[i]
        geld = geld % geldgrößen[i]
    return r

print(wechselautomat(55))


def wechselautomatGleichmäßig(geld: int) -> list:
    for i50 in range(0, geld//50):
        for i20 in range(0, geld//20):
            for i10 in range(0, geld//10):
                for i5 in range(0, geld//5):
                    for i2 in range(0, geld//2):
                        for i1 in range(0, geld//1):
                            if 50*i50 + 20*i20 + 10*i10 + 5*i5 + 2*i2 + 1*i1 == geld:
                                return [i50, i20, i10, i5, i2, i1]

print(wechselautomatGleichmäßig(55))
