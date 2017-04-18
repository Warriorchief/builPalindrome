#FROM CODEFIGHTS LEVEL 10
"""
Given a string, find the shortest possible string which can be achieved by adding 
characters to the end of initial string to make it a palindrome.

Example

For st = "abcdc", the output should be
buildPalindrome(st) = "abcdcba".

Input/Output

[time limit] 4000ms (py3)
[input] string st

A string consisting of lowercase latin letters.

Guaranteed constraints:
3 ≤ st.length ≤ 10.

[output] string
"""

import math
    
def buildPalindrome(st):
    holder=st
    i=1
    while not is_palindrome(holder):
        holder=st[i:]
        i+=1     
    print('the longest pali from the end of orig string down is',holder)
    #then from here, take everything BEFORE the holder, flip it backwards, and append to st
    noncount=len(st)-len(holder)
    print('noncount is',noncount)
    nonpart=st[:noncount]
    print('nonpart is',nonpart)
    k=len(nonpart)-1
    print('k is',k)
    out=st
    print('here, out is',out)
    while k>=0:
        out+=nonpart[k]
        print('just added the letter',nonpart[k])
        k-=1
    print('the answer should be',out)
    return out
    
def is_palindrome(x):
    if len(x)==1:
        return True
    if len(x)%2==1:
        mid=math.floor(len(x)/2)
        bottom=mid-1
        top=mid+1
        while bottom>=0:
            if x[bottom]!=x[top]:
                return False
            bottom-=1
            top+=1
        return True
    else:
        top=int(len(x)/2)
        bottom=top-1
        while bottom>=0:
            if x[bottom]!=x[top]:
                return False
            bottom-=1
            top+=1
        return True

#print(is_palindrome('blah'))
#print(is_palindrome('racecar'))
#print(buildPalindrome('maxlllllllllrrr')) #--> maxlllllllllrrrlllllllllxam
