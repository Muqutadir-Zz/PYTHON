# while True :
#   print("muqutadir")

# count = 1
# while count <= 5 :
#     print("hello")
#     count += 1

# i = 1
# while i <= 100 :
#     print("LUFFY")
#     i+=1

# i = 5 
# while i>=1 :
#     print(i)
#     i -=1

#     print("ZORO")

# PRACTICE

# i = 1
# while  i<= 100 :
#     print(i)
#     i += 1

# i = 100
# while i>=1 :
#     print(i)
#     i -= 1


# i = 1
# while i <= 10 :
#     print(3*i) 
#     i += 1  

# i = 1
# while i <= 10 :
#     print(99*i) 
#     i += 1 

# nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# print(nums[0])
# print(nums[1])
# print(nums[2])
# print(nums[3])  #.... print(nums[len(nums)-1])

# nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# idx = 0
# while idx < len(nums) :
#     print(nums[idx])
#     idx += 1


# nums =  [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# x = 25

# i = 0
# while i < len(nums) :
#     if(nums[i] == x):
#         print("FOUND at idx" , i)
#     else : 
#         print("finding.........")
#     i += 1
    
# i = 1
# while i <= 5 :
#     print(i)
#     if(i == 3) :
#         break
#     i += 1

# veggies = ["POTATO", "TOMATO", "LADYFINGER", "CUCUMBER"]

# for val in veggies:
#     print(val)   # also for tup , also str

# str = "MARVEL"

# for char in str:
#     if(char == 'R'):
#         print("R FOUND")
#         break
#     print(char)
    
#  RANGE() FUNCTION IMP FOR LOOPS

# 1. range(stop)

# seq =range(5)

# for i in range(10) :
#     print(i)

# 2. range(start, stop)

# for i in range(2, 10) :
#     print(i)

# 3. range (start, stop, step)

# for i in range(2, 10, 2) :
#     print(i)


# PASS STATEMENT 

# for i in range(3):
#     pass
#     print("some usefull work")

n = 5
sum = 0
for i in range(1, n+1) :
    sum += i

    print("total sum", sum)