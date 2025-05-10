monthly_saving = int (input ("how much money you want to save in a month? "))
annual_increase_rate = int ((input ("how much is the annual profit? ")))
annual_growth_rate = int ((input ("how much you want to increase your saving every year? "))) 
years = int (input ("for how many years you want to save? "))
annual_increase_rate = annual_increase_rate / 100
annual_growth_rate = annual_growth_rate / 100
temp = 0
i = 0
finallyResult = 0
for year in range (1 , years + 1):
    income  = ((monthly_saving * (1 + annual_growth_rate) ** i))*12
    print (income)
    finallyResult = (income * annual_increase_rate) + income + temp + finallyResult
    print("result: ", finallyResult)
    temp = income * annual_increase_rate + income + temp
    i += 1
print("final: ", finallyResult)


    
    


    


