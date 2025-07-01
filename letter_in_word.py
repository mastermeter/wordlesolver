from load_file import list_word

def wordwithspecificletter(l):
    letterset = set()
    for w in list_word:
        if l in w:
            letterset.add(w)
    return letterset

def wordbyletter():
    alphabetword = dict()
    for i in range(97,123):
        alphabetword[chr(i)]=wordwithspecificletter(chr(i))
    return alphabetword

WL = wordbyletter()