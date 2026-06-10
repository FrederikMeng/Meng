
# Realkreditlånsberegner



loan_amount = float(input("Write loan amount: "))
interest_rate = float(input("Choose interest rate (3 / 3.5 / 4): "))
years = int(input("Loan length in years (ex 30): "))

# Bond prices
if interest_rate == 3:
    bond_price = 87
elif interest_rate == 3.5:
    bond_price = 92
elif interest_rate == 4:
    bond_price = 99
else:
    print("Only choose 3, 3.5 or 4")
    exit()

# Money received after kurs
received = loan_amount * bond_price / 100
loss = loan_amount - received

# Monthly calculations
monthly_rate = (interest_rate / 100) / 12
months = years * 12

# Monthly payment formula
monthly_payment = loan_amount * (
    monthly_rate * (1 + monthly_rate) ** months
) / ((1 + monthly_rate) ** months - 1)

# Total paid
total_paid = monthly_payment * months
total_interest = total_paid - loan_amount


print("resultater")
print("Total lånt:", round(loan_amount, 2), "kr")
print("kurs på obligationer:", bond_price)
print("Penge udbetalt som rådighed fra lånet:", round(received, 2), "kr")
print("Tabt ved kurs af obligationer bag lånet:", round(loss, 2), "kr")
print("Månedlig betaling:", round(monthly_payment, 2), "kr")
print("Total paid after", years, "years:", round(total_paid, 2), "kr")
print("Totale renter betalt:", round(total_interest, 2), "kr")



# actually this isn't correct because it 