class Solution:
    def moveZeroes(self, array):
        if len(array) == 0:
            return 
        empty_space = 0
        i = 0
        while i < len(array):
            if array[i] != 0:
                array[empty_space], array[i] = array[i], array[empty_space]
                empty_space += 1
            i += 1
        return array

sol = Solution()
print(sol.moveZeroes([1,0,0,0,2,3,4,5]))         #[1,2,3,4,5,0,0,0]
print(sol.moveZeroes([]))