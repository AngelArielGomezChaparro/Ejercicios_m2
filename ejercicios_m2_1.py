
#number = input("Enter a number: ")
#reverse = number[::-1]
#print(reverse)

# Data input
C1 = int(input("Enter grade for assessment 1: "))
C2 = int(input("Enter grade for assessment 2: "))
NL = int(input("Enter lab grade: "))

NC = (59.5 - (0.3 * NL)) / 0.7
C3 = (((3 * NC) - (C1 + C2)) + 1)
print(round(C3))
