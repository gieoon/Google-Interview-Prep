def split(n):
    res1 = 0
    res2 = 0
    for i in range(len(str(n))):
        v = str(n)[i]
        if str(n)[i] == '4':
            n1 = 2
            n2 = 2
        else:
            n1 = 0
            n2 = int(v)

        res1 += n1 * int(padZeros(n, i))
        res2 += n2 * int(padZeros(n, i))
        #print("res1: ", res1)
        #print("res2: ", res2)

    return res1, res2

def padZeros(n, i):
    res = ''
    z = int(len(str(n)) - i)
    for i in xrange(1, z):
        res += '0'
    #print("returning padded: ", '1' + res)
    return '1' + res

def check4Exists(n):
    if '4' in set(str(n)):
        return True
    return False

def check0Exists(n):
    if '0' in set(str(n)):
        return True
    return False

t = int(raw_input())
for i in xrange(1, t + 1):
    #n, m = [int(s) for s in raw_input().split(" ")]
    n = int(raw_input())
    n1, n2 = split(n)
    print("Case #{}: {} {}".format(i, n1, n2))