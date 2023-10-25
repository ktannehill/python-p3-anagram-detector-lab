class Anagram:

    # instantiates with single arg, word
    # method match()
    # returns empty list if no anagrams
    # returns a list of words with matching letters

    def __init__(self, poss_anagram):
        self.poss_anagram = poss_anagram
    
    def match(self, list):
        matches = []
        for word in list:
            if sorted([char for char in self.poss_anagram]) == sorted([char for char in word]):
                matches.append(word)
        return matches