#create dictionary or something form file
file_path = 'C:/Users/Flori/Documents/AoC/Day1_Input.txt'
leftColumn = []
rightColumn = []

try:
    with open(file_path, 'r') as file:
        for line in file:
            numbersArray = line.split()
            leftColumn.append(int(numbersArray[0]))
            rightColumn.append(int(numbersArray[1]))
                 
except FileNotFoundError:
    print(f"Error: The file '{file_path}' not found.")



#sort both columns from the lowest number
leftColumn.sort()
rightColumn.sort()
#find the difference between each
index = 0
sum = 0
for number in leftColumn:
    leftNumber = leftColumn[index]
    rightNumber = rightColumn[index]
    difference = abs(leftNumber - rightNumber)
    index += 1
#add them up
    sum += difference

print("Total is: " + str(sum))