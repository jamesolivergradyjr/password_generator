#Salary Calculator
question = input("How much do you want to make an hour? ")
salarybyweek = (int(question)) * 40
print("Salary by week at " + question + " would equal " + str(salarybyweek))
salarybyyear = salarybyweek * 45
print("Salary by year at " + question + " would equal " + str(salarybyyear))
#Division/ (always gives a float)
totaltakehome = salarybyyear / 24
# print("Total take home before taxes of any kind if paid biweekly is " + str(totaltakehome))
taxedincome = totaltakehome * 0.70
print("Total actual take home after taxes if paid biweekly is " + str(taxedincome))