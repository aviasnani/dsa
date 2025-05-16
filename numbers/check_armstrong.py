def check_armstrong(number):
    string = str(number)
    arr = list(string)
    arr = [int(item) for item in arr]  # convert all elements to int
    comp = []
    for n in arr: 
        num = n ** len(arr)
        comp.append(num)
    sum = 0
    for n in comp: 
        sum += n
    if number == sum:
        return True
    return False

print(check_armstrong(407))  # Output: [1, 5, 3]