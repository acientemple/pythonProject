# -*- coding: utf-8 -*-
# python 3
# xiaodeng
# 调用网易有道词典api


import urllib
import json

class Youdao():
    def __init__(self, word):
        self.url = 'http://fanyi.youdao.com/openapi.do'  # url、key、keyfrom都是固定的值，所以采用这种方式赋值
        self.key = '929705525'
        self.keyfrom = 'pythonxiaodeng'
        self.word = word

    def getTranslation(self):
        data = {'keyfrom': self.keyfrom,
                'key': self.key,
                'type': 'data',
                'doctype': 'json',
                'version': '1.1',
                'q': self.word}
        # encode
        data = urllib.parse.urlencode(data)
        # print data
        # keyfrom=pythonxiaodeng&doctype=json&q=student&version=1.1&key=929705525&type=data
        url = self.url + '?' + data  # 链接url和参数dict
        html = urllib.request.urlopen(url).read()
        html = json.loads(html)
        return(html)
def word_info(w):
    word=Youdao(w)
    return(word.getTranslation())
def phonetic(w):
    if word_info(w).get('basic'):
        return (word_info(w)['basic']['phonetic'])
    else:
        print('No phonetic found.')

def us_phonetic(w):
    if word_info(w).get('basic'):
        return (word_info(w)['basic']['us-phonetic'])
    else:
        print('No phonetic found.')
def uk_phonetic(w):
    if word_info(w).get('basic'):
        return (word_info(w)['basic']['uk-phonetic'])
    else:
        print('No phonetic found.')
