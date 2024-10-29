def fibonacci(num):
    start_sequence = [0, 1]
    string_sequence = ""
    flage = 0
    while flage == 0:
        if type(num) == type(0):
            num = int(num)
            flage = 1
        else:
            print("Enter a valid number")
            flage = 0
    for i in range(num):
        if num > 2:
            start_sequence.append(start_sequence[i] + start_sequence[i + 1])  
    for el in range(len(start_sequence)):
        string_sequence += str(start_sequence[el]) + " "
    return string_sequence
#recursion what is that?
if __name__ == '__main__':
    print(fibonacci(5))