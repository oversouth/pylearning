def min_in_list():
    numbers = list(map(int, input().split()))
    numbers.sort()
    return numbers[0]
print(min_in_list())