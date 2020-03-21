#Recursive Sum
# Recursively find the sum of n numbers
def sumupton(n):
    #base case
	if n == 1:
        return 1
	#recursive case	
    else:
        return n + sumupton(n-1)
		
    
# Recursive Palindrome
#Recursively identify the palidrome
def is_palindrome(word):
	#base case
    if len(word)== 1:
        return True
	#recursive case	
    else:
        if word[0] != word[-1]:
            return False
        else:
            return is_palindrome(word[1:-1])
        
#Shake hand problem
#In a party of N people, each person will shake her/his hand with each other person only once. 
#On total how many hand-shakes would happen
'''
Description for recursive approach
if one person there is no shake hand = base case
if number of person greater than one handshakes will be n(n-1)/2 = recursive case
'''
def shake_hand(n):
	#base case
    if n==1:
        return 0
	#recursive case	
    else:
        return (n-1)+ shake_hand(n-1)
        
#Shake hands related gender
'''
Description for recursive approach
is an extension version of the earlier problem
if one couple there is one shake hand = base case
if number of person greater than one handshakes will be 2n - 2 shakehands not happend = recursive case
'''
def shake_gender(n):
    #base case
    if n==1:
        return 1
	#recursive case	
    else:
        return shake_hand(2*n)-(2*n - 2)
