# 1287. Element Appearing More Than 25% In Sorted Array
def findSpecialInteger(arr):
    for item in arr:
        if (arr.count(item)/ len(arr)) > 0.25:
            return item

print(findSpecialInteger([1,1]))
 