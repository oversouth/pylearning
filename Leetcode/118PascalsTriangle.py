numrows = int(input("enter numrows amonth: "))
def generate(numrows):
    if numrows < 2:
        return "numrows should be 2 or more"
    if numrows == 2:
        return [[1], [1, 1]]
    result = [[1], [1, 1]]
    for i in range(2, numrows):
        row = [1]
        for j in range(1, i):
            row.append(result[i - 1][j - 1] + result[i - 1][j])
        row.append(1)
        result.append(row)
    return result
print(generate(numrows))
