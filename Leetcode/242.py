'''
242. Valid Anagram
Given two strings s and t , write a function to determine if t is an anagram of s.
Example 1:
Input: s = "anagram", t = "nagaram"
Output: true
Example 2:
Input: s = "rat", t = "car"
Output: false
Note:
You may assume the string contains only lowercase alphabets.
'''
def anagram(s,t):
    s = s.replace(' ','').lower()
    t = t.replace(' ','').lower()   
    return (sorted(s) == sorted(t))

print(anagram('rat','tar') )

def anagram_2(s,t):
    s = s.replace(' ','').lower()
    t = t.replace(' ','').lower()  
    d = {}
    for char in s:
        if char not in d:
            d[char] =1
        else:
            d[char]+=1

    t = 'tar'
    for char in t:
        if char in d:
            d[char] -=1
        else:
            return False
    for char in d:
        if d[char] !=0:
            return False
    else:
        return True
            
print(anagram_2('rat','tar') )