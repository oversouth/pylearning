userinput = input()
target = "но " or "Но "
sentences = userinput.split(".")
sentences_with_target = []
for s in sentences:
    if target in s:
        sentences_with_target.append(s)
count = len(sentences_with_target)
print(count)
