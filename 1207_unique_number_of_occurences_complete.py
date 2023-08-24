# 1207. Unique Number of Occurrences
def uniqueOccurrences(arr):
    count_list = []
    for item in set(arr):
        count_list.append(arr.count(item))
    if len(set(count_list)) != len(count_list): return False
    else: return True


print(uniqueOccurrences([1,2]))