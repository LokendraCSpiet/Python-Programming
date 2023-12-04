#QUESTION - 
""" 
For example, if an employee user, "John Smith", enters 40 hours worked and hourly rate of $25 per
hour, as shown in Table 1. Then, the total income will be $1000, of which 20% is taxed ($200) and
10% deducted for superannuation ($100), 
as shown in Table 2:-

_____________________________________________________________
|   Employee Name   |   Hours Worked    |   Hourly Rate     |
|   John Smith      |   40              |   25              |
|   Jane Doe        |   35              |   30              |
_____________________Table 1: Employee Input_________________


_____________________________________________________________________________________________________
|   Employee Name   |   Income          |   Income Tax Deduction    |   Superannuation Deduction    |
|   John Smith      |   1000            |   200                     |   100                         |
|   Jane Doe        |   1050            |   210                     |   105                         |
_________________________Table 2:Output calculation based on table 1 Employee input__________________
"""



# CODE - 

Emp = input("Enter Employee Name :")
HrWorked = input("Enter Hours Worked :")
HourlyRate = input("Enter Hourly Rate :")
income = int(HrWorked) * int(HourlyRate)

def calculation(income):
    amount = income
    IncDeduction = (amount * 20)/100
    SupDeduction = (income * 10)/100
    result = [income,int(IncDeduction),int(SupDeduction)]
    # result = [result,HrWorked,HourlyRate]
    return result

result = calculation(income)
# print(Emp +"has -\nIncome is:""\n Income Tex Deduction is :""\n Superannuation Deduction is :")
print(Emp +" has -\nIncome is:"+str(result[0])+"\n Income Tex Deduction is :"+str(result[1])+"\n Superannuation Deduction is :"+str(result[2]))

