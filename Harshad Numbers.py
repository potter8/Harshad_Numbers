# import math
#  = input().split()
# print(n)

# for i in range(int(input())):
#     n1, n2, n3 = map(int, input().split())
#     print(n1,n2,n3)

original_num = int(input())
for i in range(original_num,1000000001):
    numbers = sum(int(i) for i in str(original_num))
    if original_num % numbers == 0:
        print(original_num)
        break
    else:
        original_num += 1

    
    
    # if numbers[i] != 0:
    # total = total + numbers[i]
    # x = total
    # print(numbers)
    # x = total
    # if original_num % x != 0:
    #     original_num = original_num + 1
    # else:
    #     print(original_num)
# print(x)    
    