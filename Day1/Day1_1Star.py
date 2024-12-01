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

#find the similarity score
sum = 0
for number in leftColumn:
    Count = rightColumn.count(number)
    similarityScore = number * Count
#add them up
    sum += similarityScore

print("Total is: " + str(sum))