"""
Given a list of integers, your function should return `True` if any value
appears at least two times in the array. Your function should return `False` if
every element is unique.

Example:

Input: [1,3,3,2,1]
Output: True

Example:

Input: [0,1,2,3]
Output: False

*Note: In your first solution, it is okay to use a simple linear search. What
is the time complexity of this approach? Other possible solutions will have
time complexities of `O(n log n)` or `O(n)`. Possible space complexities are
`O(1)` or `O(n)`. Try to come up with solutions with different time and space
complexities and think about the tradeoffs between the solutions.*
"""
# def contains_duplicate(nums):
#     # Your code here
#     num_set = set(nums)
#     return len(num_set) != len(nums)

# input = [1,3,3,2,1]
# print(contains_duplicate(input))  

def contains_duplicate(nums):
    # Your code here
    nums.sort()
    for i in range(len(nums) - 1):
        if nums[i] == nums[i + 1]:
            return True
    return False

# input = [1,3,3,2,1]
input = [0,1,2,3]
print(contains_duplicate(input))      

# another solution
def contains_duplicate(nums):
    # Your code here
    nums_count = {}:
    
    for n in nums:
        if n in nums_count: