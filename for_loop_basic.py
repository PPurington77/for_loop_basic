#1. Basic- Print all integers from 0 to 150
# for i in range(0, 151):
#     print(i)

#2. multiples of five- print all the multiples of 5 from 1000
# for i in range(5, 1000):
#     if i % 5 == 0:
#         print(i) 

#3. counting, the dojo way-print integers 1 to 100. if divisible by 5 print 'coding' if divisible by 10 print Coding Dojo
# i = 1
# while i <= 100:
#     if i % 10 == 0:
#         print("Coding Dojo")
#     elif i % 5 == 0:
#         print("Coding")
#     else:
#         print(i)
#     i +=1

#another method
# for i in range(1, 101):
#     if i % 10 == 0:
#         print("Coding Dojo")
#     elif i % 5 == 0:
#         print("Coding")
#     else: 
#         print(i)
#     i +=1 

#4. Whoa. That sucker's huge- add odd integersf from 0 to 500,000, and print the final sum
# sum = 0
# i = 0
# while i <= 500000:
#     if i % 2 != 0:
#         sum = sum + i
#     i +=1
# print(sum)

#or

# sum = 0
# for i in range(0, 500001):
#     if i % 2 != 0:
#         sum = sum + i
# print(sum)


#5. Countdown by fours- print positive numbers starting at 2018 counting down by 4
# for i in range(2018, 0, -4):
#     print(i)

#6. Flexible counter-set 3 variable lowNum, highNum, and mult. starting at lowNum and going through highNum, print only the integers that are a multple of mult. 
# lowNum = 3
# highNum = 200
# mult = 3
# for i in range(lowNum, highNum):
#     if i % mult == 0:
#         print(i)