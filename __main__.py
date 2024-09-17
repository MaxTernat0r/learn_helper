import csv

terminology = []
description = []
errors_counter = 0

with open("database/(17.09.2024)_foods.csv", encoding='utf-8') as r_file:
    file_reader = csv.reader(r_file, delimiter=';')
    for row in file_reader:
        terminology.append(str(row[1]))
        description.append(str(row[0]))

for i in range(len(terminology)):
    print(terminology[i])
    user_input = str(input())
    while user_input != description[i]:
        print("Incorrect :( Try again...")
        user_input = str(input())
    else:
        print("Correct!")
