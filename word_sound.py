import cmudict
from phonetics import arpabet2ipa
def word2arpabet(w): # get arpabet of the word
    return(cmudict.dict()[w][0])
def arpabet_len_stress(word): #get arpabet（cmu音标）, numbers of syllables(音节） , stress positon(backward) （重音位置/倒数第几个）of the word
    arpabet=word2arpabet(word)
    len = 0
    stress = 0
    for p in arpabet:
        if p[-1].isdigit():
            len += 1
            if p[-1] == '1':
                stress = len
    return (word,arpabet,len, len-stress+1)



