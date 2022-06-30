#High time complexity
# def k_nearest_duplicate(nums, k):
#     i = 0
#     val = False
#     if len(nums)<k:
#         if len(nums) != len(set(nums)):
#             val = True
        
#     else:
#         for i in range(abs(len(nums)-k+1)):
#             nums_temp = nums[i:i+k+1]
#             if len(nums_temp) != len(set(nums_temp)):
#                 val = True
#     return val



#Low time complexity

def k_nearest_duplicate(nums: list[int], k:int) -> bool:
    if len(set(nums)) == len(nums):
        return False

    l = {}
    
    for i in range(len(nums)):
        
        if nums[i] not in l:
            l[nums[i]] = i
            
        else:
            if abs(i - l[nums[i]]) <= k:
                return True
            l[nums[i]] = i
            
    return False

nums = [1,2,3,4,5,5,6,7,8]
k=3
print(k_nearest_duplicate(nums,k))