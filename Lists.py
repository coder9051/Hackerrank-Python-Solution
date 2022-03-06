if __name__ == '__main__':
    N = int(input())
    lis = []
    lis2 = []
    for i in range(1, N+1):
        a = input()
        b = a.split()
        c = len(b)
        if c == 3:
            lis.insert(int(b[1]), int(b[2]))
        elif c == 2:
            if b[0] == 'remove' :
                try :
                    g = int(b[1])
                    lis.remove(g)
                except:
                    lis.remove(b[1])  
            else :
                try :
                    g = int(b[1])
                    lis.append(g)
                except:
                    lis.append(b[1])
        else :
            if b[0] == 'sort':
                lis.sort()
            elif b[0] == 'pop':
                lis.pop()
            elif b[0] == 'reverse':
                lis.reverse()
            else:
                print(lis)
