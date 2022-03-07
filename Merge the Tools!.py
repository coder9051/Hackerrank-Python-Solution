def merge_the_tools(string, k):
    for i in range(0, len(string), k):
        new_str = string[i:i+k]
        unique = []
        for words in new_str:
            if words not in unique:
                unique.append(words)
        print("".join(unique))
    

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
