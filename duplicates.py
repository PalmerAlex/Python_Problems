def removeDuplicates(nums):
    for x in range(0,len(nums)):
        if x+1 < len(nums):
            if nums[x] == nums[x+1]:
                print("dupe")
                for y in range(x,len(nums)):
                    if y+1 < len(nums):
                        temp = nums[y]
                        nums[y] = nums[y+1]
                        nums[y+1] = temp









    return nums

print(removeDuplicates([2,1,1]))