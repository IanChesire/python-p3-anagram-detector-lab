
class Anagram:
    def __init__(self, word):
        self.word = word
    
    def match(self, word_list):
        original_word = self.word.replace(" ", "")
        matched_words = []

        for word in word_list:
            word_to_match = word.replace(" ", "")
            
            if word_to_match == original_word or len(word_to_match) != len(original_word):
                continue

            for char in word_to_match:
                if char not in original_word:
                    break
            else:
                matched_words.append(word)

        return matched_words