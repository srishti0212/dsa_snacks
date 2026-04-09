def isPalindrome(str):
    if str.strip() == '':
        return True
    str = str.lower()
    new_chars = []
    for i in range(0, len(str)):
        if str[i].isalnum():
            new_chars.append(str[i])      
    new_str = ''.join(new_chars)
    start = 0
    end = len(new_str) - 1
    while start < end:
            if new_str[start] != new_str[end]:
                return False
            start += 1
            end -= 1
    return True

def main():
    str1 = 'srishti'
    print(isPalindrome(str1)) #False
    str2 = 'srirs'
    print(isPalindrome(str2)) #True
    str3 = '12345'
    print(isPalindrome(str3)) #False
    str4 = '9889'
    print(isPalindrome(str4)) #True
    str5 = ''
    print(isPalindrome(str5)) #True
    str6 = ',' 
    print(isPalindrome(str6)) #True
    str7 = ',brb,'
    print(isPalindrome(str7)) #True

if __name__ == "__main__":
    main()