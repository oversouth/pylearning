List = [66, 52, 42]
class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        total_sum = sum(nums)
        remainder = total_sum % k
        if remainder == 0:
            return 0
        count = 0
        for num in nums:
            if num % k == remainder:
                count += 1
        return count if count > 0 else -1
