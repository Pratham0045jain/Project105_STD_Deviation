import csv 
import math

with open("Marks_data.csv") as f:
    csv_reader = csv.reader(f)
    file_data = list(csv_reader)
    data = file_data[0]


total = 0
for num in data:
    total += int(num)

mean = total/len(data)


sq_list = []
for i in data:
    sq_val = (int(i) - mean)*(int(i) - mean)
    sq_list.append(sq_val)

sum = 0
for i in sq_list:
    sum += i

result = sum/(len(sq_list)-1)

standard_deviation = math.sqrt(result)

print("The standard deviation for this data is "+ str(standard_deviation))
