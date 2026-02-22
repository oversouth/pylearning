def sum_digits(digit):
    return sum(int(x) for x in digit if x.isdigit())
print(sum_digits('67676767676767676767'))
