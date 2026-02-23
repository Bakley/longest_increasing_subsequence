"""
Command-line interface for LCIS Finder
Separate from core algorithms, handles all I/O and user interaction
"""

import argparse
import sys
from typing import List, Optional

# Import from lcis package (core algorithms)
from lis_finder.core_algo import find_length_of_lcis

# Import from utilities (longest common increasing sub-sequence utilities)
from utilities.input_parser import parse_input


def create_parser() -> argparse.ArgumentParser:
    """
    Create the argument parser for the CLI
    
    Returns:
        argparse.ArgumentParser: Configured argument parser
    """
    parser = argparse.ArgumentParser(
        description='Find the longest continuous increasing subsequence in an array',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
            Examples:
            %(prog)s "1,3,5,4,7"
            %(prog)s --input "2 2 2 2 2"
            %(prog)s --verbose "1,3,5,4,7"
            %(prog)s --file input.txt
        """
    )
    
    # Input source options
    input_group = parser.add_mutually_exclusive_group()
    input_group.add_argument('--input', '-i', type=str,
                           help='Input string of numbers (comma or space separated)')
    input_group.add_argument('--file', '-f', type=str,
                           help='Input file containing numbers')
    input_group.add_argument('numbers', nargs='*', 
                           help='Numbers as command line arguments (e.g., 1 3 5 4 7)')
    
    # Output options
    parser.add_argument('--verbose', '-v', action='store_true',
                       help='Show detailed information including the subsequence and indices')
    
    parser.add_argument('--quiet', '-q', action='store_true',
                       help='Only output the length (useful for scripting)')
    
    parser.add_argument('--format', '-F', choices=['text', 'json'], 
                       default='text', help='Output format (default: text)')
    
    parser.add_argument('--stats', '-s', action='store_true',
                       help='Show additional statistics')
    
    parser.add_argument('--version', action='version', 
                       version='LCIS Finder 1.0.0')
    
    return parser


def get_numbers_from_args(args) -> Optional[List[int]]:
    """
    Extract numbers from command line arguments
    
    Args:
        args: Parsed command line arguments
    
    Returns:
        Optional[List[int]]: List of numbers or None
    """
    try:
        if args.input:
            return parse_input(args.input)
        elif args.pipe:
        # Read from stdin
            if not sys.stdin.isatty():
                content = sys.stdin.read().strip()
                return parse_input(content)
            else:
                print("Error: No input piped. Use: echo '1,2,3' | lcis --pipe", 
                    file=sys.stderr)
                sys.exit(1)
        elif args.numbers:
        # Join all number arguments
            return parse_input(' '.join(args.numbers))
        else:
            return None
    except Exception as e:
        print(f"Error reading input: {e}", file=sys.stderr)
        sys.exit(1)


def main():
    """Main entry point for the CLI application"""
    parser = create_parser()
    args = parser.parse_args()
    
    # Get numbers from arguments
    nums = get_numbers_from_args(args)
    
    # Handle no input
    if nums is None:
        parser.print_help()
        sys.exit(1)
    
    # Validate numbers
    if not nums:
        print("0" if args.quiet else "Empty input", file=sys.stderr)
        sys.exit(0)
    
    # Select and run algorithm
    try:
        content =  find_length_of_lcis(nums)
        print(content)
    except Exception as e:
        print(f"Error processing input: {e}", file=sys.stderr)
        sys.exit(1)
    
    sys.exit(0)


if __name__ == "__main__":
    main()
