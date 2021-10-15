def to_base(num, base):
    r = ''
    if (num < 2) or (base < 2):
        return -1
    else:
        while num != 0:
            t = num % base
            if t < 10:
                r = str(t) + r
            else:
                r = chr(ord('A') + (t % 10)) + r
            num = num // base
    return r

def to_base10(num, base):
    r = 0
    n = num[::-1]
    l1 = len(num) - 1
    l2 = 0
    if base < 10:
        while l1 != -1:
            r = r + int(num[l2]) * (base ** l1)
            l1 = l1 - 1
            l2 = l2 + 1
    else:
        while l1 != -1:
            if num[l].isalpha:
                r = r + (ord(num[l2]) - 55) * (base ** l1)
            else:
                r = r + int(num[l2]) * (base ** l1)
            l1 = l1 - 1
            l2 = l2 + 1
    return str(r)

