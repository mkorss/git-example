import pandas as pd

#Read the csv file
new_purchases = pd.read_csv('new_purchases.csv')

total_ny = 0
total_sf = 0
count_ny = 0
count_sf = 0

purchases_list = new_purchases.values.tolist()

#Process each row in purchases_list
print("\nProcessing transactions for New York:")
for row in purchases_list:
    city = row[2]
    price = float(row[4])
    
    if 'New York' in city: 
        total_ny += price 
        count_ny += 1
        print(f"Order amount: ${price}, running total for New York: ${round(total_ny, 2)}")
    
    elif 'San Francisco' in city:
        total_sf += price
        count_sf += 1
        print(f"Order amount: ${price}, running total for San Francisco: ${round(total_sf, 2)}")

print(f"\nThe total transaction amount for New York is ${round(total_ny, 2)} based on {count_ny} transactions.")
print(f"The total transaction amount for San Francisco is ${round(total_sf, 2)} based on {count_sf} transactions.")

#Calculate the averages
if count_ny > 0:
    avg_ny = total_ny / count_ny

else:
    avg_ny = 0
    print('Average transaction amount in New York is $0')

if count_sf > 0:
    avg_sf = total_sf / count_sf

else:
    avg_sf = 0
    print('Average transaction amount in San Francisco is $0')
      
with open ('Transactions.txt', 'a') as f:
    f.write(f"The average transaction amount based on {count_ny} transactions in New York is ${round(avg_ny, 2)}")
    f.write(f"\nThe average transaction amount based on {count_sf} transactions in San Francisco is ${round(avg_sf, 2)}")
    
#Final
    if avg_ny > avg_sf:
        f.write("\nNew York has a higher average transaction amount than San Francisco.")

    else:
        f.write("\nSan Francisco has a higher average transaction amount than New York.")

print('Transactions Completed')
    

        

