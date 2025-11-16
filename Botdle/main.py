from random import choice

from utils import get_available_words, LetterManager


def pick_answer(available_words: set[str]):
    return choice(list(available_words))


def main():
    available_words = get_available_words()
    print(f"{len(available_words) = }")
    letter_manager = LetterManager(available_words)
    answer = pick_answer(available_words)
    # answer = "eking"
    print(f"{len(letter_manager.available_words) = }")
    
    first_guess = letter_manager.word_with_highest_count(count_duplicate_letters=False)
    print(first_guess)
    print(answer)
    
    
    

if __name__ == "__main__":
    main()