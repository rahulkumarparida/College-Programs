
def sort_ascending(nums):
    nums.sort()  
    return nums
nums = list(map(int, input("Enter numbers separated by spaces: ").split()))
sorted_nums = sort_ascending(nums)
print("Sorted list in ascending order:", sorted_nums)
