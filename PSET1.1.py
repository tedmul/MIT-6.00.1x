# Assume s is a string of lower case characters.
# Write a program that counts up the number of vowels contained in the string s. Valid vowels are: 'a', 'e', 'i', 'o', and 'u'. 
# For example, if s = 'azcbobobegghakl', your program should print:
# Number of vowels: 5

y = 0
for x in range(len(s)):
    if (s[x] == 'a') or (s[x] == 'e') or (s[x] == 'i') or (s[x] == 'o') or (s[x] == 'u'):
        y += 1
print(y)
