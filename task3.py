from collections import Counter

def rearrange_by_frequency(nums: list[int]) -> list[int]:
    freq = Counter(nums)
    return sorted(nums, key=lambda x: (-freq[x], x))


print(rearrange_by_frequency([4, 5, 6, 5, 4, 3, 4]))