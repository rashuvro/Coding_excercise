'''
A self-dividing number is a number that is divisible by every digit it contains.
For example, 128 is a self-dividing number because 128 % 1 == 0, 128 % 2 == 0, and 128 % 8 == 0.
Also, a self-dividing number is not allowed to contain the digit zero.
Given a lower and upper number bound, output a list of every possible self dividing number, including the bounds if possible.
Example 1:
Input: 
left = 1, right = 22
Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]

'''

def selfDividingNumbers(left, right):
        def self_dividing(a): 
            b = []
            for i in range(len(str(a))):
                       b.append(str(a)[i])
            for num in b:
                if int(num) == 0:
                    return False
                if a%int(num) !=0:
                     return False
            return True 
        ans = []
        for num in range(left,right+1):
            temp = self_dividing(num)
            if temp == True:
                ans.append(num)
        return ans

print(selfDividingNumbers(1,22))
