def is_palindrome(s):
    i = 0
    j = len(s) - 1
    is_palindrome_no = True

    while i < j:
       if  s[i] != s[j]:
           is_palindrome_no = False
           break
       i += 1
       j -= 1

    if is_palindrome_no:
        print("Given string is palindrome")
    else:
      print("Given string is not palindrome")

is_palindrome("malayalam")
is_palindrome("hello")





    