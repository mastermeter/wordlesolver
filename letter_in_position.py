from load_file import list_word

def wordspecificletterspecificposition(l):
    letterpos = dict()
    for i in range(5):
        letterpos[i] = set()
        for w in list_word:
            if w[i]==l:
                letterpos[i].add(w)
    return letterpos

def dictwordbyletterposition():
    alphabetposition = dict()
    for i in range(97,123):
        alphabetposition[chr(i)]=wordspecificletterspecificposition(chr(i))
    return alphabetposition

LP = dictwordbyletterposition()