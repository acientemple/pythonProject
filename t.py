
from enum import Enum
class Mopheme(Enum):
     arpabet='AE'
     american='æ'
     english='æ'
     ipa='æ'
     is_vowel=True
for m in Mopheme:
    print(m.name,':',m.value)
