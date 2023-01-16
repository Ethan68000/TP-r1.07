a = input("Entrez un mot ou une phrase")
s = ' '.join(ch for ch in a if ch.isalnum())
print(a)
def isPalindrome(a): return a == a[::-1]
rep = isPalindrome(a)

if rep:
    print("Ceci n'est pas un palindrome")
else:
    print("Ceci est un palindrome")