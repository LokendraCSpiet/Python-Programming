def starPattern(n):
    if n > 0:
        print("*" * n)
        starPattern(n-1)

        
    

n = int(input("Enter a number:"))
patt = ""
starPattern(n)
# print(starPattern(n))