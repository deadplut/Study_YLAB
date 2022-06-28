import re


def domain_name(url):
    domain = re.split(r'://', url)
    domain = re.split(r'www\.', domain[-1])
    domain = re.split(r'\.', domain[-1])
    return domain[0]


def int32_to_ip(int32):
    o1 = int(int32 / 16777216) % 256

    o2 = int(int32 / 65536) % 256
    o3 = int(int32 / 256) % 256
    o4 = int(int32) % 256

    return '%(o1)s.%(o2)s.%(o3)s.%(o4)s' % locals()


def zeros(n):
    sum = 0
    lvl = 1
    while n // 5 ** lvl > 0:
        sum += n // 5 ** lvl
        lvl += 1
    return sum


def bananas(s):
    st = set()

    def f(ss, m, n):
        if n > 5:
            st.add(ss + '-' * (len(s) - m))
        elif m < len(s):
            for i in range(m, len(s)):
                if s[i] == 'banana'[n]:
                    f(ss + '-' * (i - m) + s[i], i + 1, n + 1)
        return

    f('', 0, 0)
    return st


def count_find_num(primes, limit):
    base = eval('*'.join(map(str, primes)))

    if base > limit:
        return []

    results = [base]

    for p in primes:
        for num in results:
            num *= p
            while num not in results and num <= limit:
                results += [num]
                num *= p

    return [len(results), max(results)]
