from load_file import list_word

def wordwithoutletter(l):
    letterset = set()
    for w in list_word:
        if l not in w:
            letterset.add(w)
    return letterset

def wordbynotletter():
    alphabetword = dict()
    for i in range(97,123):
        alphabetword[chr(i)]=wordwithoutletter(chr(i))
    return alphabetword

WNL = wordbynotletter()