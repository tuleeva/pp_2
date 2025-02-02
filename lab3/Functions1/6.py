#Write a function that accepts string from user, return a sentence with the words reversed.
#`We are ready -> ready are We`
def reverse_words():
    sentence = input()
    
    words = sentence.split()
    
    reversed_words = words[::-1]
    
    # Join the reversed list of words back into a sentence
    reversed_sentence = ' '.join(reversed_words)
    
    return reversed_sentence
print(reverse_words())