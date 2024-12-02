"""

Given two strings s
 and t
 of equal length, the Hamming distance between s
 and t
, denoted dH(s,t)
, is the number of corresponding symbols that differ in s
 and t
. See Figure 2.

Given: Two DNA strings s
 and t
 of equal length (not exceeding 1 kbp).

Return: The Hamming distance dH(s,t)


"""

string1 = input("Enter DNA sequence 1: ")
string2 = input("Enter DNA sequence 2: ")
ms = zip(string1,string2)

point_mutation_counter = 0
for charx, chary in ms:
    if charx != chary:
        point_mutation_counter += 1

print(point_mutation_counter)