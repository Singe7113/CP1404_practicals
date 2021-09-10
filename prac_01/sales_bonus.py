"""
Program to calculate and display a user's bonus based on sales.  
If sales are under $1,000, the user gets a 10% bonus.  
If sales are $1,000 or over, the bonus is 15%.  

"""
sales = float(input("how mush are we talking? "))
if sales>=1000:
    bonus_rate = 0.15
elif sales<1000:
    bonus_rate = 0.1

bonus_amount = float(sales*bonus_rate)
print(bonus_amount)