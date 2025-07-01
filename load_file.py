def load_words():
    """Load words from words.txt file"""
    words = set()
    try:
        with open('words.txt') as f:
            for w in f.readlines():
                words.add(w.strip())
    except FileNotFoundError:
        print("Warning: words.txt not found")
    return words

# Load words when module is imported
list_word = load_words()