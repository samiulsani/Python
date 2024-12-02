def solve_good_sequence(n, arr):
    """
    Find minimum number of elements to remove to create a good sequence.
    
    Args:
        n (int): Length of input sequence
        arr (list): Input sequence of integers
    
    Returns:
        int: Minimum number of elements to remove
    """
    # Count frequencies of each number
    freq = {}
    for num in arr:
        freq[num] = freq.get(num, 0) + 1
    
    # Track removals
    removals = 0
    
    # Track used frequency rules
    used_freq = set()
    
    # Sort frequencies in descending order
    for num, count in sorted(freq.items(), key=lambda x: x[1], reverse=True):
        # If current count is not possible, start removing
        while freq[num] > 0:
            # Check if current count is possible
            if freq[num] == num and num not in used_freq:
                used_freq.add(num)
                break
            
            # If count not valid, remove one occurrence
            freq[num] -= 1
            removals += 1
    
    return removals

# Input reading
n = int(input())
arr = list(map(int, input().split()))

# Solve and print result
print(solve_good_sequence(n, arr))



def all_numbers(*num):
    sum = 0
    for n in num:
        sum = sum + n
    print("Sum:",sum)
all_numbers(1,2,3,5,6)


def details(**student):
    for key, value in student.items():
        print(f"{key}: {value}")

details(name="samiul", age=25, city="Dhaka")
