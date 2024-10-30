current_time = int(input("Enter the current hour (0-23): "))
number_hours = int(input("Number of hours: "))
new_time = (current_time + number_hours) %24
print (f"In {number_hours} hours, the clock will read {new_time}")