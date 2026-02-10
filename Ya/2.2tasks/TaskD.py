first_name = "Петя"
first_speed = int(input())
second_name = "Вася"
second_speed = int(input())
third_name = "Толя"
third_speed = int(input())
if first_speed < second_speed:
    first_speed, second_speed = second_speed, first_speed
    first_name, second_name = second_name, first_name

if first_speed < third_speed:
    first_speed, third_speed = third_speed, first_speed
    first_name, third_name = third_name, first_name
if second_speed < third_speed:
    second_speed, third_speed = third_speed, second_speed
    second_name, third_name = third_name, second_name
print(f"1. {first_name}")
print(f"2. {second_name}")
print(f"3. {third_name}")
