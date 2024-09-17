import csv

terminology = []
description = []
errors_counter = 0
unique_errors = 0

with open("database/(17.09.2024)_foods.csv", encoding='utf-8') as r_file:
    file_reader = csv.reader(r_file, delimiter=';')
    for row in file_reader:
        terminology.append(str(row[1]))
        description.append(str(row[0]))

print(f"Total {len(terminology)} terms. If you don't know term, write '0' to see description. Let's start!")
for i in range(len(terminology)):
    print(terminology[i])
    user_input = str(input())
    while user_input != description[i]:
        if user_input == "0":
            print(description[i])
            print("Now type it")
            user_input = str(input())
        else:
            print("Incorrect :( Try again...")
            user_input = str(input())
            errors_counter += 1
    else:
        print("Correct!")
print(f"Final! Total errors: {errors_counter}")