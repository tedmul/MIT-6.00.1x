# Assume s is a string of lower case characters.
# Write a program that prints the longest substring of s in which the letters occur in alphabetical order. For example, if s = 'azcbobobegghakl', then your program should print
# Longest substring in alphabetical order is: begghIn the case of ties, print the first substring. For example, if s = 'abcbcd', then your program should print
# Longest substring in alphabetical order is: abc
# Note: This problem may be challenging. We encourage you to work smart. If you've spent more than a few hours on this problem, 
# we suggest that you move on to a different part of the course. If you have time, come back to this problem after you've had a break and cleared your head.

y = []
for x in range(len(s)):
    y.append(ord(s[x]))
    
y.append(0)

z = []
for i in range(len(y[:-1])):
    if y[i] <= y[i+1]:
        z.append(chr(y[i]))
    elif y[i] >= y[i-1]:
        z.append(chr(y[i]))
        z.append(0)
    else:
        z.append(0)
        
long_list = [[]]
v = 0

for t in range(len(z)):
    if type(z[t]) is str:
        long_list[v].append(z[t])
    elif z[t] == 0:
        long_list.append([])
        v += 1 

print('Longest substring in alphabetical order is: ' + ''.join(max(long_list,key=len)))
