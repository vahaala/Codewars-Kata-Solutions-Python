word = 'racer'
words = ['crazer', 'carer', 'racar', 'caers', 'racer']

def anagrams(word, words):
    return [item for item in words if sorted(item) == sorted(word)]
    
print (anagrams(word, words))