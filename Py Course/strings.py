text = "123456789"
print(text[1::2])  # 2468
print(text[0::2])  # OR text[::2] => 13579

text = "Hello My name 1 is Lucky and my name also populor "
print(text)
print(text.find("My"))              # find position of word in string
print(text.count("name"))           # count a word in string
print(text.endswith("populor"))     # check word exist in string, return boolean
print(text.startswith("Hello"))     # check word exist in string, return boolean
print(text.split(" name "))         # split string (just like implode)

s = "---"
list1 = ["aa","bb"]
print(s.join(list1))                # just like implode

print(text.replace("Hello","Hey"))
print(text.strip())                 # returns a string with whitespace removed from the start and end

print(text.isalpha())
print(text.isdigit())
print(text.isspace())
# s.isalpha()/s.isdigit()/s.isspace()


#-------------------------------------------------------------------------------------------------------------
########################  String Formatting :- ###########################

value = 2.791514
result = f'approximate value = {value:.1f}'
print(result)
print(f'approximate value = {value:.2f}')  # approximate value = 2.79

car = {'tires':4, 'doors':2}
car = [1,2,3]
print(f'car = {car}') # car = {'tires': 4, 'doors': 2}
print('The Car is : %s' % car)


address_book = [{'name':'N.X.', 'addr':'15 Jones St', 'bonus': 70},
    {'name':'J.P.', 'addr':'1005 5th St', 'bonus': 400},
    {'name':'A.A.', 'addr':'200001 Bdwy', 'bonus': 5},]

for person in address_book:
  print(f'{person["name"]:<5} || {person["addr"]:^20} || {person["bonus"]:>5}')

# N.X.     || 15 Jones St          ||    70
# J.P.     || 1005 5th St          ||   400
# A.A.     || 200001 Bdwy          ||     5


  # % operator
text = "%d little pigs come out, or I'll %s, and I'll %s, and I'll blow your %s down." % (3, 'huff', 'puff', 'house')
print(text)

data = ("John", "Doe", 53.44)
format_string = "Hello %s %s. Your current balance is $%s."
print(format_string % (data[0],data[1],data[2]))

data = ("John", "Doe", 53.44)
format_string = "Hello %s %s. Your current balance is $%.2f."
print(format_string % (data[0],data[1],data[2]))


subject = "Check Kar"
message = "hey Manish it's a test mail By Lucky"
email_body= f"Subject:{subject}\n\n{message}"
print(email_body)
