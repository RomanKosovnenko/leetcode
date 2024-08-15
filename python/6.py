def convert(s: str, numRows: int) -> str:
    if numRows < 2:
        return s
    ar = [[] for _ in range(numRows)]
    change = 1
    c_row = 0
    for i in range(len(s)):
        ar[c_row].append(s[i])
        if (c_row+change) % numRows == 0 and (c_row+change) // numRows % 2 == 1:
            change *= -1
        elif i != 0 and c_row == 0:
            change *= -1
        c_row += change

    return "".join(''.join(l) for l in ar)


if __name__ == '__main__':
    print(convert("ABC", 1))