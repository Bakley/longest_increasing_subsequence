from typing import List

def find_length_of_lcis(nums: List[int]) -> int:
    """
    Find the length of the longest continuous increasing subsequence
    
    Args:
        nums: List of integers
    
    Returns:
        int: Length of the longest continuous increasing subsequence

    Examples:
        >>> find_length_of_lcis([1,3,5,4,7])
        3
        >>> find_length_of_lcis([2,2,2,2,2])
        1
        >>> find_length_of_lcis([])
        0
    """
    if not nums:
        return 0
    
    max_length = 1
    current_length = 1
    
    for i in range(1, len(nums)):
        if nums[i] > nums[i - 1]:
            current_length += 1
            max_length = max(max_length, current_length)
        else:
            current_length = 1
    
    return max_length
