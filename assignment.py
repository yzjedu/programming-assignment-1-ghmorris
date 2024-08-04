# Name: Grace-Ann Morris 
# Course: CS701/GB735, Dr. Yalew
# Date: August 6, 2024 
# Programming Assignment: 1
# Program Inputs: Dimensions of the room (length, width, height) in feet
# Program Outputs: Total area to be painted (in square feet), amount of primer (in gallons), amount of paint (in gallons)

def main():
    
    '''This program calculates the total area to be painted (in square feet), amount of primer (in gallons) and amount of paint (in gallons)'''

    # Algorithm Step 1: Input 
    # Ask user for the dimensions of a room 
    # Dimensions include: length, width, and ,height
    length = float (input("What is the length of the room? (in feet) "))
    width = float (input("What is the width of the room? (in feet)"))
    height = float(input("What is the height of the room? (in feet)"))
    
    # Step 2: Calculate the total area of the four walls and ceiling not including the floor 
    # wall area = 2 * height * (length + width)
    # ceiling area  = length * width
    # total area = wall area + ceiling area 
    wall_area = 2 * height * (length + width)
    ceiling_area = length * width 
    total_area = wall_area + ceiling_area

    # Step 3: Compute the amount of primer and paint needed
    # Define constants: coverage of primer, coverage of paint
    # coverage of primer = 200 square feet per gallon
    # coverage of paint = 350 square feet per gallon
    coverage_of_primer = 200 
    coverage_of_paint = 350 
    primer_needed = total_area / coverage_of_primer 
    paint_needed = total_area / coverage_of_paint

    # Step 4: Output 
    # Print the total area and the amount of primer and paint needed
    print(f"Total area to be painted: {total_area:.2f} square feet")
    print(f"Amount of primer needed: {primer_needed:.2f} gallons")
    print(f"Amount of paint needed: {paint_needed:.2f} gallons")

if __name__ == "__main__":
    main()