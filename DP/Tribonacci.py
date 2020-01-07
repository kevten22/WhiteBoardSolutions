#Problem: https://leetcode.com/problems/n-th-tribonacci-number/
class Solution:
    def tribonacci(self, n: int) -> int:
        memo = {0:0, 1:1, 2:1}
        def tribRecursive(n):
            if n in memo:
                return memo.get(n)
            else:
                memo[n] = tribRecursive(n-3) + tribRecursive(n-2) + tribRecursive(n-1)
            return memo[n]
            
        return tribRecursive(n) 