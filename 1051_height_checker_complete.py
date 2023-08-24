# 1051. Height Checker
def heightChecker(heights):
    expected_heights = sorted(heights)
    mismatch_count = 0
    for item in range(0, len(heights)):
        if heights[item] != expected_heights[item]:
            mismatch_count +=1
    return mismatch_count

mismatch = heightChecker([5,1,2,3,4])
print("Mismatch count is:",mismatch)