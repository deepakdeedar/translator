print("How many kilometers did you run today?")
kms = input()
miles = float(kms)/1.60094
miles = round(miles, 2)
print(f"Your {kms}Km walk was {miles}mile(s)")

#round(variable to round, how many decimal places)