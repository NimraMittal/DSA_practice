def is_palindrome(s):
    palindrome = True
    if len(s) <= 1:
        return palindrome
    
    else:
        first = s[0] 
        last = s[-1]
        if first != last:
            palindrome = False
            return palindrome
        else: 
            new = s[1:-1]
            return is_palindrome(new)
    
s = "aabcbaa"
print(is_palindrome(s))

