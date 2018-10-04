temperatures=[10,-20,-289,100]
def writer(c,filepath):
    with open("exercise3.txt", "w+") as file:
        for c in temperatures:
            if c > -273.15:
                var = str(c*9/5+32)
                print(var)
                file.write(var + "\n")

writer(temperatures, "temps.txt")





