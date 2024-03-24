def palindrome(text):
    if len(text) < 2:
        return "Text is a palindrome"
    else: 
        if text[0] == text[-1]:
            return palindrome(text[1:-1])
        else:
            return "Not A Palindrome"

text = input("Please Enter A Text: ")
print(palindrome(text))
