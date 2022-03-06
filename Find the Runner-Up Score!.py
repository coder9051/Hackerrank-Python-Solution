if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    k = set(arr)
    a = list(k)
    a.sort()
    print(a[-2])
