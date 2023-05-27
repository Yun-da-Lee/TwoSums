import numpy as np
import random

def TwoSums_my_code(nums:list,target:int)->list:
    select1 = random.choice(nums)  # 從nums隨機挑一個數
    rest_arrs = nums[:nums.index(select1)] + nums[nums.index(select1) + 1:]  # 將nums移除挑選的數
    rest_arrs.insert(nums.index(select1), 'selected')
    should_select2 = target - select1
    in_rest = 'no'
    failed_pos = []
    while in_rest == 'no':
        if should_select2 in rest_arrs:
            in_rest = 'yes'
            return [nums.index(select1), rest_arrs.index(should_select2)]
        else:
            failed_pos.append(nums.index(select1))
            nums2 = nums[:nums.index(select1)] + nums[nums.index(select1) + 1:]  # 將nums移除失敗挑選的數
            select1 = random.choice(nums2)  # 從nums隨機挑一個數
            rest_arrs = nums2[:nums2.index(select1)] + nums2[nums2.index(select1) + 1:]  # 將nums移除挑選的數
            rest_arrs.insert(nums2.index(select1), 'selected')
            should_select2 = target - select1
            if should_select2 in rest_arrs:
                in_rest = 'yes'
                values = np.array(nums)
                if select1 == should_select2:
                    result = np.where(values == select1)[0]
                    return result
                else:
                    return [nums.index(select1), nums.index(should_select2)]
            else:
                in_rest = 'no'


def TwoSums_best_memory_saving(nums,target):
    for i in range(0, len(nums)):
        for j in range(i + 1, len(nums)):
            if (target == nums[i] + nums[j]):
                return [i, j]


def binary_search(sorted_list, target):
    low = 0
    high = len(sorted_list) - 1

    while low <= high:
        mid = (low + high) // 2
        mid_val = sorted_list[mid]

        if mid_val == target:
            return mid
        elif mid_val < target:
            low = mid + 1
        else:
            high = mid - 1
    return None


def TwoSums_best_runtime(nums: list[int], target: int):
    sorting = np.argsort(nums)
    sorted_nums = np.array(nums)[sorting]
    for i in range(len(sorted_nums)):
        bin_result = binary_search(sorted_nums[i + 1:], target - sorted_nums[i])
        if bin_result is not None:
            return [sorting[i], sorting[i + 1 + bin_result]]
    return None


if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 9
    my_result = TwoSums_my_code(nums, target)
    best_runtime = TwoSums_best_runtime(nums, target)
    best_memory_saving = TwoSums_best_memory_saving(nums, target)
    print('what you choose:', my_result)
    print('what you choose:', best_runtime)
    print('what you choose:', best_memory_saving)