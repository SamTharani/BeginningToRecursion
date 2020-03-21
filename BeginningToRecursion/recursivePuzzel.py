#Recursive Sum
def sumupton(n):
    if n == 1:
        return 1
    else:
        return n + sumupton(n-1)
    
# Recursive Palindrome
def is_palindrome(word):
    if len(word)== 1:
        return True
    else:
        if word[0] != word[-1]:
            return False
        else:
            return is_palindrome(word[1:-1])
        
#Shake hand problem

def shake_hand(n):
    if n==1:
        return 0
    else:
        return (n-1)+ shake_hand(n-1)
        
#Shake hands related gender
def shake_gender(n):
    if n==1:
        return 1
    else:
        return shake_hand(2*n)-(2*n - 2)
