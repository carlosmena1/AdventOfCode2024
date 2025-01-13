f = open("inputday2.txt", "r")
report = []
total_safe_reports = 0

for line in f:
    report = line.split()
    print(report)
    
    line_safe = 0
    decreasing = 0
    increasing = 0


    for index, number in enumerate(report[:-1]):
        if int(number) > int(report[index + 1]): 
            decreasing += 1
        elif int(number) < int(report[index + 1]): 
            increasing += 1
        
        print(f"{number} - {report[index + 1]} = {abs(int(number) - int(report[index + 1]))}")
        if 1 <= (abs(int(number) - int(report[index + 1]))) <= 3 :
            line_safe += 1


    if line_safe == (len(report) - 1) and (line_safe == decreasing or line_safe == increasing): 
        print(line_safe)
        print(increasing)
        print(decreasing)
        print(f"safe  {report}")
        total_safe_reports += 1
    

print(total_safe_reports)

