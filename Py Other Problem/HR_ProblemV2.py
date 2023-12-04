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
def calculation(HrWorked,HourlyRate):
        income = int(HrWorked) * int(HourlyRate)
        IncDeduction = (income * 20)/100
        SupDeduction = (income * 10)/100

        Income.append(income)
        Income_Tax_Deduction.append(IncDeduction)
        Superannuation_Deduction.append(SupDeduction)

employee_name = []
Income = []
Income_Tax_Deduction = []
Superannuation_Deduction = []
for i in range(2):
        Emp = input(f"Enter Employee Name ({i+1}):")
        employee_name.append(Emp)
        HrWorked = input("Enter Hours Worked :")
        HourlyRate = input("Enter Hourly Rate :")
        calculation(HrWorked,HourlyRate)

Output = {
        "Employee Name":employee_name,
        "Income":Income,
        "Income Tax Deduction":Income_Tax_Deduction,
        "Superannuation Deduction":Superannuation_Deduction
        }

print(Output)

import pandas as pd
brics = pd.DataFrame(Output)
print(brics)

