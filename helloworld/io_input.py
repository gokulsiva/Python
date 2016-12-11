def reverse(text):
    return text[::-1]


def palindrome(text):
    return text == reverse(text)


txt = raw_input('Enter a String to check : ')
txt1 = txt
txt = txt.lower()
checker = ''
for ch in txt:
    if ch.isalpha():
        checker = checker+ch
if palindrome(checker):
    print '{} is a palindrome'.format(txt1)
else:
    print '{} is not a palindrome'.format(txt1)
