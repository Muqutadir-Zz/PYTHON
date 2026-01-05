# function defination
# def cal_sum(a,b) : #parameters
#     return(a,b)

# sum = cal_sum(1,2)   #function call;arguments
# print (sum)

# def calc_avg(a, b, c) :
#     sum = a+b+c
#     avg = sum/3
#     print(avg)
#     return avg

# calc_avg(60, 30, 70)

# BUILT IN FUNCTION

#  print()

#  len()  defiine interger value

# tpye()  , range()

# cities = ["delhi", "mumbai", "hyd", "pune"]
# heros = ["superman", "batman"]

# def print_len(list) :
#     print(len(list))

# print_len(cities)
# print_len(heros)

# def cal_fact(n):
#     fact = 1
#     for i in range(1, n+2):
#         fact *= i
#         print(fact)

# cal_fact(6)

# def conveter(usd_value):
#     inr_value = usd_value * 83
#     print(usd_value, "USD =", inr_value, "INR")

# conveter(73)

# RECURSION

# def show(n):
#     if(n == 5):
#         return
#     print(n)
#     show(n-1)

# print(2)

# def show(n):
#     if(n==0):
#         return
#     print(n)
#     show(n-1)

# show(2) # prints n to 1 backwards

# def fact(n):
#     if(n==0 or n==1):
#         return 1
#     else:
#         return n * fact(n-1) 
    
# print(fact(6))

# PRACTICE
# def cal_sum(n):
#     if(n==0):
#         return 0
#     return cal_sum(n-1) + n

# sum = cal_sum(55)
# print(sum)


def print_list(list, idx=0):
    if(idx == len(list)):
        return
    print(list[idx])
    print_list(list, idx+1)

fruits = ["apple", "banana" ]
print_list(fruits)