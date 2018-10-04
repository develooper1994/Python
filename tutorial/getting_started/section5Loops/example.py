def c_to_f(c):
    if c< -273.15:
        return float('nan') #"That temperature doesn't make sense!"
    else:
        f=c*9/5+32
        return f

temperatures=[10,-20,-289,100]

celc_temp=[c_to_f(items) for items in temperatures]
print(celc_temp)