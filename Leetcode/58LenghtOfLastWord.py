s = input("enter s ")
def lenlastword(s):
    s = s.strip()
    last_word = s.split(" ")[-1]
    return len(last_word)
print(lenlastword(s))