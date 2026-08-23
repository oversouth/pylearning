usr_inp = input("enter nums: ")
nums = eval(usr_inp)
def solution(nums):
    return nums + nums[::-1]    
print(solution)
