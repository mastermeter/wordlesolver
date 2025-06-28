from load_file import list_word

def wordcorrectposition(letter, position):
    match_word = [w for w in list_word if w[position]==letter]
    return match_word

def wordlettermissposition(letter, position):
    match_word = [w for w in list_word if letter in w and w[position]!=letter]
    print(len(match_word))
    return match_word

def wordwithoutletter(letter):
    match_word = [w for w in list_word if letter not in w]
    return match_word

if __name__ == "__main__":
    print(f"Loaded {len(list_word)} words")
    # Example usage
    print("Words with 'a' in position 0:", len(wordcorrectposition('a', 0)))