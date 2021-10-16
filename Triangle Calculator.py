"""
Name: Wayne Wei Chen
Student Number: 501033652
Asks the user to input the length of each side of a triangle.
The program then tells the user the classification of the triangle,
the value of each angle in degrees, perimeter, and area.
"""
import math


# Function to return the type of angle based on pythagorean theorem
def angle_type(lengths):
    t = ""  # String variable to store angle type
    if lengths[0] ** 2 == lengths[1] ** 2 + lengths[2] ** 2:  # If C^2 = A^2 + B^2, then return right
        t = "right."
    elif lengths[0] ** 2 > lengths[1] ** 2 + lengths[2] ** 2:  # If C^2 > A^2 + B^2, then it is obtuse
        t = "obtuse."
    if t == "":     # If t is still an empty string, it is acute
        t = "acute."
    return t


# Function to calculate the value of the angles
def angle_val(lengths):
    # Uses a rearranged law of cosines to solve for the angles
    angle_one = math.degrees(math.acos((lengths[0] ** 2 + lengths[1] ** 2 - lengths[2] ** 2) /
                                       (2 * lengths[0] * lengths[1])))
    # Switches the values of A, B, and C in the law of cosines to solve for a different angle
    angle_two = math.degrees(math.acos((lengths[1] ** 2 + lengths[2] ** 2 - lengths[0] ** 2) /
                                       (2 * lengths[1] * lengths[2])))
    angle_three = math.degrees(math.acos((lengths[2] ** 2 + lengths[0] ** 2 - lengths[1] ** 2) /
                                         (2 * lengths[2] * lengths[0])))
    # Rounds each angle to 3 decimal places, and adds them to a list
    angle_list = [round(angle_one, 3), round(angle_two, 3), round(angle_three, 3)]
    return angle_list


# Function to calculate the area of the triangle
def area(lengths):
    height = sum(lengths)/2     # Finds the height of the triangle
    a = math.sqrt(height * (height - lengths[0]) * (height - lengths[1]) * (height - lengths[2]))   # Finds the area
    a = round(a, 3)     # Rounds area to 3 decimal places
    return a


sides = []      # Creates an empty list to store the lengths
exist = True    # Boolean variable used to see if the triangle can exist
for i in range(1, 4):   # Loop to prompt the user for the length, repeats 3 times
    side = float(input("What is the length of side #" + str(i) + ": "))  # Asks the user, and converts input to a float
    while side <= 0:  # Asks the user again if they input an invalid length (0 or less than 0)
        side = float(input("Please enter a valid length for side #" + str(i) + ": "))
    sides.append(side)  # Adds the length to the list if it is valid
sides.sort(reverse=True)    # Sorts the list by descending order
if sides[1] + sides[2] <= sides[0]:  # If A + B <= C, then the triangle cannot exist
    print("The triangle cannot exist")
    exist = False
if exist:   # Only runs if the triangle can exist
    print("Triangle: ", end="")     # Creates a line to put the classifications and angle types
    if sides[0] == sides[1] and sides[1] == sides[2]:   # If all sides are equal, it is equilateral and acute
        print("Equilateral and acute.")      # angle_type is not needed, equilateral is always acute
        angles = angle_val(sides)
        print("The angles in degrees are ", end="")     # Creates a line to put the angle values
        print(angles[0], angles[1], angles[2], sep=", ")
        print("The perimeter is", sum(sides))   # Calculates perimeter by adding sides
        print("The area is", area(sides))
    elif sides[0] == sides[1] or sides[1] == sides[2] or sides[2] == sides[0]:
        """
        If only 2 sides are equal, it is isosceles 
        """
        print("Isosceles and", angle_type(sides))
        angles = angle_val(sides)
        print("The angles in degrees are ", end="")     # Creates a line to put the angle values
        print(angles[0], angles[1], angles[2], sep=", ")
        print("The perimeter is", sum(sides))   # Calculates perimeter by adding sides
        print("The area is", area(sides))
    else:   # If it is not isosceles or equilateral, it is scalene
        print("Scalene and", angle_type(sides))
        angles = angle_val(sides)
        print("The angles in degrees are ", end="")     # Creates a line to put the angle values
        print(angles[0], angles[1], angles[2], sep=", ")
        print("The perimeter is", sum(sides))   # Calculates perimeter by adding sides
        print("The area is", area(sides))
