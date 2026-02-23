"""
Input parsing utilities for handling different input formats
"""

from typing import List


def parse_input(input_str: str) -> List[int]:
    """
    Parse input string into a list of integers
    
    Args:
        input_str: String containing numbers (comma or space separated)
    
    Returns:
        list: List of integers
        
    Raises:
        ValueError: If input contains invalid numbers
        
    Examples:
        >>> parse_input("1,3,5,4,7")
        [1, 3, 5, 4, 7]
        >>> parse_input("2 2 2 2 2")
        [2, 2, 2, 2, 2]
        >>> parse_input("")
        []
        >>> parse_input("1,2,three,4")
        Traceback (most recent call last):
        ...
        ValueError: Invalid number: 'three'. Please provide valid integers.
    """
    if not input_str or not input_str.strip():
        return []
    
    # Handle different separators
    if ',' in input_str:
        parts = input_str.split(',')
    else:
        parts = input_str.split()
    
    # Convert to integers, stripping whitespace
    result = []
    for p in parts:
        p = p.strip()
        if p:  # Skip empty strings
            try:
                result.append(int(p))
            except ValueError:
                raise ValueError(f"Invalid number: '{p}'. Please provide valid integers.")
    
    return result
