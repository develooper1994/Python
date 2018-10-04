def currency_converter(rate,euros):
    dollars=euros*rate; return dollars

r=float(input("Enter rate: "))
e=float(input("Enter euros: "))
print(currency_converter(r,e))