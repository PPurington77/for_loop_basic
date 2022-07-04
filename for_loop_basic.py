#1. basic: print all integers from 0 to 150
# for i in range(0, 151):
#     print(i)

#2. multiples of five: print all the multiples of 5 from 5 to 1,000
# i = 5
# while i < 1000:
#     print(i)
#     i = i * 5

#3. counting the dojo way. print integers 1 to 100. if divisible by 5 print "coding" instead, if divisible by 10, print "coding dojo"

# for i in range(1, 101):
#     if i % 10 == 0:
#         print("Coding Dojo")
#     elif i % 5 == 0:
#         print("Coding")
#     else:
#         print(i)

#4. whoa. that sucker's huge. add odd integers from 0 to 500,000, and print the final sum
# x = 0
# sum = 0
# while x < 500000:
#     if x % 2 != 0:
#         sum = sum + x
#     x+=1
# print(sum)

#5 countdown by 4's. print positive numbers starting at 2019 counting down by fours
# for i in range(2018, 0, -4):
#     print(i)

#6. flexible bounter. set three variables: lowNum, highNum, mult. starting at lownum and going through highnum, print only the intergers that are a mulitple of mult. 
lowNum = 10
highNum = 100
mult = 5
while lowNum <= highNum:
    if lowNum % mult == 0:
        print(lowNum)
    lowNum +=1