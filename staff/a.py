def is_palindrome(s):
    return s == s[::-1]

def PalindromeCreator(strParam):
    if is_palindrome(strParam):
        return "palindrome"

    for i in range(len(strParam)):
        substring = strParam[:i] + strParam[i+1:]
        if is_palindrome(substring):
            return strParam[i]

        for j in range(i+1, len(strParam)):
            subsubstring = substring[:j-i-1] + substring[j-i:]
            if is_palindrome(subsubstring):
                return strParam[i:j+1]

    return "not possible"

# Test cases
print(PalindromeCreator("emoр"))  # Output: not possible
print(PalindromeCreator("kjjjh13"))  # Output: k
