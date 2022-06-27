class Phoneme:

    def __init__(self, arpabet, american, english, ipa, is_vowel):
        '''
        :param arpabet: ARPAbet
        :param american: 美音
        :param english: 英音
        :param ipa: 国际音标
        :param is_vowel: 是否是元音
        '''
        self._arpabet = arpabet
        self._american = american
        self._english = english
        self._is_vowel = is_vowel
        self._ipa = ipa

    @property
    def ipa(self):
        return self._ipa

    @property
    def english(self):
        return self._english

    @property
    def american(self):
        return self._american

    @property
    def arpabet(self):
        return self._arpabet

    @property
    def is_vowel(self):
        return self._is_vowel

vowels = [Phoneme(arpabet='AA', american='ɑ',  english='ɑ:', ipa='ɑ',  is_vowel=True),
          Phoneme(arpabet='AE', american='æ',  english='æ',  ipa='æ',  is_vowel=True),
          Phoneme(arpabet='AH', american='ʌ',  english='ʌ',  ipa='ʌ',  is_vowel=True),
          Phoneme(arpabet='AO', american='ɔ',  english='ɔ:', ipa='ɔ',  is_vowel=True),
          Phoneme(arpabet='AW', american='aʊ', english='aʊ', ipa='aʊ', is_vowel=True),
          Phoneme(arpabet='AX', american='ə',  english='ə',  ipa='ə',  is_vowel=True),
          Phoneme(arpabet='ER', american='ɚ',  english='ər', ipa='ər', is_vowel=True),
          Phoneme(arpabet='AY', american='aɪ', english='aɪ', ipa='aɪ', is_vowel=True),
          Phoneme(arpabet='EH', american='ɛ',  english='e',  ipa='e',  is_vowel=True),
          Phoneme(arpabet='ER', american='ɝ',  english='ɜ:', ipa='ɜr', is_vowel=True),
          Phoneme(arpabet='EY', american='e',  english='eɪ', ipa='eɪ', is_vowel=True),
          Phoneme(arpabet='IH', american='ɪ',  english='ɪ',  ipa='ɪ',  is_vowel=True),
          Phoneme(arpabet='IX', american='ɨ',  english='ɨ',  ipa='ɨ',  is_vowel=True),
          Phoneme(arpabet='IY', american='i',  english='i:', ipa='i:', is_vowel=True),
          Phoneme(arpabet='OW', american='o',  english='əʊ', ipa='oʊ', is_vowel=True),
          Phoneme(arpabet='OY', american='ɔɪ', english='ɔɪ', ipa='ɔɪ', is_vowel=True),
          Phoneme(arpabet='UH', american='ʊ',  english='ʊ',  ipa='ʊ',  is_vowel=True),
          Phoneme(arpabet='UW', american='u',  english='u:', ipa='u',  is_vowel=True),
          Phoneme(arpabet='UX', american='ʉ',  english='ʉ',  ipa='ʉ',  is_vowel=True)]