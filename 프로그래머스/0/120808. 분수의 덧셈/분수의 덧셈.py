def solution(numer1, denom1, numer2, denom2):
    denom = denom1 * denom2
    numer = numer1 * denom2 + numer2 * denom1
    
    for i in reversed(range(2, denom + 1)):
        while denom % i == 0 and numer % i == 0:
            denom = denom // i
            numer = numer // i

    return [numer, denom]
