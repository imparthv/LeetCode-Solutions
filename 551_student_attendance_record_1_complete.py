#Student Attendance Record I
def checkRecord(s):
    s = s + 'M'
    absent_criteria  = s.count('A')
    late_count = 0
    for item in s:
        if item == 'L':
            late_count += 1
            if late_count >= 3: 
                return False
                break
        else:
            late_count = 0
    if absent_criteria < 2 : return True
    else: return False
    

input_data = "PPALLL"
print(checkRecord(input_data))