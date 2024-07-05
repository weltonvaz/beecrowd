import sys
from datetime import date

# Define the date for Christmas
christmas = date(2016, 12, 25)

# Iterate through each line of input until EOF
for line in sys.stdin:
    # Split the input line into month and day
    month, day = map(int, line.strip().split())

    # Create a date object for the input date
    current_date = date(2016, month, day)
    
    # Calculate the difference in days between the current date and Christmas
    delta = (christmas - current_date).days
    
    # Determine the output message based on the number of days until Christmas
    if delta == 0:
        print("E natal!")
    elif delta == 1:
        print("E vespera de natal!")
    elif delta < 0:
        print("Ja passou!")
    else:
        print(f"Faltam {delta} dias para o natal!")
