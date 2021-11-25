import sys

rentalCode = input("(B)udget, (D)aily, or (W)eekly rental?\n").upper()
if rentalCode == 'B' or rentalCode == 'D' or rentalCode =='W': #This If statement helps to make sure that the inputs provided are only one of the three options. If they are not then they are able to try again.
  if rentalCode == 'B' or rentalCode == 'D':  # For this branch we are able to determine what kind of information is needed depending on the input provided.
      rentalPeriod = input("Number of Days Rented:\n")  # Here we see an input that is stored in a variable.
  else: #
     rentalPeriod = input("Number of Weeks Rented:\n")
  budgetCharge = 40.00
  dailyCharge = 60.00
  weeklyCharge = 190.00

  if rentalCode == 'B': #Through the information provided the system is able to make the correct calculations for the category of the first input they gave.
      baseCharge = int(rentalPeriod) * budgetCharge
  elif rentalCode == 'D':
      baseCharge = int(rentalPeriod) * dailyCharge
  else:
      baseCharge = int(rentalPeriod) * weeklyCharge

  odoStart = input("Starting Odometer Reading:\n")
  odoEnd = input("Ending Odometer Reading:\n")
  totalMiles = int(odoEnd) - int(odoStart)  # Here we see two variables that are being converted into integers,
# they are also used as a math problem and lastly their answer changes what totalMiles stands for.

  if rentalCode == 'B':  # In this If Branch it determines it determines what is being charged for the rental code provided.
      mileCharge = float(totalMiles) * 0.25  # For the totalMiles variable it is being converted into a float to be able to complete the problem.
  elif rentalCode == 'D':
      averageDayMiles = int(totalMiles) / int(rentalPeriod)
      if averageDayMiles <= 100:  # This Branch is contained inside of a conditional statement which helps to narrow down the correct calculations that are needed.
          extraMiles = 0
      elif averageDayMiles > 100:
          extraMiles = averageDayMiles - 100
          mileCharge = extraMiles * .25
  else:
      averageWeekMiles = int(totalMiles) / int(rentalPeriod)
      if averageWeekMiles <= 900:
          mileCharge = 0
      elif averageWeekMiles > 900:
          mileCharge = 100 * int(rentalPeriod)
  amtDue = float(baseCharge) + float(mileCharge)
else: # This is connected to the if statement in the beginning that helps to determine if the input is valid. If it is not it then comes down here to verify what needs to be down next.
    print("Incorrect input: Please use B for Budget, D for Daily, W for Weekly")
    rentalCode = input("(B)udget, (D)aily, or (W)eekly rental?\n").upper() #Here we clarify what inputs are valid and then we ask them once again to input a code.

print("Rental Summary") #Once all the calculations are done we come down here and print out a summary of the necessary information.
print("Rental Code:        " + str(rentalCode))
print("Rental Period:        " + str(rentalPeriod))
print("Starting Odometer:  " + str(odoStart))
print("Ending Odometer:    " + str(odoEnd))
print("Miles Driven:       " + str(totalMiles))
print("Amount Due:         $" + str("%0.2f" % amtDue))