import youdao
import word_sound
import cmudict
def get_phonetic_alphabet(w):
    youdao.word_trans(w)
def add_label(w):
    p1=cmudict.dict()[w]
    p1.append([get_label(w)])
    return({w:p1})
