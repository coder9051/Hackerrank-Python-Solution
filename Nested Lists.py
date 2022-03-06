if __name__ == '__main__':
    dict = {}
    scr = list()
    for i in range(int(input())):
        name = input()
        score = float(input())
        if score in dict:
            dict[score].append(name)
        else:
            dict[score] = [name]
        if score not in scr:
            scr.append(score)
    m = min(scr)
    scr.remove(m)
    m1 = min(scr)
    dict[m1].sort()
    for i in dict[m1]:
        print(i)
