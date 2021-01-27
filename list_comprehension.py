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

#leaving off here to pickup tomorrow: 
cuts_under_30 = [hairstyle[i] for hairstyle[i] if hairstyle < 30]

