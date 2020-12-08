'''
Count the number of prime numbers less than a non-negative number, n.
Example 1:
Input: n = 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
Example 2:
Input: n = 0
Output: 0
Example 3:
Input: n = 1
Output: 0
'''

def prime_count(n):
    def prime(num):
        if num <=1:
            return False
        for i in range(2,num):
            if num%i==0:
                return False
        return True
    a = []
    for i in range(n+1):
        prime_num  = prime(i)
        if prime_num == True:
            a.append(prime_num)
    return len(a)
print(prime_count(500))


import  pandas as pd



