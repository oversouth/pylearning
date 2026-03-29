print("PseudoCharacterAI")
greeting = input("Ты: ")
if greeting == "привет":
    print("привет, как дела?")
    mood = input("Ты: ")
    if mood == "хорошо":
        print("я рад за тебя")
    else:
        print("я надеюсь, что у тебя все будет хорошо")
else:
    print("понятно")
question = input("Ты: ")
if question == "как тебя зовут":
    print("меня зовут ПсевдоИИ, а тебя как?")
    name = input("Ты: ")
    if name == "не хочу говорить своё имя":
        print("ок, я буду тебя называть друг")
    else:
        print("приятно познакомиться, " + name)