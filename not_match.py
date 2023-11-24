
n = int(input())
arr = list(map(int, input().split()))
element = int(input())

def count_non_element(n, arr, element):
    count = 0
    for num in arr:
        if num != element:
            count += 1
    return count

print(count_non_element(n, arr, element))