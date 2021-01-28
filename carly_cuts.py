hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]

prices = [30, 25, 40, 20, 20, 35, 50, 35]

last_week = [2, 3, 5, 8, 4, 4, 6, 2]

# Prices and Cuts:
total_price = 0

for price in prices:
  total_price += price
print("* Total price is: " + str(total_price))

average_price = (total_price / len(prices))
print("* Average Haircut Price: " + str(average_price))

new_prices = [price - 5 for price in prices]
print(new_prices)

# Revenue:
total_revenue = 0

for i in range(len(hairstyles)):
  total_revenue += (prices[i] * last_week[i])
print("Total Revenue: " + str(total_revenue))

average_daily_value = total_revenue / 7

print("The average daily value is: " +  str(average_daily_value))

'''
Carly thinks she can bring in more customers by advertising all of the haircuts she has that are under 30 dollars.

Use a list comprehension to create a list called cuts_under_30 that has the entry hairstyles[i] for each i for which new_prices[i] is less than 30.

You can use range() in your list comprehension to make i go from 0 to len(new_prices) - 1.
'''
cuts_under_30 = [hairstyles[i] for i in range(len(hairstyles[i])) if new_prices[i] < 30]

print(cuts_under_30)

