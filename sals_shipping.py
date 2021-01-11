# Ground Shipping
# 2 lb or less price = 1.50
# Over 2 lb but less than or equal to 6lb price = 3.00
# Over 6 lb but less than or equal to 10 lb price = 4.00
# Over 10 lb price = 4.75 

# Drone Shipping
# 2 lb or less price = 4.50
# Over 2 lb but less than or equal to 6 lb price = 9.00
# Over 6 lb but less than or equal to 10 lb price = 12.00
# Over 10 lb price = 14.25

# Premium Ground Shipping 
# Flat charge of $125.00 
premium_ground_shipping = 125

# write a function for the cost of groun shipping. 
def shipping_ground(weight):
	if weight <= 2:
		cost_of_shipping = (1.50 * weight) 
	elif weight <= 6:
		cost_of_shipping = (3.00 * weight)
	elif weight < 10:
		cost_of_shipping = (4.00 * weight)
	else:
		cost_of_shipping = (4.75 * weight)
	return cost_of_shipping + 20

#print(cost_shipping_ground(8.4))
# (8.4lb x $4.00 + $20 flat charge) =>  should print $53.60 

def drone_shipping(weight):
  if weight <= 2:
    cost_of_shipping = (weight * 4.50)
  elif weight <= 6:
    cost_of_shipping = (weight * 9.00)
  elif weight <= 10:
    cost_of_shipping = (weight * 12.00)
  else:
    cost_of_shipping = (weight * 14.25)
  return cost_of_shipping

#print(cost_drone_shipping(1.5))
#should print 6.75
def cheapest_method(weight):
  ground = shipping_ground(weight)
  drone = drone_shipping(weight)
  premium = premium_ground_shipping

  if ground < drone and ground < premium:
    method = "standard ground"
    cost = ground
  elif drone < ground and drone < premium:
    method = "drone"
    cost = drone
  else:
    method = "premium ground"
    cost = premium
  print("The cheapest option available is $%.2f with %s shipping." % (cost, method))
  
cheapest_method(4.8)
# Expecting => The cheapest option available is $34.40 with standard ground shipping.
cheapest_method(41.5)
# Expecting => The cheapest option available is $125.00 with premium ground shipping.