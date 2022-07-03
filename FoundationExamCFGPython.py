### QUESTION 3
def sqr(numbers):
    squared = []
    numbers.sort()
    for i in numbers:
        sqrd = i ** 2
        squared.append(sqrd)
    print("Numbers:", numbers)
    print("Squared numbers: ", squared)
    
sqr([1,2,3,4,5])


## QUESTION 9 

numbers_lst = []
def NumSum(numbers, target_num):
    for num in range(0, len(numbers)-1):
        for new_num in range(num + 1, len(numbers)):
            num1 = numbers[num]
            num2 = numbers[new_num]
            if num1 + num2 == target_num:
                numbers_lst.append([num1,num2])
                print(f"{numbers_lst} sums to get {target_num}")
    if len(numbers_lst) == 0:
        print(numbers_lst)
    

NumSum([3,11,12,24],36)







