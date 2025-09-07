#Ask the user for a word. Print whether it’s a palindrome (same forward and backward).


word = input("Let's check if word is palindrome or not. Give me word! ")
#in place of 3 line we can jut replace line 4 to if word == word[::-1] this will remove line 3
check = word[::-1]
if check == word:
    print("its palindrome")
else:
    print("its not a palindrome")   