import os
from aip import AipSpeech

APP_ID = ''  # 自己填入百度智能云注册的app_id
API_KE = ''  # follow above
SECRET_KEY = ''  # follow above
client = AipSpeech(APP_ID, API_KE, SECRET_KEY)


def get_file_path(filepath):
    with open(filepath, 'rb') as f:
        return f.read()


def write_srtxt(txtfile, line):
    with codecs.open(txtfile, 'a', 'utf-8') as f:
        f.seek(0)  # 重定位
        f.write(line)


def dt_sr(srcfile):
    speechrate = 16000
    speechsaccu = 16
    buffer = get_file_path(srcfile)
    sizepersec = int((speechsaccu / 8) * speechrate)
    timesec = int(len(buffer) / sizePerSec)
    timeMinute = int((timeSec + 59) / 60)
    print(timeMinute)

    for count in range(0, timeMinute):
        print(min((count + 1) * sizePerSec * 60, len(buffer)))
        speechBuffer = buffer[count * sizePerSec * 60: min((count + 1) * sizePerSec * 60, len(buffer))]
        result = client.asr(speechBuffer, 'pcm', 16000, {
            'lan': 'zh',
        })
        if (result['err_no'] == 0):
            print(result['result'])
            line = str(count) + ':00' + "--" + str(count) + ":59  " + result['result'][0] + '\n'
            # 功能拓展输入到机器人中
            write_srtxt(txtFile, line)
            # 导入传入方法
        else:
            # print(result)
            print("语音识别错误，错误码是: ", result['err_no'], " , 错误信息是：" + result['err_msg'])


pcmFile = 'd:\\workroom\\testroom\\sr.raw'
txtFile = 'd:\\workroom\\testroom\\srtxt.txt'
cmd = "ffmpeg -i " + pcmFile + " -f s16le -ar 16000 -acodec pcm_s16le -b:a 16 -ac 1 -y " + pcmFile
os.system(cmd)
dt_sr(pcmFile)
