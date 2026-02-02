weight = 41.5
cost = 0
#Ground Shipping
if weight <= 2:
  cost = weight * 1.50 + 20.00
elif weight > 2 and weight <= 6:
  cost = weight * 3 + 20.00
elif weight > 6 and weight <= 10:
  cost = weight * 4 + 20.00
elif weight > 10:
  cost = weight * 4.75 + 20.00
else:
  print("Error")
print("The Ground Shipping cost is $" + str(cost))
#Ground Shipping Premium
cost_of_premium = 125.00
print("The Ground Shipping Premium cost is $" + str(cost_of_premium))
#Drone Shipping
if weight <= 2:
  cost = weight * 4.50
elif weight > 2 and weight <= 6:
  cost = weight * 9.00 
elif weight > 6 and weight <= 10:
  cost = weight * 12.00
elif weight > 10:
  cost = weight * 14.25
else:
  print("Error")
print("The Drone Shipping cost is $" + str(cost))
