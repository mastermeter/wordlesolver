from load_file import list_word

def wordletternotinposition(l):
    letterpos = dict()
    for i in range(5):
        letterpos[i] = set()
        for w in list_word:
            if w[i]!=l:
                letterpos[i].add(w)
    return letterpos

def dictwordletternotinposition():
    alphabetposition = dict()
    for i in range(97,123):
        alphabetposition[chr(i)]=wordletternotinposition(chr(i))
    return alphabetposition

LNP = dictwordletternotinposition()