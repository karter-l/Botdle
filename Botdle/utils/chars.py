import string
from collections import Counter

class LetterManager():
    def __init__(self, available_words: set[str]):
        self.available_words = available_words
        self._letter_dict = \
            {
                letter.lower(): {
                    "eliminated": None,
                    "positions": [],
                    "not_positions": [],
                    "prevalence": 0
                } 
            for letter in string.ascii_lowercase
        }
        self._initial_analysis()
            
    def _initial_analysis(self):
        all_letters = ''.join(self.available_words)
        
        letter_counts = Counter(all_letters)
        
        for letter, count in letter_counts.items():
            if count == 0:
                print(f'eliminated: {letter}')
                self._letter_dict[letter]["eliminated"]=True
            
            self._letter_dict[letter]["prevalence"] = count
            
    def word_with_highest_count(self, count_duplicate_letters: bool = False) -> str:
        selected_word = ""
        max_word_score = 0

        for word in self.available_words:
            if not count_duplicate_letters:
                seen_letters = set()
                word = ''.join([letter for letter in word if letter not in seen_letters and not seen_letters.add(letter)])

            word_score = sum([self._letter_dict[letter]["prevalence"] for letter in word])

            if word_score > max_word_score:
                max_word_score = word_score
                selected_word = word

        return selected_word

            