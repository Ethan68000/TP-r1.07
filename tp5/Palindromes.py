s = input("Entrer un mot ou une phrase")
s = ' '.join(ch for ch in s if ch.isalnum())
def isPalindrome(s): return s == s[::-1]
rep = isPalindrome(s)

if rep:
    print("C'est un palindrome")
else:
    print("Ce n'est pas un palindrome")
