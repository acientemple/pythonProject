import re
#chrome 右键:检查/网络/名称(没内容需刷新，如F5）
# 下方引号内添加替换掉请求头内容
# # headers_str = """
# Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
# Accept-Encoding: gzip, deflate
# Accept-Language: zh-CN,zh;q=0.9,en;q=0.8,und;q=0.7
# Cache-Control: max-age=0
# Connection: keep-alive
# Cookie: _ga=GA1.2.678590470.1654960035; __utma=100617052.678590470.1654960035.1654963569.1654963569.1; __utmc=100617052; __utmz=100617052.1654963569.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); _gid=GA1.2.279666038.1655175321; _gat=1; _dd_s=logs=1&id=031367b7-a545-42a2-8aeb-446e858a7ed4&created=1655203750319&expire=1655204668191
# Host: www.speech.cs.cmu.edu
# Referer: http://www.speech.cs.cmu.edu/cgi-bin/cmudict?in=Dictionary&stress=-s
# Upgrade-Insecure-Requests: 1
# User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36
# """
def headers(str):
  pattern = '^(.*?):(.*)$'
  for line in str.splitlines():
    print(re.sub(pattern,'\'\\1\':\'\\2\',',line).replace(' ',''))

#结果
# 'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
# 'Accept-Encoding':'gzip,deflate',
# 'Accept-Language':'zh-CN,zh;q=0.9,en;q=0.8,und;q=0.7',
# 'Cache-Control':'max-age=0',
# 'Connection':'keep-alive',
# 'Cookie':'_ga=GA1.2.678590470.1654960035;__utma=100617052.678590470.1654960035.1654963569.1654963569.1;__utmc=100617052;__utmz=100617052.1654963569.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none);_gid=GA1.2.279666038.1655175321;_gat=1;_dd_s=logs=1&id=031367b7-a545-42a2-8aeb-446e858a7ed4&created=1655203750319&expire=1655204668191',
# 'Host':'www.speech.cs.cmu.edu',
# 'Referer':'http://www.speech.cs.cmu.edu/cgi-bin/cmudict?in=Dictionary&stress=-s',
# 'Upgrade-Insecure-Requests':'1',
# 'User-Agent':'Mozilla/5.0(WindowsNT10.0;Win64;x64)AppleWebKit/537.36(KHTML,likeGecko)Chrome/102.0.0.0Safari/537.36'
