def two_sum(nums: int, target: int) -> list[int]:
    
    # works but has O(n^2) complexity
    
    initial_idx = 0
    target_idxs = []
    
    for num_idx, num in enumerate(nums, start = 1):
        print(f"initial_idx: {initial_idx}, num_idx: {num_idx}, num: {num}")
        if target - num in nums:
            target_idxs = [initial_idx - 1, num_idx - 1]
        initial_idx += 1

    if len(target_idxs) == 0:
        return "No solution could be found"
    else:
        return target_idxs
    
def two_sum_improved(nums: int, target: int) -> list[int]:
    
    # uses dictionary instead to reduce lookup to O(1) -> O(n) complexity overall by storing the index of the number instead of doing list comprehension
    
    checked_nums = {}
    
    for num_idx, num in enumerate(nums):
        
        print(checked_nums)
        
        num_diff = target - num
        if num_diff in checked_nums:
            return [checked_nums[num_diff], num_idx]
        checked_nums[num] = num_idx

if __name__ == "__main__":
    solution = two_sum_improved([2, 11, 15, 8, 6, 7], 9)
    print(solution)