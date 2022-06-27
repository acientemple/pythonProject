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
        self.edit_by='James Chow'
        self.word = word

    def word_info(self):
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
    @property
    def phonetic(self):
        if self.word_info().get('basic'):
            return (self.word_info()['basic']['phonetic'])
        else:
            print('No phonetic found.')

    @property
    def us_phonetic(self):
        if self.word_info().get('basic'):
            return (self.word_info()['basic']['us-phonetic'])
        else:
            print('No phonetic found.')

    @property
    def uk_phonetic(self):
        if self.word_info().get('basic'):
            return (self.word_info()['basic']['uk-phonetic'])
        else:
            print('No phonetic found.')

    @property
    def translation(self):
        if self.word_info().get('translation'):
            return (self.word_info()['translation'])
        else:
            print('No translation found.')

    @property
    def explains(self):
        if self.word_info().get('basic'):
            return (self.word_info()['basic']['explains'])
        else:
            print('No explians found.')


