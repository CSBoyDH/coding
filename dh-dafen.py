def is_palindrome(s):
    end = len(s) - 1
    i = 0

    while (s[i] != s[end]):
        if s[i] != s[end]:
            return False
        i += 1
        end -= 1

    return  True
