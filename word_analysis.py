from load_file import list_word
import matplotlib.pyplot as plt

letter_occurence = []

for w in list_word:
    word = set()
    for l in w:
        word.add(l)
    letter_occurence.append(word)

def occurence():
    occurence_letter = dict()
    for w in letter_occurence:
        for i in range(97,123):
            if chr(i) in w:
                if chr(i) not in occurence_letter:
                    occurence_letter[chr(i)]=1
                else:
                    occurence_letter[chr(i)]+=1
    

    return occurence_letter

data_occurence_letter = occurence()

plt.bar(range(len(data_occurence_letter)),list(data_occurence_letter.values()))
plt.xticks(range(len(data_occurence_letter)), list(data_occurence_letter.keys()))
plt.show()