# Assume s is a string of lower case characters.
# Write a program that prints the number of times the string 'bob' occurs in s. For example, if s = 'azcbobobegghakl', then your program should print
# Number of times bob occurs is: 2

y = 0
for x in range(len(s[:-2])):
    if 'bob' == s[x:(x+3)]:
        y += 1
print("Number of times bob occurs is: " + str(y))
