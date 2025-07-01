from letter_in_position import LP
from letter_in_word import WL
from letter_notin_position import LNP
from letter_notin_word import WNL
from load_file import list_word

base = list_word

constraint = [LP['a'][0],
 LNP['c'][3],
 WNL['d'],
 WNL['y'],
 WNL['q'],
 WNL['e'],
 WNL['t'],
 WNL['h'],
 WNL['n'],
 LNP['i'][4],
 WNL['o'],
 WNL['u'],
 WNL['r'],
 WNL['s'],
 WNL['l'],
 WNL['b'],
 WNL['z']]

for i in constraint:
    print(len(base))
    step = base.intersection(i)
    base = step
print(base)