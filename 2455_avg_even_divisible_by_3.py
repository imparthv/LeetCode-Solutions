# 2455. Average Value of Even Numbers That Are Divisible by Three
def avaerageValue(nums):
    '''
    sum = count = 0
    for num in nums:
        if num % 2 == 0 and num % 3 == 0:
            sum+=num
            count+=1
    if count !=0 : return int(sum/count)
    else: return 0
    '''
    '''
    evenList = []
    evenList = [num for num in nums if num % 2 == 0 and num % 3 == 0]
    if evenList : return int(sum(evenList)/len(evenList))
    return 0
    '''
    evenlist = list(filter(lambda evenNum : ((evenNum % 2 == 0) and (evenNum % 3 == 0)), nums))
    if evenlist: return int(sum(evenlist)/len(evenlist))
    return 0
    
    

print(avaerageValue([1,2,4,7,10]))