n = int(input())
list_of_nums = []

if n == 0:
    print(0)
elif n == 1:
    print(1)
else:
    while len(list_of_nums) < n:
        for i in range(1, n):
            for j in range(1, i + 1):
                list_of_nums.append(i)
        
for i in list_of_nums[:n]:
    print(i, end=' ') 
    
