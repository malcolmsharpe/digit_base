def digit_to_chr(n):
    assert 0 <= n < 36
    if n < 10: return str(n)
    return chr(ord('A') + (n-10))

def prime_power_factors_of(n):
    factorization = []

    while n>1:
        for d in range(2,n+1):
            if n%d == 0:
                factorization.append(d)
                n //= d
                break
    
    ret = []

    while factorization:
        d = factorization[-1]
        pp = 1
        while factorization and factorization[-1] == d:
            pp *= d
            factorization.pop()
        ret.append(pp)

    ret.reverse()
    return ret

assert prime_power_factors_of(12) == [4, 3]

def expand_digits(n, b):
    ret = []
    rs = []

    r = 1

    while True:
        if r == 0:
            return '0.' + ''.join(ret)

        rs.append(r)
        r *= b
        q = r // n
        r -= q*n

        ret.append(digit_to_chr(q))

        try:
            i = rs.index(r)
            return '0.' + ''.join(ret[:i]) + '(' + ''.join(ret[i:]) + ')'
        except ValueError:
            pass

def is_easy_div(n, b):
    expansion = expand_digits(n, b)

    # Either finite or of form '0.(x)'
    return '(' not in expansion or len(expansion) == 5

def main():
    nums = range(2,13)
    #bases = [6, 10, 12]
    bases = range(2, 33)

    line = 8*[' ']
    for b in bases:
        line.append('%20d' % b)
    print(''.join(line))

    hards = len(bases)*[0]

    for n in nums:
        line = ['%8d' % n]
        for i,b in enumerate(bases):
            line.append('%20s' % expand_digits(n, b))

            is_hard = False
            for m in prime_power_factors_of(n):
                if not is_easy_div(m, b):
                    is_hard = True
            if is_hard:
                hards[i] += 1

        print(''.join(line))

    ranking = []

    print()
    line = ['%8s' % 'hards']
    for i,b in enumerate(bases):
        line.append('%20d' % hards[i])
        ranking.append((hards[i], b))
    print(''.join(line))
    print()

    ranking.sort()
    print('Ranking:')
    for h,b in ranking:
        print('%8d%8d' % (h,b))

if __name__ == '__main__':
    main()
