class Solution:
    def sumGame(self, num: str) -> bool:
        n = len(num)
        leftsum = sum(int(c) for c in num[:n // 2] if c != '?')
        rightsum = sum(int(c) for c in num[n // 2:] if c != '?')
        leftq = num[:n // 2].count('?')
        rightq = num[n // 2:].count('?')
        if (leftq + rightq) % 2:
            return True
        return leftsum - rightsum != 9 * (rightq - leftq) // 2
