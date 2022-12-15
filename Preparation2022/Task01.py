test_str = "ThisisaTesttoTest"

all_freq = {}

for i in test_str:
    if i in all_freq:
        all_freq[i] += 1
    else:
        all_freq[i] = 1


print("Count of all characters in" + " "+
        test_str +" "+
        "is :\n "
      + str(all_freq))

# classic solution
def frequency_char (word):
    res = { }
    for c in word:
        if c in res:
            res[c] += 1
        else:
            res [c] = 1
    return res

# dictionary comprehension
def frequency_char2 (word):
    res = { c:0 for c in word }
    for c in word:
        res[c] += 1
    return res

# using get method of dictionary
def frequency_char3 (word) :
    res = { }
    for c in word :
        # the method get returns res[c] if this value exists, 0 otherwise
        res[c] = res.get( c, 0 ) + 1
    return res

print(frequency_char("the aviator"))
# displays {'t': 2, 'h': 1, 'e': 1, ' ': 1, 'a': 2, 'v': 1, 'i': 1, 'o': 1, 'r': 1}