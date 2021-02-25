
original_num = int(input())
for i in range(original_num,1000000001):
    numbers = sum(int(i) for i in str(original_num))
    if original_num % numbers == 0:
        print(original_num)
        break
    else:
        original_num += 1

    
    
    
    