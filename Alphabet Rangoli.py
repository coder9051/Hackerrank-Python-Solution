def print_rangoli(size):
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    l = []
    for i in range(size):
        s = "-".join(alpha[i:size])
        l.append((s[::-1]+s[1:]).center(4*size - 3, "-"))
    print("\n".join(l[:0:-1]+l)) 
