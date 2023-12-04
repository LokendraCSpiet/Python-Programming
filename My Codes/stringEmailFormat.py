email = '''Hello <|NAME|>,
\t You are selected as a <|POST|> at <|COMPANY|>.
Thanks & Regards,
<|REGARDS|>
Date : <|DATE|>'''

name = input("Enter Applicant Name: ")
post = input("Enter Job Post: ")
company = input("Enter Company Name: ")
Regards = input("Enter REGARDS: ")
date = input("Enter Date: ")

email = email.replace("<|NAME|>",name)
email = email.replace("<|POST|>",post)
email = email.replace("<|COMPANY|>",company)
email = email.replace("<|REGARDS|>",Regards)
email = email.replace("<|DATE|>",date)

# parameter = ["<|NAME|>","<|POST|>","<|COMPANY|>","<|REGARDS|>","<|DATE|>"]
# values = [name,post,company,REGARDS,date]

# for i in range(5):
#     email = email.replace(parameter[i],values[i])

print(email)

