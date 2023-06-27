# your code goes here!env shell
class Anagram:
    def __init__(self, word):
        self.word = word

    def match(self, list):
        seperate_word = sorted([letter for letter in self.word])
        anagrams_array = []
        for array in list:
            if(seperate_word == sorted(array)):
                anagrams_array.append(array)
                print(anagrams_array)
        if(len(anagrams_array) > 0):
            return anagrams_array
        else:
            return []