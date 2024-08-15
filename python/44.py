def isMatch(s: str, p: str) -> bool:
    i,j = 0, 0
    while i < len(s) and j < len(p):
        if s[i] == p[j]:
            i += 1
            j += 1
        elif p[j] in ["*", "?"]:
            i += 1
            if p[j] == "?":
                j +=1
        else:
            return False
    return i==len(s) and j == len(p)

if __name__ == '__main__':
    print(isMatch("aa", "a"))
    print(isMatch("aa", "*"))
    print(isMatch("aa", "*p"))
    print(isMatch("cb", "?a"))