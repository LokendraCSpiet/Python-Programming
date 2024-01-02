""" 
Generate all Pairs of 0 and 1 -
Given N pairs of Binary Numbers 0 and 1, your task is to generate 
all possible combinations such that for each 0 there should be 
a corresponding 1 in the combination not vice versa. 
In simple words for every 0 on the left there should be a 1 on the right.

"0011" is a valid combination as for both zeros there are two 1's present in the right.

"0110" is not a valid combination as there is a 1 for the first 0 
but no 1 is present for the last 0 on its right.

For Example :
    N = 1
    Output : 1
    Explanation : 
        All possible combination of pair 1 = "01", 
        but "10" is not a valid pair as there is no valid 1 for 0 on the right of it.
    
    N = 2
    Output : 2
    Explanation :
        All possible combination of pair 2 = "0011", "0101" 
        Notice here that for every 0 on the left there is a 1 on the right.

OBSERVATION:
    1.The problem becomes simple to understand 
       if consider 0 as left bracket "(" and 1 as right bracket ")".

    2.Now we just need to balance these brackets in all possible ways.

    3.For N = 3, such possible combinations can be:
    ((())),
    (()()),
    (())(),
    ()(()),
    ()()()

"""

# def generatePairs_0_1(N,n):
#     if()


# n = int(input("Enter a number:"))
# generatePairs_0_1(n*2,n)

list1 = ["0011","0101"]
print(f'All possible combination of pair 1 ="{list1[0]}"')
