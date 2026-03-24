def fast_power(base, exp):
    # 1. Base Case: Anything to the power of 0 is 1
    if exp == 0:
        return 1
    
    # 2. The Recursive Step: Divide the problem in half
    # We calculate (base^(exp/2)) ONCE and store it
    half = fast_power(base, exp // 2)
    
    # 3. Combine the results
    if exp % 2 == 0:
        # If exponent is even (like 2^4), it's just (2^2) * (2^2)
        return half * half
    else:
        # If exponent is odd (like 2^5), it's 2 * (2^2) * (2^2)
        return base * half * half

# Testing it out
print(fast_power(2, 10)) # Should give 1024