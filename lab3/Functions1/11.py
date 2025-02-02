#Write a Python function that checks whether a word or phrase is `palindrome` or not.
#  Note: A palindrome is word, phrase, or sequence that reads the same backward as forward, e.g., madam

def Palindrome(word):
    word=word.replace(" ", "").lower() #убираем скобки и переобразуем в нижний регистр
    s=word[::-1]
    return s==word
String=input()
if Palindrome(String):
    print("yes, it's palindrome!")
else:
    print("no, it's not palindrome.")