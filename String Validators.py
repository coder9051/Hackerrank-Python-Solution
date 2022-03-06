if __name__ == '__main__':
    s = input()
    a = []
    b = []
    c = []
    d = []
    e = []
    for i in range(len(s)):
        l = s[i].isalnum()
        a.append(l)
        m = s[i].isalpha()
        b.append(m)
        o = s[i].isdigit()
        c.append(o)
        p = s[i].islower()
        d.append(p)
        q = s[i].isupper()
        e.append(q)
    print(any(a))
    print(any(b))
    print(any(c))
    print(any(d))
    print(any(e))
