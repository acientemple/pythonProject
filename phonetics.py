import cmudict,copy
from arpabetandipaconvertor import arpabet2phoneticalphabet
from arpabetandipaconvertor import phoneticarphabet2arpabet
cmudict_ipa=copy.deepcopy(cmudict.dict())
def arpabet2ipa(arp):
    return (arpabet2phoneticalphabet.ARPAbet2PhoneticAlphabetConvertor().
            convert_to_international_phonetic_alphabet(arp))#arp:string of arpabet
def arpabet2american(arp):
    return (arpabet2phoneticalphabet.ARPAbet2PhoneticAlphabetConvertor().
            convert_to_american_phonetic_alphabet(arp))
def arpabet2english(arp):
    return (arpabet2phoneticalphabet.ARPAbet2PhoneticAlphabetConvertor().
            convert_to_english_phonetic_alphabet(arp))
def american2arpabet(am):
    return (phoneticarphabet2arpabet.PhoneticAlphabet2ARPAbetConvertor().convert(am))
def get_cmudictipa():
    for key in cmudict_ipa.keys():
        lst_arpabet=cmudict_ipa[key][0] #get list of arpabet
        arpabet=' '.join(lst_arpabet) # get string of arpabet
        ipa=arpabet2ipa(arpabet) #convert string of arpabet into ipa
        cmudict_ipa[key].append([arpabet]) #add string of arpabet to dic
        cmudict_ipa[key].append([ipa]) #add ipa to dic
    return (cmudict_ipa)




