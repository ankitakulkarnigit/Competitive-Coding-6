# 526. Beautiful Arrangement
# Attempted
# Medium
# Topics
# conpanies icon
# Companies
# Suppose you have n integers labeled 1 through n. A permutation of those n integers perm (1-indexed) is considered a beautiful arrangement if for every i (1 <= i <= n), either of the following is true:

# perm[i] is divisible by i.
# i is divisible by perm[i].
# Given an integer n, return the number of the beautiful arrangements that you can construct.

 

# Example 1:

# Input: n = 2
# Output: 2
# Explanation: 
# The first beautiful arrangement is [1,2]:
#     - perm[1] = 1 is divisible by i = 1
#     - perm[2] = 2 is divisible by i = 2
# The second beautiful arrangement is [2,1]:
#     - perm[1] = 2 is divisible by i = 1
#     - i = 2 is divisible by perm[2] = 1


class Solution:
    def __init__(self):
        self.count = 0

    def countArrangement(self, n: int) -> int:
        self.visited = [False] * (n+1)
        self.n = n
        self.permute(1)
        return self.count
    
    def permute(self, pivot):
        if pivot > self.n:
            self.count += 1
            return
        
        for i in range(1, self.n+1):
            if self.visited[i] == False and (pivot % i == 0 or i % pivot == 0):
                self.visited[i] = True
                self.permute(pivot+1)
                self.visited[i] = False

        


            
            
            