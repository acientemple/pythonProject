#arpabetandipaconvertor
from arpabetandipaconvertor import arpabet2phoneticalphabet as ap
from arpabetandipaconvertor import phoneticarphabet2arpabet as pa
import arpabetandipaconvertor as ai
from arpabetandipaconvertor import model
from arpabetandipaconvertor import excepts

import cmudict

dict=cmudict.dict()
for word in cmudict.words():
    raw_arpabet=' '.join(cmudict.dict()[word][0])
    ipa=ai.arpabet2phoneticalphabet.ARPAbet2PhoneticAlphabetConvertor().convert_to_international_phonetic_alphabet(raw_arpabet)
    dict[word].append(ipa)

def exp(a,b,c=2,*var,**kw):
    print(f'a={a}，bb={b},c={c},var={var},kw={kw}')
