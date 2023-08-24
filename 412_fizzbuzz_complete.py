# 412. FizzBuzz
def fizzBuzz(n):
    output_container = []
    for i in range(1, n+1):
        if i%3 == 0 and i%5 != 0 :
            output_container.append("Fizz")
        elif i%5 == 0 and i%3 != 0:
            output_container.append("Buzz")
        elif i%15 == 0:
            output_container.append("FizzBuzz")
        else:
            output_container.append(str(i))
    return output_container


print("Enter length:")
list_length = int(input())
output_list = fizzBuzz(list_length)
print(output_list)