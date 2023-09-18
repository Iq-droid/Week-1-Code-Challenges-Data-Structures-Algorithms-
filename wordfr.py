import string

def word_frequency(sentence):
    words = sentence.split()
    word_count = {}
    
    for word in words:
        word = word.strip(string.punctuation).lower()
        if word:
            word_count[word] = word_count.get(word, 0) + 1
    
    return word_count

# Test case
sentence = "This is a test sentence. This sentence is a test."
result = word_frequency(sentence)
print(result)