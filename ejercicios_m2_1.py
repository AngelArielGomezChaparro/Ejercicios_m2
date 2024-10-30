firstcatetus = float(input("What's the first leg of a triangle?: "))
secondcatetus = float(input("What's the second leg of a triangle?: "))

hypotenuse = ((firstcatetus ** 2 + secondcatetus ** 2) ** 0.5)

print(f"""The hypotenuse is: {hypotenuse}""")