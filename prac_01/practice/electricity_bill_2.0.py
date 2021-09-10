print("Electricity bill estimator 2.0 ")
TARIFF_11 = 0.244618
TARIFF_31 = 0.136928

which_tariff = str(input("which tariff? 11 or 31: "))
a = 11
b = 31
while which_tariff != a or != b:
    which_tariff = str(input("which tariff? 11 or 31: "))
    if which_tariff == '11':
        power_price_kwh = TARIFF_11
        break
    elif which_tariff == '31':
        power_price_kwh = TARIFF_31
        break
    else:
        print("invalde input")
daily_usage_kwh = float(input("daily use in kWh: "))
number_of_days_per_bill = float(input("number of days in the billing period: "))
estimated_bill = str((power_price_kwh/100)*(daily_usage_kwh*number_of_days_per_bill))
print("Estimated bill: $"+estimated_bill)