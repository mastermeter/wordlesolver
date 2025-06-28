from load_file import list_word

letter_appearance = dict()
for w in list_word:
    for l in w:
        if l not in letter_appearance:
            letter_appearance[l]=dict()
        else :
            letter_appearance[l]
print(letter_appearance)