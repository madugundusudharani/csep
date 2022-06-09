#find wheather a string is anagram of given string?
s1 =input("enter the string:")
s2 =input("enter the string:")
def check(s1, s2):
    if(sorted(s1)== sorted(s2)):
        print("The strings are anagrams.")
    else:
        print("The strings aren't anagrams.")         
check(s1, s2)
