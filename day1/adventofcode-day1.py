f = open("inputday1.txt", "r")
column1 = []
column2 = []

for line in f:
    columns = line.split("   ")
    column1.append(int(columns[0]))
    column2.append(int(columns[1].replace("\n","")))
    
column1.sort()
column2.sort()

total_distance = 0

for index, num in enumerate(column1):
    total_distance += abs(num - column2[index])

print(f"Total distance: {total_distance}")

similarity_score = 0

for index, num in enumerate(column1):
    
    similarity_score += num * column2.count(num)

print(f"similarity_score: {similarity_score}")