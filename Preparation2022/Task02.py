# function to check if two strings are
# anagram or not
def check(s1, s2):
    # the sorted strings are checked
    if (sorted(s1) == sorted(s2)):
        print("The strings are anagrams.")
    else:
        print("The strings aren't anagrams.")


s1 = "listen"
s2 = "silent"
check(s1, s2)

def frequency_char (word):
    res = { }
    for c in word:
        if c in res:
            res[c] += 1
        else:
            res [c] = 1
    return res
# Anagram
def anagram(word1, word2):
    f1 = frequency_char(word1)
    f2 = frequency_char(word2)

    return f1 == f2


print(anagram("listen", "silent"))
