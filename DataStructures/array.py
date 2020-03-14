total=0
ave=0
numbers=[19,15,20,5]
for i in numbers:
    total=i+total
    numberslen=len(numbers)
    ave = total / numberslen
print("Numbers: " , numbers)
print("Average: " , ave)
